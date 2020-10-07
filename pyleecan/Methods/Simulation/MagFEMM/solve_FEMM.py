import numpy as np

from numpy import zeros, pi, roll, mean, max as np_max, min as np_min
from os.path import basename, splitext
from SciDataTool import DataLinspace, DataTime, VectorField, Data1D
from os.path import join

from ....Functions.FEMM.update_FEMM_simulation import update_FEMM_simulation
from ....Functions.FEMM.comp_FEMM_torque import comp_FEMM_torque
from ....Functions.FEMM.comp_FEMM_Phi_wind import comp_FEMM_Phi_wind
from ....Functions.Winding.gen_phase_list import gen_name


def solve_FEMM(self, femm, output, sym):

    # Loading parameters for readibility
    angle = output.mag.angle
    L1 = output.simu.machine.stator.comp_length()

    save_path = self.get_path_save(output)
    FEMM_dict = output.mag.FEMM_dict

    # Get dimensions including periodicity
    Nt_comp = output.mag.time.get_length(is_oneperiod=self.is_periodicity_t)
    Na_comp = output.mag.angle.get_length(is_oneperiod=self.is_periodicity_a)
    sym_dict = dict()
    if self.is_periodicity_t:
        sym_dict.update(output.time.symmetries)
    if self.is_periodicity_a:
        sym_dict.update(output.angle.symmetries)

    if (
        hasattr(output.simu.machine.stator, "winding")
        and output.simu.machine.stator.winding is not None
    ):
        qs = output.simu.machine.stator.winding.qs  # Winding phase number
        Npcpp = output.simu.machine.stator.winding.Npcpp
        Phi_wind_stator = zeros((Nt_comp, qs))
    else:
        Phi_wind_stator = None

    # Create the mesh
    femm.mi_createmesh()

    # Initialize results matrix
    Br = zeros((Nt_comp, Na_comp))
    Bt = zeros((Nt_comp, Na_comp))
    Tem = zeros((Nt_comp))

    Rag = output.simu.machine.comp_Rgap_mec()

    # Compute the data for each time step
    for ii in range(Nt_comp):
        self.get_logger().debug("Solving step " + str(ii + 1) + " / " + str(Nt_comp))
        # Update rotor position and currents
        update_FEMM_simulation(
            femm=femm,
            output=output,
            materials=FEMM_dict["materials"],
            circuits=FEMM_dict["circuits"],
            is_mmfs=self.is_mmfs,
            is_mmfr=self.is_mmfr,
            j_t0=ii,
            is_sliding_band=self.is_sliding_band,
        )
        # try "previous solution" for speed up of FEMM calculation
        if self.is_sliding_band:
            try:
                base = basename(self.get_path_save_fem(output))
                ans_file = splitext(base)[0] + ".ans"
                femm.mi_setprevious(ans_file, 0)
            except:
                pass

        # Run the computation
        femm.mi_analyze()
        femm.mi_loadsolution()

        # Get the flux result
        if self.is_sliding_band:
            for jj in range(Na_comp):
                Br[ii, jj], Bt[ii, jj] = femm.mo_getgapb("bc_ag2", angle[jj] * 180 / pi)
        else:
            for jj in range(Na_comp):
                B = femm.mo_getb(Rag * np.cos(angle[jj]), Rag * np.sin(angle[jj]))
                Br[ii, jj] = B[0] * np.cos(angle[jj]) + B[1] * np.sin(angle[jj])
                Bt[ii, jj] = -B[0] * np.sin(angle[jj]) + B[1] * np.cos(angle[jj])

        # Compute the torque
        Tem[ii] = comp_FEMM_torque(femm, FEMM_dict, sym=sym)

        if (
            hasattr(output.simu.machine.stator, "winding")
            and output.simu.machine.stator.winding is not None
        ):
            # Phi_wind computation
            Phi_wind_stator[ii, :] = comp_FEMM_Phi_wind(
                femm,
                qs,
                Npcpp,
                is_stator=True,
                Lfemm=FEMM_dict["Lfemm"],
                L1=L1,
                sym=sym,
            )

        # Load mesh data & solution
        if (self.is_sliding_band or Nt_comp == 1) and (
            self.is_get_mesh or self.is_save_FEA
        ):
            tmpmeshFEMM, tmpB, tmpH, tmpmu, tmpgroups = self.get_meshsolution(
                femm, save_path, ii
            )

            if ii == 0:
                meshFEMM = [tmpmeshFEMM]
                groups = [tmpgroups]
                B_elem = np.zeros([Nt_comp, meshFEMM[ii].cell["triangle"].nb_cell, 3])
                H_elem = np.zeros([Nt_comp, meshFEMM[ii].cell["triangle"].nb_cell, 3])
                mu_elem = np.zeros([Nt_comp, meshFEMM[ii].cell["triangle"].nb_cell])

            B_elem[ii, :, 0:2] = tmpB
            H_elem[ii, :, 0:2] = tmpH
            mu_elem[ii, :] = tmpmu

    # Shift to take into account stator position
    roll_id = int(self.angle_stator * Na_comp / (2 * pi))
    Br = roll(Br, roll_id, axis=1)
    Bt = roll(Bt, roll_id, axis=1)

    # Store the results
    Time = output.mag.time  # Same symmetry as input
    Angle = output.mag.angle  # Same symmetry as input
    Br_data = DataTime(
        name="Airgap radial flux density",
        unit="T",
        symbol="B_r",
        axes=[Time, Angle],
        symmetries=sym_dict,
        values=Br,
    )
    Bt_data = DataTime(
        name="Airgap tangential flux density",
        unit="T",
        symbol="B_t",
        axes=[Time, Angle],
        symmetries=sym_dict,
        values=Bt,
    )
    output.mag.B = VectorField(
        name="Airgap flux density",
        symbol="B",
        components={"radial": Br_data, "tangential": Bt_data},
    )

    output.mag.Tem = DataTime(
        name="Electromagnetic torque",
        unit="Nm",
        symbol="T_{em}",
        axes=[Time],
        symmetries=sym_dict,
        values=Tem,
    )
    output.mag.Tem_av = mean(Tem)
    self.get_logger().debug("Average Torque: " + str(output.mag.Tem_av) + " N.m")
    output.mag.Tem_rip_pp = abs(np_max(Tem) - np_min(Tem))  # [N.m]
    if output.mag.Tem_av != 0:
        output.mag.Tem_rip_norm = output.mag.Tem_rip_pp / output.mag.Tem_av  # []
    else:
        output.mag.Tem_rip_norm = None

    if (
        hasattr(output.simu.machine.stator, "winding")
        and output.simu.machine.stator.winding is not None
    ):
        Phase = Data1D(
            name="phase",
            unit="",
            values=gen_name(qs, is_add_phase=True),
            is_components=True,
        )
        output.mag.Phi_wind_stator = DataTime(
            name="Stator Winding Flux",
            unit="Wb",
            symbol="Phi_{wind}",
            axes=[Time, Phase],
            symmetries=sym_dict,
            values=Phi_wind_stator,
        )

    output.mag.FEMM_dict = FEMM_dict

    if self.is_get_mesh:
        output.mag.meshsolution = self.build_meshsolution(
            Nt_comp, meshFEMM, Time, B_elem, H_elem, mu_elem, groups
        )

    if self.is_save_FEA:
        save_path_fea = join(save_path, "MeshSolutionFEMM.h5")
        output.mag.meshsolution.save(save_path_fea)

    if (
        hasattr(output.simu.machine.stator, "winding")
        and output.simu.machine.stator.winding is not None
    ):
        # Electromotive forces computation (update output)
        self.comp_emf()
    else:
        output.mag.emf = None

    if self.is_close_femm:
        femm.closefemm()

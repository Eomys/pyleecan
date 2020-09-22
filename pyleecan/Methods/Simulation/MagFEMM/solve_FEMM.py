import numpy as np

from numpy import zeros, pi, roll, mean, max as np_max, min as np_min
from os.path import basename, splitext
from SciDataTool import DataLinspace, DataTime, VectorField
from os.path import join

from ....Functions.FEMM.update_FEMM_simulation import update_FEMM_simulation
from ....Functions.FEMM.comp_FEMM_torque import comp_FEMM_torque
from ....Functions.FEMM.comp_FEMM_Phi_wind import comp_FEMM_Phi_wind
from ....Classes.MeshMat import MeshMat


def solve_FEMM(self, femm, output, sym):

    # Loading parameters for readibility
    angle = output.mag.angle
    L1 = output.simu.machine.stator.comp_length()
    Nt_tot = output.mag.Nt_tot  # Number of time step
    Na_tot = output.mag.Na_tot  # Number of angular step
    save_path = self.get_path_save(output)
    FEMM_dict = output.mag.FEMM_dict

    if (
        hasattr(output.simu.machine.stator, "winding")
        and output.simu.machine.stator.winding is not None
    ):
        qs = output.simu.machine.stator.winding.qs  # Winding phase number
        Npcpp = output.simu.machine.stator.winding.Npcpp
        Phi_wind_stator = zeros((Nt_tot, qs))
    else:
        Phi_wind_stator = None

    # Create the mesh
    femm.mi_createmesh()

    # Initialize results matrix
    Br = zeros((Nt_tot, Na_tot))
    Bt = zeros((Nt_tot, Na_tot))
    Tem = zeros((Nt_tot))

    Rag = output.simu.machine.comp_Rgap_mec()

    # Compute the data for each time step
    for ii in range(Nt_tot):
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
            for jj in range(Na_tot):
                Br[ii, jj], Bt[ii, jj] = femm.mo_getgapb("bc_ag2", angle[jj] * 180 / pi)
        else:
            for jj in range(Na_tot):
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
        if (self.is_sliding_band or Nt_tot == 1) and (
            self.is_get_mesh or self.is_save_FEA
        ):
            tmpmeshFEMM, tmpB, tmpH, tmpmu, tmpgroups = self.get_meshsolution(
                femm, save_path, ii
            )

            if ii == 0:
                meshFEMM = [tmpmeshFEMM]
                groups = [tmpgroups]
                B_elem = np.zeros([Nt_tot, meshFEMM[ii].cell["triangle"].nb_cell, 3])
                H_elem = np.zeros([Nt_tot, meshFEMM[ii].cell["triangle"].nb_cell, 3])
                mu_elem = np.zeros([Nt_tot, meshFEMM[ii].cell["triangle"].nb_cell])

            B_elem[ii, :, 0:2] = tmpB
            H_elem[ii, :, 0:2] = tmpH
            mu_elem[ii, :] = tmpmu

    # Shift to take into account stator position
    roll_id = int(self.angle_stator * Na_tot / (2 * pi))
    Br = roll(Br, roll_id, axis=1)
    Bt = roll(Bt, roll_id, axis=1)

    # Store the results
    Time = DataLinspace(
        name="time",
        unit="s",
        symmetries={},
        initial=output.mag.time[0],
        final=output.mag.time[-1],
        number=Nt_tot,
        include_endpoint=True,
    )
    Angle = DataLinspace(
        name="angle",
        unit="rad",
        symmetries={},
        initial=angle[0],
        final=angle[-1],
        number=Na_tot,
        include_endpoint=True,
    )
    Br_data = DataTime(
        name="Airgap radial flux density",
        unit="T",
        symbol="B_r",
        axes=[Time, Angle],
        values=Br,
    )
    Bt_data = DataTime(
        name="Airgap tangential flux density",
        unit="T",
        symbol="B_t",
        axes=[Time, Angle],
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
        values=Tem,
    )
    output.mag.Tem_av = mean(Tem)
    output.mag.Tem_rip_pp = abs(np_max(Tem) - np_min(Tem))  # [N.m]
    if output.mag.Tem_av != 0:
        output.mag.Tem_rip_norm = output.mag.Tem_rip_pp / output.mag.Tem_av  # []
    else:
        output.mag.Tem_rip_norm = None
    output.mag.Phi_wind_stator = Phi_wind_stator
    output.mag.FEMM_dict = FEMM_dict

    if self.is_get_mesh:
        output.mag.meshsolution = self.build_meshsolution(
            Nt_tot, meshFEMM, Time, B_elem, H_elem, mu_elem, groups
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

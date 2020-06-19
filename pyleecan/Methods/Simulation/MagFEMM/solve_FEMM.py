import femm
import numpy as np

from numpy import zeros, pi, roll, mean, max as np_max, min as np_min
from os.path import basename, splitext
from SciDataTool import DataLinspace, DataTime
from os.path import join

from ....Functions.FEMM.update_FEMM_simulation import update_FEMM_simulation
from ....Functions.FEMM.comp_FEMM_torque import comp_FEMM_torque
from ....Functions.FEMM.comp_FEMM_Phi_wind import comp_FEMM_Phi_wind
from ....Classes.MeshMat import MeshMat


def solve_FEMM(self, output, sym, FEMM_dict):

    # Loading parameters for readibility
    angle = output.mag.angle
    L1 = output.simu.machine.stator.comp_length()
    Nt_tot = output.mag.Nt_tot  # Number of time step
    Na_tot = output.mag.Na_tot  # Number of angular step
    save_path = self.get_path_save(output)

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
    Tem = zeros((Nt_tot, 1))

    lam_int = output.simu.machine.get_lamination(True)
    lam_ext = output.simu.machine.get_lamination(False)
    Rgap_mec_int = lam_int.comp_radius_mec()
    Rgap_mec_ext = lam_ext.comp_radius_mec()

    if self.is_get_mesh or self.is_save_FEA:
        meshFEMM = [MeshMat() for ii in range(Nt_tot)]
    else:
        meshFEMM = [MeshMat()]

    # Compute the data for each time step
    for ii in range(Nt_tot):
        # Update rotor position and currents
        update_FEMM_simulation(
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
            Rag = (Rgap_mec_ext + Rgap_mec_int) / 2
            for jj in range(Na_tot):
                B = femm.mo_getb(Rag * np.cos(angle[jj]), Rag * np.sin(angle[jj]))
                Br[ii, jj] = B[0] * np.cos(angle[jj]) + B[1] * np.sin(angle[jj])
                Bt[ii, jj] = -B[0] * np.sin(angle[jj]) + B[1] * np.cos(angle[jj])

        # Compute the torque
        Tem[ii] = comp_FEMM_torque(FEMM_dict, sym=sym)

        if (
            hasattr(output.simu.machine.stator, "winding")
            and output.simu.machine.stator.winding is not None
        ):
            # Phi_wind computation
            Phi_wind_stator[ii, :] = comp_FEMM_Phi_wind(
                qs, Npcpp, is_stator=True, Lfemm=FEMM_dict["Lfemm"], L1=L1, sym=sym
            )

        # Load mesh data & solution
        if self.is_get_mesh or self.is_save_FEA:
            meshFEMM[ii], tmpB, tmpH, tmpmu = self.get_meshsolution(save_path, ii
            )

            if self.is_sliding_band or Nt_tot == 1: # To make sure solution have the same size at every time step
                if ii == 0:
                    B = np.zeros([Nt_tot, meshFEMM[ii].cell["Triangle3"].nb_cell, 2])
                    H = np.zeros([Nt_tot, meshFEMM[ii].cell["Triangle3"].nb_cell, 2])
                    mu = np.zeros([Nt_tot, meshFEMM[ii].cell["Triangle3"].nb_cell])

                B[ii, :] = tmpB
                H[ii, :] = tmpH
                mu[ii, :] = tmpmu


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
    )
    Angle = DataLinspace(
        name="angle",
        unit="rad",
        symmetries={},
        initial=angle[0],
        final=angle[-1],
        number=Na_tot,
    )
    output.mag.Br = DataTime(
        name="Airgap radial flux density",
        unit="T",
        symbol="B_r",
        axes=[Time, Angle],
        values=Br,
    )
    output.mag.Bt = DataTime(
        name="Airgap tangential flux density",
        unit="T",
        symbol="B_t",
        axes=[Time, Angle],
        values=Bt,
    )
    output.mag.Tem = Tem
    output.mag.Tem_av = mean(Tem)
    if output.mag.Tem_av != 0:
        output.mag.Tem_rip = abs((np_max(Tem) - np_min(Tem)) / output.mag.Tem_av)
    output.mag.Phi_wind_stator = Phi_wind_stator
    output.mag.FEMM_dict = FEMM_dict

    if self.is_get_mesh:
        output.mag.meshsolution = self.build_meshsolution(Nt_tot, meshFEMM, Time, B, H, mu)

    if self.is_save_FEA:
        save_path_fea = join(save_path, "MeshSolutionFEMM.json")
        output.mag.meshsolution.save(save_path_fea)

    if (
        hasattr(output.simu.machine.stator, "winding")
        and output.simu.machine.stator.winding is not None
    ):
        # Electromotive forces computation (update output)
        self.comp_emf()
    else:
        output.mag.emf = None

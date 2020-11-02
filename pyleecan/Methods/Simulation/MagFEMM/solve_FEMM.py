import numpy as np

from numpy import zeros, pi, roll
from os.path import basename, splitext

from ....Functions.FEMM.update_FEMM_simulation import update_FEMM_simulation
from ....Functions.FEMM.comp_FEMM_torque import comp_FEMM_torque
from ....Functions.FEMM.comp_FEMM_Phi_wind import comp_FEMM_Phi_wind


def solve_FEMM(self, femm, output, sym, Nt, angle, Is, Ir, angle_rotor):
    """
    Solve FEMM model to calculate airgap flux density, torque instantaneous/average/ripple values,
    flux induced in stator windings and flux density, field and permeability maps

    /!\ Any changes in solve_FEMM must be also made in solve_FEMM_parallel

    Parameters
    ----------
    self: MagFEMM
        A MagFEMM object
    femm: FEMMHandler
        Object to handle FEMM
    output: Output
        An Output object
    sym: int
        Spatial symmetry factor
    Nt: int
        Number of time steps for calculation
    angle: ndarray
        Angle vector for calculation
    Is : ndarray 
        Stator current matrix [qs,Nt]
    Ir : ndarray
        Stator current matrix [qs,Nt]
    angle_rotor: ndarray
        Rotor angular position vector for calculation
    """
    # Init outputs
    meshFEMM, B_elem, H_elem, mu_elem, groups = None, None, None, None, None
    
    # Number of angular steps
    Na = angle.size

    # Loading parameters for readibility
    Rag = output.simu.machine.comp_Rgap_mec()
    L1 = output.simu.machine.stator.comp_length()
    save_path = self.get_path_save(output)
    FEMM_dict = output.mag.FEA_dict
    is_internal_rotor = output.simu.machine.rotor.is_internal
    
    # Init stator winding flux matrix
    if (
        hasattr(output.simu.machine.stator, "winding")
        and output.simu.machine.stator.winding is not None
    ):
        qs = output.simu.machine.stator.winding.qs  # Winding phase number
        Npcpp = output.simu.machine.stator.winding.Npcpp
        Phi_wind_stator = zeros((Nt, qs))
    else:
        Phi_wind_stator = None

    # Create the mesh
    # femm.mi_createmesh()

    # Initialize results matrix
    Br = zeros((Nt, Na))
    Bt = zeros((Nt, Na))
    Tem = zeros((Nt))  

    # Compute the data for each time step
    for ii in range(Nt):
        self.get_logger().debug("Solving step " + str(ii + 1) + " / " + str(Nt))
        # Update rotor position and currents
        # circuits, is_mmfs, is_mmfr, angle_rotor, Is, Ir, is_sliding_band, is_internal_rotor, Npcpp_stator, Npcpp_rotor
        update_FEMM_simulation(
            femm=femm,
            circuits=FEMM_dict["circuits"],
            is_sliding_band=self.is_sliding_band,
            is_internal_rotor=is_internal_rotor,
            angle_rotor=angle_rotor,
            Is=Is,
            Ir=Ir,
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

        # Load results
        femm.mi_loadsolution()

        # Get the flux result
        if self.is_sliding_band:
            for jj in range(Na):
                Br[ii, jj], Bt[ii, jj] = femm.mo_getgapb("bc_ag2", angle[jj] * 180 / pi)
        else:
            for jj in range(Na):
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
        if (self.is_sliding_band or Nt == 1) and (
            self.is_get_mesh or self.is_save_FEA
        ):
            tmpmeshFEMM, tmpB, tmpH, tmpmu, tmpgroups = self.get_meshsolution(
                femm, save_path, ii
            )

            if ii == 0:
                meshFEMM = [tmpmeshFEMM]
                groups = [tmpgroups]
                B_elem = np.zeros([Nt, meshFEMM[ii].cell["triangle"].nb_cell, 3])
                H_elem = np.zeros([Nt, meshFEMM[ii].cell["triangle"].nb_cell, 3])
                mu_elem = np.zeros([Nt, meshFEMM[ii].cell["triangle"].nb_cell])

            B_elem[ii, :, 0:2] = tmpB
            H_elem[ii, :, 0:2] = tmpH
            mu_elem[ii, :] = tmpmu

    # Shift to take into account stator position
    roll_id = int(self.angle_stator * Na / (2 * pi))
    Br = roll(Br, roll_id, axis=1)
    Bt = roll(Bt, roll_id, axis=1)

    if self.is_close_femm:
        femm.closefemm()
        
    return Br, Bt, Tem, Phi_wind_stator, FEMM_dict, meshFEMM, B_elem, H_elem, mu_elem, groups

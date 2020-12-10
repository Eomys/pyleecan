from os.path import basename, splitext

from numpy import zeros, pi, roll, cos, sin

# from scipy.interpolate import interp1d

from ....Classes._FEMMHandler import _FEMMHandler
from ....Functions.FEMM.update_FEMM_simulation import update_FEMM_simulation
from ....Functions.FEMM.comp_FEMM_torque import comp_FEMM_torque
from ....Functions.FEMM.comp_FEMM_Phi_wind import comp_FEMM_Phi_wind


def solve_FEMM(
    self,
    femm,
    output,
    out_dict,
    FEMM_dict,
    sym,
    Nt,
    angle,
    Is,
    Ir,
    angle_rotor,
    is_close_femm,
    filename=None,
    start_t=0,
    end_t=None,
):
    """
    Solve FEMM model to calculate airgap flux density, torque instantaneous/average/ripple values,
    flux induced in stator windings and flux density, field and permeability maps

    Parameters
    ----------
    self: MagFEMM
        A MagFEMM object
    femm: _FEMMHandler
        Object to handle FEMM
    output: Output
        An Output object
    out_dict: dict
        Dict containing the following quantities to update for each time step:
            Br : ndarray
                Airgap radial flux density (Nt,Na) [T]
            Bt : ndarray
                Airgap tangential flux density (Nt,Na) [T]
            Tem : ndarray
                Electromagnetic torque over time (Nt,) [Nm]
            Phi_wind : list of ndarray # TODO should it rather be a dict with lam label?
                List of winding flux with respect to Machine.get_lamlist (qs,Nt) [Wb]
    FEMM_dict : dict
        Dict containing FEMM model parameters
    sym: int
        Spatial symmetry factor
    Nt: int
        Number of time steps for calculation
    angle: ndarray
        Angle vector for calculation
    Is : ndarray
        Stator current matrix (qs,Nt) [A]
    Ir : ndarray
        Stator current matrix (qs,Nt) [A]
    angle_rotor: ndarray
        Rotor angular position vector (Nt,)
    is_close_femm: bool
        True to close FEMM handler in the end
    filename: str
        Path to FEMM model to open
    start_t: int
        Index of first time step (0 by default, used for parallelization)
    end_t: int
        Index of last time step (Nt by default, used for parallelization)

    Returns
    -------
    B: ndarray
        3D Magnetic flux density for all time steps and each element (Nt, Nelem, 3) [T]
    H : ndarray
        3D Magnetic field for all time steps and each element (Nt, Nelem, 3) [A/m]
    mu : ndarray
        Magnetic relative permeability for all time steps and each element (Nt, Nelem) []
    mesh: MeshMat
        Object containing magnetic mesh at first time step
    groups: dict
        Dict whose values are group label and values are array of indices of related elements

    """
    # Open FEMM file if not None, else it is already open
    if filename is not None:
        try:
            # Open the document
            femm.openfemm(1)
        except:
            # Create a new FEMM handler in case of parallelization on another FEMM instance
            femm = _FEMMHandler()
            output.mag.internal.handler_list.append(femm)
            # Open the document
            femm.openfemm(1)

        # Import FEMM file
        femm.opendocument(filename)

    # Take last time step at Nt by default
    if end_t is None:
        end_t = Nt

    # Init mesh solution as None since array allocation can only be done once
    # number of elements is known, i.e. after first time step resolution
    B_elem, H_elem, mu_elem, meshFEMM, groups = None, None, None, None, None

    # Number of angular steps
    Na = angle.size

    # Loading parameters for readibility
    machine = output.simu.machine
    Rag = machine.comp_Rgap_mec()
    L1 = machine.stator.comp_length()
    save_path = self.get_path_save(output)
    is_internal_rotor = machine.rotor.is_internal
    if "Phi_wind" in out_dict:
        qs = []
        Npcpp = []
        for idx, lam in enumerate(machine.get_lam_list()):
            if out_dict["Phi_wind"][idx] is not None:
                qs.append(lam.winding.qs)  # Winding phase number
                Npcpp.append(lam.winding.Npcpp)  # parallel paths
            else:
                qs.append(None)
                Npcpp.append(None)

    # Account for initial angular shift of stator and rotor and apply it to the sliding band
    angle_shift = self.angle_rotor_shift - self.angle_stator_shift

    # Compute the data for each time step
    for ii in range(start_t, end_t):
        self.get_logger().debug("Solving step " + str(ii + 1) + " / " + str(Nt))
        # Update rotor position and currents
        update_FEMM_simulation(
            femm=femm,
            circuits=FEMM_dict["circuits"],
            is_sliding_band=self.is_sliding_band,
            is_internal_rotor=is_internal_rotor,
            angle_rotor=angle_rotor + angle_shift,
            Is=Is,
            Ir=Ir,
            ii=ii,
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
                out_dict["Br"][ii, jj], out_dict["Bt"][ii, jj] = femm.mo_getgapb(
                    "bc_ag2", angle[jj] * 180 / pi
                )
        else:
            for jj in range(Na):
                B = femm.mo_getb(Rag * cos(angle[jj]), Rag * sin(angle[jj]))
                out_dict["Br"][ii, jj] = B[0] * cos(angle[jj]) + B[1] * sin(angle[jj])
                out_dict["Bt"][ii, jj] = -B[0] * sin(angle[jj]) + B[1] * cos(angle[jj])

        # Compute the torque
        out_dict["Tem"][ii] = comp_FEMM_torque(femm, FEMM_dict, sym=sym)

        if "Phi_wind" in out_dict:
            # Phi_wind computation
            # TODO fix inconsistency for multi lam machines here
            for idx, lam in enumerate(machine.get_lam_list()):
                if out_dict["Phi_wind"][idx] is not None:
                    out_dict["Phi_wind"][idx][ii, :] = comp_FEMM_Phi_wind(
                        femm,
                        qs[idx],
                        Npcpp[idx],
                        is_stator=lam.is_stator,
                        Lfemm=FEMM_dict["Lfemm"],
                        L1=L1,
                        sym=sym,
                    )

        # Load mesh data & solution
        if (self.is_sliding_band or Nt == 1) and (self.is_get_mesh or self.is_save_FEA):
            # Get mesh data and magnetic quantities from .ans file
            tmpmeshFEMM, tmpB, tmpH, tmpmu, tmpgroups = self.get_meshsolution(
                femm,
                save_path,
                j_t0=ii,
                id_worker=start_t,
                is_get_mesh=ii == start_t,
            )

            # Initialize mesh and magnetic quantities for first time step
            if ii == start_t:
                meshFEMM = [tmpmeshFEMM]
                groups = [tmpgroups]
                Nelem = meshFEMM[0].cell["triangle"].nb_cell
                Nt0 = end_t - start_t
                B_elem = zeros([Nt0, Nelem, 3])
                H_elem = zeros([Nt0, Nelem, 3])
                mu_elem = zeros([Nt0, Nelem])

            # Shift time index ii in case start_t is not 0 (parallelization)
            ii0 = ii - start_t
            # Store magnetic flux density, field and relative permeability for the current time step
            B_elem[ii0, :, 0:2] = tmpB
            H_elem[ii0, :, 0:2] = tmpH
            mu_elem[ii0, :] = tmpmu

    # Shift to take into account stator position
    if self.angle_stator_shift != 0:
        roll_id = int(self.angle_stator_shift * Na / (2 * pi))
        out_dict["Br"] = roll(out_dict["Br"], roll_id, axis=1)
        out_dict["Bt"] = roll(out_dict["Bt"], roll_id, axis=1)

        # # Interpolate on updated angular position # TODO to improve accuracy
        # angle_new = (angle - self.angle_stator_shift) % (2 * pi / sym)
        # out_dict["Br"] = interp1d(append(angle, 2 * pi / sym), append(out_dict["Br"], out_dict["Br"][:,0]), axis=1)[angle_new]
        # out_dict["Bt"] = interp1d(append(angle, 2 * pi / sym), append(out_dict["Bt"], out_dict["Bt"][:,0]), axis=1)[angle_new]

    # Close FEMM handler
    if is_close_femm:
        femm.closefemm()
        output.mag.internal.handler_list.remove(femm)

    return B_elem, H_elem, mu_elem, meshFEMM, groups

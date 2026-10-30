from numpy import zeros

from ....Classes._FEMMHandler import _FEMMHandler
from ....Classes.OutMagFEMM import OutMagFEMM
from ....Functions.FEMM.draw_FEMM import draw_FEMM
from ....Functions.labels import STATOR_LAB


def comp_flux_airgap(self, output, axes_dict, Is_val=None, Ir_val=None):
    """Build and solve FEMM model to calculate and store magnetic quantities

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    output : Output
        an Output object
    axes_dict: {Data}
        Dict of axes used for magnetic calculation

    Returns
    -------
    out_dict: dict
        Dict containing the following quantities:
            Br : ndarray
                Airgap radial flux density (Nt,Na) [T]
            Bt : ndarray
                Airgap tangential flux density (Nt,Na) [T]
            Tem : ndarray
                Electromagnetic torque over time (Nt,) [Nm]
            Phi_wind_stator : ndarray
                Stator winding flux (qs,Nt) [Wb]
            Phi_wind : dict
                Dict of winding fluxlinkage with respect to Machine.get_lam_list_label (qs,Nt) [Wb]
            meshsolution: MeshSolution
                MeshSolution object containing magnetic quantities B, H, mu for each time step
    """

    logger = self.get_logger()

    # Init output
    out_dict = dict()
    if output.mag.internal is None:
        output.mag.internal = OutMagFEMM()

    # Get time and angular axes
    Angle = axes_dict["angle"]
    Time = axes_dict["time"]

    # Set the angular symmetry factor according to the machine and check if it is anti-periodic
    sym, is_antiper_a = Angle.get_periodicity()

    # Import angular vector from Data object
    angle = Angle.get_values(
        is_oneperiod=self.is_periodicity_a,
        is_antiperiod=is_antiper_a and self.is_periodicity_a,
    )
    Na = angle.size

    # Check if the time axis is anti-periodic
    _, is_antiper_t = Time.get_periodicity()

    # Number of time steps
    time = Time.get_values(
        is_oneperiod=self.is_periodicity_t,
        is_antiperiod=is_antiper_t and self.is_periodicity_t,
    )
    Nt = time.size

    # Get rotor angular position
    angle_rotor = output.get_angle_rotor()[0:Nt]

    # Setup the FEMM simulation
    # Geometry building and assigning property in FEMM
    # Instanciate a new FEMM
    femm = _FEMMHandler()
    output.mag.internal.handler_list.append(femm)
    if self.import_file is None:
        path_femm = self.get_path_save_fem(output)
        logger.debug("Drawing machine in FEMM at " + path_femm)
        FEMM_dict = draw_FEMM(
            femm,
            output,
            is_mmfr=self.is_mmfr,
            is_mmfs=self.is_mmfs,
            sym=sym,
            is_antiper=is_antiper_a,
            type_calc_leakage=self.type_calc_leakage,
            is_remove_ventS=self.is_remove_ventS,
            is_remove_ventR=self.is_remove_ventR,
            is_remove_slotS=self.is_remove_slotS,
            is_remove_slotR=self.is_remove_slotR,
            type_BH_stator=self.type_BH_stator,
            type_BH_rotor=self.type_BH_rotor,
            kgeo_fineness=self.Kgeo_fineness,
            kmesh_fineness=self.Kmesh_fineness,
            user_FEMM_dict=self.FEMM_dict_enforced,
            path_save=path_femm,
            is_sliding_band=self.is_sliding_band,
            transform_list=self.transform_list,
            rotor_dxf=self.rotor_dxf,
            stator_dxf=self.stator_dxf,
            is_fast_draw=self.is_fast_draw,
            T_mag=self.T_mag,
        )
    else:
        logger.debug("Reusing the FEMM file: " + self.import_file)
        if output.mag.internal.FEMM_dict is not None:
            FEMM_dict = output.mag.internal.FEMM_dict
        else:
            FEMM_dict = self.FEMM_dict_enforced

    # Init flux arrays in out_dict
    out_dict["B_{rad}"] = zeros((Nt, Na))
    out_dict["B_{circ}"] = zeros((Nt, Na))
    if self.is_calc_torque_energy:
        # Init torque array in out_dict
        out_dict["Tem"] = zeros(Nt)
    # Init lamination winding flux list of arrays in out_dict
    machine = output.simu.machine
    out_dict["Phi_wind"] = {}
    axes_dict_elec = output.elec.axes_dict
    for label in machine.get_lam_list_label():
        if "phase_" + label in axes_dict_elec:
            qs = axes_dict_elec["phase_" + label].get_length(is_smallestperiod=True)
            out_dict["Phi_wind"][label] = zeros((Nt, qs))
    # delete 'Phi_wind' if empty
    if len(out_dict["Phi_wind"]) == 0:
        out_dict.pop("Phi_wind")

    # Solve for all time step and store all the results in out_dict
    if self.nb_worker > 1:
        # A Femm handler will be created for each worker
        femm.closefemm()
        output.mag.internal.handler_list.remove(femm)
        # With parallelization
        (
            B_elem,
            H_elem,
            mu_elem,
            A_node,
            meshFEMM,
            groups,
            A_elem,
        ) = self.solve_FEMM_parallel(
            femm,
            output,
            out_dict,
            FEMM_dict=FEMM_dict,
            sym=sym,
            Nt=Nt,
            angle=angle,
            Is=Is_val,
            Ir=Ir_val,
            angle_rotor=angle_rotor,
            filename=self.import_file,
        )
    else:
        # Without parallelization
        B_elem, H_elem, mu_elem, A_node, meshFEMM, groups, A_elem = self.solve_FEMM(
            femm,
            output,
            out_dict,
            FEMM_dict=FEMM_dict,
            sym=sym,
            Nt=Nt,
            angle=angle,
            Is=Is_val,
            Ir=Ir_val,
            angle_rotor=angle_rotor,
            is_close_femm=self.is_close_femm,
            filename=self.import_file,
        )

    # Store FEMM_dict in to avoid drawing the machine several times
    output.mag.internal.FEMM_dict = FEMM_dict

    # Store stator winding flux
    if STATOR_LAB + "-0" in out_dict["Phi_wind"].keys():
        out_dict["Phi_wind_stator"] = out_dict["Phi_wind"][STATOR_LAB + "-0"]

    # Store mesh data & solution
    if self.is_get_meshsolution and B_elem is not None:
        if self.is_periodicity_t:
            # Reduce output quantities to original number of time steps
            Nt_S = axes_dict["time_S"].get_length(is_smallestperiod=True)
            quantity_list = [
                "B_{rad}",
                "B_{circ}",
                "Phi_wind",
                "Tem",
                "Phi_wind_stator",
            ]
            for quantity in quantity_list:
                if quantity in out_dict:
                    if quantity == "Phi_wind":
                        for key, val in out_dict[quantity].items():
                            out_dict[quantity][key] = val[:Nt_S, ...]
                    else:
                        out_dict[quantity] = out_dict[quantity][:Nt_S, ...]

            self.build_meshsolution_dict(
                out_dict,
                axes_dict,
                B_elem,
                H_elem,
                mu_elem,
                A_node,
                meshFEMM,
                groups,
                A_elem,
            )

        else:
            self.build_meshsolution(
                out_dict,
                axes_dict,
                B_elem,
                H_elem,
                mu_elem,
                A_node,
                meshFEMM,
                groups,
                A_elem,
            )

    return out_dict

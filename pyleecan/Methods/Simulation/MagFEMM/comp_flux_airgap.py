from os.path import isfile
from shutil import copyfile

from numpy import zeros

from SciDataTool import Data1D

from ....Classes._FEMMHandler import _FEMMHandler
from ....Classes.OutMagFEMM import OutMagFEMM

from ....Functions.labels import STATOR_LAB
from ....Functions.FEMM.draw_FEMM import draw_FEMM
from ....Functions.MeshSolution.build_solution_data import build_solution_data
from ....Functions.MeshSolution.build_meshsolution import build_meshsolution
from ....Functions.MeshSolution.build_solution_vector import build_solution_vector


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
        out_dict["Tem"] = zeros((Nt))
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

        # Define axis
        Time = Time.copy()
        meshFEMM[0].sym = sym
        meshFEMM[0].is_antiper_a = is_antiper_a
        indices_cell = meshFEMM[0].cell["triangle"].indice
        Indices_Cell = Data1D(
            name="indice", values=indices_cell, is_components=True, is_overlay=False
        )
        # Slice = axes_dict["z"]
        axis_list = [Time, Indices_Cell]

        B_sol = build_solution_vector(
            field=B_elem[:, :, None, :],  # quick fix for slice issue
            axis_list=axis_list,
            name="Magnetic Flux Density",
            symbol="B",
            unit="T",
        )
        H_sol = build_solution_vector(
            field=H_elem[:, :, None, :],
            axis_list=axis_list,
            name="Magnetic Field",
            symbol="H",
            unit="A/m",
        )
        mu_sol = build_solution_data(
            field=mu_elem[:, :, None],
            axis_list=axis_list,
            name="Magnetic Permeability",
            symbol="\mu",
            unit="H/m",
        )
        Ae_sol = build_solution_data(
            field=A_elem[:, :, None],
            axis_list=axis_list,
            name="Magnetic Potential Vector (per element)",
            symbol="A_z^{element}",
            unit="Wb/m",
        )

        indices_nodes = meshFEMM[0].node.indice
        Indices_Nodes = Data1D(name="indice", values=indices_nodes, is_components=True)
        axis_list_node = [Time, Indices_Nodes]

        An_sol = build_solution_data(
            field=A_node,
            axis_list=axis_list_node,
            name="Magnetic Potential Vector (nodal)",
            symbol="A_z",
            unit="Wb/m",
        )
        An_sol.type_cell = "node"

        list_solution = [B_sol, H_sol, mu_sol, An_sol, Ae_sol]

        out_dict["meshsolution"] = build_meshsolution(
            list_solution=list_solution,
            label="FEMM 2D Magnetostatic",
            list_mesh=meshFEMM,
            group=groups,
        )

    return out_dict

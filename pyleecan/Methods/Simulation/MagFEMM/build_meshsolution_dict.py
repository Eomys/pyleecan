from numpy import array, unique
from numpy import mean as np_mean
from SciDataTool import Data1D

from ....Functions.labels import ROTOR_LAB, STATOR_LAB
from ....Functions.MeshSolution.build_meshsolution import build_meshsolution
from ....Functions.MeshSolution.build_solution_data import build_solution_data
from ....Functions.MeshSolution.build_solution_vector import build_solution_vector


def build_meshsolution_dict(
    self, out_dict, axes_dict, B_elem, H_elem, mu_elem, A_node, meshFEMM, groups, A_elem
):
    """Build meshsolution dict from FEMM results.
    The meshsolution dict contains meshsolution for stator and rotor frame with their respective time periodicity.

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    out_dict: dict
        Dict containing the magnetic quantities resulting from FEMM calculations
    axes_dict: {Data}
        Dict of axes used for magnetic calculation
    B_elem: ndarray
        3D Magnetic flux density for each element (Nelem, 3) [T]
    H_elem : ndarray
        3D Magnetic field for each element (Nelem, 3) [A/m]
    mu_elem : ndarray
        Magnetic relative permeability for each element (Nelem,1) []
    A_node : ndarray
        Magnetic Vector Potential for each node (Nnode,1) []
    mesh: MeshMat
        Object containing magnetic mesh
    groups: dict
        Dict whose values are group label and values are array of indices of related elements
    A_elem : ndarray
        Magnetic Vector Potential for each elem (Nelem,1) []

    """

    machine = self.parent.machine

    # Get the angular symmetry factor
    sym, is_antiper_a = axes_dict["angle"].get_periodicity()

    # Separate stator and rotor elements
    list_elem_R = list()
    list_elem_S = list()
    groups_R = dict()
    groups_S = dict()
    for name, ind in groups.items():
        if STATOR_LAB.lower() in name:
            list_elem_S.extend(ind)
            groups_S[name] = ind
        elif ROTOR_LAB.lower() in name:
            list_elem_R.extend(ind)
            groups_R[name] = ind
        elif "airgap" in name:
            if self.Rag_enforced is not None:
                # Take enforced value
                Rag = self.Rag_enforced
            else:
                Rag = machine.comp_Rgap_mec()
            # Separate airgap belonging to rotor and airgap belonging to stator
            elem_ag_coords = meshFEMM.get_element_coordinate(element_indices=ind)[
                "triangle"
            ]
            elem_ag_centers = np_mean(elem_ag_coords, axis=1)
            elem_ag_dist = elem_ag_centers[:, 0] ** 2 + elem_ag_centers[:, 1] ** 2
            if machine.rotor.is_internal:
                is_elem_ag_R = elem_ag_dist < Rag**2
            else:
                is_elem_ag_R = elem_ag_dist > Rag**2
            list_elem_ag_R = array(ind)[is_elem_ag_R].tolist()
            list_elem_ag_S = array(ind)[~is_elem_ag_R].tolist()

            if len(list_elem_ag_R) > 0:
                list_elem_R.extend(list_elem_ag_R)
                groups_R[name + "_R"] = list_elem_ag_R
            if len(list_elem_ag_S) > 0:
                list_elem_S.extend(list_elem_ag_S)
                groups_S[name + "_S"] = list_elem_ag_S
    list_elem_R = unique(list_elem_R).tolist()
    list_elem_S = unique(list_elem_S).tolist()

    # Define axes
    meshFEMM.sym = sym
    meshFEMM.is_antiper_a = is_antiper_a

    Indice_Element = Data1D(
        name="indice",
        values=array(meshFEMM.element_dict["triangle"].indice),
        is_components=True,
        is_overlay=False,
    )

    Indice_Element_R = Data1D(
        name="indice",
        values=list_elem_R,
        is_components=True,
        is_overlay=False,
    )
    axis_list_R = [axes_dict["time_R"].copy(), Indice_Element_R]

    Indice_Element_S = Data1D(
        name="indice",
        values=list_elem_S,
        is_components=True,
        is_overlay=False,
    )
    axis_list = [axes_dict["time_S"].copy(), Indice_Element_S]

    # Store element values in stator frame
    # Reduce mesh quantities to original number of time steps
    Nt_S = axes_dict["time_S"].get_length(is_smallestperiod=True)
    B_sol = build_solution_vector(
        field=B_elem[:Nt_S, list_elem_S, None, :],  # quick fix for slice issue
        axis_list=axis_list,
        name="Magnetic Flux Density",
        symbol="B",
        unit="T",
    )
    Ae_sol = build_solution_data(
        field=A_elem[:Nt_S, list_elem_S, None],
        axis_list=axis_list,
        name="Magnetic Potential Vector (per element)",
        symbol="A_z^{element}",
        unit="Wb/m",
    )

    # Store element values in rotor frame
    B_sol_R = build_solution_vector(
        field=B_elem[:, list_elem_R, None, :],  # quick fix for slice issue
        axis_list=axis_list_R,
        name="Magnetic Flux Density",
        symbol="B",
        unit="T",
    )
    Ae_sol_R = build_solution_data(
        field=A_elem[:, list_elem_R, None],
        axis_list=axis_list_R,
        name="Magnetic Potential Vector (per element)",
        symbol="A_z^{element}",
        unit="Wb/m",
    )

    if self.type_meshsolution == 1:
        # Only store element flux density B and element vector potential Ae

        # Build solution vector/data dicts
        solution_dict_S = {solution.label: solution for solution in [B_sol, Ae_sol]}

        solution_dict_R = {solution.label: solution for solution in [B_sol_R, Ae_sol_R]}

    elif self.type_meshsolution == 0:
        Indice_Node = Data1D(
            name="indice",
            values=array(meshFEMM.node.indice),
            is_components=True,
            is_overlay=False,
        )

        H_sol = build_solution_vector(
            field=H_elem[:Nt_S, list_elem_S, None, :],
            axis_list=axis_list,
            name="Magnetic Field",
            symbol="H",
            unit="A/m",
        )
        mu_sol = build_solution_data(
            field=mu_elem[:Nt_S, list_elem_S, None],
            axis_list=axis_list,
            name="Magnetic Permeability",
            symbol="\\mu",
            unit="H/m",
        )

        H_sol_R = build_solution_vector(
            field=H_elem[:, list_elem_R, None, :],
            axis_list=axis_list_R,
            name="Magnetic Field",
            symbol="H",
            unit="A/m",
        )
        mu_sol_R = build_solution_data(
            field=mu_elem[:, list_elem_R, None],
            axis_list=axis_list_R,
            name="Magnetic Permeability",
            symbol="\\mu",
            unit="H/m",
        )

        # Store nodal MVP in all motor (separate rotor and stator values)
        elem_con = meshFEMM.element_dict["triangle"].connectivity
        indice_node_S = unique(elem_con[list_elem_S, :].flatten()).astype(int)
        indice_node_R = unique(elem_con[list_elem_R, :].flatten()).astype(int)

        Indice_Node_S = Data1D(name="indice", values=indice_node_S, is_components=True)
        Indice_Node_R = Data1D(name="indice", values=indice_node_R, is_components=True)

        axis_list_node_S = [axes_dict["time_S"].copy(), Indice_Node_S]
        axis_list_node_R = [axes_dict["time_R"].copy(), Indice_Node_R]

        An_sol_S = build_solution_data(
            field=A_node[:Nt_S, indice_node_S],
            axis_list=axis_list_node_S,
            name="Magnetic Potential Vector (nodal)",
            symbol="A_z",
            unit="Wb/m",
            type_element="node",
        )

        An_sol_R = build_solution_data(
            field=A_node[:, indice_node_R],
            axis_list=axis_list_node_R,
            name="Magnetic Potential Vector (nodal)",
            symbol="A_z",
            unit="Wb/m",
            type_element="node",
        )

        # Build solution vector dicts
        solution_dict_S = {
            solution.label: solution
            for solution in [B_sol, H_sol, mu_sol, Ae_sol, An_sol_S]
        }

        solution_dict_R = {
            solution.label: solution
            for solution in [B_sol_R, H_sol_R, mu_sol_R, Ae_sol_R, An_sol_R]
        }

        # Store node indices axes in axes_dict
        axes_dict["indice_node"] = Indice_Node
        axes_dict["indice_node_S"] = Indice_Node_S
        axes_dict["indice_node_R"] = Indice_Node_R

    # Build meshsolutions dict for stator and rotor frame
    meshsolution_dict = {
        STATOR_LAB + "-0": build_meshsolution(
            solution_dict=solution_dict_S,
            label="FEMM 2D Magnetostatic Stator",
            mesh=meshFEMM,
            group=groups_S,
        ),
        ROTOR_LAB + "-0": build_meshsolution(
            solution_dict=solution_dict_R,
            label="FEMM 2D Magnetostatic Rotor",
            mesh=meshFEMM,
            group=groups_R,
        ),
    }

    # Store element indices axes in axes_dict
    axes_dict["indice_element"] = Indice_Element
    axes_dict["indice_element_S"] = Indice_Element_S
    axes_dict["indice_element_R"] = Indice_Element_R

    # Store meshsolution dict in out_dict
    out_dict["meshsolution_dict"] = meshsolution_dict

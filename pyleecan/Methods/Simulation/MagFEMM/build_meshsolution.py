from numpy import array
from SciDataTool import Data1D

from ....Functions.MeshSolution.build_meshsolution import (
    build_meshsolution as build_meshsolution_fct,
)
from ....Functions.MeshSolution.build_solution_data import build_solution_data
from ....Functions.MeshSolution.build_solution_vector import build_solution_vector


def build_meshsolution(
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

    # Get the angular symmetry factor
    sym, is_antiper_a = axes_dict["angle"].get_periodicity()

    # Define axes
    meshFEMM.sym = sym
    meshFEMM.is_antiper_a = is_antiper_a

    Indice_Element = Data1D(
        name="indice",
        values=array(meshFEMM.element_dict["triangle"].indice),
        is_components=True,
        is_overlay=False,
    )

    axis_list = [axes_dict["time"].copy(), Indice_Element]

    B_sol = build_solution_vector(
        field=B_elem[:, :, None, :],  # quick fix for slice issue
        axis_list=axis_list,
        name="Magnetic Flux Density",
        symbol="B",
        unit="T",
    )

    Ae_sol = build_solution_data(
        field=A_elem[:, :, None],
        axis_list=axis_list,
        name="Magnetic Potential Vector (per element)",
        symbol="A_z^{element}",
        unit="Wb/m",
    )

    if self.type_meshsolution == 1:
        # Only store element flux density B and element vector potential Ae

        # Build solution vector/data dict
        solution_dict = {solution.label: solution for solution in [B_sol, Ae_sol]}

    elif self.type_meshsolution == 0:
        Indice_Node = Data1D(
            name="indice",
            values=array(meshFEMM.node.indice),
            is_components=True,
            is_overlay=False,
        )

        axis_list_node = [axes_dict["time"].copy(), Indice_Node]

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
            symbol="\\mu",
            unit="H/m",
        )

        An_sol = build_solution_data(
            field=A_node,
            axis_list=axis_list_node,
            name="Magnetic Potential Vector (nodal)",
            symbol="A_z",
            unit="Wb/m",
            type_element="node",
        )

        # Build solution vector/data dict
        solution_dict = {
            solution.label: solution
            for solution in [B_sol, H_sol, mu_sol, An_sol, Ae_sol]
        }

        # Store node indices axes in axes_dict
        axes_dict["indice_node"] = Indice_Node

    ms_mag = build_meshsolution_fct(
        solution_dict=solution_dict,
        label="FEMM 2D Magnetostatic",
        mesh=meshFEMM,
        group=groups,
    )

    # Store element indices axes in axes_dict
    axes_dict["indice_element"] = Indice_Element

    # Store meshsolution dict in out_dict
    out_dict["meshsolution"] = ms_mag

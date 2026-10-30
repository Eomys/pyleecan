import numpy as np

from ....Classes.SolutionData import SolutionData
from ....Classes.SolutionVector import SolutionVector
from ....Functions.labels import ROTOR_LAB, STATOR_LAB
from ....Functions.MeshSolution.build_meshsolution import build_meshsolution
from ....Functions.MeshSolution.build_solution_data import build_solution_data
from ....Functions.MeshSolution.build_solution_vector import build_solution_vector


def get_meshsolution(self, Time=None):
    """Get mesholution object if it exists, if not calculate it from meshsolution_dict based on input Time axis.

    Parameters
    ----------
    self : OutMag
        a OutMag object

    Returns
    -------
    groups: dict
        Dict whose values are group label and values are array of indices of related elements
    """

    if self.meshsolution is None and self.meshsolution_dict is not None:
        if Time is None:
            Time = self.axes_dict["time"].get_axis_periodic(Nper=1, is_aper=False)

        time_val = Time.get_values(is_smallestperiod=True)

        meshsol_S = self.meshsolution_dict[STATOR_LAB + "-0"]
        meshsol_R = self.meshsolution_dict[ROTOR_LAB + "-0"]

        # Get full mesh from meshsolution containing stator results (meshsolution for rotor has the full mesh as well)
        mesh = meshsol_S.mesh

        Indice_Element = self.axes_dict["indice_element"]
        Indice_Node = self.axes_dict["indice_node"]

        indice_element = Indice_Element.values
        indice_element_S = self.axes_dict["indice_element_S"].values
        indice_element_R = self.axes_dict["indice_element_R"].values
        indice_node = Indice_Node.values
        indice_node_S = self.axes_dict["indice_node_S"].values
        indice_node_R = self.axes_dict["indice_node_R"].values

        Nelem = indice_element.size
        Nnode = indice_node.size

        Nt = time_val.size
        Nz = self.axes_dict["z"].get_length(is_pattern=True)

        # Rebuild solution dict containing both stator and rotor element values
        solution_dict = {}
        for sol_S, sol_R in zip(meshsol_S.values(), meshsol_R.values()):
            if sol_S.type_element == "node":
                Nval = Nnode
                ind_S = indice_node_S
                ind_R = indice_node_R
                axis_list = [
                    Time.copy(),
                    Indice_Node.copy(),
                    self.axes_dict["z"].copy(),
                ]
            else:
                Nval = Nelem
                ind_S = indice_element_S
                ind_R = indice_element_R
                axis_list = [
                    Time.copy(),
                    Indice_Element.copy(),
                    self.axes_dict["z"].copy(),
                ]

            # print(f"""{key} {sol_S.label+"_S"}  {sol_R.label+"_S"}""")
            if isinstance(sol_S, SolutionVector):
                # Case for B, H

                # Calculate stator and rotor VectorField on time values
                vf_S = sol_S.field.get_vectorfield_along(
                    "time=axis_data",
                    "indice",
                    "z[smallestpattern]",
                    axis_data={"time": time_val},
                )

                vf_R = sol_R.field.get_vectorfield_along(
                    "time=axis_data",
                    "indice",
                    "z[smallestpattern]",
                    axis_data={"time": time_val},
                )

                # Rebuild a SolutionVector for each component containing values for both rotor and stator elements
                # Rebuild values array in initial mesh format
                sol_val = np.zeros((Nt, Nval, Nz, 2), dtype=float)
                for ii, (comp_S, comp_R) in enumerate(
                    zip(
                        vf_S.components.values(),
                        vf_R.components.values(),
                    )
                ):
                    if comp_S.values.ndim == 2:  # No slices
                        # Add stator values for each component
                        sol_val[:, ind_S, :, ii] = comp_S.values.T[:, :, None]
                        # Add rotor values for each component
                        sol_val[:, ind_R, :, ii] = comp_R.values.T[:, :, None]
                    else:
                        # Add stator values for each component
                        sol_val[:, ind_S, :, ii] = comp_S.values.swapaxes(0, 1)
                        # Add rotor values for each component
                        sol_val[:, ind_R, :, ii] = comp_R.values.swapaxes(0, 1)

                solution_dict[sol_S.label] = build_solution_vector(
                    field=sol_val,
                    axis_list=axis_list,
                    name=vf_S.name,
                    symbol=sol_S.label,
                    unit=comp_S.unit,
                )

            elif isinstance(sol_S, SolutionData):
                # Case for Az_elem, Az_node, mu

                # Calculate stator and rotor DataTime on time values
                dt_S = sol_S.field.get_data_along(
                    "time=axis_data",
                    "indice",
                    "z[smallestpattern]",
                    axis_data={"time": time_val},
                )
                dt_R = sol_R.field.get_data_along(
                    "time=axis_data",
                    "indice",
                    "z[smallestpattern]",
                    axis_data={"time": time_val},
                )

                # Rebuild a SolutionVector for each component containing values for both rotor and stator elements
                # Rebuild values array in initial mesh format
                sol_val = np.zeros((Nt, Nval, Nz), dtype=float)

                if dt_S.values.ndim == 2:  # No slices
                    # Add stator values for each component
                    sol_val[:, ind_S, :] = dt_S.values[:, :, None]
                    # Add rotor values for each component
                    sol_val[:, ind_R, :] = dt_R.values[:, :, None]
                else:
                    # Add stator values for each component
                    sol_val[:, ind_S, :] = dt_S.values
                    # Add rotor values for each component
                    sol_val[:, ind_R, :] = dt_R.values

                solution_dict[sol_S.label] = build_solution_data(
                    field=sol_val,
                    axis_list=axis_list,
                    name=dt_S.name,
                    symbol=sol_S.label,
                    unit=dt_S.unit,
                )

            else:
                raise Exception("Expecting SolutionVector or SolutionData as field")

            solution_dict[sol_S.label].type_element = sol_S.type_element

        # Merge stator and rotor groups
        group = {}
        group = {"airgap": list(meshsol_S.group["airgap_S"])}
        group["airgap"].extend(list(meshsol_R.group["airgap_R"]))
        for key, val in meshsol_S.group.items():
            if "airgap" not in key:
                group[key] = list(val)
        for key, val in meshsol_R.group.items():
            if "airgap" not in key:
                group[key] = list(val)

        # Store all solutions into meshsolution
        self.meshsolution = build_meshsolution(
            solution_dict=solution_dict,
            label=meshsol_S.label,
            mesh=mesh,
            group=group,
        )

    return self.meshsolution

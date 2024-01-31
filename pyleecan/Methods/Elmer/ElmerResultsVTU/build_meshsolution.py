# -*- coding: utf-8 -*-
from os.path import join, split, splitext

from meshio import read
from numpy import arange
from SciDataTool import Data1D, DataTime, Norm_ref, VectorField

from ....Classes.MeshSolution import MeshSolution
from ....Classes.MeshVTK import MeshVTK
from ....Classes.SolutionData import SolutionData
from ....Classes.SolutionVector import SolutionVector
from ....Methods.Elmer.ElmerResultsVTU import ElmerResultsVTUError

# TODO add groups, see get_meshsolution of MagFEMM


def build_meshsolution(self):
    """Get the mesh and solution data from an Elmer VTU results file

    Parameters
    ----------
    self : ElmerResultsVTU
        a ElmerResultsVTU object

    Returns
    -------
    success: bool
        Information if meshsolution could be created

    """
    # create meshsolution
    meshsol = MeshSolution(label=self.label)

    # get the mesh
    save_path, fn = split(self.file_path)
    file_name, file_ext = splitext(fn)
    if file_ext != ".vtu":
        raise ElmerResultsVTUError("ElmerResultsVTU: Results file must be of type VTU.")

    meshvtk = MeshVTK(path=save_path, name=file_name, format="vtu")
    # TODO maybe convert to MeshMat before
    meshsol.mesh = meshvtk

    # get the solution data on the mesh
    meshsolvtu = read(self.file_path)
    pt_data = meshsolvtu.point_data  # point_data is of type dict

    # setup axes
    indices = arange(meshsolvtu.points.shape[0])
    Indices = Data1D(name="indice", values=indices, is_components=True)

    # store only data from store dict if available
    comp_ext = ["x", "y", "z"]

    for key, value in pt_data.items():
        # check if value should be stored
        if key in self.store_dict.keys():
            siz = value.shape[1]
            # only regard max. 3 components
            if siz > 3:
                self.get_logger().warning(
                    f'ElmerResultsVTU.build_meshsolution(): size of data "{key}" > 3'
                    + " - "
                    + "Data will be truncated."
                )
                siz = 3

            components = []
            comp_name = []

            # loop though components
            for i in range(siz):
                # setup name, symbol and component name extension
                if siz == 1:
                    ext = ""
                else:
                    ext = comp_ext[i]

                # setup data object
                data = DataTime(
                    name=self.store_dict[key]["name"] + " " + ext,
                    unit=self.store_dict[key]["unit"],
                    symbol=self.store_dict[key]["symbol"] + ext,
                    axes=[Indices],
                    values=value[:, i],
                    normalizations={"ref": Norm_ref(ref=self.store_dict[key]["norm"])},
                )
                components.append(data)
                comp_name.append("comp_" + ext)

            # setup solution depending on number of field components
            if siz == 1:
                field = components[0]
                solution = SolutionData(
                    field=field,
                    type_element="point",
                    label=self.store_dict[key]["symbol"],
                )

                label = self.store_dict[key]["symbol"]
                meshsol.add_solution(solution=solution, label=label)

            else:
                comps = {}
                for i in range(siz):
                    comps[comp_name[i]] = components[i]
                field = VectorField(
                    name=self.store_dict[key]["name"],
                    symbol=self.store_dict[key]["symbol"],
                    components=comps,
                )
                solution = SolutionVector(
                    field=field,
                    type_element="point",
                    label=self.store_dict[key]["symbol"],
                )
                label = self.store_dict[key]["symbol"]

                meshsol.add_solution(solution=solution, label=label)

    return meshsol

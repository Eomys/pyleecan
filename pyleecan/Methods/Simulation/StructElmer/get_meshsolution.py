# -*- coding: utf-8 -*-
from numpy import arange
from meshio import read
from os.path import join

from SciDataTool import DataTime, Data1D, VectorField

from ....Classes.SolutionData import SolutionData
from ....Classes.SolutionVector import SolutionVector
from ....Classes.MeshSolution import MeshSolution
from ....Classes.MeshVTK import MeshVTK


# TODO define "Results" dir, etc. in __init__
# TODO add groups, see get_meshsolution of MagFEMM
# TODO move reusable code to Elmer class


def get_meshsolution(self, output):
    """Get and set the mesh data and solution data.

    Parameters
    ----------
    self : StructElmer
        a StructElmer object
    save_path: str
        Full path to folder in which the results are saved

    Returns
    -------
    success: bool
        Information if meshsolution could be created

    """
    # logger
    logger = self.get_logger()

    # create meshsolution
    meshsol = MeshSolution(label="Elmer Structural")

    # if meshsoltion is not requested set empty MeshSolution
    if not self.is_get_mesh or not self.is_save_FEA:
        logger.info("StructElmer: MeshSolution is not stored by request.")
        output.struct.meshsolution = meshsol
        return False

    # get the mesh
    fea_path = self.get_path_save_fea(output)
    meshvtk = MeshVTK(path=join(fea_path, "Results"), name="case_t0001", format="vtu")
    # TODO maybe convert to MeshMat before
    meshsol.mesh = [meshvtk]

    # get the solution data on the mesh
    filename = join(fea_path, "Results", "case_t0001.vtu")
    meshsolvtu = read(filename)
    pt_data = meshsolvtu.point_data  # point_data is of type dict

    # setup axes
    indices = arange(meshsolvtu.points.shape[0])
    Indices = Data1D(name="indice", values=indices, is_components=True)

    # store only certain data
    store_dict = {
        "displacement": {
            "name": "Displacement",
            "unit": "mm",
            "symbol": "disp",
            "norm": 1e-3,
        },
        "vonmises": {
            "name": "Von Mises Stress",
            "unit": "MPa",
            "symbol": "vonmises",
            "norm": 1e6,
        },
    }
    comp_ext = ["x", "y", "z"]

    sol_list = []  # list of solutions

    for key, value in pt_data.items():
        # check if value should be stored
        if key in store_dict.keys():
            siz = value.shape[1]
            # only regard max. 3 components
            if siz > 3:
                logger.warning(
                    f'StructElmer get_meshsolution: size of data "{key}" > 3'
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
                    name=store_dict[key]["name"] + " " + ext,
                    unit=store_dict[key]["unit"],
                    symbol=store_dict[key]["symbol"] + ext,
                    axes=[Indices],
                    values=value[:, i],
                    normalizations={"ref": store_dict[key]["norm"]},
                )
                components.append(data)
                comp_name.append("comp_" + ext)

            # setup solution depending on number of field components
            if siz == 1:
                field = components[0]
                sol_list.append(
                    SolutionData(
                        field=field,
                        type_cell="point",
                        label=store_dict[key]["symbol"],
                    )
                )
            else:
                comps = {}
                for i in range(siz):
                    comps[comp_name[i]] = components[i]
                field = VectorField(
                    name=store_dict[key]["name"],
                    symbol=store_dict[key]["symbol"],
                    components=comps,
                )
                sol_list.append(
                    SolutionVector(
                        field=field,
                        type_cell="point",
                        label=store_dict[key]["symbol"],
                    )
                )

    meshsol.solution = sol_list

    output.struct.meshsolution = meshsol

    return True

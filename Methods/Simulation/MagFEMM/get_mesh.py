import os
import numpy as np

from pyleecan.Generator import MAIN_DIR
from pyleecan.Classes.MeshSolution import MeshSolution
from pyleecan.Classes.Mesh import Mesh
from pyleecan.Classes.ElementMat import ElementMat
from pyleecan.Classes.NodeMat import NodeMat
from pyleecan.Classes.SolutionFEMM import SolutionFEMM
from femm import callfemm
from os.path import join


def get_mesh(self, is_get_mesh, is_save_FEA, save_path, j_t0):
    """Load the mesh data and solution data. FEMM must be working and a simulation must have been solved.

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    is_get_mesh : bool
        1 to load the mesh and solution into the simulation
    is_save_FEA : bool
        1 to save the mesh and solution into a .json file
    j_t0 : int
        Targeted time step

    Returns
    -------
    res_path: str
        path to the result folder
    """
    # TODO: Not saving the mesh (only the solution) when the sliding band is activated

    idworker = "1"  # For parallelization TODO

    path_txt = join(MAIN_DIR, "Functions", "FEMM") + "\\"
    path_txt_lua = path_txt.replace("\\", "/")
    path_lua_in = join(path_txt, "get_mesh_data_FEMM.lua")
    path_lua_out = join(save_path, "get_mesh_data_FEMM" + idworker + ".lua")
    path_txt_out = save_path + "\\"
    path_txt_out = path_txt_out.replace("\\", "/")

    # Create a new LUA script with current paths
    file_lua = open(path_lua_in, "r")
    text_lua = file_lua.read()
    file_lua.close()
    text_lua = text_lua.replace("my_path_txt", path_txt_out)
    text_lua = text_lua.replace("my_id_worker", idworker)

    file_lua_out = open(path_lua_out, "w")
    file_lua_out.write(text_lua)
    file_lua_out.close()

    # Run the LUA externally using FEMM LUA console and store the data in the
    # temporary text files
    path_lua_out2 = path_lua_out.replace("\\", "/")
    callfemm('dofile("' + path_lua_out2 + '")')

    # Delete the LUA script
    os.remove(path_lua_out)

    # Read the nodes and elements files
    path_node = join(save_path, "nodes" + idworker + ".txt")
    path_element = join(save_path, "elements" + idworker + ".txt")
    listNd0 = np.loadtxt(path_node, delimiter=" ")
    listElem0 = np.loadtxt(path_element, dtype="i", delimiter=" ")
    NbNd = len(listNd0)
    NbElem = len(listElem0)

    # Node list
    listNd = np.zeros(shape=(NbNd, 3))
    listNd[:, 0] = listNd0[:, 0]
    listNd[:, 1] = listNd0[:, 1]

    # Element list
    # listElem = np.zeros(shape=(NbElem, 3))
    listElem = listElem0[:, 0:3] - 1

    # Delete text files
    os.remove(path_node)
    os.remove(path_element)

    # Read the results file
    path_results = join(save_path, "results" + idworker + ".txt")
    results = np.loadtxt(path_results, delimiter=" ")

    # Delete text files
    os.remove(path_results)

    # Save data
    if is_get_mesh:

        # Create Mesh and Solution dictionaries
        mesh = Mesh()
        mesh.element = ElementMat(
            connectivity=listElem,
            nb_elem=NbElem,
            group=listElem0[:, 6],
            nb_node_per_element=3,
        )
        mesh.node = NodeMat(coordinate=listNd[:, 0:2], nb_node=NbNd)

        solution = SolutionFEMM(B=results[:, 0:2], H=results[:, 2:4], mu=results[:, 4])

        meshFEMM = MeshSolution(
            name="FEMM_magnetic_mesh", mesh=mesh, solution=[solution]
        )

        if is_save_FEA:
            save_path_fea = join(save_path, "meshFEMM" + str(j_t0) + ".json")
            meshFEMM.save(save_path_fea)

        return meshFEMM

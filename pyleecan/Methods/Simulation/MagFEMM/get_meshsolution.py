import os
import numpy as np

from ....definitions import MAIN_DIR
from ....Classes.MeshMat import MeshMat
from ....Classes.CellMat import CellMat
from ....Classes.NodeMat import NodeMat
from ....Classes.RefTriangle3 import RefTriangle3

from os.path import join

from ....Functions.FEMM import FEMM_GROUPS


def get_meshsolution(self, femm, save_path, j_t0, id_worker=0, is_get_mesh=False):
    """Load the mesh data and solution data. FEMM must be working and a simulation must have been solved.

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    femm : FEMMHandler
        client to send command to a FEMM instance
    save_path: str
        Full path to folder in which to save results
    j_t0 : int
        time step index
    id_worker : int
        worker index
    is_get_mesh : bool
        True to load and create the mesh or not

    Returns
    -------
    mesh: MeshMat
        Object containing magnetic mesh
    B: ndarray
        3D Magnetic flux density for each element (Nelem, 3) [T]
    H : ndarray
        3D Magnetic field for each element (Nelem, 3) [A/m]
    mu : ndarray
        Magnetic relative permeability for each element (Nelem,1) []
    groups: dict
        Dict whose values are group label and values are array of indices of related elements

    """

    idworker = str(id_worker)  # For parallelization TODO

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
    femm.callfemm('dofile("' + path_lua_out2 + '")')

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

    ## Create Mesh and Solution dictionaries

    # Save MeshMat for only 1 time step with sliding band
    if is_get_mesh:
        mesh = MeshMat()
        mesh.label = "FEMM"
        mesh.cell["triangle"] = CellMat(
            connectivity=listElem,
            nb_cell=NbElem,
            nb_node_per_cell=3,
            indice=np.linspace(0, NbElem - 1, NbElem, dtype=int),
        )
        mesh.cell["triangle"].interpolation.ref_cell = RefTriangle3(epsilon=1e-9)
        mesh.node = NodeMat(
            coordinate=listNd[:, 0:2],
            nb_node=NbNd,
            indice=np.linspace(0, NbNd - 1, NbNd),
        )
        # get all groups that are in the FEMM model
        groups = dict()
        for grp in FEMM_GROUPS:
            idx = FEMM_GROUPS[grp]["ID"]
            name = FEMM_GROUPS[grp]["name"]
            ind = np.where(listElem0[:, 6] == idx)[0]
            if ind.size > 0:
                groups[name] = mesh.cell["triangle"].indice[ind]
    else:
        mesh = None
        groups = None

    B = results[:, 0:2]
    H = results[:, 2:4]
    mu = results[:, 4]

    return mesh, B, H, mu, groups

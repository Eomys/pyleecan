import os
from os.path import join

import numpy as np

from ....Classes.ElementMat import ElementMat
from ....Classes.FPGNTri import FPGNTri
from ....Classes.MeshMat import MeshMat
from ....Classes.NodeMat import NodeMat
from ....Classes.RefTriangle3 import RefTriangle3
from ....Classes.ScalarProductL2 import ScalarProductL2
from ....definitions import MAIN_DIR
from ....Functions.FEMM import FEMM_GROUPS


def get_meshsolution(
    self, femm, FEMM_dict, save_path, j_t0, id_worker=0, is_get_mesh=False
):
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

    # Save MeshMat for only 1 time step with sliding band
    path_node = join(save_path, "nodes" + idworker + ".txt")
    path_element = join(save_path, "elements" + idworker + ".txt")
    results_nodes = np.loadtxt(path_node, delimiter=" ")
    if is_get_mesh:
        # Read the nodes and elements files
        listElem0 = np.loadtxt(path_element, dtype="f", delimiter=" ").astype(
            np.float64
        )
        NbNd = len(results_nodes)
        NbElem = len(listElem0)

        # Node list
        listNd = np.zeros(shape=(NbNd, 3))
        listNd[:, 0] = results_nodes[:, 0]
        listNd[:, 1] = results_nodes[:, 1]

        # Element list
        # listElem = np.zeros(shape=(NbElem, 3))
        listElem = listElem0[:, 0:3] - 1

        mesh = MeshMat()
        mesh.element_dict["triangle"] = ElementMat(
            connectivity=listElem,
            nb_element=NbElem,
            nb_node_per_element=3,
            indice=np.linspace(0, NbElem - 1, NbElem, dtype=int),
        )
        mesh.element_dict["triangle"].ref_element = RefTriangle3(epsilon=1e-9)
        mesh.element_dict["triangle"].gauss_point = FPGNTri(nb_gauss_point=1)
        mesh.element_dict["triangle"].scalar_product = ScalarProductL2()

        mesh.node = NodeMat(
            coordinate=listNd[:, 0:2],
            nb_node=NbNd,
            indice=np.linspace(0, NbNd - 1, NbNd, dtype=int),
        )
        # get all groups that are in the FEMM model
        groups = dict()
        for grp, val in FEMM_dict["groups"].items():
            if grp != "lam_group_list":
                idx = FEMM_GROUPS[grp]["ID"]
                name = FEMM_GROUPS[grp]["name"]
                if isinstance(val, list):
                    # Create a sub group for each index of the list, e.g for magnets
                    ind = np.array([], dtype=int)
                    for ii, id_i in enumerate(val):
                        name_i = name + "_" + str(ii)
                        ind_i = np.where(listElem0[:, 6] == id_i)[0]
                        if ind_i.size > 0:
                            # Store the list of indices for the ith subgroup
                            groups[name_i] = (
                                mesh.element_dict["triangle"].indice[ind_i].tolist()
                            )
                            # Concatenate all sub groups to keep the main group of rotor magnets
                            ind = np.concatenate((ind, ind_i))
                else:
                    # Create a group with all elements og group indice idx
                    ind = np.where(listElem0[:, 6] == idx)[0]

                if ind.size > 0:
                    groups[name] = mesh.element_dict["triangle"].indice[ind].tolist()
    else:
        mesh = None
        groups = None

    # Delete text files
    os.remove(path_node)
    os.remove(path_element)

    # Read the results file
    path_results = join(save_path, "results" + idworker + ".txt")
    results = np.loadtxt(path_results, delimiter=" ")

    # Delete text files
    os.remove(path_results)

    B = results[:, 0:2]
    H = results[:, 2:4]
    mu = results[:, 4]
    A_elem = results[:, 5]
    A = results_nodes[:, 2]

    return mesh, B, H, mu, A, groups, A_elem

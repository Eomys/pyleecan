import os
import numpy as np

from ....definitions import MAIN_DIR
from ....Classes.MeshMat import MeshMat
from ....Classes.CellMat import CellMat
from ....Classes.PointMat import PointMat
from os.path import join

from ....Functions.FEMM import (
    GROUP_SC,
    GROUP_AG,
    GROUP_RC,
    GROUP_SW,
    GROUP_RW,
    GROUP_AGM,
    GROUP_IN,
    GROUP_FM,
    GROUP_SV,
    GROUP_RV,
    GROUP_SSI,
    GROUP_RSI,
    GROUP_SN,
    GROUP_RN,
    GROUP_SH,
    GROUP_RH,
)


def get_meshsolution(self, femm, save_path, j_t0):
    """Load the mesh data and solution data. FEMM must be working and a simulation must have been solved.

    Parameters
    ----------
    self : MagFEMM
        a MagFEMM object
    femm : FEMMHandler
        client to send command to a FEMM instance
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
    if j_t0 == 0:
        mesh = MeshMat()
        mesh.label = "FEMM"
        mesh.cell["triangle"] = CellMat(
            connectivity=listElem,
            nb_cell=NbElem,
            nb_pt_per_cell=3,
            indice=np.linspace(0, NbElem - 1, NbElem, dtype=int),
        )
        mesh.point = PointMat(
            coordinate=listNd[:, 0:2], nb_pt=NbNd, indice=np.linspace(0, NbNd - 1, NbNd)
        )
        groups = dict()
        groups["stator"] = mesh.cell["triangle"].indice[
            np.where(listElem0[:, 6] == GROUP_SC)[0]
        ]
        groups["airgap"] = mesh.cell["triangle"].indice[
            np.where(listElem0[:, 6] == GROUP_AG)[0]
        ]
        groups["stator_windings"] = mesh.cell["triangle"].indice[
            np.where(listElem0[:, 6] == GROUP_SW)[0]
        ]
        groups["rotor"] = mesh.cell["triangle"].indice[
            np.where(listElem0[:, 6] == GROUP_RC)[0]
        ]
        # If necessary, other groups can be defined here

    else:
        mesh = None
        groups = None

    B = results[:, 0:2]
    H = results[:, 2:4]
    mu = results[:, 4]

    return mesh, B, H, mu, groups

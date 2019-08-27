# -*- coding: utf-8 -*-
from pyManatee.Classes.MeshMat import MeshMat
from pyManatee.Classes.MeshTriangle import MeshTriangle
from pyleecan.Methods.Import.ImportMatlab import MatFileError
from os.path import isfile
import numpy as np


def get_data(self, Nt_tot):
    """Return the value from the .mat file

    Parameters
    ----------
    self : ImportMatlab
        An ImportMatlab object

    Returns3
    -------
    value : ?
        Loaded data
    """

    # if self.project_path[-4:] != ".dat":
    #     self.file_path += ".dat"
    # if not isfile(self.file_path):
    #     raise MatFileError("ERROR: The dat file doesn't exist " + self.file_path)

    path_save = self.project_path
    #path_save = join(MAIN_DIR, "Results", "Femm", "Mesh") + '\\'

    mesh = [MeshMat() for ii in range(Nt_tot)]
    mesh_tmp = MeshTriangle()

    for ii in range(Nt_tot):

        listElem = np.loadtxt(path_save + 'Mesh_elem' + str(ii) + '.dat')
        listElem = listElem.astype(int)
        mesh_tmp.nb_elem = len(listElem)
        mesh_tmp.element = listElem

        listNd = np.loadtxt(path_save + 'Mesh_nodes' + str(ii) + '.dat')
        mesh_tmp.nb_node = len(listNd)
        mesh_tmp.node = listNd

        results = np.loadtxt(path_save + 'Solution_' + str(ii) + '.dat')
        mesh_tmp.solution = dict()
        mesh_tmp.solution["Bx"] = results[:, 0]
        mesh_tmp.solution["By"] = results[:, 1]
        mesh_tmp.solution["Hx"] = results[:, 2]
        mesh_tmp.solution["Hy"] = results[:, 3]
        mesh_tmp.solution["mu"] = results[:, 4]

        mesh[ii] = mesh_tmp

    return mesh

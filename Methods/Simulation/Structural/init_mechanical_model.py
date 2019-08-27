# -*- coding: utf-8 -*-
import numpy as np
from os.path import join
from pyleecan.Generator import MAIN_DIR
from Classes.MeshMat import MeshMat

def init_mechanical_model(self, output):
    """Generate or load the mechanical model (mesh, boundary condition, material ...)

    Parameters
    ----------
    self : Structural
        a Structural object
    output : Output
        an Output object (to update)
    """

    mechanical_mesh = MeshMat()

    # Temporary: The same magnetic mesh is used for the 1st validation of the mesh2mesh projection librairy
    path_save = join(MAIN_DIR, "Results", "Femm", "Mesh") + '\\'
    mechanical_mesh = np.loadtxt(path_save + 'Nodalforces_' + str(1) + '.dat')

    output.struct.mechanical_mesh = mechanical_mesh
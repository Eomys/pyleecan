# import os
# import numpy as np

# from ....definitions import MAIN_DIR
# from ....Classes.MeshMat import MeshMat
# from ....Classes.CellMat import CellMat
# from ....Classes.PointMat import PointMat
# from ....Classes.RefTriangle3 import RefTriangle3

def get_meshsolution(self, save_path):
    """Load the mesh data and solution data. Elmer simulation must have been solved.

    Parameters
    ----------
    self : MagElmer
        a MagElmer object
    is_get_mesh : bool
        1 to load the mesh and solution into the simulation
    is_save_FEA : bool
        1 to save the mesh and solution into a .json file

    Returns
    -------
    # TODO
    """

    mesh = None
    groups = None
    B = None
    H = None
    mu = None

    return mesh, B, H, mu, groups

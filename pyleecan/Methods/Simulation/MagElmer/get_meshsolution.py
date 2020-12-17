# import os
# import numpy as np

# from ....definitions import MAIN_DIR
# from ....Classes.MeshMat import MeshMat
# from ....Classes.CellMat import CellMat
# from ....Classes.PointMat import PointMat
# from ....Classes.RefTriangle3 import RefTriangle3
from ....Classes.MeshSolution import MeshSolution


def get_meshsolution(self):
    """Build the MeshSolution objects from the FEA outputs.

    Parameters
    ----------
    self : MagElmer
        a MagElmer object

    Returns
    -------
    meshsol: MeshSolution
        a MeshSolution object with Elmer outputs at every time step
    """
    logger = self.get_logger()
    meshsol = MeshSolution(label="Elmer MagnetoDynamics")

    if not self.is_get_mesh or not self.is_save_FEA:
        logger.info("MagElmer: MeshSolution is not stored by request.")
        return False


    return meshsol

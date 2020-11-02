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

    meshsol = MeshSolution(
        label="Elmer Solution",
        # mesh=meshElmer,
        # solution=sol_list,
        # dimension=2,
    )

    return meshsol

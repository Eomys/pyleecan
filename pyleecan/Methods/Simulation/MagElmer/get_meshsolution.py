# import os
# import numpy as np
import meshio
import pyvista as pv
from os.path import join

# from ....definitions import MAIN_DIR
# from ....Classes.MeshMat import MeshMat
# from ....Classes.CellMat import CellMat
# from ....Classes.PointMat import PointMat
# from ....Classes.RefTriangle3 import RefTriangle3
from ....Classes.MeshSolution import MeshSolution
from ....Classes.MeshVTK import MeshVTK


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

    mesh = pv.read("/media/sf_Linux/python-files/pyleecan/pyleecan/Results/elmer/Elmer/ELMER_simulation/step_t0001.vtu")
    #m.write("/media/sf_Linux/python-files/pyleecan/pyleecan/Results/elmer/Elmer/ELMER_simulation/step_t0001.vtk")
    #3mesh_import = MeshVTK(path="/media/sf_Linux/python-files/pyleecan/pyleecan/Results/elmer/Elmer/ELMER_simulation", name="step_t0001", format="vtu")
    mesh.plot(scalars="magnetic flux density e", cpos="xy", show_edges=True)
    meshsol = MeshSolution(
        label="Elmer Solution",
        mesh=[mesh],
        # solution=sol_list,
        # dimension=2,
    )
    #meshsol.plot_mesh()

    return meshsol

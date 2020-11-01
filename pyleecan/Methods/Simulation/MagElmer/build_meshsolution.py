# from ....Classes.SolutionData import SolutionData
# from ....Classes.SolutionVector import SolutionVector
from ....Classes.MeshSolution import MeshSolution
# from SciDataTool import DataTime, Data1D, VectorField
# import numpy as np


def build_meshsolution(self, Nt_tot, meshElmer, Time, B, H, mu, groups):
    """Build the MeshSolution objects from the Elmer outputs.

    Parameters
    ----------
    self : MagElmer
        a MagElmer object
    is_get_mesh : bool
        1 to load the mesh and solution into the simulation
    is_save_FEA : bool
        1 to save the mesh and solution into a .json file
    j_t0 : int
        Targeted time step

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

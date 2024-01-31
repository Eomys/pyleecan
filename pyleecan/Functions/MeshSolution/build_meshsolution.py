from typing import Dict, Optional

import numpy as np

from ...Classes.Mesh import Mesh
from ...Classes.MeshSolution import MeshSolution
from ...Classes.Solution import Solution


def build_meshsolution(
    solution_dict: Dict[str, Solution],
    mesh: Mesh,
    label: str = "",
    dimension: int = 2,
    group: Optional[Dict[str, np.ndarray]] = None,
) -> MeshSolution:
    """Build the MeshSolution object from FEMM outputs.

    Parameters
    ----------
    field : ndarray
        a vec
    is_get_mesh : bool
        1 to load the mesh and solution into the simulation
    is_save_FEA : bool
        1 to save the mesh and solution into a .json file
    j_t0 : int
        Targeted time step

    Returns
    -------
    meshsol: MeshSolution
        a MeshSolution object with FEMM outputs at every time step
    """

    meshsol = MeshSolution(
        label=label,
        mesh=mesh,
        solution_dict=solution_dict,
        dimension=dimension,
        group=group,
    )

    return meshsol

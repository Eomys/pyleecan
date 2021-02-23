from ...Classes.MeshSolution import MeshSolution


def build_meshsolution(list_solution, list_mesh, label="", dimension=2, group=None):
    """Build the MeshSolution objets from FEMM outputs.

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
    if len(list_mesh) == 1:
        is_same_mesh = True

    meshsol = MeshSolution(
        label=label,
        mesh=list_mesh,
        solution=list_solution,
        is_same_mesh=is_same_mesh,
        dimension=dimension,
        group=group,
    )

    return meshsol

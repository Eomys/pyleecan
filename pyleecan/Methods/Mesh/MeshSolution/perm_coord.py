def perm_coord(
    self,
    perm_coord_list=[0, 1, 2],
):
    """Permute coordinates of Mesh Solution in place

    Parameters
    ----------
    self : MeshSolution
        a MeshSolution object
    perm_coord_list : list
        list of the coordinates to be permuted

    """

    # swap mesh solution
    for sol in self.solution:
        # swap modal shapes
        meshsol_field = sol.field
        meshsol_field = meshsol_field.T[perm_coord_list].T
        sol.field = meshsol_field

    # swap mesh VTK
    meshsol_mesh = self.get_mesh()
    self.mesh = [meshsol_mesh.perm_coord(perm_coord_list=perm_coord_list)]

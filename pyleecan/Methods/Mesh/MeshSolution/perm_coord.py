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
    len_perm_coord_list = len(perm_coord_list)

    # swap mesh solution
    for solution in self.values():
        # swap modal shapes
        meshsol_field = solution.field
        if len_perm_coord_list != meshsol_field.shape[-1]:
            raise ValueError(
                f"Wrong permutation list size, expected {meshsol_field.shape[-1]}, got {len_perm_coord_list}."
            )
        meshsol_field = meshsol_field[..., perm_coord_list]
        solution.field = meshsol_field

    # swap mesh VTK
    self.mesh = self.mesh.perm_coord(perm_coord_list=perm_coord_list)

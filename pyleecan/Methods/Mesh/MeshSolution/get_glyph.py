from numpy import (
    zeros,
    hstack,
    real,
)


def get_glyph(self, *args, label, index, indices, field_name):
    """Get the vector field, the field name and the corresponding pyvista mesh in format adapted to a glyph plot.

    Parameters
    ----------
    self : MeshSolution
        a MeshSolution object
    *args: list of strings
        List of axes requested by the user, their units and values (optional)
    label : str
        a label
    index : int
        an index
    indices : list
        list of the points to extract (optional)
    field_name : str
        title of the field to display on plot

    Returns
    -------
    vect_field : ndaray
        field to plot
    field_name : str
        name of the field
    mesh_pv : UnstructuredGrid
        pyvista mesh to plot
    """
    # Get mesh_pv and field

    # Get the mesh
    mesh_pv, vect_field, _ = self.get_mesh_field_pv(
        *args,
        label=label,
        index=index,
        indices=indices,
        field_name=field_name,
    )

    solution = self.get_solution(
        label=label,
        index=index,
    )

    axes_list = solution.get_axes_list(*args)

    # Add third dimension if needed
    ind = axes_list[0].index("component")
    if axes_list[1][ind] == 2:
        vect_field = hstack((vect_field, zeros((vect_field.shape[0], 1))))
        is_2D = True
    else:
        is_2D = False

    if field_name is None:
        if label is not None:
            field_name = label
        elif self.get_solution(index=index).label is not None:
            field_name = self.get_solution(index=index).label
        else:
            field_name = "Field"

        # if self.dimension:
        #     p.view_xy()

    return vect_field, field_name, mesh_pv, is_2D

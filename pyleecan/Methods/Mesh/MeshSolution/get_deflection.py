from numpy import (
    zeros,
    hstack,
)


def get_deflection(self, *args, label, indices, field_name):
    """Get the vector field, the field name and the corresponding pyvista mesh in format adapted to a glyph plot.

    Parameters
    ----------
    self : MeshSolution
        a MeshSolution object
    *args: list of strings
        List of axes requested by the user, their units and values (optional)
    label : str
        a label
    indices : list
        list of the points to extract (optional)
    field_name : str
        title of the field to display on plot

    Returns
    -------
    vect_field : ndaray
        vector field to plot
    field_normal_amp : ndarray
        scalar field which is the normal/radial component of vect_field (to adjust the colormap)
    field_name : str
        name of the field
    mesh_pv : UnstructuredGrid
        pyvista mesh to plot
    """
    # Get mesh_pv and field

    # Try to get normal field, else use radial
    try:
        mesh_pv, field_normal_amp, field_name = self.get_mesh_field_pv(
            *args,
            label=label,
            indices=indices,
            field_name=field_name,
            is_normal=True,
        )
    except:
        mesh_pv, field_normal_amp, field_name = self.get_mesh_field_pv(
            *args,
            label=label,
            indices=indices,
            field_name=field_name,
            is_radial=True,
        )

    _, vect_field, _ = self.get_mesh_field_pv(
        *args,
        label=label,
        indices=indices,
        field_name=field_name,
    )

    solution = self.get_solution(
        label=label,
    )

    axes_list = solution.get_axes_list(*args)

    # Add third dimension if needed
    ind = axes_list[0].index("component")
    if axes_list[1][ind] == 2:
        vect_field = hstack((vect_field, zeros((vect_field.shape[0], 1))))

    if field_name is None:
        field_name = label if label is not None else "Field"

    return vect_field, field_normal_amp, field_name, mesh_pv

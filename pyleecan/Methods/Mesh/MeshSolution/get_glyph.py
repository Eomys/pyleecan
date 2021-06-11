from numpy import (
    zeros,
    hstack,
    real,
)


def get_glyph(self, *args, label, index, indices, field_name):
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

    if field_name is None:
        if label is not None:
            field_name = label
        elif self.get_solution(index=index).label is not None:
            field_name = self.get_solution(index=index).label
        else:
            field_name = "Field"

    return vect_field, field_name, mesh_pv

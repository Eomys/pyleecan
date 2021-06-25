# -*- coding: utf-8 -*-


def get_mesh_field_pv(
    self,
    *args,
    label=None,
    index=None,
    indices=None,
    is_surf=False,
    is_radial=False,
    is_center=False,
    field_name=None,
    itimefreq=0,
):
    """Return the mesh and field adapted to pyvista plots.

    Parameters
    ----------
    self : MeshSolution
        an MeshSolution object
    *args: list of strings
        List of axes requested by the user, their units and values (optional)
    label : str
        a label
    index : int
        an index
    indices : list
        list of indices
    is_radial : bool
        radial component only
    is_center : bool
        field at cell centers
    field_name : str
        label of the field to return
    itimefreq : int
        if the field depends has a time/freqs axis, return the timefreq-th slice.

    Returns
    -------
    mesh_pv: vtk.vtkPointSet
        a pyvista mesh object
    field : ndarray
        an extracted field
    field_name : str
        name of the extracted field (useful if not specified as input)

    """

    mesh = self.get_mesh(label=label, index=index)
    new_mesh = mesh.copy()

    new_mesh.renum()

    mesh_pv = new_mesh.get_mesh_pv()

    solution = self.get_solution(
        label=label,
        index=index,
    )

    args_list = list()
    args_list.append("indice")
    args_list.append("components")
    if len(args) > 0:
        for a in args:
            args_list.append(a)

    field = self.get_field(
        *args_list,
        label=label,
        index=index,
        indices=indices,
        is_surf=is_surf,
        is_radial=is_radial,
        is_center=is_center,
    )

    if field_name is None:
        if label is not None:
            field_name = label
        elif self.get_solution(index=index).label is not None:
            field_name = self.get_solution(index=index).label
        else:
            field_name = "Field"

    return mesh_pv, field, field_name

# -*- coding: utf-8 -*-


def get_mesh_field_pv(
    self,
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

    field = self.get_field(
        label=label,
        index=index,
        indices=indices,
        is_surf=is_surf,
        is_radial=is_radial,
        is_center=is_center,
    )
    axes_list = solution.get_axes_list()

    is_timefreq = False
    if "time" in axes_list[0]:
        ind = axes_list[0].index("time")
        is_timefreq = True
    elif "freqs" in axes_list[0]:
        ind = axes_list[0].index("freqs")
        is_timefreq = True

    if is_timefreq:
        field = field.take((itimefreq), axis=ind)

    if field_name is None:
        if label is not None:
            field_name = label
        elif self.get_solution(index=index).label is not None:
            field_name = self.get_solution(index=index).label
        else:
            field_name = "Field"

    return mesh_pv, field, field_name

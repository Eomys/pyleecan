# -*- coding: utf-8 -*-


def get_indices_limited(
    meshsolution,
    label=None,
    group_names=None,
    max_value=float("Inf"),
    min_value=float("-Inf"),
):
    """Get the indices of the specified groups of a MeshSolution,
    with the field 'label' values magnitude must be within the given limits.

    Parameters
    ----------
    meshsolution : MeshSolution
        a MeshSolution object
    label : str
        label of a MeshSolution solution field
    group_names : list of str
        list of the groups names or string of a single group

    max_value : float
        max. field magnitude (over time)
    min_value : float
        min. field magnitude (over time)

    Return
    ------
    area : float
        surface area of the specified groups and indices

    """
    grp = meshsolution.get_group(group_names=group_names)
    msh = grp.mesh

    indices = msh.element_dict["triangle"].indice

    field = grp.get_field(label=label)

    # TODO check field size and axes
    field_mag = (field[:, :, 0] ** 2 + field[:, :, 1] ** 2) ** (1 / 2)
    field_max = field_mag.max(axis=0)
    field_min = field_mag.min(axis=0)

    idx_max = field_max >= max_value
    idx_min = field_min <= min_value

    idx = idx_max + idx_min

    if any(idx):
        inds = indices[idx]
    else:
        inds = []

    return inds

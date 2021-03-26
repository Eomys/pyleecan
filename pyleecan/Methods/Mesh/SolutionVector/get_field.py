# -*- coding: utf-8 -*-
import numpy as np


def get_field(self, *args, is_squeeze=False):
    """Get the value of variables stored in Solution.

    Parameters
    ----------
    self : SolutionVector
        an SolutionVector object
    *args: list of strings
        List of axes requested by the user, their units and values (optional)

    Returns
    -------
    field: array
        an array of field values

    """
    if len(args) == 1 and type(args[0]) == tuple:
        args = args[0]

    axname, axsize = self.get_axes_list()

    id = 0
    for name in axname:
        if name == "component":
            if axsize[id] == 2:
                dim = 2
            else:
                dim = 3
        id += 1

    if not args:
        field = np.zeros(axsize)
        field_dict = self.field.get_xyz_along(tuple(axname), is_squeeze=is_squeeze)
    else:
        field_dict = self.field.get_xyz_along(args, is_squeeze=is_squeeze)
        comp_x = field_dict["comp_x"]
        size = np.hstack((comp_x.shape, dim))
        field = np.zeros(size)

    field[..., 0] = field_dict["comp_x"]
    field[..., 1] = field_dict["comp_y"]

    if dim == 3:
        field[..., 2] = field_dict["comp_z"]

    return field

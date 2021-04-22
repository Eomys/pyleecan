# -*- coding: utf-8 -*-
import numpy as np

from pyleecan.Functions.make_ndarray_equal import make_ndarray_equal


def get_axes_list(self):
    """Get the axis of variables stored in Solution.

    Parameters
    ----------
    self : SolutionVector
        an SolutionVector object
    field_name : str
        name of the field to return

    Returns
    -------
    field: array
        an array of field values

    """

    # Build axis list
    ax_name = list()
    ax_size = list()

    if "comp_x" in self.field.components:
        comp = self.field.components["comp_x"]
    elif "radial" in self.field.components:
        comp = self.field.components["radial"]
    else:
        raise Exception(
            "self.field.components shall have either " "comp_x" " or " "radial" " key"
        )
    for axis in comp.axes:
        ax_name.append(axis.name)
        ax_size.append(axis.get_length())

    ax_name.append("component")
    ax_size.append(len(self.field.components))

    return ax_name, ax_size

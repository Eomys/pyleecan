# -*- coding: utf-8 -*-
import numpy as np

from ....Functions.Structural.conversions import pol2cart


def get_field(self, *args, is_squeeze=False, node=None, is_rthetaz=False):
    """Get the value of variables stored in Solution.

    Parameters
    ----------
    self : SolutionVector
        an SolutionVector object
    *args: list of strings
        List of axes requested by the user, their units and values (optional)
    nodes : array of float
        Node of the mesh (optional)
    is_rthetaz : bool
        cylindrical coordinates

    Returns
    -------
    field: array
        an array of field values

    """
    # if len(args) == 1 and type(args[0]) == tuple:
    #     args = args[0]

    if is_squeeze:
        axname, axsize = self.get_axes_list(*args)
    else:
        axname, axsize = self.get_axes_list()

    components = self.field.components
    ind_0 = axname.index("component")

    field_list = list()
    if "comp_x" in components:
        results = self.field.get_xyz_along(args, is_squeeze=is_squeeze)

        if "comp_x" in results:
            field_list.append(results["comp_x"])

        if "comp_y" in results:
            field_list.append(results["comp_y"])

        if "comp_z" in results and self.dimension == 3:
            field_list.append(results["comp_z"])

    else:
        results = self.field.get_rphiz_along(args, is_squeeze=is_squeeze)

        if "radial" in results:
            field_list.append(results["radial"])

        if "axial" in results and self.dimension == 3:
            field_list.append(results["axial"])

        # if "circ" in results:
        #     field_dict["1"] = results["circ"]

        if "tangential" in results:
            field_list.append(results["tangential"])

    field = np.array(field_list)
    field = np.moveaxis(field, 0, ind_0)

    return field

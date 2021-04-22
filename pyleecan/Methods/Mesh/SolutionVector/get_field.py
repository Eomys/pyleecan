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

    # Case of unstructured mesh
    components = self.field.components
    if node is not None:
        if "radial" in components:
            comp_zero = np.zeros(
                components["radial"].get_along(args)[components["radial"].symbol].shape
            )
            if "axial" in components:
                field_pol = np.stack(
                    (
                        components["radial"].get_along(args)[
                            components["radial"].symbol
                        ],
                        components["circ"].get_along(args)[components["circ"].symbol],
                        components["axial"].get_along(args)[components["axial"].symbol],
                    ),
                    axis=-1,
                )
            elif "circ" in components:
                field_pol = np.stack(
                    (
                        components["radial"].get_along(args)[
                            components["radial"].symbol
                        ],
                        components["circ"].get_along(args)[components["circ"].symbol],
                        comp_zero,
                    ),
                    axis=-1,
                )
            else:
                field_pol = np.stack(
                    (
                        components["radial"].get_along(args)[
                            components["radial"].symbol
                        ],
                        comp_zero,
                        comp_zero,
                    ),
                    axis=-1,
                )
            if len(field_pol.shape) == 1:
                field_pol = field_pol[np.newaxis,:]
            if is_rthetaz:
                field = field_pol
            else:
                field = pol2cart(field_pol, node)
        else:
            # TODO
            pass
    else:
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

        # TODO: cart2pol if is_rthetaz                              
    return field

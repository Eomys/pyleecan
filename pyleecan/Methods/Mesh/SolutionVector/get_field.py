# -*- coding: utf-8 -*-
import numpy as np


def get_field(self, args=None):
    """Get the value of variables stored in Solution.

     Parameters
     ----------
     self : Solution
         an Solution object
     field_name : str
         name of the field to return

     Returns
     -------
     field: array
         an array of field values

     """

    if args is None:
        args = dict()

    field = list()
    along_arg = list()
    if "component" in args:
        comp = self.field.components[args["component"]]
        for axis in self.field.components[comp].axes:
            if axis.name in args:
                if isinstance(args[axis.name], int):
                    along_arg.append(axis.name + "[" + str(args[axis.name]) + "]")
                else:
                    along_arg.append(axis.name + str(args[axis.name]))
            else:
                along_arg.append(axis.name)

        field.append(
            self.field.components[comp].get_along(tuple(along_arg))[
                self.field.components[comp].symbol
            ]
        )
    else:
        for comp in self.field.components:
            for axis in self.field.components[comp].axes:
                if axis.name in args:
                    if isinstance(args[axis.name], int):
                        along_arg.append(axis.name + "[" + str(args[axis.name]) + "]")
                    else:
                        along_arg.append(axis.name + str(args[axis.name]))
                else:
                    along_arg.append(axis.name)

            field.append(
                self.field.components[comp].get_along(tuple(along_arg))[
                    self.field.components[comp].symbol
                ]
            )

    field = np.array(field)
    field = np.moveaxis(field, 0, -1)  # put the component axis at the end

    # add a 1 dimension axis for all axis
    all_ax = self.get_axis()
    pos = 0
    for i in all_ax:
        if all_ax[i] == 1:
            field = field[..., np.newaxis]
            field = np.moveaxis(field, -1, pos)
        pos = pos + 1

    return field

# -*- coding: utf-8 -*-
import numpy as np


def get_field(self, *args):
    """Get the value of variables stored in Solution.

    Parameters
    ----------
    self : Solution
        an Solution object
    *args: list of strings
        List of axes requested by the user, their units and values (optional)

    Returns
    -------
    field: ndarray
        an ndarray of field values

    """
    if args is None:
        args = dict()
    else:
        if len(args) == 1 and type(args[0]) == tuple:
            args = args[0]

    field = self.field
    if self.axis_name is not None:
        nb_axis = len(self.axis_name)
        for i in range(nb_axis):
            ax = np.where(np.array(field.shape) == self.axis_size[i])[0][0]
            ax_name = self.axis_name[i]

            for axis_str in args:
                if ax_name in axis_str:
                    if "[" in axis_str:
                        elems = axis_str.split("[")
                        ind_str = elems[1].strip("]")

                        # Range of indices
                        if ":" in ind_str:
                            elems2 = ind_str.split(":")
                            indices = [i for i in range(int(elems2[0]), int(elems2[1]) + 1)]
                        # List of indices
                        elif "," in ind_str:
                            indices = [int(x) for x in ind_str.split(",")]
                        # Single index
                        else:
                            indices = [int(ind_str)]

                        field = np.take(field, indices=indices, axis=ax)

        return field

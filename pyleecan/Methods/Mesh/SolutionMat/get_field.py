# -*- coding: utf-8 -*-
import numpy as np


def get_field(self, *args, is_squeeze=False, node=None, is_rthetaz=False):
    """Get the value of variables stored in Solution.

    Parameters
    ----------
    self : Solution
        an Solution object
    *args: list of strings
        List of axes requested by the user, their units and values (optional)
    is_squeeze : boolean
        To numpy.squeeze the output ndarray

    Returns
    -------
    field_new: ndarray
        an ndarray of field values sliced according to args.

    """
    if args is None:
        args = dict()
    else:
        if len(args) == 1 and type(args[0]) == tuple:
            args = args[0]

    field_new = self.field.copy()

    if len(args) > 0:
        if self.axis_name is not None:
            nb_axis = len(self.axis_name)
            for i in range(nb_axis):
                # ax = np.where(np.array(field.shape) == self.axis_size[i])[0][0]
                ax_name = self.axis_name[i]
                is_found = False
                for axis_str in args:
                    if ax_name in axis_str:
                        is_found = True
                        if "[" in axis_str:
                            elems = axis_str.split("[")
                            ind_str = elems[1].strip("]")

                            # Range of indices
                            if ":" in ind_str:
                                elems2 = ind_str.split(":")
                                indices = [
                                    i for i in range(int(elems2[0]), int(elems2[1]) + 1)
                                ]
                            # List of indices
                            elif "," in ind_str:
                                indices = [int(x) for x in ind_str.split(",")]
                            # Single index
                            else:
                                indices = [int(ind_str)]

                            field_new = np.take(field_new, indices=indices, axis=i)

                if not is_found:
                    field_new = np.take(field_new, indices=0, axis=i)
                    field_new = np.expand_dims(field_new, i)

    if is_squeeze:
        field_new = np.squeeze(field_new)

    return field_new

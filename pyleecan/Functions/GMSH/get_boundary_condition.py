# -*- coding: utf-8 -*-
from ...Functions.labels import BOUNDARY_PROP_LAB


def get_boundary_condition(line, boundary_prop):
    """Returns the boundary name on a line that is used in FEA coupling

    Parameters
    ----------
    line :
        a line with a label

    Returns
    -------
    label : string
        boundary name
    """
    # The id index at the end of lamination label is removed because
    # MagElemer and StructElmer dictionaries don't support it
    if line.prop_dict and BOUNDARY_PROP_LAB in line.prop_dict:
        label_with_id = line.prop_dict[BOUNDARY_PROP_LAB]
        if "-0" in label_with_id[-2:] or "-1" in label_with_id[-2:]:
            label_without_id = label_with_id[:-2]
        else:
            label_without_id = label_with_id
        if label_without_id in boundary_prop:
            return boundary_prop[label_without_id]
    return ""

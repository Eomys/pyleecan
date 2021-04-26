from ....Functions.Geometry.merge_notch_list import merge_notch_list


def get_notch_list(self, sym=1, is_yoke=False):
    """Returns an ordered description of the notches

    Parameters
    ----------
    self : Lamination
        A Lamination object
    sym: int
        Number of symmetry
    is_yoke : bool
        Selected yoke or bore notches

    Returns
    -------
    notch_list : list
        list of dictionary with key: "begin_angle", "end_angle", "obj"
    """

    if is_yoke:
        notch_list = self.yoke_notch
    else:
        notch_list = self.notch

    if notch_list is None or len(notch_list) == 0:  # No notch
        return list()
    else:
        desc_list = notch_list[0].get_notch_list(sym=sym)
        # If more than one notch list, we need to merge in order the description
        # (check if notches are coliding)
        for ii in range(len(notch_list) - 1):
            desc_list = merge_notch_list(
                desc_list, notch_list[ii + 1].get_notch_list(sym=sym)
            )
        return desc_list

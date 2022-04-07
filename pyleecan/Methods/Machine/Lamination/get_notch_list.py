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

    if self.notch is None or len(self.notch) == 0:  # No notch
        return list()
    else:
        notch_list = [notch for notch in self.notch if notch.is_yoke == is_yoke]
        desc_list = notch_list[0].get_notch_list(sym=sym)
        # If more than one notch, we need to merge and order the description
        # TODO: check if notches are coliding
        for ii in range(len(notch_list) - 1):
            desc_list = merge_notch_list(
                desc_list, notch_list[ii + 1].get_notch_list(sym=sym)
            )
        return desc_list

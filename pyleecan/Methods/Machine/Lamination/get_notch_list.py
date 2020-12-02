from ....Functions.Geometry.merge_notch_list import merge_notch_list


def get_notch_list(self, sym=1):
    """Returns an ordered description of the notches

    Parameters
    ----------
    self : Lamination
        A Lamination object
    sym: int
        Number of symmetry

    Returns
    -------
    notch_list : list
        list of dictionary with key: "begin_angle", "end_angle", "obj"
    """

    if self.notch is None or len(self.notch) == 0:  # No notch
        return list()
    else:
        notch_list = self.notch[0].get_notch_list(sym=sym)
        # If more than one notch list, we need to merge in order the description
        # (check if notches are coliding)
        for ii in range(len(self.notch) - 1):
            notch_list = merge_notch_list(
                notch_list, self.notch[ii + 1].get_notch_list(sym=sym)
            )
        return notch_list

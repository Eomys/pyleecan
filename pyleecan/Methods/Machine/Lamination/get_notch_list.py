from ....Functions.Geometry.merge_notch_list import merge_notch_list


def get_notch_list(self, is_bore, sym=1):
    """Returns an ordered description of the notches

    Parameters
    ----------
    self : Lamination
        A Lamination object
    sym: int
        Number of symmetry
    is_bore : bool
        Selected yoke or bore notches

    Returns
    -------
    notch_list : list
        list of dictionary with key: "begin_angle", "end_angle", "obj"
    """

    if not self.has_notch(is_bore=is_bore):  # No notch on requested radius
        return list()
    else:
        # Get all the notch on the selected radius
        notch_list = [
            notch for notch in self.notch if notch.notch_shape.is_bore == is_bore
        ]
        # Get description of first notch
        desc_list = notch_list[0].get_notch_list(sym=sym)
        # If more than one notch, we need to merge and order the description
        for ii in range(len(notch_list) - 1):
            desc_list = merge_notch_list(
                desc_list, notch_list[ii + 1].get_notch_list(sym=sym)
            )
        return desc_list

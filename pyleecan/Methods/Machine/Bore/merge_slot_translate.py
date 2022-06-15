def merge_slot_translate(self, radius_desc_list, prop_dict, sym):
    """Merge the Bore shape with notches/slot on the bore/yoke
    Translate method: Translate lines of notch/slot to match the radius of the shape
    technically Keep the slot/notch height by reduicing the yoke height

    Parameters
    ----------
    radius_desc_list : list
        List of dict to describe the bore/yoke radius
    prop_dict : dict
        Property dictionary to apply on the radius lines (not on slot/notch)
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)

    Returns
    -------
    line_list : list
        List of lines needed to draw the radius
    """

    raise Exception("Not Implemented Yet")

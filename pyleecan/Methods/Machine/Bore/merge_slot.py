def merge_slot(self, radius_desc_list, prop_dict, sym):
    """Merge the Bore shape with notches/slot on the bore/yoke

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
    if self.type_merge_slot == 0:
        return self.merge_slot_connect(radius_desc_list, prop_dict=prop_dict, sym=sym)
    if self.type_merge_slot == 1:
        return self.merge_slot_intersect(radius_desc_list, prop_dict=prop_dict, sym=sym)
    if self.type_merge_slot == 2:
        return self.merge_slot_translate(radius_desc_list, prop_dict=prop_dict, sym=sym)
    else:
        raise Exception("Not implemented yet")

def get_slot_desc_list(self, sym=1, is_bore=True):
    """Returns an ordered description of the slot

    Parameters
    ----------
    self : LamSlotMulti
        A LamSlotMulti object
    sym: int
        Number of symmetry
    is_bore : bool
        True generate desc of bore, else yoke

    Returns
    -------
    slot_desc : list
        trigo ordered list of dictionary with key:
            "begin_angle" : float [rad]
            "end_angle" : float [rad]
            "obj" : Slot / None for Radius
            "lines : lines corresponding to the radius part
            "label" : Radius/Notch/Slot
    """

    slot_list = list()
    for ii in range(len(self.slot_list) // sym):
        if self.slot_list[ii].is_bore == is_bore:
            slot = self.slot_list[ii]
            op = slot.comp_angle_opening()
            lines = slot.build_geometry()
            # Apply rotation
            for line in lines:
                line.rotate(self.alpha[ii])
            bore_dict = dict()
            bore_dict["begin_angle"] = self.alpha[ii] - op / 2
            bore_dict["end_angle"] = self.alpha[ii] + op / 2
            bore_dict["obj"] = slot
            bore_dict["lines"] = lines
            bore_dict["label"] = "Slot"
            slot_list.append(bore_dict)

    return slot_list

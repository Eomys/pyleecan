from numpy import pi


def get_slot_desc_list(self, sym=1, is_bore=True):
    """Returns an ordered description of the slot

    Parameters
    ----------
    self : LamSlot
        A LamSlot object
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

    if self.slot.is_bore != is_bore:
        return list()

    slot_list = list()
    op = self.slot.comp_angle_opening()
    Zs = self.slot.Zs

    for ii in range(Zs // sym):
        slot_dict = dict()
        slot_dict["begin_angle"] = 2 * pi / Zs * ii - op / 2 + pi / Zs
        slot_dict["end_angle"] = 2 * pi / Zs * ii + op / 2 + pi / Zs
        slot_dict["obj"] = self.slot
        slot_dict["lines"] = self.slot.build_geometry()
        # Apply rotation
        for line in slot_dict["lines"]:
            line.rotate((slot_dict["begin_angle"] + slot_dict["end_angle"]) / 2)
        slot_dict["label"] = "slot"
        slot_list.append(slot_dict)

    return slot_list

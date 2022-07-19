def has_slot(self, is_bore=True):
    """Return if the lamination has slot on the requested radius
    (notches not taken into account, cf has_notch)

    Parameters
    ----------
    self : LamSlotMulti
        A LamSlotMulti object
    is_bore : bool
        True check if there are slots on the bore, else yoke

    Returns
    -------
    has_slot : bool
        True if the lamination has slot on the requested radius
    """

    if self.slot_list is None or len(self.slot_list) == 0:
        return False

    # notch_shape.is_bore = None => Default is True
    if is_bore:
        return any([slot.is_bore in [None, True] for slot in self.slot_list])
    else:
        return any([slot.is_bore == False for slot in self.slot_list])

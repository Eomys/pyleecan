from ....Functions.Load.import_class import import_class


def convert_to_SlotUD2(self):
    """Convert the slot to the equivalent SlotUD2

    Parameters
    ----------
    self : Slot
        a Slot object

    Returns
    -------
    new_slot : SlotUD2
        SlotUD2 version of the Slot
    """
    SlotUD2 = import_class("pyleecan.Classes", "SlotUD2")
    new_slot = SlotUD2()
    new_slot.Zs = self.Zs
    new_slot.line_list = self.build_geometry()
    new_slot.active_surf = self.build_geometry_active(Nrad=1, Ntan=1)[0]
    new_slot.split_active_surf_dict = None

    return new_slot

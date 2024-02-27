from .....Classes.SlotW11_2 import SlotW11_2
from .....Classes.SlotW23 import SlotW23
from .....Classes.SlotW26 import SlotW26
from .....Classes.SlotW30 import SlotW30


def select_slot_rotor_rules(self, is_stator):
    """selects step to add rules for slot in rotor and converts slot

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """
    # In Pyleecan :
    #   Single set of slot
    #   Single type of slot
    # In Motor-Cad :
    #   Single set of slot
    #   Multiple type of slot (possibility to have 2 slot)

    # select slot type and add it to obj machine or in dict
    if self.is_P_to_other:
        self.convert_slot_rotor_to_other()
    else:
        self.convert_slot_rotor_to_P()

    slot = self.machine.rotor.slot
    # add the correct rule depending on the slot
    if isinstance(slot, SlotW11_2):
        self.add_rule_rotor_slotW11_2(is_stator)
    elif isinstance(slot, SlotW23):
        self.add_rule_rotor_slotW23(is_stator)
    elif isinstance(slot, SlotW26):
        self.add_rule_rotor_slotW26(is_stator)
    elif isinstance(slot, SlotW30):
        self.add_rule_rotor_slotW30(is_stator)

    self.select_material_rules("machine.rotor.slot.wedge_mat")

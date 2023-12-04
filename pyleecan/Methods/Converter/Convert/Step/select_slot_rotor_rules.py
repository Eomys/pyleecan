from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.Classes.SlotW26 import SlotW26
from pyleecan.Classes.SlotW30 import SlotW30


def select_slot_rotor_rules(self, is_stator):
    """selection step to add rules for slot rotor

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    # select slot type and add it to obj machine or in dict
    if self.is_P_to_other:
        self.convert_slot_rotor_to_MC()
    else:
        self.convert_slot_rotor_to_P()

    slot = self.machine.rotor.slot
    # add the correct rule depending on the slot
    if isinstance(slot, SlotW11):
        self.add_rule_rotor_parallel_tooth_slotW11(is_stator)
    elif isinstance(slot, SlotW23):
        self.add_rule_rectangular_slotW23(is_stator)
    elif isinstance(slot, SlotW26):
        self.add_rule_round_slotW26(is_stator)
    elif isinstance(slot, SlotW30):
        self.add_rule_pears_slotW30(is_stator)

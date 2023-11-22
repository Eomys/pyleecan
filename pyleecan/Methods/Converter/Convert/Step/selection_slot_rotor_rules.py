from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.SlotW15 import SlotW15
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.Classes.SlotW26 import SlotW26


def selection_slot_rotor_rules(self, is_stator):
    """selection step to add rules for slot rotor

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """
    if self.is_P_to_other:
        self.convert_slot_rotor_type_MC()

    else:
        self.convert_slot_rotor_type_P()

    # add the correct rule depending on the slot
    if isinstance(self.machine.rotor.slot, SlotW11):
        self.add_rule_rotor_parallel_tooth_slotW11(is_stator)

    elif isinstance(self.machine.rotor.slot, SlotW15):
        self.add_rule_pears_slotW15(is_stator)

    elif isinstance(self.machine.rotor.slot, SlotW23):
        self.add_rule_rectangular_slotW23(is_stator)

    elif isinstance(self.machine.rotor.slot, SlotW26):
        self.add_rule_round_slotW26(is_stator)

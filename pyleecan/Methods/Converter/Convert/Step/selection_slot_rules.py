from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.SlotW14 import SlotW14
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.Classes.SlotW29 import SlotW29


def selection_slot_rules(self, is_stator):
    """selection step to add rules for slot and convert slot

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    # selection slot type and inlementation in obj machine or in dict
    if self.is_P_to_other:
        self.convert_slot_type_MC()
    else:
        self.convert_slot_type_P()

    # selection name of slot
    slot_type = type(self.machine.stator.slot).__name__

    # add the correct rule depending on the slot
    if isinstance(self.machine.stator.slot, SlotW11):
        self.add_rule_parallel_tooth_slotW11(is_stator)
    elif isinstance(self.machine.stator.slot, SlotW14):
        self.add_rule_parallel_tooth_SqB_slotW11(is_stator)
    elif isinstance(self.machine.stator.slot, SlotW21):
        self.add_rule_parallel_slot_slotW21(is_stator)
    elif isinstance(self.machine.stator.slot, SlotW23):
        self.add_rule_tapered_slot_slotW23(is_stator)
    elif slot_type == "Slotless":
        pass
    elif isinstance(self.machine.stator.slot, SlotW29):
        self.add_rule_form_wound_slotW29(is_stator)

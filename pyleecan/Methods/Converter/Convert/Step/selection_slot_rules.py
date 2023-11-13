from pyleecan.Methods.Converter.ConvertMC.Rules.Slot.add_rule_parallel_tooth_slotW11 import (
    add_rule_parallel_tooth_slotW11,
)


def selection_slot_rules(self, is_stator):
    """selection step to add rules for slot

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    # slection slot type and inlementation in obj machine or in dict
    if self.is_P_to_other:
        self.convert_slot_type_MC()
    else:
        self.convert_slot_type_P()

    # selection name of slot
    slot_type = type(self.machine.stator.slot).__name__

    # add the correct rule depending on the slot
    if slot_type == "SlotW11":
        add_rule_parallel_tooth_slotW11(self, is_stator)
    elif slot_type == "Parallel Tooth SqB":
        pass
    elif slot_type == "Parallel Slot":
        pass
    elif slot_type == "Tapered Slot":
        pass
    elif slot_type == "Slotless":
        pass
    elif slot_type == "Form Wound":
        pass

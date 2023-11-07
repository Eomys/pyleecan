from pyleecan.Classes.RuleSimple import RuleSimple
from pyleecan.Methods.Converter.ConvertMC.Rules.Slot.add_rule_parallel_tooth_slotW11 import (
    add_rule_parallel_tooth_slotW11,
)


def selection_slot_rules(self, is_stator):
    # check the dirction of conversion to select slot
    if self.is_P_to_other:
        slot_type = type(self.machine.stator.slot).__name__

    else:
        slot_type = self.other_dict["[Calc_Options]"]["Slot_Type"]

    # add the correct rule depending on the slot
    if slot_type in ["Parallel_Tooth", "SlotW11"]:
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

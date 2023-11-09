from pyleecan.Methods.Converter.ConvertMC.Rules.Slot.add_rule_rotor_parallel_tooth_slotW11 import (
    add_rule_rotor_parallel_tooth_slotW11,
)


def selection_slot_rotor_rules(self, is_stator):
    """selection step to add rules for slot

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """
    slot_rotor_type = self.other_dict["[Design_Options]"]["Top_Bar_Type"]

    if slot_rotor_type == 0:
        pass

    elif slot_rotor_type == 1:
        pass

    elif slot_rotor_type == 2:
        # self.rules_list = add_rule_rotor_parallel_tooth_slotW11(self.rules_list)
        pass
    elif slot_rotor_type == 3:
        pass
        # add_rules_parallel_slot_slotW11

    return self.rules_list

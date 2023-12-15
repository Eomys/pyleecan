from pyleecan.Classes.SlotW63 import SlotW63
from pyleecan.Classes.SlotW62 import SlotW62
from pyleecan.Classes.SlotW29 import SlotW29


def select_pole_rules(self, is_stator):
    """selects step to add rules for pole

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    if is_stator:
        raise ValueError("Pole are just in rotor")

    if self.is_P_to_other:
        self.convert_pole_to_MC()

    else:
        self.convert_pole_to_P()

    slot = self.machine.rotor.slot
    # add the correct rule depending on the pole
    if isinstance(slot, SlotW62):
        self.add_rule_salient_pole_slotW62()

    elif isinstance(slot, SlotW63):
        self.add_rule_parallel_tooth_slotW63()

    elif isinstance(slot, SlotW29):
        self.add_rule_parallel_slot_slotW29()

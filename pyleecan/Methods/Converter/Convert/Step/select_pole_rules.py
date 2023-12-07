from pyleecan.Classes.SlotW61 import SlotW61
from pyleecan.Classes.SlotW62 import SlotW62
from pyleecan.Classes.SlotW29 import SlotW29


def select_pole_rules(self, is_stator):
    """selection step to add rules for pole

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    if is_stator:
        raise ValueError("Hole are just in rotor")

    if self.is_P_to_other:
        self.convert_hole_to_MC()

    else:
        self.convert_hole_to_P()

    for hole_id, hole in enumerate(self.machine.rotor.hole):
        # add the correct rule depending on the hole
        if isinstance(hole, SlotW61):
            self.add_rule_salient_pole_slotW61(hole_id)

        elif isinstance(hole, SlotW62):
            self.add_rule_parallel_tooth_slotW62(hole_id)

        elif isinstance(hole, SlotW29):
            self.add_rule_parallel_slot_slotW29(hole_id)

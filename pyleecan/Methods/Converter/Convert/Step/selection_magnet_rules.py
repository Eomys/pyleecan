from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.Classes.SlotM13 import SlotM13
from pyleecan.Classes.SlotM15 import SlotM15
from pyleecan.Classes.SlotM16 import SlotM16


def selection_magnet_rules(self, is_stator):
    """selection step to add rules for slot

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """
    if self.is_P_to_other:
        self.convert_magnet_type_MC()

    else:
        self.convert_magnet_type_P()

    # add the correct rule depending on the hole
    if isinstance(self.machine.rotor.slot, SlotM11):
        self.add_rule_surface_radial_slotM11(is_stator)

    elif isinstance(self.machine.rotor.slot, SlotM15):
        self.add_rule_surface_parallel_slotM15(is_stator)

from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.Classes.SlotM12 import SlotM12
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
    if isinstance(self.machine.rotor.slot, SlotM11) and self.machine.rotor.slot.H0 == 0:
        self.add_rule_surface_radial_slotM11(is_stator)

    elif (
        isinstance(self.machine.rotor.slot, SlotM15) and self.machine.rotor.slot.H0 == 0
    ):
        self.add_rule_surface_parallel_slotM15(is_stator)

    elif (
        isinstance(self.machine.rotor.slot, SlotM13) and self.machine.rotor.slot.H0 == 0
    ):
        self.add_rule_surface_breadloaf_slotM13(is_stator)

    elif (
        isinstance(self.machine.rotor.slot, SlotM11) and self.machine.rotor.slot.H0 != 0
    ):
        self.add_rule_inset_radial_slotM11(is_stator)

    elif (
        isinstance(self.machine.rotor.slot, SlotM15) and self.machine.rotor.slot.H0 != 0
    ):
        self.add_rule_inset_parallel_slotM15(is_stator)

    elif isinstance(self.machine.rotor.slot, SlotM12):
        self.add_rule_inset_breadloaf_slotM12(is_stator)

    elif isinstance(self.machine.rotor.slot, SlotM16):
        self.add_rule_spoke_slotM16(is_stator)

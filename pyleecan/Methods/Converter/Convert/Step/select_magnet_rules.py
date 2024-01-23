from .....Classes.SlotM11 import SlotM11
from .....Classes.SlotM12 import SlotM12
from .....Classes.SlotM13 import SlotM13
from .....Classes.SlotM14 import SlotM14
from .....Classes.SlotM15 import SlotM15
from .....Classes.SlotM16 import SlotM16


def select_magnet_rules(self, is_stator):
    """select step to add rules for magnet and convert the magnet

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    # In Pyleecan :
    #   Multiple set of notch
    #   Multiple type of notch
    # In Motor-Cad :
    #   Single set of notch
    #   Single type of notch

    # set the machine or dict with the corect conversion of magnet
    if self.is_P_to_other:
        self.convert_magnet_to_other()

    else:
        self.convert_magnet_to_P()

    # add the correct rule depending on the hole

    if isinstance(self.machine.rotor.slot, SlotM11):
        self.add_rule_slotM11()

    elif isinstance(self.machine.rotor.slot, SlotM12):
        self.add_rule_slotM12()

    elif isinstance(self.machine.rotor.slot, SlotM13):
        self.add_rule_slotM13()

    elif isinstance(self.machine.rotor.slot, SlotM14):
        self.add_rule_slotM14()

    elif isinstance(self.machine.rotor.slot, SlotM15):
        self.add_rule_slotM15()

    elif isinstance(self.machine.rotor.slot, SlotM16):
        self.add_rule_slotM16()

    self.select_material_rules("machine.rotor.magnet.mat_type")

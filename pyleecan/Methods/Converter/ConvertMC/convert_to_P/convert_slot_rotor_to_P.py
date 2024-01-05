from .....Classes.LamSquirrelCage import LamSquirrelCage
from .....Classes.SlotW11_2 import SlotW11_2
from .....Classes.SlotW30 import SlotW30
from .....Classes.SlotW23 import SlotW23
from .....Classes.SlotW26 import SlotW26


def convert_slot_rotor_to_P(self):
    """Selects correct slot for rotor and implements it in obj machine

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    slot_type = self.other_dict["[Design_Options]"]["Top_Bar"]

    # initialisation to set the slot in rotor
    self.machine.rotor = LamSquirrelCage()
    self.machine.rotor.is_stator = False
    self.machine.rotor.is_internal = True

    # set the slot in obj machine, and add particularity
    if slot_type == "Parallel_Tooth":
        self.machine.rotor.slot = SlotW11_2()
        self.machine.rotor.slot.is_cstt_tooth = True
        self.machine.rotor.slot.H1_is_rad = True

    elif slot_type == "Round":
        self.machine.rotor.slot = SlotW26()
        self.machine.rotor.slot.H1 = 0
        self.machine.rotor.slot.R2 = 0

    elif slot_type == "Rectangular":
        self.machine.rotor.slot = SlotW23()
        self.machine.rotor.slot.H1_is_rad = True

    elif slot_type == "Pear":
        self.machine.rotor.slot = SlotW30()

    else:
        raise NotImplementedError(
            f"Type of slot {slot_type} has not equivalent or has not been implementated"
        )

    self.get_logger().info(
        f"Conversion {slot_type} into {type(self.machine.rotor.slot).__name__}"
    )

    # Motor-Cad has possibility to have 2 slots, nested one on top of the other
    # We have dicided to select just the top_BAR
    if self.other_dict["[Design_Options]"]["Bottom_Bar"] != None:
        self.get_logger().error(
            f"Conversion with 2 slot in rotor is not accept in Pyleecan"
        )

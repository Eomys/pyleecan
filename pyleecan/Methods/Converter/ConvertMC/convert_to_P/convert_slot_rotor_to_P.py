from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.SlotW30 import SlotW30
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.Classes.SlotW26 import SlotW26


def convert_slot_rotor_to_P(self):
    """Selection correct slot and implementation in obj machine

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    slot_type = self.other_dict["[Design_Options]"]["Top_Bar"]

    # initialisation to set the slot in rotor
    dict_machine = self.machine.rotor.as_dict()
    self.machine.rotor = LamSquirrelCage(init_dict=dict_machine)
    self.machine.rotor.is_stator = False
    self.machine.rotor.is_internal = True

    # set the slot in obj machine, and add particularity
    if slot_type == "Parallel_Tooth":
        self.machine.rotor.slot = SlotW11()
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
        raise Exception("Conversion of machine doesn't exist")

    self.get_logger().info(
        f"Conversion {slot_type} into {type(self.machine.rotor.slot).__name__}"
    )

    if self.other_dict["[Design_Options]"]["Bottom_Bar"] != None:
        self.get_logger().error(
            f"Conversion with 2 slot in rotor is not accept in Pyleecan"
        )

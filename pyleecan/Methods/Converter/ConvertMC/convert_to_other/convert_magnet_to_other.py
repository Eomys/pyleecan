from .....Classes.SlotM11 import SlotM11
from .....Classes.SlotM12 import SlotM12
from .....Classes.SlotM13 import SlotM13
from .....Classes.SlotM15 import SlotM15
from .....Classes.SlotM16 import SlotM16
from pyleecan.Classes.SlotM16 import SlotM16


def convert_magnet_to_other(self):
    """Selects correct magnet and implements it in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    # conversion to Motor-CAD
    slot = self.machine.rotor.slot
    magnet_type = type(slot).__name__

    # selection type of Slot
    if isinstance(slot, SlotM11) and self.machine.rotor.slot.H0 == 0:
        if slot.H0 == 0:
            # magnet is on surface of rotor
            name_slot = "Surface_Radial"
        else:
            name_slot = "Inset_Radial"

    elif isinstance(slot, SlotM15):
        if slot.H0 == 0:
            # magnet is on surface of rotor
            name_slot = "Surface_Parallel"
        else:
            name_slot = "Inset_Parallel"

    elif isinstance(slot, SlotM12):
        name_slot = "Inset_Breadleaof"

    elif isinstance(slot, SlotM13):
        name_slot = "Surface_Breadleaof"

    elif isinstance(slot, SlotM16):
        name_slot = "Spoke"

    else:
        raise NotImplementedError(
            f"Type of magnet {magnet_type} has not equivalent or has not been implementated"
        )

    # writting magnet type in other_dict
    if "[Design_Options]" not in self.other_dict:
        self.other_dict["[Design_Options]"] = {"BPM_Rotor": name_slot}
    else:
        self.other_dict["[Design_Options]"]["BPM_Rotor"] = name_slot

    self.get_logger().info(f"Conversion {magnet_type} into {name_slot}")

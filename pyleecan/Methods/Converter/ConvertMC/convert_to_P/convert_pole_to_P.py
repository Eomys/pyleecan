from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW63 import SlotW63
from pyleecan.Classes.SlotW62 import SlotW62
from pyleecan.Classes.SlotW29 import SlotW29


def convert_pole_to_P(self):
    """Selects correct pole and implements it in obj machine

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object

    """

    pole_type = self.other_dict["[Design_Options]"]["Sync_Rotor"]

    # initialisation to set the hole in rotor
    self.machine.rotor = LamSlotWind()
    self.machine.rotor.is_stator = False
    self.machine.rotor.is_internal = True

    # set the hole in obj machine, and add particularity to hole
    if pole_type == "Sync_Salient_Pole":
        self.machine.rotor.slot = SlotW62()

    elif pole_type == "Sync_Parallel_Tooth":
        self.machine.rotor.slot = SlotW63()

    elif pole_type == "Sync_Parallel_Slot":
        self.machine.rotor.slot = SlotW29()
        self.machine.rotor.slot.H0 = 0
        self.get_logger().info("Approximation for tip angle, not possible in pyleecan")

    else:
        raise NotImplementedError(
            f"Type of hole {pole_type} has not equivalent in pyleecan or has not implement"
        )

    self.get_logger().info(
        f"Conversion {pole_type} into {type(self.machine.rotor.slot).__name__}"
    )

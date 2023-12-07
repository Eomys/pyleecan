from pyleecan.Classes.LamHoleNS import LamHoleNS
from pyleecan.Classes.SlotW61 import SlotW61
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
    self.machine.rotor = LamHoleNS()
    self.machine.rotor.is_stator = False
    self.machine.rotor.is_internal = True

    # set the hole in obj machine, and add particularity to hole
    if pole_type == "Sync_Salient_Pole":
        self.machine.rotor.hole.append(SlotW61())

    elif pole_type == "Sync_Parallel_Tooth":
        self.machine.rotor.hole.append(SlotW62())

    elif pole_type == "Sync_Parallel_Slot":
        self.machine.rotor.hole.append(SlotW29())

    else:
        raise NotImplementedError(
            f"Type of hole {pole_type} has not equivalent in pyleecan or has not implement"
        )

    self.get_logger().info(
        f"Conversion {pole_type} into {type(self.machine.rotor.hole[0]).__name__}"
    )

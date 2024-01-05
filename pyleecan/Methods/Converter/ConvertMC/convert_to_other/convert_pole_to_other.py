from .....Classes.SlotW61 import SlotW61
from .....Classes.SlotW62 import SlotW62
from .....Classes.SlotW29 import SlotW29


def convert_pole_to_other(self):
    """Selects correct pole and implements it in dict
    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    Returns
    ---------
    """
    # conversion to motor-cad
    pole_type = self.machine.rotor.slot

    # selection type of pole
    if isinstance(pole_type, SlotW61):
        name_pole = "Sync_Salient_Pole"

    elif isinstance(pole_type, SlotW62):
        name_pole = "Sync_Parallel_Tooth"

    elif isinstance(pole_type, SlotW29):
        name_pole = "Sync_Parallel_Slot"

    else:
        raise NotImplementedError(
            f"Type of pole {pole_type.__class__.__name__} has not equivalent or has not been implementated"
        )

    # writting in dict
    if "[Design_Options]" not in self.other_dict:
        self.other_dict["[Design_Options]"] = {"Sync_Rotor": name_pole}
    else:
        self.other_dict["[Design_Options]"]["Sync_Rotor"] = name_pole

    self.get_logger().info(
        f"Conversion {pole_type.__class__.__name__} into {name_pole}"
    )

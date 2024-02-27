from .....Classes.SlotW11 import SlotW11
from .....Classes.SlotW14 import SlotW14
from .....Classes.SlotW21 import SlotW21
from .....Classes.SlotW23 import SlotW23
from .....Classes.SlotW29 import SlotW29


def convert_slot_to_other(self):
    """Selects correct slot and implements it in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    # conversion to pyleecan
    slot = self.machine.stator.slot

    # selection type of Slot
    if isinstance(slot, SlotW11):
        name_slot = "Parallel_Tooth"

    elif isinstance(slot, SlotW14):
        name_slot = "Parallel_tooth_SqB"

    elif isinstance(slot, SlotW21):
        name_slot = "Parallel_Slot"

    elif isinstance(slot, SlotW23):
        name_slot = "Tapered_slot"

    elif isinstance(slot, SlotW29):
        name_slot = "Form_Wound"

    else:
        raise NotImplementedError(
            f"Type of slot {name_slot} has not equivalent or has not been implementated"
        )
    self.get_logger().info(f"Conversion {slot.__class__.__name__} into {name_slot}")

    # writting in dict
    if "[Calc_Options]" not in self.other_dict:
        self.other_dict["[Calc_Options]"] = {"Slot_Type": name_slot}
    else:
        self.other_dict["[Calc_Options]"]["Slot_Type"] = name_slot

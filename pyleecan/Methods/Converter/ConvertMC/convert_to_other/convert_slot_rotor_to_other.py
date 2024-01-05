from .....Classes.SlotW11_2 import SlotW11_2
from .....Classes.SlotW23 import SlotW23
from .....Classes.SlotW26 import SlotW26
from .....Classes.SlotW30 import SlotW30


def convert_slot_rotor_to_other(self):
    """Selects correct slot for rotor and implements it in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # conversion to pyleecan
    slot = self.machine.rotor.slot

    # selection type of Slot
    if isinstance(slot, SlotW11_2):
        name_slot = "Parallel_Tooth"

    elif isinstance(slot, SlotW23):
        name_slot = "Rectangular"

    elif isinstance(slot, SlotW26):
        name_slot = "Round"

    elif isinstance(slot, SlotW30):
        name_slot = "Pear"

    else:
        raise NotImplementedError(
            f"Type of slot {name_slot} has not equivalent or has not been implementated"
        )

    self.get_logger().info(f"Conversion {slot.__class__.__name__} into {name_slot}")

    # writting in dict
    if "[Design_Options]" not in self.other_dict:
        self.other_dict["[Design_Options]"] = {"Top_Bar": name_slot}
    else:
        self.other_dict["[Design_Options]"]["Top_Bar"] = name_slot

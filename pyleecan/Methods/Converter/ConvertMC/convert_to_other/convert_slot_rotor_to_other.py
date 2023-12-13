from .....Classes.SlotW11 import SlotW11
from .....Classes.SlotW23 import SlotW23
from .....Classes.SlotW26 import SlotW26
from .....Classes.SlotW30 import SlotW30


def convert_slot_rotor_to_MC(self):
    """Selection correct slot and implementation in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # conversion to pyleecan
    slot = type(self.machine.rotor.slot).__name__

    # selection type of Slot
    if isinstance(slot, SlotW11):
        name_slot = "Parallel_Tooth"

    elif isinstance(slot, SlotW23):
        name_slot = "Rectangular"

    elif isinstance(slot, SlotW26):
        name_slot = "Round"

    elif isinstance(slot, SlotW30):
        name_slot = "Pear"

    else:
        raise Exception("Conversion of machine doesn't exist")

    self.get_logger().info(f"Conversion {slot.__class__.__name__} into {name_slot}")

    # writting in dict
    if "[Design_Options]" not in self.other_dict:
        self.other_dict["[Design_Options]"] = {"Top_Bar": name_slot}
    else:
        self.other_dict["[Design_Options]"]["Top_Bar"] = name_slot

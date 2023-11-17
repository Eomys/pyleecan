from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.SlotW14 import SlotW14
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.SlotW23 import SlotW23
from pyleecan.Classes.SlotW29 import SlotW29


def convert_slot_type_P(self):
    """Selection correct slot and implementation in obj machine or in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    slot_type = self.other_dict["[Calc_Options]"]["Slot_Type"]

    # initialisation to set the slot in stator
    dict_machine = self.machine.stator.as_dict()
    self.machine.stator = LamSlotWind(init_dict=dict_machine)

    if slot_type == "Parallel_Tooth":
        # set the slot in obj machine, and add particularity to slotW11
        self.machine.stator.slot = SlotW11()
        self.machine.stator.slot.is_cstt_tooth = True
        self.machine.stator.slot.H1_is_rad = True
        self.machine.stator.is_internal = False

    elif slot_type == "Parallel_tooth_SqB":
        # set the slot in obj machine, and add particularity to slotW11
        self.machine.stator.slot = SlotW14()
        self.machine.stator.is_internal = False

    elif slot_type == "Parallel_Slot":
        # set the slot in obj machine, and add particularity to slotW11
        self.machine.stator.slot = SlotW21()
        self.machine.stator.slot.H1_is_rad = True
        self.machine.stator.is_internal = False

    elif slot_type == "Tapered_slot":
        # set the slot in obj machine, and add particularity to slotW11
        self.machine.stator.slot = SlotW23()
        self.machine.stator.slot.is_cstt_tooth = True
        self.machine.stator.slot.H1_is_rad = True
        self.machine.stator.is_internal = False

    elif slot_type == "Form_Wound":
        # set the slot in obj machine, and add particularity to slotW11
        self.machine.stator.slot = SlotW29()
        self.machine.stator.slot.is_cstt_tooth = True
        self.machine.stator.slot.H1_is_rad = True
        self.machine.stator.is_internal = False

    else:
        raise Exception("Conversion of machine doesn't exist")

    self.get_logger().info(
        f"Conversion {slot_type} into {type(self.machine.stator.slot).__name__}"
    )

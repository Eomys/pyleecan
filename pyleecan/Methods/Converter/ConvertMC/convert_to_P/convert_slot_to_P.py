from .....Classes.LamSlotWind import LamSlotWind
from .....Classes.SlotW11 import SlotW11
from .....Classes.SlotW14 import SlotW14
from .....Classes.SlotW21 import SlotW21
from .....Classes.SlotW23 import SlotW23
from .....Classes.SlotW29 import SlotW29
from .....Classes.Material import Material


def convert_slot_to_P(self):
    """Selects correct slot and implements it in obj machine

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    slot_type = self.other_dict["[Calc_Options]"]["Slot_Type"]

    # initialisation to set the slot in stator
    dict_machine = self.machine.stator.as_dict()
    self.machine.stator = LamSlotWind(init_dict=dict_machine)

    # set the slot in obj machine, and add particularity
    if slot_type == "Parallel_Tooth":
        if self.other_dict["[Dimensions]"]["Slot_Corner_Radius"] == 0:
            self.machine.stator.slot = SlotW23()
            self.machine.stator.slot.is_cstt_tooth = True
            self.machine.stator.slot.H1_is_rad = True
            self.machine.stator.is_internal = False

        else:
            self.machine.stator.slot = SlotW11()
            self.machine.stator.slot.is_cstt_tooth = True
            self.machine.stator.slot.H1_is_rad = True
            self.machine.stator.is_internal = False
            self.get_logger().warning(
                "Approximation: top of slot is flat in Pyleecan contrary to MC top is rounded"
            )

    elif slot_type == "Parallel_Tooth_SqBase":
        self.machine.stator.slot = SlotW14()
        self.machine.stator.is_internal = False
        self.machine.stator.slot.H1_is_rad = True
        self.machine.stator.slot.wedge_type = 1

    elif slot_type == "Parallel_Slot":
        self.machine.stator.slot = SlotW21()
        self.machine.stator.slot.H1_is_rad = True
        self.machine.stator.is_internal = False

    elif slot_type == "Tapered_Slot":
        if self.other_dict["[Dimensions]"]["Slot_Corner_Radius"] == 0:
            self.machine.stator.slot = SlotW23()
            self.machine.stator.slot.is_cstt_tooth = False
            self.machine.stator.slot.H1_is_rad = True
            self.machine.stator.is_internal = False

        else:
            self.machine.stator.slot = SlotW11()
            self.machine.stator.slot.is_cstt_tooth = False
            self.machine.stator.slot.H1_is_rad = True
            self.machine.stator.is_internal = False
            self.get_logger().warning(
                "Approximation: top of slot is flat in Pyleecan contrary to MC top is rounded"
            )

    elif slot_type == "Form_Wound":
        self.machine.stator.slot = SlotW29()
        self.machine.stator.is_internal = False
        self.machine.stator.slot.wedge_type = 1

    elif slot_type == "Slotless":
        self.get_logger().error("Slotless has not equivalent in Pyleecan")

    else:
        raise NotImplementedError(
            f"type of slot {slot_type} has not equivalent in pyleecan or has not been implementated"
        )

    self.get_logger().info(
        f"Conversion {slot_type} into {type(self.machine.stator.slot).__name__}"
    )

    # selection type of wedge
    if "Wedge_Model" in self.other_dict["[Winding_Design]"]:
        wedge = self.other_dict["[Winding_Design]"]["Wedge_Model"]

    else:
        wedge = "Air"

    # set the correct wedge
    if wedge == "Air":
        self.machine.stator.slot.wedge_mat = None
    elif wedge == "Wedge":
        self.machine.stator.slot.wedge_mat = Material()
    elif wedge == "Wound_Space":
        self.machine.stator.slot.wedge_mat = None
        self.get_logger().info(
            f"Conversion Wound_Space for {type(self.machine.stator.slot).name} has no equivalent in pyleecan. No wedge defined in the converted slot"
        )

    else:
        self.machine.stator.slot.wedge_mat = None
        self.get_logger().warning(
            f"Error for conversion of wedge (unknow wedge type: {wedge}). No wedge defined in the converted slot"
        )

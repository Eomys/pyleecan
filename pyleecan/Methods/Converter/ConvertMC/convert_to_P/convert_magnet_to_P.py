from .....Classes.LamSlotMag import LamSlotMag
from .....Classes.SlotM11 import SlotM11
from .....Classes.SlotM12 import SlotM12
from .....Classes.SlotM13 import SlotM13
from .....Classes.SlotM14 import SlotM14
from .....Classes.SlotM15 import SlotM15
from .....Classes.SlotM16 import SlotM16


def convert_magnet_to_P(self):
    """Selects correct magnet and implements it in obj machine

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # conversion to pyleecan
    magnet_type = self.other_dict["[Design_Options]"]["BPM_Rotor"]

    # initialisation to set the slot in stator
    self.machine.rotor = LamSlotMag()

    # set the slot in obj machine, and add particularity
    if magnet_type == "Surface_Radial":
        self.machine.rotor.slot = SlotM14()
        self.machine.rotor.slot.H0 = 0  # slot is on surface

    elif magnet_type == "Surface_Parallel":
        self.machine.rotor.slot = SlotM15()
        self.machine.rotor.slot.H0 = 0  # slot is on surface

    elif magnet_type == "Surface_Breadloaf":
        self.machine.rotor.slot = SlotM13()
        self.machine.rotor.slot.H0 = 0  # slot is on surface

    elif magnet_type == "Inset_Radial":
        self.machine.rotor.slot = SlotM11()

    elif magnet_type == "Inset_Parallel":
        self.machine.rotor.slot = SlotM15()
        self.machine.rotor.slot.H0 = 0.001  # To pass the check for inset parallel
        self.get_logger().warning(
            "Approximation for slotM15 hasn't equivalent in Pyleecan"
        )

    elif magnet_type == "Inset_Breadloaf":
        self.machine.rotor.slot = SlotM12()

    elif magnet_type == "Spoke":
        self.machine.rotor.slot = SlotM16()

    else:
        raise NotImplementedError(
            f"type of magnet {magnet_type} has not equivalent in pyleecan or has not been implementated"
        )

    self.machine.rotor.is_stator = False
    self.machine.rotor.is_internal = True
    other_value = self.other_dict["[Dimensions]"]["Pole_Number"]
    self.machine.rotor.set_pole_pair_number(other_value // 2)

    self.get_logger().info(
        f"Conversion {magnet_type} into {type(self.machine.rotor.slot).__name__}"
    )

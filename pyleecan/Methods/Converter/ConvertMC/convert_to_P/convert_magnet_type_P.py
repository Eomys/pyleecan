from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.Classes.SlotM12 import SlotM12
from pyleecan.Classes.SlotM15 import SlotM15
from pyleecan.Classes.SlotM13 import SlotM13
from pyleecan.Classes.SlotM16 import SlotM16


def convert_magnet_type_P(self):
    """Selection correct magnet and implementation in obj machine

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # conversion to pyleecan
    motor_type = self.other_dict["[Design_Options]"]["BPM_Rotor"]

    # initialisation to set the slot in stator
    dict_machine = self.machine.rotor.as_dict()
    self.machine.rotor = LamSlotMag(init_dict=dict_machine)

    # set the slot in obj machine, and add particularity
    if motor_type == "Surface_Radial":
        self.machine.rotor.slot = SlotM11()
        self.machine.rotor.slot.H0 = 0

    elif motor_type == "Surface_Parallel":
        self.machine.rotor.slot = SlotM15()
        self.machine.rotor.slot.H0 = 0

    elif motor_type == "Surface_Breadloaf":
        self.machine.rotor.slot = SlotM13()
        self.machine.rotor.slot.H0 = 0

    elif motor_type == "Inset_Radial":
        self.machine.rotor.slot = SlotM11()

    elif motor_type == "Inset_Parallel":
        self.machine.rotor.slot = SlotM15()

    elif motor_type == "Inset_Breadloaf":
        self.machine.rotor.slot = SlotM12()

    elif motor_type == "Spoke":
        self.machine.rotor.slot = SlotM16()

    else:
        raise Exception("Conversion of machine doesn't exist")

    self.machine.rotor.is_stator = False
    self.machine.rotor.is_internal = True
    other_value = self.other_dict["[Dimensions]"]["Pole_Number"]
    self.machine.rotor.set_pole_pair_number(int(other_value / 2))

    self.get_logger().info(
        f"Conversion {motor_type} into {type(self.machine.rotor.slot).__name__}"
    )

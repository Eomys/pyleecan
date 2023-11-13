from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM11 import SlotM11


def convert_magnet_type_P(self):
    """Selection correct magnet and implementation in obj machine or in dict

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

    if motor_type == "Surface_Radial":
        # set the slot in obj machine, and add particularity to slotW11
        self.machine.rotor.slot = SlotM11()
        self.machine.rotor.is_stator = False
        self.machine.rotor.is_internal = True
        self.machine.rotor.slot.H0 = 0
        other_value = self.other_dict["[Dimensions]"]["Pole_Number"]
        self.machine.rotor.set_pole_pair_number(int(other_value / 2))

    else:
        raise Exception("Conversion of machine doesn't exist")

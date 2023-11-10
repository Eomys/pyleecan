from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM11 import SlotM11


def convert_magnet_type(self):
    """Selection correct magnet and implementation in obj machine or in dict

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    # check the direction of conversion
    if self.is_P_to_other == True:  # conversion to pyleecan
        motor_type = type(self.machine.rotor.slot).__name__

        # selection type of Slot
        if motor_type == "SlotM11":
            name_slot = "Surface_Radial"

        elif motor_type == "":
            name_slot = ""

        else:
            raise Exception("Conversion of machine doesn't exist")

        # writting in dict
        if "[Design_Options]" not in self.other_dict:
            self.other_dict["[Design_Options]"] = {}
            temp_dict = self.other_dict["[Design_Options]"]
            temp_dict["BPM_Rotor"] = name_slot
        else:
            self.other_dict["[Design_Options]"]["BPM_Rotor"] = name_slot

    else:
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

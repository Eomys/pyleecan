from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.Methods.Converter.Rules.set_other import set_other

from pyleecan.Methods.Slot.SlotW11.get_H1 import get_H1


def other_to_P(self, machine, other_dict):
    dict_machine = machine.rotor.as_dict()

    machine.rotor = LamSlotMag(init_dict=dict_machine)

    machine.rotor.slot = SlotM11()
    machine.rotor.is_stator = False
    machine.rotor.is_internal = True
    machine.rotor.slot.H0 = 0
    other_value = other_dict["[Dimensions]"]["Pole_Number"]
    machine.rotor.set_pole_pair_number(int(other_value / 2))

    return machine


def P_to_other(self, machine, other_dict):
    if "[Design_Options]" not in other_dict:
        other_dict["[Design_Options]"] = {}

    temp_dict = other_dict["[Design_Options]"]

    temp_dict["BPM_Rotor"] = "Surface_Radial"

    return other_dict

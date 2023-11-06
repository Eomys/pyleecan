from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Methods.Converter.Rules.set_other import set_other

from pyleecan.Methods.Slot.SlotW11.get_H1 import get_H1


def other_to_P(self, machine):
    dict_machine = machine.stator.as_dict()

    machine.stator = LamSlotWind(init_dict=dict_machine)

    machine.stator.slot = SlotW11()

    machine.stator.slot.is_cstt_tooth = True
    machine.stator.slot.H1_is_rad = True

    machine.stator.is_internal = False
    return machine


def P_to_other(self, other_dict):
    if "[Calc_Options]" not in other_dict:
        other_dict["[Calc_Options]"] = {}

    temp_dict = other_dict["[Calc_Options]"]

    temp_dict["Slot_Type"] = "Parallel_Tooth"

    return other_dict

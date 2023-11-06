from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW23 import SlotW23

from pyleecan.Methods.Slot.SlotW23.get_H1 import get_H1


def other_to_P(self, machine):
    dict_machine = machine.stator.as_dict()

    machine.stator = LamSlotWind(init_dict=dict_machine)

    machine.stator.slot = SlotW23()

    machine.stator.slot.is_cstt_tooth = False
    machine.stator.slot.H1_is_rad = True

    machine.stator.is_internal = False
    return machine


def P_to_other(self, other_dict):
    print("other_to_P")
    return other_dict

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Methods.Converter.Rules.set_other import set_other

from pyleecan.Methods.Slot.SlotW11.get_H1 import get_H1


def other_to_P(self, machine):
    return machine


def P_to_other(self, other_dict):
    return other_dict

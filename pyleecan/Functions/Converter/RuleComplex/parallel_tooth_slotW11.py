from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW11 import SlotW11

from pyleecan.Methods.Slot.SlotW11.get_H1 import get_H1


def parallel_tooth_slotW11(machine):
    dict_machine = machine.stator.as_dict()

    machine.stator = LamSlotWind(init_dict=dict_machine)

    machine.stator.slot = SlotW11()

    machine.stator.slot.is_cstt_tooth = True
    machine.stator.slot.H1_is_rad = True

    machine.stator.is_internal = False
    return machine


def slotW11_H1(machine):
    H1 = get_H1(machine.stator.slot)

    machine.stator.slot.H1 = H1
    machine.stator.slot.H1_is_rad = False
    return machine

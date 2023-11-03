from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotW11 import SlotW11

from pyleecan.Methods.Slot.SlotW11.get_H1 import get_H1
from pyleecan.Methods.Slot.SlotW11._comp_W import _comp_W


def rotor_slotW11(machine):
    dict_machine = machine.rotor.as_dict()

    machine.rotor = LamSlotMag(init_dict=dict_machine)

    machine.rotor.slot = SlotW11()

    machine.rotor.slot.is_cstt_tooth = True
    machine.rotor.slot.H1_is_rad = True

    machine.rotor.is_internal = True
    return machine


def rotor_slotW11_H1(machine):
    H1 = get_H1(machine.rotor.slot)

    machine.rotor.slot.H1 = H1
    machine.rotor.slot.H1_is_rad = False
    # machine.rotor.slot = _comp_W(machine.rotor.slot)
    return machine

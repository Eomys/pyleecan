from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW11 import SlotW11


def slotW11(machine):
    dict_machine = machine.stator.as_dict()

    machine.stator = LamSlotWind(init_dict=dict_machine)

    machine.stator.slot = SlotW11()

    machine.stator.slot.is_cstt_tooth = True
    machine.stator.slot.H1_is_rad = True
    return machine

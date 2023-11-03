from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW29 import SlotW29


def other_to_P(self, machine):
    dict_machine = machine.stator.as_dict()

    machine.stator = LamSlotWind(init_dict=dict_machine)

    machine.stator.slot = SlotW29()

    machine.stator.slot.H1_is_rad = True
    machine.stator.is_internal = False
    return machine


def P_to_other(self, machine):
    print("other_to_P")

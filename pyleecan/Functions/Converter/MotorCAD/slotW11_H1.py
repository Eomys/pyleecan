def other_to_P(self, machine):
    H1 = machine.stator.slot.get_H1()

    machine.stator.slot.H1 = H1
    machine.stator.slot.H1_is_rad = False
    return machine


def P_to_other(self, other_dict):
    print("other_to_P")
    return other_dict
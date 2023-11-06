def other_to_P(self, machine):
    H1 = machine.stator.slot.het_H1()

    machine.stator.slot.H1 = H1
    machine.stator.slot.H1_is_rad = False
    return machine


def P_to_other(self, machine):
    print("other_to_P")

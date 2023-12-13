# !!!!! not use for the moment


def other_to_P(self, machine, other_dict):
    H1 = machine.rotor.slot.get_H1()

    machine.rotor.slot.H1 = H1
    machine.rotor.slot.H1_is_rad = False
    # machine.rotor.slot = _comp_W(machine.rotor.slot)
    return machine


def P_to_other(self, machine, other_dict):
    return other_dict

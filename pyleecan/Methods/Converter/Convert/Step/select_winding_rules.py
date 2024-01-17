from .....Classes.MachineWRSM import MachineWRSM


def select_winding_rules(self, is_stator):
    """select step to add rules for winding

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor
    """

    if isinstance(self.machine, MachineWRSM) and not is_stator:
        # WRSM has particular winding
        self.machine.rotor.winding.qs = 1
        self.machine.rotor.winding.Nlayer = 2
        self.machine.rotor.winding.is_change_layer = False
        self.machine.rotor.winding.coil_pitch = 1
        self.machine.rotor.winding.Ntcoil = 1
    else:
        self.add_rule_winding(is_stator)

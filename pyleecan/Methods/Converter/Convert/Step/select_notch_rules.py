from .....Classes.SlotM19 import SlotM19


def select_notch_rules(self, is_stator):
    """selection step to add rules for notch

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor
    """
    if self.is_P_to_other:
        self.convert_notch_to_other(is_stator)
    else:
        self.convert_notch_to_P(is_stator)

    if is_stator:
        notch = self.machine.stator.notch
    else:
        notch = self.machine.rotor.notch

    for nb_notch, notch in enumerate(notch):
        if isinstance(notch.notch_shape, SlotM19):
            self.add_rule_notch_slotM19(is_stator, nb_notch)

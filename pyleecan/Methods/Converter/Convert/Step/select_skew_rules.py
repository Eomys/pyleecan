from .....Classes.Skew import Skew


def select_skew_rules(self, is_stator):
    """selects step to add rules for skew

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    if self.is_P_to_other:
        self.convert_skew_to_other()
    else:
        self.convert_skew_to_P()

    if isinstance(self.machine.rotor.skew, Skew):
        self.add_rule_skew()

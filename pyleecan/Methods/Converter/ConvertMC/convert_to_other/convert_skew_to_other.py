from .....Classes.Skew import Skew


def convert_skew_to_other(self):
    """Selects correct skew and implements it in dict
    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    Returns
    ---------
    """

    if isinstance(self.machine.rotor.skew, Skew):
        self.add_rule_skew()

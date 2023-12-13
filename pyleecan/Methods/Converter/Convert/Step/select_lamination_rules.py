def select_lamination_rules(self, is_stator):
    """selects step to add rules for lamination

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    self.select_duct_rules(is_stator)
    self.select_notch_rules(is_stator)

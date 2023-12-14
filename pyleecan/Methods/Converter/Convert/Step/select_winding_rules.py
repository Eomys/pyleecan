def select_winding_rules(self, is_stator):
    """select step to add rules for winding

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor
    """

    self.add_rule_winding()

def select_lamination_rules(self, is_stator):
    """selection step to add rules for lamination

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    # selection of number and to layers
    if not self.is_P_to_other:
        self.convert_duct_to_P(is_stator)
        self.convert_notch_to_P(is_stator)

    else:
        self.convert_duct_to_MC(is_stator)
        self.convert_notch_to_MC(is_stator)

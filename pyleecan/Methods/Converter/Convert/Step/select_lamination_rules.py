def select_lamination_rules(self, is_stator):
    """selects step to add rules for lamination

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    self.add_rule_lamination(is_stator)
    self.select_duct_rules(is_stator)
    self.select_notch_rules(is_stator)

    if is_stator:
        self.select_material_rules("machine.stator.mat_type")
    else:
        self.select_material_rules("machine.rotor.mat_type")

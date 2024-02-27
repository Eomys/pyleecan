def select_LamSlotWind_rules(self, is_stator):
    """select all steps related to lamination

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object

    is_stator : bool
        True lam is stator, False lam is rotor
    """

    self.select_slot_rules(is_stator)
    self.select_lamination_rules(is_stator)
    self.select_winding_rules(is_stator)
    self.select_conductor_rules(is_stator)

def selection_LamSlotWind_rules(self, is_stator):
    """Selection all steps related to lamination

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object

    is_stator : bool
        True lam is stator, False lam is rotor
    """

    self.selection_slot_rules(is_stator)
    self.selection_lamination_rules(is_stator)
    self.selection_winding_rules(is_stator)
    self.selection_conductor_rules(is_stator)

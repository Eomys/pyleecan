def selection_LamSlotWind_rules(self):
    """Selection all step related to lamination

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """
    is_stator = True
    self.selection_slot_rules(is_stator)
    self.selection_lamination_rules(is_stator)
    self.selection_winding_rules(is_stator)
    self.selection_conductor_rules(is_stator)

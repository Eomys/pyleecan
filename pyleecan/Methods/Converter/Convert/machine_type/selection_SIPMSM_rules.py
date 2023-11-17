def selection_SIPMSM_rules(self):
    """selection step to have rules for motor SIPMSM

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    # step for stator
    self.selection_LamSlotWind_rules(is_stator=True)

    # step for rotor
    is_stator = False
    self.selection_magnet_rules(is_stator)
    self.selection_lamination_rules(is_stator)
    self.selection_skew_rules(is_stator)

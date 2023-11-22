def selection_WRSM_rules(self):
    """selection step to have rules for motor WRSM

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object

    """
    # step for stator
    self.selection_LamSlotWind_rules(is_stator=True)

    # step for rotor
    is_stator = False
    self.selection_rotor_pole_rules()
    self.selection_lamination_rules(is_stator)
    self.selection_winding_rules(is_stator)
    self.selection_bar_rules(is_stator)
    self.selection_conductor_rules(is_stator)
    self.selection_skew_rules(is_stator)

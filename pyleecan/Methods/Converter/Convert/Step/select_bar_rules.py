def select_bar_rules(self, is_stator):
    """selects step to add bar rules

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    self.add_rule_rotor_bar(is_stator)

    self.get_logger().error("Approximation for rotor bar conversion")

    self.select_material_rules("machine.rotor.ring_mat")

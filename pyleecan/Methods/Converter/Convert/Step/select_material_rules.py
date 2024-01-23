def select_material_rules(self, path_P):
    """selects rules for material

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    is_stator : bool
        True slot is in stator, False slot is in rotor

    """

    if self.is_P_to_other:
        type_material = self.convert_material_to_other(path_P)
    else:
        type_material = self.convert_material_to_P(path_P)

    if type_material != "":
        self.add_rule_material(path_P, type_material)
        self.add_rule_material_magnetics(path_P, type_material)

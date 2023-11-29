def convert_to_P(self, other_dict, machine, other_unit_dict):
    """Selects value in other_dict and implements it in machine

    Parameters
    ----------
    self : RulesEquation
        A RuleEquation object
    other_dict : dict
        dict created from the file to be converted
    machine : Machine
        A pyleecan machine
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)

    """

    value = self.solve_equation(
        other_dict, machine, other_unit_dict, is_P_to_other=True
    )

    for param in self.param:
        if param["variable"] == "x":
            self.set_P(machine, value, param["path"])

    return machine

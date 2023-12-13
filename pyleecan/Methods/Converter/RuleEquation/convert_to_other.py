def convert_to_other(self, other_dict, machine, other_unit_dict):
    """Selects value in machine and implements it in other_dict

    Parameters
    ----------
    self : RuleEquation
        A RuleEquation object
    other_dict : dict
        dict created from the machine to be converted
    machine : Machine
        A pyleecan machine
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)
    """

    value = self.solve_equation(
        other_dict, machine, other_unit_dict, is_P_to_other=False
    )

    # adding value in other_dict
    for variable in self.param:
        if variable["variable"] == "y":
            list_path = variable["path"]
            other_dict = self.set_other(other_dict, value, other_unit_dict, list_path)

    return other_dict

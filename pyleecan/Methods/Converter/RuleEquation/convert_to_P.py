from sympy.solvers import solve


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

    equation = self.equation

    for param in self.param:
        if param["src"] == "other":
            other_value = self.get_other(other_dict, param["path"], other_unit_dict)
            equation = equation.replace(param["variable"], str(other_value))

    for param in self.param:
        if param["src"] == "pyleecan":
            if not param["variable"] == "x":
                P_value = self.get_P(param["path"], machine)
                equation = equation.replace(param["variable"], str(P_value))

    # equation cleaning, delete space and replace + and - to delete =
    equation = equation.replace(" ", "")
    equation = equation.split("=")

    equation = equation[0] + "-(" + equation[1] + ")"
    # result = eval(equation)

    value = solve(equation)
    value = float(value[0])

    for param in self.param:
        if param["variable"] == "x":
            self.set_P(machine, value, param["path"])

    return machine

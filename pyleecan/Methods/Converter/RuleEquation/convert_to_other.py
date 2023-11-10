from sympy import Symbol
from sympy.solvers import solve


def convert_to_other(self, other_dict, machine, other_unit_dict):
    """Select value in machine and implements in other_dict

    Parameters
    ----------
    self : RuleEquation
        A RuleEquation object
    other_dict : dict
        dict created from the file to be converted
    machine : Machine
        A pyleecan machine
    other_unit_dict : dict
        dict with unit to make conversion (key: unit family, value: factor)

    """
    # we must have the same unit
    equation = self.equation

    # replace varialble mot
    for param in self.param:
        if param["src"] == "other" and not param["variable"].lower() == "y":
            other_value = self.get_other(other_dict, param["path"], other_unit_dict)
            equation = equation.replace(param["variable"], str(other_value))

    # replace variable pyleecan
    for param in self.param:
        if param["src"] == "pyleecan":
            P_value = self.get_P(param["path"], machine)

            equation = equation.replace(param["variable"], str(P_value))

    # equation cleaning, delete space and replace + and - to delete =
    equation = equation.replace(" ", "")
    equation = equation.split("=")

    equation = equation[0] + "-(" + equation[1] + ")"
    # result = eval(equation)

    value = solve(equation)
    value = float(value[0])

    # adding value in other_dict
    for variable in self.param:
        if variable["variable"] == "y":
            list_path = variable["path"]
            other_dict = self.set_other(other_dict, value, other_unit_dict, list_path)

    return other_dict

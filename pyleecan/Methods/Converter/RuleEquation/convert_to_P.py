from sympy import Symbol
from sympy.solvers import solve


def convert_to_P(self, other_dict, machine, other_unit_dict):
    """Select value in other_dict and implements in machine

    Parameters
    ----------
    self : RulesEquation
        A RuleEquation object
    other_dict : dict
        dict created from the file to be converted
    machine : Machine
        A pyleecan machine

    """
    # self.param
    # self.scaling_to_P

    # we must have the same unit
    unit = other_unit_dict[self.unit_type]

    scaling = self.scaling_to_P

    for param in self.param:
        if param["src"] == "other":
            other_value = self.get_other(other_dict, param["path"], unit)

            scaling = scaling.replace(param["variable"], str(other_value))

    for param in self.param:
        if param["src"] == "pyleecan":
            if not param["variable"] == "x":
                P_value = self.get_P(param["path"], machine, unit=1)

                scaling = scaling.replace(param["variable"], str(P_value))

    # equation cleaning, delete space and replace + and - to delete =
    scaling = scaling.replace(" ", "")
    scaling = scaling.split("=")

    equation = scaling[0] + "-(" + scaling[1] + ")"
    # result = eval(equation)

    value = solve(equation)
    value = float(value[0])

    for param in self.param:
        if param["variable"] == "x":
            value_split = param["path"].split(".")

    path = value_split[0]
    for temp in range(1, len(value_split) - 1):
        path = eval('path+"."+value_split[temp]')

    setattr(
        eval(path),
        value_split[-1],
        value,
    )

    return machine

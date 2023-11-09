from sympy import Symbol
from sympy.solvers import solve


def convert_to_other(self, other_dict, machine, other_unit_dict):
    """Select value in machine and implements in other_dict

    Parameters
    ----------
    self : RulesEquation
        A RuleEquation object
    other_dict : dict
        dict created from the file to be converted
    machine : Machine
        A pyleecan machine

    """
    # self.param_other
    # self.param_pyleecan
    # self.scaling_to_P

    # we must have the same unit
    unit = other_unit_dict[self.unit_type]

    scaling = self.scaling_to_P

    # replace varialble mot
    for param in self.param:
        if param["src"] == "other":
            if not param["variable"] == "y":
                # unit = 1 beacause we want convert in the unit other so we don't need to change this unit
                other_value = self.get_other(other_dict, param["path"], unit=1)
                scaling = scaling.replace(param["variable"], str(other_value))

    # replace variable pyleecan
    for param in self.param:
        if param["src"] == "pyleecan":
            P_value = self.get_P(param["path"], machine, unit)

            scaling = scaling.replace(param["variable"], str(P_value))

    # equation cleaning, delete space and replace + and - to delete =
    scaling = scaling.replace(" ", "")
    scaling = scaling.split("=")

    equation = scaling[0] + "-(" + scaling[1] + ")"
    # result = eval(equation)

    value = solve(equation)
    value = float(value[0])

    # adding value in dict_other
    dict_temp = other_dict

    for variable in self.param:
        if variable["variable"] == "y":
            list_path = variable["path"]

            # self.set_other(other_dict, value)
            dict_temp = other_dict
            for key in list_path[:-1]:
                if key not in dict_temp:
                    dict_temp[key] = dict()
                dict_temp = dict_temp[key]
            # Set the value
            last_key = list_path[-1]
            dict_temp[last_key] = value

    return other_dict

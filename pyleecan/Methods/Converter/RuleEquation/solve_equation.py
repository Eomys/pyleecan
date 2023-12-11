from sympy.solvers import solve


def solve_equation(self, other_dict, machine, other_unit_dict, is_P_to_other):
    if is_P_to_other:
        name_var = "x"
    else:
        name_var = "y"

    # we must have the same unit for all parameters used in equation
    equation = self.equation

    for param in self.param:
        if param["src"] == "other":
            if param["src"] == "other" and not param["variable"].lower() == name_var:
                other_value = self.get_other(other_dict, param["path"], other_unit_dict)
                equation = equation.replace(param["variable"], str(other_value))

    for param in self.param:
        if param["src"] == "pyleecan":
            if not param["variable"] == name_var:
                P_value = self.get_P(param["path"], machine)
                equation = equation.replace(param["variable"], str(P_value))

    # equation cleaning, delete space and replace + and - to delete =
    equation = equation.replace(" ", "")
    equation = equation.split("=")

    equation = equation[0] + "-(" + equation[1] + ")"

    value = solve(equation)
    # value return a list of equation, all equations are first order so have only one solution
    return float(value[0])

from sympy import Symbol
from sympy.solvers import solve


def convert_to_P(self, other_dict, machine):
    # self.param
    # self.scaling_to_P

    # we must have the same unit
    unit = self.unit_type

    scaling = self.scaling_to_P

    for param in self.param:
        if param["src"] == "other":
            dict_temp = other_dict
            for temp in param["path"]:
                dict_temp = dict_temp[temp]

            # conversion unit
            unit = self.set_unit(self.unit_type)

            dict_temp = dict_temp * unit

            scaling = scaling.replace(param["variable"], str(dict_temp))

    for param in self.param:
        if param["src"] == "pyleecan":
            if not param["variable"] == "x":
                value_split = param["path"].split(".")

                path = value_split[0]
                for temp in range(1, len(value_split) - 1):
                    path = eval('path+"."+value_split[temp]')

                val_P = getattr(
                    eval(path),
                    value_split[-1],
                )

                # conversion unit
                unit = self.set_unit(self.unit_type)

                val_P = val_P * unit

                scaling = scaling.replace(param["variable"], str(val_P))

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

def convert_to_P(self, other_dict, unit_list, machine):
    # selection correct value
    dict_temp = other_dict
    for temp in self.other:
        dict_temp = dict_temp[temp]

    other_value = dict_temp

    unit = self.unit_type

    # possibility to have str in other_value
    if self.scaling_to_P != 1:
        other_value = other_value * self.scaling_to_P

    # set value in object machine
    value_split = self.pyleecan.split(".")

    path = value_split[0]
    for temp in range(1, len(value_split) - 1):
        path = eval('path+"."+value_split[temp]')

    setattr(
        eval(path),
        value_split[-1],
        other_value,
    )

    return machine

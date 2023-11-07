def convert_to_other(self, other_dict, machine):
    # select value in object machine
    P_value = self.get_P(machine)

    unit = self.set_unit(self.unit_type)

    # possibility to have str in other_value and conversion
    if self.scaling_to_P != 1:
        P_value = (P_value / self.scaling_to_P) * unit

    # set value in other_dict
    other_dict = self.set_other(other_dict, P_value)

    return other_dict

def convert_to_P(self, other_dict, unit_list, machine):
    if self.fct_name == "slotW11" or self.fct_name == "slotW11_H1":
        machine = globals()[self.fct_name](machine)

    elif self.fct_name == "rotor_slotW11" or self.fct_name == "rotor_slotW11_H1":
        machine = globals()[self.fct_name](machine)

    elif self.fct_name == "set_pole_pair_number_py":
        other_value = other_dict["[Dimensions]"]["Pole_Number"]
        # set_pole_pair_number(machine, other_value)

    else:
        print("complex")

    return machine

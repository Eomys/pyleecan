def convert_to_P(self, other_dict, unit_list, machine):
    # file_path = self.set_fct_name()

    if self.fct_name == "parallel_tooth_slotW11":
        machine = self.other_to_P(machine)

        # machine = globals()[self.fct_name](machine)
        # getattr(nom_classe, self.fct_name)

    elif self.fct_name == "set_pole_pair_number_py":
        other_value = other_dict["[Dimensions]"]["Pole_Number"]
        # set_pole_pair_number(machine, other_value)

    else:
        print("complex")

    return machine

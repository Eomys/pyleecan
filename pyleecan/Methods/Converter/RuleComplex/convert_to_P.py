from pyleecan.Methods.Converter.RuleComplex.def_slotW11 import slotW11, slotW11_H1


def convert_to_P(self, other_dict, unit_list, machine):
    if self.fct_name == "slotW11" or self.fct_name == "slotW11_H1":
        machine = globals()[self.fct_name](machine)

    elif self.fct_name == "set_pole_pair_number":
        machine = globals()[self.fct_name](machine)

    else:
        print("complex")

    return machine

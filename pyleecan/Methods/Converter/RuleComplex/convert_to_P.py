from pyleecan.Methods.Converter.RuleComplex.def_slotW11 import slotW11


def convert_to_P(self, other_dict, unit_list, machine):
    if self.fct_name == "def_slotW11":
        machine = slotW11(machine)

    else:
        print("complex")

    return machine

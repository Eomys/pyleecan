from pyleecan.Methods.Converter.RuleComplex.def_slotW11 import slotW11, slotW11_H1


def convert_to_P(self, other_dict, unit_list, machine):
    if self.fct_name == "def_slotW11":
        machine = slotW11(machine)

    if self.fct_name == "slotW11_H1":
        machine = slotW11_H1(machine)

    else:
        print("complex")

    return machine

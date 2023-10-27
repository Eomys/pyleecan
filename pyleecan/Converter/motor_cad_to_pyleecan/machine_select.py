from pyleecan.Converter.motor_cad_to_pyleecan.change_mot_dict import convert_mot_dict
from pyleecan.Methods.Converter.Machine_type_mot.get_BPM import get_BPM


class machine_select:
    def __init__(self, rules=[]):
        self.rules = rules
        self.mot_dict = convert_mot_dict()

    def add_rules(self, mot_dict, rules):
        return rules

    def machine_selection(self):
        dict_tmp = self.mot_dict["[Calc_Options]"]
        motor_type = dict_tmp["Motor_Type"]

        self.rules = self.add_rules(self.mot_dict, self.rules)

        if motor_type == "BPM":
            print("BPM")
            get_BPM(self)
        elif motor_type == "IM":
            print("IM")
        elif motor_type == "SRM":
            print("SRM")
        elif motor_type == "BPMO":
            print("BPMO")
        elif motor_type == "PMDC":
            print("PMDC")
        elif motor_type == "SYNC":
            print("SYNC")
        elif motor_type == "CLAW":
            print("CLAW")
        elif motor_type == "IM1PH":
            print("IM1PH")
        elif motor_type == "WFC":
            print("WFC")


if __name__ == "__main__":
    machine_select = machine_select()
    machine_select.machine_selection()

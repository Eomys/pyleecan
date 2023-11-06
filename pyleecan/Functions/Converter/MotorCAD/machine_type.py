def other_to_P(self, machine):
    print("ok")
    return machine


def P_to_other(self, other_dict):
    if "[Calc_Options]" not in other_dict:
        other_dict["[Calc_Options]"] = {}

    temp_dict = other_dict["[Calc_Options]"]

    temp_dict["Motor_Type"] = "BPM"

    return other_dict

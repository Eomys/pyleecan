def get_slot(self, is_stator):
    self.is_stator = is_stator
    dict_tmp = self.mot_dict["[Calc_Options]"]
    slot_type = dict_tmp["Slot_Type"]
    print(slot_type)

    if self.is_stator == True:
        print("stator")
    else:
        print("rotor")

    return self.rules

def set_other(self, other_dict, P_value):
    # Make sure that all the sub-keys exist
    dict_temp = other_dict
    for key in self.other_key_list[:-1]:
        if key not in dict_temp:
            dict_temp[key] = dict()
        dict_temp = dict_temp[key]
    # Set the value
    last_key = self.other_key_list[-1]
    dict_temp[last_key] = P_value

    return other_dict
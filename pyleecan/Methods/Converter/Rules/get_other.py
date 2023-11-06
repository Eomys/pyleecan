def get_other(self, other_dict):
    # selection correct value in other_dict
    dict_temp = other_dict
    for temp in self.other_key_list:
        dict_temp = dict_temp[temp]

    other_value = dict_temp

    return other_value

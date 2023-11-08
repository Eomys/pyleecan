# -*- coding: utf-8 -*-

import pytest
from pyleecan.Classes.ConvertMC import ConvertMC
from pyleecan.Methods.Converter.ConvertMC.convert_other_to_dict import (
    convert_other_to_dict,
)


path = "EMD240_v16.mot"


class Test_converter_mot(object):
    def compare(self, path):
        converter = ConvertMC()

        machine = converter.convert_to_P(path)
        dict_to_other = {}
        dict_to_other = converter.convert_to_other(machine, dict_to_other)

        dict_to_mot = convert_other_to_dict(path)

        for path_dict in dict_to_other:
            temp_dict = dict_to_other[path_dict]

            for path_2 in temp_dict:
                value = temp_dict[path_2]

                if path_dict not in dict_to_other:
                    pass
                elif path_2 not in dict_to_other[path_dict]:
                    pass
                else:
                    temp = dict_to_mot[path_dict][path_2]
                    msg = f"{path_dict}, {path_2}"
                    if type(value) != str:
                        assert abs(dict_to_mot[path_dict][path_2]) == pytest.approx(
                            value
                        ), msg

                    elif value != temp:
                        raise ValueError


if __name__ == "__main__":
    a = Test_converter_mot()
    a.compare(path)
    print("Done")

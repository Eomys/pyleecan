# -*- coding: utf-8 -*-

import pytest

from pyleecan.Methods.Converter.Convert.convert import convert_to_P, convert_to_other
from pyleecan.Methods.Converter.ConvertMC.convert_other_to_dict import (
    convert_other_to_dict,
)


path = "pyleecan\pyleecan\Methods\Converter\ConvertMC\EMD240_v16.mot"


class Test_converter_mot(object):
    def compare(self, path):
        machine = convert_to_P(path)
        dict_to_other = {}
        dict_to_other = convert_to_other(machine, dict_to_other)

        dict_to_mot = convert_other_to_dict(path)

        for path_dict in dict_to_other:
            temp_dict = dict_to_other[path_dict]

            for path_2 in temp_dict:
                value = temp_dict[path_2]

                # print(path_dict)
                # print(path_2)
                # print(value)

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

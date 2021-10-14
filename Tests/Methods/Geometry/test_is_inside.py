# -*- coding: utf-8 -*

import pytest
from pyleecan.Classes.Circle import Circle
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine

# Configuring the test of is_inside
inside_test = list()

# Test 1 : checking if a point is inside a circle of radius 1 at 0 + 0j
C1 = Circle()
inside_test.append({"surf": C1, "Z": 0, "result": True})  # inside
inside_test.append({"surf": C1, "Z": 1, "result": False})  # online not OK
inside_test.append({"surf": C1, "Z": 1, "is_online":True,"result": True})  # online OK
inside_test.append({"surf": C1, "Z": 20, "result": False})  # outside

# Test 2 : checking if a point is inside a "C-shape" surface
A0 = 0
A1 = 0 + 4j
A2 = 3 + 4j
A3 = 3 + 3j
A4 = 1 + 3j
A5 = 1 + 1j
A6 = 3 + 1j
A7 = 3

line_list1 = list()
line_list1.append(Segment(A0, A1))
line_list1.append(Segment(A1, A2))
line_list1.append(Segment(A2, A3))
line_list1.append(Segment(A3, A4))
line_list1.append(Segment(A4, A5))
line_list1.append(Segment(A5, A6))
line_list1.append(Segment(A6, A7))
line_list1.append(Segment(A7, A0))

C2 = SurfLine(line_list=line_list1, point_ref=A0)

inside_test.append({"surf": C2, "Z": 0.5 + 2j, "result": True})  # inside
inside_test.append({"surf": C2, "Z": 2 + 2j, "result": False})  # outside
inside_test.append({"surf": C2, "Z": 3, "result": False})  # online not OK
inside_test.append({"surf": C2, "Z": 3, "is_online":True,"result": True})  # online OK


@pytest.mark.parametrize("test_dict", inside_test)
def test_is_inside(test_dict):
    # Function that test is_inside for a circle and for a C-shaped surface
    surf = test_dict["surf"]
    Z = test_dict["Z"]
    result = test_dict["result"]

    if "is_online" in test_dict:
        is_online = test_dict["is_online"]
        assert result ==  surf.is_inside(Z,is_online)
    else:
        assert result == surf.is_inside(Z)

if __name__ == "__main__":
    for test_dict in inside_test:
        test_is_inside(test_dict)  
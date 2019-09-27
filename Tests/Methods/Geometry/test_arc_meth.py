# -*- coding: utf-8 -*-
"""
@author: pierre_b
"""

from unittest import TestCase

from ddt import ddt, data

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Arc2 import Arc2
from pyleecan.Classes.Arc3 import Arc3
from numpy import pi, array, exp, sqrt


# For AlmostEqual
DELTA = 1e-6

split_test = list()
# 1) Arc1, 1 Intersection
split_test.append(
    {
        "arc": Arc1(begin=1, end=1j, radius=1, is_trigo_direction=True),  # Arc to split
        "Z1": 0,  # First point of cutting line
        "Z2": 1j + 1,  # Seconf point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [1 * exp(1j * pi / 4)],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=1 * exp(1j * pi / 4), end=1j, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=1, end=1 * exp(1j * pi / 4), radius=1, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 2) Case 1 with is_trigo = False
split_test.append(
    {
        "arc": Arc1(
            begin=1, end=1j, radius=1, is_trigo_direction=False
        ),  # Arc to split
        "Z1": 0,  # First point of cutting line
        "Z2": 1j + 1,  # Seconf point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [1 * exp(1j * 5 * pi / 4)],  # Expected intersection points
        "Zs_top": [
            Arc1(
                begin=1 * exp(1j * 5 * pi / 4),
                end=1j,
                radius=-1,
                is_trigo_direction=False,
            )
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(
                begin=1,
                end=1 * exp(1j * 5 * pi / 4),
                radius=-1,
                is_trigo_direction=False,
            )
        ],  # Expected result for slip not is_top
    }
)
# 3) Case 1 with reverse Z1 and Z2
split_test.append(
    {
        "arc": Arc1(begin=1, end=1j, radius=1, is_trigo_direction=True),  # Arc to split
        "Z1": 1j + 1,  # First point of cutting line
        "Z2": 0,  # Seconf point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [1 * exp(1j * pi / 4)],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=1, end=1 * exp(1j * pi / 4), radius=1, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=1 * exp(1j * pi / 4), end=1j, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 4) Arc1, No Intersection
split_test.append(
    {
        "arc": Arc1(
            begin=1 - 1j, end=-1 - 1j, radius=1, is_trigo_direction=True
        ),  # Arc to split
        "Z1": 1 - 1.1j,  # First point of cutting line
        "Z2": -1 - 1.1j,  # Seconf point of cutting line
        "center": -1j,  # Center of the arc (should not be changed by the split)
        "Zi": [],  # Expected intersection points
        "Zs_top": [],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=1 - 1j, end=-1 - 1j, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip not is_top
    }
)
# 5) Arc1, 1 Intersection = begin (no tangent)
split_test.append(
    {
        "arc": Arc1(
            begin=1 - 1j, end=-1 - 1j, radius=1, is_trigo_direction=True
        ),  # Arc to split
        "Z1": -2j,  # First point of cutting line
        "Z2": 2,  # Seconf point of cutting line
        "center": -1j,  # Center of the arc (should not be changed by the split)
        "Zi": [1 - 1j],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=1 - 1j, end=-1 - 1j, radius=1, is_trigo_direction=True)
        ],  # Expected result for slip is_top
        "Zs_bot": [],  # Expected result for slip not is_top
    }
)
# 6) Arc1, 1 Intersection = end (no tangent)
split_test.append(
    {
        "arc": Arc1(
            begin=-2 - 2j, end=-2 + 2j, radius=-sqrt(5), is_trigo_direction=False
        ),  # Arc to split
        "Z1": 1 + 2j,  # First point of cutting line
        "Z2": 2 + 2j,  # Seconf point of cutting line
        "center": -1,  # Center of the arc (should not be changed by the split)
        "Zi": [-2 + 2j],  # Expected intersection points
        "Zs_top": [],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=-2 - 2j, end=-2 + 2j, radius=-sqrt(5), is_trigo_direction=False)
        ],  # Expected result for slip not is_top
    }
)
# 7) Arc1, 1 Intersection (tangent)
split_test.append(
    {
        "arc": Arc1(
            begin=-2 - 2j, end=-2 + 2j, radius=2, is_trigo_direction=False
        ),  # Arc to split
        "Z1": -4 + 2j,  # First point of cutting line
        "Z2": -4 - 2j,  # Seconf point of cutting line
        "center": -2,  # Center of the arc (should not be changed by the split)
        "Zi": [-4],  # Expected intersection points
        "Zs_top": [
            Arc1(begin=-2 - 2j, end=-4, radius=-2, is_trigo_direction=False)
        ],  # Expected result for slip is_top
        "Zs_bot": [
            Arc1(begin=-4, end=-2 + 2j, radius=-2, is_trigo_direction=False)
        ],  # Expected result for slip not is_top
    }
)
# 8) Arc3 No Intersection
split_test.append(
    {
        "arc": Arc3(begin=1, end=-1, is_trigo_direction=False),  # Arc to split
        "Z1": 2 + 2j,  # First point of cutting line
        "Z2": 3 + 2j,  # Seconf point of cutting line
        "center": 0,  # Center of the arc (should not be changed by the split)
        "Zi": [],  # Expected intersection points
        "Zs_top": [],  # Expected result for slip is_top
        "Zs_bot": [
            Arc3(begin=1, end=-1, is_trigo_direction=False)
        ],  # Expected result for slip not is_top
    }
)


@ddt
class test_Arc_split_meth(TestCase):
    """unittest for Arc split methods"""

    @data(*split_test)
    def test_split_line(self, test_dict):
        """Check that the intersection and the split_line is computed correctly
        """
        arc_obj = test_dict["arc"]

        # Check center
        Zc = arc_obj.get_center()
        msg = (
            "Wrong center: returned "
            + str(Zc)
            + ", expected: "
            + str(test_dict["center"])
        )
        self.assertAlmostEqual(abs(Zc - test_dict["center"]), 0, msg=msg)

        # Check intersection
        result = arc_obj.intersect_line(test_dict["Z1"], test_dict["Z2"])
        self.assertEqual(len(result), len(test_dict["Zi"]))
        msg = (
            "Wrong intersection: returned "
            + str(result)
            + ", expected: "
            + str(test_dict["Zi"])
        )
        for ii in range(len(result)):
            self.assertAlmostEqual(abs(result[ii] - test_dict["Zi"][ii]), 0, msg=msg)

        # Check split_line is_top=True
        split_list = arc_obj.split_line(test_dict["Z1"], test_dict["Z2"], is_top=True)
        self.assertEqual(len(split_list), len(test_dict["Zs_top"]))
        msg = "Wrong split top: returned [\n"
        for split in split_list:
            msg += (
                "beg:"
                + str(split.get_begin())
                + ", end:"
                + str(split.get_end())
                + ", R:"
                + str(split.comp_radius())
                + ", alpha:"
                + str(split.get_angle())
                + "\n"
            )
        msg += "], expected: [\n"
        for split in test_dict["Zs_top"]:
            msg += (
                "beg:"
                + str(split.get_begin())
                + ", end:"
                + str(split.get_end())
                + ", R:"
                + str(split.comp_radius())
                + ", alpha:"
                + str(split.get_angle())
                + "\n"
            )
        msg += "]"
        for ii in range(len(split_list)):
            self.assertEqual(type(split_list[ii]), type(test_dict["Zs_top"][ii]), msg)
            self.assertAlmostEqual(
                abs(split_list[ii].get_begin() - test_dict["Zs_top"][ii].get_begin()),
                0,
                msg=msg,
            )
            self.assertAlmostEqual(
                abs(split_list[ii].get_end() - test_dict["Zs_top"][ii].get_end()),
                0,
                msg=msg,
            )
            self.assertEqual(
                split_list[ii].comp_radius(), test_dict["Zs_top"][ii].comp_radius(), msg
            )
            self.assertAlmostEqual(
                split_list[ii].get_angle(),
                test_dict["Zs_top"][ii].get_angle(),
                delta=1e-6,
                msg=msg,
            )
            # Check center
            Zc = split_list[ii].get_center()
            msg = (
                "Wrong Split center top: returned "
                + str(Zc)
                + ", expected: "
                + str(test_dict["center"])
            )
            self.assertAlmostEqual(abs(Zc - test_dict["center"]), 0, msg=msg)
        # Check split_line is_top=False
        split_list = arc_obj.split_line(test_dict["Z1"], test_dict["Z2"], is_top=False)
        self.assertEqual(len(split_list), len(test_dict["Zs_bot"]))
        msg = "Wrong split bot: returned [\n"
        for split in split_list:
            msg += (
                "beg:"
                + str(split.get_begin())
                + ", end:"
                + str(split.get_end())
                + ", R:"
                + str(split.comp_radius())
                + ", alpha:"
                + str(split.get_angle())
                + "\n"
            )
        msg += "\n], expected: [\n"
        for split in test_dict["Zs_bot"]:
            msg += (
                "beg:"
                + str(split.get_begin())
                + ", end:"
                + str(split.get_end())
                + ", R:"
                + str(split.comp_radius())
                + ", alpha:"
                + str(split.get_angle())
                + "\n"
            )
        msg += "]"
        for ii in range(len(split_list)):
            self.assertEqual(type(split_list[ii]), type(test_dict["Zs_bot"][ii]), msg)
            self.assertAlmostEqual(
                abs(split_list[ii].get_begin() - test_dict["Zs_bot"][ii].get_begin()),
                0,
                msg=msg,
            )
            self.assertAlmostEqual(
                abs(split_list[ii].get_end() - test_dict["Zs_bot"][ii].get_end()),
                0,
                msg=msg,
            )
            self.assertEqual(
                split_list[ii].comp_radius(), test_dict["Zs_bot"][ii].comp_radius(), msg
            )
            self.assertAlmostEqual(
                split_list[ii].get_angle(),
                test_dict["Zs_bot"][ii].get_angle(),
                delta=1e-6,
                msg=msg,
            )
            # Check center
            Zc = split_list[ii].get_center()
            msg = (
                "Wrong Split center bot: returned "
                + str(Zc)
                + ", expected: "
                + str(test_dict["center"])
            )
            self.assertAlmostEqual(abs(Zc - test_dict["center"]), 0, msg=msg)

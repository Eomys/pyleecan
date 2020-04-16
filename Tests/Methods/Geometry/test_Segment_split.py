# -*- coding: utf-8 -*-

from unittest import TestCase

from ddt import ddt, data

from ....Classes.Segment import Segment

from ....Methods.Geometry.Segment.check import PointSegmentError
from ....Methods.Geometry.Segment.discretize import NbPointSegmentDError
from numpy import pi, array, exp


# For AlmostEqual
DELTA = 1e-6

split_list = list()
# 1) Intersection is a point of the cutting line
split_list.append(
    {
        "begin": 0,  # Begin of the segment
        "end": 1,  # End of the segment
        "Z1": 0.5,  # First point of cutting line
        "Z2": 1j,  # Seconf point of cutting line
        "Zi": [0.5],  # Expected intersection points
        "Zb_top": 0,  # Expected begin for cutting with is_top
        "Ze_top": 0.5,  # Expected end for cutting with is_top
        "Zb_bot": 0.5,  # Expected begin for cutting with not is_top
        "Ze_bot": 1,  # Expected end for cutting with not is_top
    }
)
# 2) Same case as previous one with reverse Z1 and Z2
split_list.append(
    {
        "begin": 0,  # Begin of the segment
        "end": 1,  # End of the segment
        "Z1": 1j,  # First point of cutting line
        "Z2": 0.5,  # Seconf point of cutting line
        "Zi": [0.5],  # Expected intersection points
        "Zb_top": 0.5,  # Expected begin for cutting with is_top
        "Ze_top": 1,  # Expected end for cutting with is_top
        "Zb_bot": 0,  # Expected begin for cutting with not is_top
        "Ze_bot": 0.5,  # Expected end for cutting with not is_top
    }
)
# 3) No intersection
split_list.append(
    {
        "begin": 0,  # Begin of the segment
        "end": 1,  # End of the segment
        "Z1": 1j,  # First point of cutting line
        "Z2": 1j + 1,  # Seconf point of cutting line
        "Zi": [],  # Expected intersection points
        "Zb_top": None,  # Expected begin for cutting with is_top
        "Ze_top": None,  # Expected end for cutting with is_top
        "Zb_bot": 0,  # Expected begin for cutting with not is_top
        "Ze_bot": 1,  # Expected end for cutting with not is_top
    }
)
# 4) Same case as previous one with reverse Z1 and Z2
split_list.append(
    {
        "begin": 0,  # Begin of the segment
        "end": 1,  # End of the segment
        "Z1": 1j + 1,  # First point of cutting line
        "Z2": 1j,  # Seconf point of cutting line
        "Zi": [],  # Expected intersection points
        "Zb_top": 0,  # Expected begin for cutting with is_top
        "Ze_top": 1,  # Expected end for cutting with is_top
        "Zb_bot": None,  # Expected begin for cutting with not is_top
        "Ze_bot": None,  # Expected end for cutting with not is_top
    }
)
# 5) Cutting point is begin
split_list.append(
    {
        "begin": -1,  # Begin of the segment
        "end": 1j,  # End of the segment
        "Z1": -1 - 1j,  # First point of cutting line
        "Z2": -1 + 1j,  # Seconf point of cutting line
        "Zi": [-1],  # Expected intersection points
        "Zb_top": None,  # Expected begin for cutting with is_top
        "Ze_top": None,  # Expected end for cutting with is_top
        "Zb_bot": -1,  # Expected begin for cutting with not is_top
        "Ze_bot": 1j,  # Expected end for cutting with not is_top
    }
)
# 6) Cutting point is end
split_list.append(
    {
        "begin": -1,  # Begin of the segment
        "end": 1j,  # End of the segment
        "Z1": -1j,  # First point of cutting line
        "Z2": +1j,  # Seconf point of cutting line
        "Zi": [1j],  # Expected intersection points
        "Zb_top": -1,  # Expected begin for cutting with is_top
        "Ze_top": 1j,  # Expected end for cutting with is_top
        "Zb_bot": None,  # Expected begin for cutting with not is_top
        "Ze_bot": None,  # Expected end for cutting with not is_top
    }
)
# 7) Segment is part of the cutting line
split_list.append(
    {
        "begin": 0,  # Begin of the segment
        "end": 1 + 1j,  # End of the segment
        "Z1": -1 - 1j,  # First point of cutting line
        "Z2": -2 - 2j,  # Seconf point of cutting line
        "Zi": [0, 1 + 1j],  # Expected intersection points
        "Zb_top": 0,  # Expected begin for cutting with is_top
        "Ze_top": 1 + 1j,  # Expected end for cutting with is_top
        "Zb_bot": 0,  # Expected begin for cutting with not is_top
        "Ze_bot": 1 + 1j,  # Expected end for cutting with not is_top
    }
)


@ddt
class test_Segment_split_meth(TestCase):
    """unittest for Segment split methods"""

    @data(*split_list)
    def test_intersect(self, test_dict):
        """Check that the intersection is computed correctly
        """
        seg = Segment(test_dict["begin"], test_dict["end"])

        # Check intersection
        result = seg.intersect_line(test_dict["Z1"], test_dict["Z2"])
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
        seg2 = seg.split_line(test_dict["Z1"], test_dict["Z2"], is_top=True)
        self.assertEqual(type(seg2), list)
        if len(seg2) > 0:
            self.assertEqual(len(seg2), 1)
            msg = (
                "Wrong begin with is_top: returned "
                + str(seg2[0].begin)
                + ", expected: "
                + str(test_dict["Zb_top"])
            )
            self.assertAlmostEqual(abs(seg2[0].begin - test_dict["Zb_top"]), 0, msg=msg)
            msg = (
                "Wrong end with is_top: returned "
                + str(seg2[0].end)
                + ", expected: "
                + str(test_dict["Ze_top"])
            )
            self.assertAlmostEqual(abs(seg2[0].end - test_dict["Ze_top"]), 0, msg=msg)
        else:  # No intersection
            self.assertIsNone(test_dict["Zb_top"])

        # Check split_line is_top=False
        seg3 = seg.split_line(test_dict["Z1"], test_dict["Z2"], is_top=False)
        self.assertEqual(type(seg3), list)
        if len(seg3) > 0:
            self.assertEqual(len(seg3), 1)
            msg = (
                "Wrong begin with not is_top: returned "
                + str(seg3[0].begin)
                + ", expected: "
                + str(test_dict["Zb_bot"])
            )
            self.assertAlmostEqual(abs(seg3[0].begin - test_dict["Zb_bot"]), 0, msg=msg)
            msg = (
                "Wrong end with not is_top: returned "
                + str(seg3[0].end)
                + ", expected: "
                + str(test_dict["Ze_bot"])
            )
            self.assertAlmostEqual(abs(seg3[0].end - test_dict["Ze_bot"]), 0, msg=msg)
        else:  # No intersection
            self.assertIsNone(test_dict["Zb_bot"])

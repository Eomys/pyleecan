# -*- coding: utf-8 -*-
"""
Created on Fri Dec 05 11:19:47 2014

@author: pierre_b
"""

from unittest import TestCase

from ddt import ddt, data

from pyleecan.Classes.Segment import Segment

from pyleecan.Methods.Geometry.Segment.check import PointSegmentError
from pyleecan.Methods.Geometry.Segment.discretize import NbPointSegmentDError
from numpy import pi, array, exp


# For AlmostEqual
DELTA = 1e-6

discretize_test = list()

# Horizontal segment (in complex) : 0 to 10
discretize_test.append({"nb_point": 3, "begin": 0, "end": 10})
discretize_test[0]["result"] = array([0 + 0j, 2.5 + 0j, 5 + 0j, 7.5 + 0j, 10 + 0j])

# X= Y segment (in complex) : 0 to 10+10j
discretize_test.append(
    {"nb_point": 0, "begin": 0, "end": 14.1421356237 * exp(1j * pi / 4)}
)
discretize_test[1]["result"] = array([0j, 10.0 + 10.0j])

# X= Y segment (in complex) : 0 to 10+10j
discretize_test.append(
    {"nb_point": 1, "begin": 0, "end": 14.1421356237 * exp(1j * pi / 4)}
)
discretize_test[2]["result"] = array([0j, 5 + 5j, 10.0 + 10.0j])

comp_length_test = list()
comp_length_test.append(
    {"begin": 0, "end": 14.1421356237 * exp(1j * pi / 4), "length": 14.1421356237}
)
comp_length_test.append({"begin": 0, "end": 10, "length": 10})
comp_length_test.append({"begin": 1, "end": 10, "length": 9})
comp_length_test.append({"begin": 1j, "end": 10j, "length": 9})
comp_length_test.append({"begin": 0, "end": 3 + 4j, "length": 5})


@ddt
class test_Segment_meth(TestCase):
    """unittest for Segment methods"""

    def test_check(self):
        """Check that you can detect a one point segment
        """
        segment = Segment(0, 0)
        with self.assertRaises(PointSegmentError):
            segment.check()

    @data(*discretize_test)
    def test_dicretize(self, test_dict):
        """Check that you can discretize a segment
        """
        segment = Segment(test_dict["begin"], test_dict["end"])

        result = segment.discretize(test_dict["nb_point"])

        self.assertEqual(result.size, test_dict["result"].size)
        for i in range(0, result.size):
            self.assertAlmostEqual(result[i], test_dict["result"][i], delta=DELTA)

    def test_discretize_Point_error(self):
        """Check that dicretize can detect a one point segment
        """
        segment = Segment(0, 0)
        with self.assertRaises(PointSegmentError):
            segment.discretize(5)

    def test_discretize_Nb_error(self):
        """Check that you can detect a wrong argument
        """
        segment = Segment(0, 10)
        with self.assertRaises(NbPointSegmentDError):
            segment.discretize(-1)

    @data(*comp_length_test)
    def test_comp_length(self, test_dict):
        """Check that you the length return by comp_length is correct
        """
        segment = Segment(test_dict["begin"], test_dict["end"])

        self.assertAlmostEqual(segment.comp_length(), test_dict["length"])

    def test_comp_length_Point_error(self):
        """Check that comp_length can detect a one point segment
        """
        segment = Segment(0, 0)
        with self.assertRaises(PointSegmentError):
            segment.comp_length()

    def test_get_middle(self):
        """Check that you can compute the middle of the segment
        """
        segment = Segment(0, 10)
        result = segment.get_middle()
        expect = 5.0
        self.assertAlmostEqual(abs(result - expect), 0)

        segment = Segment(10, 10 * exp(1j * pi / 2))
        result = segment.get_middle()
        expect = 5 + 5j
        self.assertAlmostEqual(abs(result - expect), 0)

    def test_rotate(self):
        """Check that you can rotate the segment
        """
        segment = Segment(0, 1)
        segment.rotate(pi / 2)
        expect_begin = 0
        expect_end = 1j
        self.assertAlmostEqual(abs(expect_begin - segment.begin), 0)
        self.assertAlmostEqual(abs(expect_end - segment.end), 0)

        segment = Segment(1 + 1j, 1)
        segment.rotate(-pi / 2)
        expect_begin = 1 - 1j
        expect_end = -1j
        self.assertAlmostEqual(abs(expect_begin - segment.begin), 0)
        self.assertAlmostEqual(abs(expect_end - segment.end), 0)

    def test_translate(self):
        """Check that you can translate the segment
        """
        segment = Segment(0, 3j)
        segment.translate(2)
        expect_begin = 2
        expect_end = 2 + 3j
        self.assertAlmostEqual(abs(expect_begin - segment.begin), 0)
        self.assertAlmostEqual(abs(expect_end - segment.end), 0)

        segment = Segment(-2 + 1j, 2 + 3j)
        segment.translate(-2 - 3j)
        expect_begin = -4 - 2j
        expect_end = 0
        self.assertAlmostEqual(abs(expect_begin - segment.begin), 0)
        self.assertAlmostEqual(abs(expect_end - segment.end), 0)

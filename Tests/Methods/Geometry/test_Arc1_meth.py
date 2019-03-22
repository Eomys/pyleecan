# -*- coding: utf-8 -*-
"""
Created on Mon Dec 08 11:31:14 2014

@author: pierre_b
"""
from unittest import TestCase

from ddt import ddt, data

from pyleecan.Classes.Arc1 import Arc1

from pyleecan.Methods.Geometry.Arc1.check import PointArc1Error, RadiusArc1Error
from pyleecan.Methods.Geometry.Arc1.discretize import NbPointArc1DError
from numpy import pi, exp, sqrt, array


# For AlmostEqual
DELTA = 1e-6

discretize_test = list()

# inner left top arc
discretize_test.append(
    {"nb_point": 9, "begin": 1 * exp(1j * pi), "end": 1 * exp(1j * pi / 2), "Radius": 1}
)
discretize_test[0]["result"] = array(
    [
        -1,
        -0.84356553 + 1.23116594e-02j,
        -0.69098301 + 4.89434837e-02j,
        -0.54600950 + 1.08993476e-01j,
        -0.41221475 + 1.90983006e-01j,
        -0.29289322 + 2.92893219e-01j,
        -0.19098301 + 4.12214748e-01j,
        -0.10899348 + 5.46009500e-01j,
        -0.04894348 + 6.90983006e-01j,
        -0.01231166 + 8.43565535e-01j,
        1j,
    ]
)

# extern left top arc
discretize_test.append(
    {
        "nb_point": 9,
        "begin": 1 * exp(1j * pi),
        "end": 1 * exp(1j * pi / 2),
        "Radius": -1,
    }
)
discretize_test[1]["result"] = array(
    [
        -1,
        -9.87688341e-01 + 1.56434465e-01j,
        -9.51056516e-01 + 3.09016994e-01j,
        -8.91006524e-01 + 4.53990500e-01j,
        -8.09016994e-01 + 5.87785252e-01j,
        -7.07106781e-01 + 7.07106781e-01j,
        -5.87785252e-01 + 8.09016994e-01j,
        -4.53990500e-01 + 8.91006524e-01j,
        -3.09016994e-01 + 9.51056516e-01j,
        -1.56434465e-01 + 9.87688341e-01j,
        1j,
    ]
)

# extern right top arc
discretize_test.append(
    {"nb_point": 9, "begin": 1, "end": 1 * exp(1j * pi / 2), "Radius": 1}
)
discretize_test[2]["result"] = array(
    [
        1,
        9.87688341e-01 + 0.15643447j,
        9.51056516e-01 + 0.30901699j,
        8.91006524e-01 + 0.4539905j,
        8.09016994e-01 + 0.58778525j,
        7.07106781e-01 + 0.70710678j,
        5.87785252e-01 + 0.80901699j,
        4.53990500e-01 + 0.89100652j,
        3.09016994e-01 + 0.95105652j,
        1.56434465e-01 + 0.98768834j,
        1j,
    ]
)

# inner right top arc
discretize_test.append(
    {"nb_point": 9, "begin": 1, "end": 1 * exp(1j * pi / 2), "Radius": -1}
)
discretize_test[3]["result"] = array(
    [
        1,
        8.43565535e-01 + 0.01231166j,
        6.90983006e-01 + 0.04894348j,
        5.46009500e-01 + 0.10899348j,
        4.12214748e-01 + 0.19098301j,
        2.92893219e-01 + 0.29289322j,
        1.90983006e-01 + 0.41221475j,
        1.08993476e-01 + 0.5460095j,
        4.89434837e-02 + 0.69098301j,
        1.23116594e-02 + 0.84356553j,
        1j,
    ]
)

# extern left bottom arc
discretize_test.append(
    {
        "nb_point": 9,
        "begin": 1 * exp(1j * pi),
        "end": 1 * exp(1j * 3 * pi / 2),
        "Radius": 1,
    }
)
discretize_test[4]["result"] = array(
    [
        -1,
        -9.87688341e-01 - 1.56434465e-01j,
        -9.51056516e-01 - 3.09016994e-01j,
        -8.91006524e-01 - 4.53990500e-01j,
        -8.09016994e-01 - 5.87785252e-01j,
        -7.07106781e-01 - 7.07106781e-01j,
        -5.87785252e-01 - 8.09016994e-01j,
        -4.53990500e-01 - 8.91006524e-01j,
        -3.09016994e-01 - 9.51056516e-01j,
        -1.56434465e-01 - 9.87688341e-01j,
        -1j,
    ]
)

# inner left bottom arc
discretize_test.append(
    {
        "nb_point": 9,
        "begin": 1 * exp(1j * pi),
        "end": 1 * exp(1j * 3 * pi / 2),
        "Radius": -1,
    }
)
discretize_test[5]["result"] = array(
    [
        -1,
        -0.84356553 - 1.23116594e-02j,
        -0.69098301 - 4.89434837e-02j,
        -0.54600950 - 1.08993476e-01j,
        -0.41221475 - 1.90983006e-01j,
        -0.29289322 - 2.92893219e-01j,
        -0.19098301 - 4.12214748e-01j,
        -0.10899348 - 5.46009500e-01j,
        -0.04894348 - 6.90983006e-01j,
        -0.01231166 - 8.43565535e-01j,
        -1j,
    ]
)

# inner right bottom arc
discretize_test.append(
    {"nb_point": 9, "begin": 1, "end": 1 * exp(1j * 3 * pi / 2), "Radius": 1}
)
discretize_test[6]["result"] = array(
    [
        1,
        8.43565535e-01 - 0.01231166j,
        6.90983006e-01 - 0.04894348j,
        5.46009500e-01 - 0.10899348j,
        4.12214748e-01 - 0.19098301j,
        2.92893219e-01 - 0.29289322j,
        1.90983006e-01 - 0.41221475j,
        1.08993476e-01 - 0.5460095j,
        4.89434837e-02 - 0.69098301j,
        1.23116594e-02 - 0.84356553j,
        -1j,
    ]
)

# extern right bottom arc
discretize_test.append(
    {"nb_point": 9, "begin": 1, "end": 1 * exp(1j * 3 * pi / 2), "Radius": -1}
)
discretize_test[7]["result"] = array(
    [
        1,
        9.87688341e-01 - 0.15643447j,
        9.51056516e-01 - 0.30901699j,
        8.91006524e-01 - 0.4539905j,
        8.09016994e-01 - 0.58778525j,
        7.07106781e-01 - 0.70710678j,
        5.87785252e-01 - 0.80901699j,
        4.53990500e-01 - 0.89100652j,
        3.09016994e-01 - 0.95105652j,
        1.56434465e-01 - 0.98768834j,
        -1j,
    ]
)

comp_length_test = list()
comp_length_test.append({"begin": 0, "end": 1, "Radius": 2, "length": 1.010721020568})
comp_length_test.append(
    {"begin": 1, "end": 1 * exp(1j * pi / 2), "Radius": 1, "length": pi / 2}
)
comp_length_test.append(
    {"begin": 1, "end": 1 * exp(1j * 3 * pi / 2), "Radius": -1, "length": pi / 2}
)
comp_length_test.append(
    {"begin": 1, "end": 1 * exp(1j * pi), "Radius": 1, "length": pi}
)

# Dictionary to test get_middle
comp_mid_test = list()
comp_mid_test.append(
    {
        "begin": 1,
        "end": 1 * exp(1j * pi / 2),
        "radius": 1,
        "expect": sqrt(2) / 2 * (1 + 1j),
    }
)
comp_mid_test.append(
    {
        "begin": 2 * exp(1j * 3 * pi / 4),
        "end": 2 * exp(1j * pi / 4),
        "radius": -2,
        "expect": 2j,
    }
)
comp_mid_test.append({"begin": 2, "end": 3, "radius": -4, "expect": 2.5 + 0.031373j})
# Dictionary to test rotation
comp_rotate_test = list()
comp_rotate_test.append(
    {
        "begin": 1,
        "end": 1j,
        "radius": 1,
        "angle": pi / 2,
        "exp_begin": 1j,
        "exp_end": -1,
    }
)
comp_rotate_test.append(
    {
        "begin": 1 + 1j,
        "end": 2j,
        "radius": 1,
        "angle": -pi / 2,
        "exp_begin": 1 - 1j,
        "exp_end": 2,
    }
)
comp_rotate_test.append(
    {
        "begin": -1 + 2j,
        "end": -2 + 1j,
        "radius": 1,
        "angle": pi / 4,
        "exp_begin": -2.12132034 + 0.70710678j,
        "exp_end": -2.1213203 - 0.7071067j,
    }
)
# Dictonary to test translation
comp_translate_test = list()
comp_translate_test.append(
    {
        "begin": 1,
        "end": 1j,
        "radius": 1,
        "delta": 2 + 2j,
        "exp_begin": 3 + 2j,
        "exp_end": 2 + 3j,
    }
)
comp_translate_test.append(
    {
        "begin": 1 + 1j,
        "end": 2j,
        "radius": 1,
        "delta": -3,
        "exp_begin": -2 + 1j,
        "exp_end": -3 + 2j,
    }
)
comp_translate_test.append(
    {
        "begin": -1 + 2j,
        "end": -2 + 1j,
        "radius": 1,
        "delta": 2j,
        "exp_begin": -1 + 4j,
        "exp_end": -2 + 3j,
    }
)

get_angle_test = list()
get_angle_test.append({"begin": 1,
                       "end": 1j,
                       "radius": 1,
                       "is_deg": True,
                       "exp_angle": 90})
get_angle_test.append({"begin": 1j,
                       "end": 1,
                       "radius": 1,
                       "is_deg": True,
                       "exp_angle": 90.0})
get_angle_test.append({"begin": 1,
                       "end": 1j,
                       "radius": -1,
                       "is_deg": True,
                       "exp_angle": -90})
get_angle_test.append({"begin": 0,
                       "end": -2j-2,
                       "radius": 2,
                       "is_deg": False,
                       "exp_angle": pi/2})
get_angle_test.append({"begin": 1+1j,
                       "end": 1-1j,
                       "radius": -1,
                       "is_deg": False,
                       "exp_angle": -pi})
get_angle_test.append({"begin": 2+1j,
                       "end": 2-1j,
                       "radius": -1,
                       "is_deg": False,
                       "exp_angle": -pi})

@ddt
class test_Arc1_meth(TestCase):
    """unittest for Arc1 methods"""

    def test_check_Point(self):
        """Check that you can detect a one point arc
        """
        arc = Arc1(0, 0, 1)
        with self.assertRaises(PointArc1Error):
            arc.check()

    def test_check_Radius(self):
        """Check that you can detect null radius
        """
        arc = Arc1(0, 1, 0)
        with self.assertRaises(RadiusArc1Error):
            arc.check()

    @data(*discretize_test)
    def test_dicretize(self, test_dict):
        """Check that you can discretize an arc1
        """
        arc = Arc1(test_dict["begin"], test_dict["end"], test_dict["Radius"])

        result = arc.discretize(test_dict["nb_point"])

        self.assertEqual(result.size, test_dict["result"].size)
        for i in range(0, result.size):
            a = result[i]
            b = test_dict["result"][i]
            self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)

    def test_discretize_Point_error(self):
        """Check that discretize detect a one point arc1
        """
        arc = Arc1(0, 0, 2)
        with self.assertRaises(PointArc1Error):
            arc.discretize(5)

    def test_discretize_Radius_error(self):
        """Check that discretize detect a null radius
        """
        arc = Arc1(0, 1, 0)
        with self.assertRaises(RadiusArc1Error):
            arc.discretize(5)

    def test_discretize_Nb_error(self):
        """Check that discretize can detect a wrong arg
        """
        arc = Arc1(0, 1, 1)
        with self.assertRaises(NbPointArc1DError):
            arc.discretize(-1)

    def test_discretize_Nb_Type_error(self):
        """Check that discretize can detect a wrong arg
        """
        arc = Arc1(0, 1, 1)
        with self.assertRaises(NbPointArc1DError):
            arc.discretize("test")

    @data(*comp_length_test)
    def test_comp_length(self, test_dict):
        """Check that you the length return by comp_length is correct
        """
        arc = Arc1(test_dict["begin"], test_dict["end"], test_dict["Radius"])

        a = float(arc.comp_length())
        b = float(test_dict["length"])
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)

    def test_comp_length_Point_error(self):
        """Check that discretize detect a one point arc1
        """
        arc = Arc1(0, 0, 2)
        with self.assertRaises(PointArc1Error):
            arc.comp_length()

    def test_comp_length_Radius_error(self):
        """Check that discretize detect a null radius arc1
        """
        arc = Arc1(0, 1, 0)
        with self.assertRaises(RadiusArc1Error):
            arc.comp_length()

    def test_get_center(self):
        """Check that the can compute the center of the arc1
        """
        arc = Arc1(begin=1, end=1 * exp(1j * pi / 2), radius=1)
        result = arc.get_center()
        expect = 0
        self.assertAlmostEqual(abs(result - expect), 0)

        arc = Arc1(begin=2 * exp(1j * 3 * pi / 4), end=2 * exp(1j * pi / 4), radius=-2)
        result = arc.get_center()
        expect = 0
        self.assertAlmostEqual(abs(result - expect), 0)

        arc = Arc1(begin=2, end=3, radius=-0.5)
        result = arc.get_center()
        expect = 2.5
        self.assertAlmostEqual(abs(result - expect), 0, delta=1e-3)

    @data(*comp_mid_test)
    def test_get_middle(self, test_dict):
        """Check that you can compute the arc middle
        """
        arc = Arc1(
            begin=test_dict["begin"], end=test_dict["end"], radius=test_dict["radius"]
        )
        result = arc.get_middle()
        self.assertAlmostEqual(abs(result - test_dict["expect"]), 0, delta=1e-6)

    @data(*comp_rotate_test)
    def test_rotate(self, test_dict):
        """Check that you can rotate the arc1
        """
        arc = Arc1(
            begin=test_dict["begin"], end=test_dict["end"], radius=test_dict["radius"]
        )
        expect_radius = arc.radius
        arc.rotate(test_dict["angle"])

        self.assertAlmostEqual(abs(arc.begin - test_dict["exp_begin"]), 0, delta=1e-6)
        self.assertAlmostEqual(abs(arc.end - test_dict["exp_end"]), 0, delta=1e-6)
        self.assertAlmostEqual(abs(arc.radius - expect_radius), 0)

    @data(*comp_translate_test)
    def test_translate(self, test_dict):
        """Check that you can translate the arc1
        """
        arc = Arc1(
            begin=test_dict["begin"], end=test_dict["end"], radius=test_dict["radius"]
        )
        expect_radius = arc.radius
        arc.translate(test_dict["delta"])

        self.assertAlmostEqual(abs(arc.begin - test_dict["exp_begin"]), 0, delta=1e-6)
        self.assertAlmostEqual(abs(arc.end - test_dict["exp_end"]), 0, delta=1e-6)
        self.assertAlmostEqual(abs(arc.radius - expect_radius), 0)

    @data(*get_angle_test)
    def test_get_angle(self, test_dict):
        """Check that the arc1 computed angle is correct
        """
        arc = Arc1(begin=test_dict["begin"], end=test_dict["end"], radius=test_dict["radius"])
        result = arc.get_angle(test_dict["is_deg"])
        self.assertAlmostEqual(result, test_dict["exp_angle"])


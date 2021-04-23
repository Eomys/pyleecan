# -*- coding: utf-8 -*-

from pyleecan.Classes.Arc2 import Arc2

from pyleecan.Methods.Geometry.Arc2 import (
    PointArc2Error,
    AngleArc2Error,
    NbPointArc2DError,
    AngleRotationArc2Error,
    PointTranslateArc2Error,
)
from numpy import pi, array, sqrt, exp, angle
import pytest


# For AlmostEqual
DELTA = 1e-6

discretize_test = list()

# inner left top arc
discretize_test.append(
    {
        "nb_point": 9,
        "begin": 1 * exp(1j * pi),
        "center": 1.41421356237 * exp(1j * 3 * pi / 4),
        "angle": pi / 2,
    }
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
    {"nb_point": 9, "begin": 1 * exp(1j * pi), "center": 0, "angle": -pi / 2}
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
discretize_test.append({"nb_point": 9, "begin": 1, "center": 0, "angle": pi / 2})
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
    {
        "nb_point": 9,
        "begin": 1,
        "center": 1.41421356237 * exp(1j * pi / 4),
        "angle": -pi / 2,
    }
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
    {"nb_point": 9, "begin": 1 * exp(1j * pi), "center": 0, "angle": pi / 2}
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
        "center": 1.41421356237 * exp(1j * 5 * pi / 4),
        "angle": -pi / 2,
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
    {
        "nb_point": 9,
        "begin": 1,
        "center": 1.41421356237 * exp(1j * 7 * pi / 4),
        "angle": pi / 2,
    }
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
discretize_test.append({"nb_point": 9, "begin": 1, "center": 0, "angle": -pi / 2})
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
comp_length_test.append({"begin": 1, "center": 0, "angle": pi / 2, "length": pi / 2})
comp_length_test.append({"begin": 2, "center": 0, "angle": pi / 4, "length": pi / 2})
# Dictionary to test get_middle
comp_mid_test = list()
comp_mid_test.append(
    {"begin": 1, "center": 0, "angle": pi / 2, "expect": sqrt(2) / 2 * (1 + 1j)}
)
comp_mid_test.append(
    {"begin": 2 * exp(1j * 3 * pi / 4), "center": 0, "angle": -pi / 2, "expect": 2j}
)
comp_mid_test.append({"begin": 2, "center": 1, "angle": pi, "expect": 1 + 1j})
# Dictionary to test rotation
comp_rotate_test = list()
comp_rotate_test.append(
    {
        "begin": 1,
        "center": 0,
        "angle": pi / 2,
        "alpha": pi / 2,
        "exp_begin": 1j,
        "exp_center": 0,
    }
)
comp_rotate_test.append(
    {
        "begin": 2 + 1j,
        "center": 1 + 1j,
        "angle": pi / 2,
        "alpha": -pi / 2,
        "exp_begin": 1 - 2j,
        "exp_center": 1 - 1j,
    }
)
comp_rotate_test.append(
    {
        "begin": 1 - 1j,
        "center": 1,
        "angle": -pi / 4,
        "alpha": -pi / 4,
        "exp_begin": -sqrt(2) * 1j,
        "exp_center": (sqrt(2) / 2) * (1 - 1j),
    }
)
# Dictonary to test translation
comp_translate_test = list()
comp_translate_test.append(
    {
        "begin": 1j,
        "center": 0,
        "angle": pi / 2,
        "delta": 2,
        "exp_begin": 2 + 1j,
        "exp_center": 2,
    }
)
comp_translate_test.append(
    {
        "begin": 0,
        "center": 10,
        "angle": -pi / 4,
        "delta": 1 + 1j,
        "exp_begin": 1 + 1j,
        "exp_center": 11 + 1j,
    }
)
comp_translate_test.append(
    {
        "begin": -5 + 2j,
        "center": 8 + 3j,
        "angle": pi / 8,
        "delta": 3 + 2j,
        "exp_begin": -2 + 4j,
        "exp_center": 11 + 5j,
    }
)

get_angle_test = list()
get_angle_test.append(
    {
        "begin": 1 + 0j,
        "center": 0.5 + 0.5j,
        "angle": pi / 4,
        "is_deg": True,
        "exp_angle": 45.0,
    }
)
get_angle_test.append(
    {
        "begin": 1 + 0j,
        "center": 0.5 + 0.5j,
        "angle": pi / 4,
        "is_deg": False,
        "exp_angle": pi / 4,
    }
)
get_angle_test.append(
    {"begin": 1 + 0j, "center": 0, "angle": pi / 3, "is_deg": True, "exp_angle": 60.0}
)

split_half_test = list()
split_half_test.append(
    {
        "begin": 1,
        "center": 0,
        "angle": pi,
        "is_begin": True,
        "N_begin": 1,
        "N_center": 0,
        "N_angle": pi / 2,
    }
)
split_half_test.append(
    {
        "begin": 1,
        "center": 0,
        "angle": -pi,
        "is_begin": False,
        "N_begin": -1j,
        "N_center": 0,
        "N_angle": -pi / 2,
    }
)
split_half_test.append(
    {
        "begin": 2,
        "center": 1,
        "angle": pi / 2,
        "is_begin": True,
        "N_begin": 2,
        "N_center": 1,
        "N_angle": pi / 4,
    }
)
split_half_test.append(
    {
        "begin": 2,
        "center": 1,
        "angle": pi / 2,
        "is_begin": False,
        "N_begin": exp(1j * pi / 4) + 1,
        "N_center": 1,
        "N_angle": pi / 4,
    }
)


class Test_Arc2_meth(object):
    """unittest for Arc2 methods"""

    def test_check_Point(self):
        """Check that you can detect a one point arc"""
        arc = Arc2(0, 0, 1)
        with pytest.raises(PointArc2Error):
            arc.check()

    def test_check_Angle(self):
        """Check that you can detect null angle"""
        arc = Arc2(0, 1, 0)
        with pytest.raises(AngleArc2Error):
            arc.check()
        arc = Arc2(0, 1, 2 * pi)
        with pytest.raises(AngleArc2Error):
            arc.check()

    @pytest.mark.parametrize("test_dict", discretize_test)
    def test_dicretize(self, test_dict):
        """Check that you can discretize an arc2"""
        arc = Arc2(test_dict["begin"], test_dict["center"], test_dict["angle"])

        result = arc.discretize(test_dict["nb_point"])

        assert result.size == test_dict["result"].size
        for i in range(0, result.size):
            a = result[i]
            b = test_dict["result"][i]
            assert abs((a - b) / a - 0) < DELTA

    def test_discretize_Point_error(self):
        """Check that dicretize can detect a one point arc2"""
        arc = Arc2(0, 0, 2)
        with pytest.raises(PointArc2Error):
            arc.discretize(5)

    def test_discretize_Angle_error(self):
        """Check that discretize can detect a null angle arc2"""
        arc = Arc2(0, 1, 0)
        with pytest.raises(AngleArc2Error):
            arc.discretize(5)

    def test_discretize_Nb_error(self):
        """Check that discretize can detect a wrong arg"""
        arc = Arc2(0, 1, 1)
        with pytest.raises(NbPointArc2DError):
            arc.discretize(-1)

    def test_discretize_Nb_Type_error(self):
        """Check that discretize can detect a wrong arg"""
        arc = Arc2(0, 1, 1)
        with pytest.raises(NbPointArc2DError):
            arc.discretize("test")

    @pytest.mark.parametrize("test_dict", comp_length_test)
    def test_comp_length(self, test_dict):
        """Check that you the length return by comp_length is correct"""
        arc = Arc2(test_dict["begin"], test_dict["center"], test_dict["angle"])

        a = float(arc.comp_length())
        b = float(test_dict["length"])
        assert abs((a - b) / a - 0) < DELTA

    def test_comp_length_Point_error(self):
        """Check that comp_length can detect a one point arc2"""
        arc = Arc2(0, 0, 2)
        with pytest.raises(PointArc2Error):
            arc.comp_length()

    def test_comp_length_angle_error(self):
        """Check that comp_length can detect a null angle arc2"""
        arc = Arc2(0, 1, 0)
        with pytest.raises(AngleArc2Error):
            arc.comp_length()

    def test_comp_radius(self):
        """Check that the radius is correct"""
        test_obj = Arc2(1, 0, pi / 2)
        result = test_obj.comp_radius()

        assert round(abs(result - 1), 7) == 0

        test_obj = Arc2(2 * exp(1j * 3 * pi / 4), 0, -pi / 2)
        result = test_obj.comp_radius()

        assert round(abs(result - 2), 7) == 0

    def test_get_center(self):
        """Check that the center is returned correctly"""
        test_obj = Arc2(1, 1 + 1j, pi)
        result = test_obj.get_center()
        assert result == 1 + 1j

    def test_get_end(self):
        """Check that the end is correct"""
        test_obj = Arc2(1, 0, pi / 2)
        result = test_obj.get_end()

        assert result == 1 * exp(1j * pi / 2)

        test_obj = Arc2(0, 1, -pi / 2)
        result = test_obj.get_end()

        a = abs(result)
        b = 1.414213

        assert abs((a - b) / a - 0) < DELTA

        a = angle(result)
        b = pi / 4
        assert abs((a - b) / a - 0) < DELTA

        # The end point is to close from 0

        test_obj = Arc2(0, 0.00000000000000000001, -pi / 6)
        result = test_obj.get_end()

        assert result == 0

    @pytest.mark.parametrize("test_dict", comp_mid_test)
    def test_get_middle(self, test_dict):
        """Check that the middle is computed correctly"""
        arc = Arc2(
            begin=test_dict["begin"],
            center=test_dict["center"],
            angle=test_dict["angle"],
        )
        result = arc.get_middle()
        assert abs(abs(result - test_dict["expect"]) - 0) < 1e-3

    def test_get_middle_zero(self):
        """Checking that get_middle() can return 0"""
        arc = Arc2(begin=0.000000001, center=0.000000002, angle=pi)
        result = arc.get_middle()
        assert result == 0

    @pytest.mark.parametrize("test_dict", comp_rotate_test)
    def test_rotate(self, test_dict):
        """Check that you can rotate the arc2"""
        arc = Arc2(
            begin=test_dict["begin"],
            center=test_dict["center"],
            angle=test_dict["angle"],
        )
        expect_angle = arc.angle
        arc.rotate(test_dict["alpha"])

        assert round(abs(abs(test_dict["exp_begin"] - arc.begin) - 0), 7) == 0
        assert round(abs(abs(expect_angle - arc.angle) - 0), 7) == 0
        assert round(abs(abs(test_dict["exp_center"] - arc.center) - 0), 7) == 0

    @pytest.mark.parametrize("test_dict", comp_translate_test)
    def test_translate(self, test_dict):
        """Check that you can translate the arc2"""
        arc = Arc2(
            begin=test_dict["begin"],
            center=test_dict["center"],
            angle=test_dict["angle"],
        )
        expect_angle = arc.angle
        arc.translate(test_dict["delta"])

        assert round(abs(abs(test_dict["exp_begin"] - arc.begin) - 0), 7) == 0
        assert round(abs(abs(expect_angle - arc.angle) - 0), 7) == 0
        assert round(abs(abs(test_dict["exp_center"] - arc.center) - 0), 7) == 0

    @pytest.mark.parametrize("test_dict", get_angle_test)
    def test_get_angle(self, test_dict):
        """Check that the arc2 computed angle is correct"""
        arc = Arc2(
            begin=test_dict["begin"],
            center=test_dict["center"],
            angle=test_dict["angle"],
        )
        result = arc.get_angle(test_dict["is_deg"])
        assert round(abs(result - test_dict["exp_angle"]), 7) == 0

    @pytest.mark.parametrize("test_dict", split_half_test)
    def test_split_half(self, test_dict):
        """Check that the arc2 split is correct"""
        arc = Arc2(
            begin=test_dict["begin"],
            center=test_dict["center"],
            angle=test_dict["angle"],
        )
        arc.split_half(is_begin=test_dict["is_begin"])
        assert round(abs(arc.begin - test_dict["N_begin"]), 7) == 0
        assert round(abs(arc.center - test_dict["N_center"]), 7) == 0
        assert round(abs(arc.angle - test_dict["N_angle"]), 7) == 0

    def test_arc_rotate_error(self):
        """Check that the arc3 rotate raise an error"""
        arc = Arc2(
            begin=1 - 5j,
            center=3 + 2j,
            angle=pi / 2,
        )
        with pytest.raises(AngleRotationArc2Error) as context:
            arc.rotate("error")

    def test_translate_error(self):
        """Check that you can't translate an arc2 when an error occurs"""
        arc = Arc2(
            begin=1 - 5j,
            center=3 + 2j,
            angle=pi / 2,
        )
        with pytest.raises(PointTranslateArc2Error) as context:
            arc.translate("error")

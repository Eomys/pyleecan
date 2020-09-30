# -*- coding: utf-8 -*-
from pyleecan.Classes.Circle import Circle
from pyleecan.Classes.Arc3 import Arc3
from pyleecan.Methods.Geometry.Circle.rotate import AngleRotationCircleError
from pyleecan.Methods.Geometry.Circle.translate import PointTranslateCircleError
from numpy import pi, sqrt, exp, linspace
import pytest

# Dictionary to test comp_length
comp_length_test = list()
comp_length_test.append({"center": 0, "radius": 5, "ref": 0, "expect": 2 * 5 * pi})
comp_length_test.append(
    {"center": 10 + 2j, "radius": 2, "ref": 9, "expect": 2 * 2 * pi}
)
comp_length_test.append({"center": -5, "radius": 10, "ref": -15, "expect": 2 * 10 * pi})

# Dictionary to test rotate
rotate_test = list()
rotate_test.append(
    {"center": 1j, "radius": 1, "ref": 0, "alpha": pi / 2, "exp_center": -1}
)
rotate_test.append(
    {"center": 0, "radius": 2, "ref": 1, "alpha": pi / 2, "exp_center": 0}
)
rotate_test.append(
    {
        "center": -10 - 10j,
        "radius": 10,
        "ref": -6,
        "alpha": pi / 4,
        "exp_center": -sqrt(200) * 1j,
    }
)
rotate_test.append(
    {
        "center": -10 - 10j,
        "radius": 10,
        "ref": -10 - 10j,
        "alpha": -pi / 4,
        "exp_center": -sqrt(200),
    }
)

# Dictionary to test translate
translate_test = list()
translate_test.append(
    {"center": 1j, "radius": 1, "ref": 0, "delta": -6, "exp_center": -6 + 1j}
)
translate_test.append(
    {"center": 0, "radius": 2, "ref": 0, "delta": 5 + 10j, "exp_center": 5 + 10j}
)
translate_test.append(
    {"center": -10 - 10j, "radius": 10, "ref": -10, "delta": 0, "exp_center": -10 - 10j}
)

# Dictionary to test get_lines
lines_test = list()
lines_test.append({"center": 0, "radius": 1, "ref": 0})
lines_test[0]["result"] = [
    Arc3(begin=1, end=-1, is_trigo_direction=True),
    Arc3(begin=-1, end=1, is_trigo_direction=True),
]
lines_test.append({"center": 5 + 5j, "radius": 1, "ref": 4})
lines_test[1]["result"] = [
    Arc3(begin=6 + 5j, end=4 + 5j, is_trigo_direction=True),
    Arc3(begin=4 + 5j, end=6 + 5j, is_trigo_direction=True),
]

# Dictionary to test discretize
disc_test = list()
disc_test.append({"center": 0, "radius": 1, "ref": 0})
disc_test[0]["result"] = exp(1j * linspace(0, 2 * pi, 200, endpoint=False))
disc_test.append({"center": 5 + 5j, "radius": 1, "ref": 4})
disc_test[1]["result"] = exp(1j * linspace(0, 2 * pi, 200, endpoint=False)) + 5 + 5j


@pytest.mark.METHODS
class Test_Circle_meth(object):
    """Unittest for Class Circle"""

    @pytest.mark.parametrize("test_dict", comp_length_test)
    def test_comp_length(self, test_dict):
        """Check that you can compute the circle length"""
        circle = Circle(
            center=test_dict["center"],
            point_ref=test_dict["ref"],
            radius=test_dict["radius"],
        )
        result = circle.comp_length()
        assert round(abs(abs(result - test_dict["expect"]) - 0), 7) == 0

    def test_rotate_fail(self):
        """Check that the rotate method can detect a wrong arg"""
        circle = Circle(point_ref=1j, radius=1)
        with pytest.raises(AngleRotationCircleError):
            circle.rotate("")

    @pytest.mark.parametrize("test_dict", rotate_test)
    def test_rotate(self, test_dict):
        """Check that you can rotate a circle"""
        circle = Circle(
            center=test_dict["center"],
            point_ref=test_dict["ref"],
            radius=test_dict["radius"],
        )
        circle.rotate(test_dict["alpha"])
        assert round(abs(abs(test_dict["radius"] - circle.radius) - 0), 7) == 0
        assert round(abs(abs(test_dict["exp_center"] - circle.center) - 0), 7) == 0

    def test_translate_fail(self):
        """Check that the translate method can detect a wrong arg"""
        circle = Circle(point_ref=1j, radius=1)
        with pytest.raises(PointTranslateCircleError):
            circle.translate("")

    @pytest.mark.parametrize("test_dict", translate_test)
    def test_translate(self, test_dict):
        """Check that you can translate a circle"""
        circle = Circle(
            center=test_dict["center"],
            point_ref=test_dict["ref"],
            radius=test_dict["radius"],
        )
        circle.translate(test_dict["delta"])
        assert round(abs(abs(test_dict["radius"] - circle.radius) - 0), 7) == 0
        assert round(abs(abs(test_dict["exp_center"] - circle.center) - 0), 7) == 0

    @pytest.mark.parametrize("test_dict", lines_test)
    def test_get_lines(self, test_dict):
        """Check that you get the correct lines to draw the circle"""
        circle = Circle(
            center=test_dict["center"],
            point_ref=test_dict["ref"],
            radius=test_dict["radius"],
        )
        lines = circle.get_lines()
        assert lines == test_dict["result"]

    @pytest.mark.parametrize("test_dict", disc_test)
    def test_discretize(self, test_dict):
        """Check that you can discretize the circle"""
        circle = Circle(
            center=test_dict["center"],
            point_ref=test_dict["ref"],
            radius=test_dict["radius"],
        )
        points = circle.discretize()
        assert len(points) == len(test_dict["result"])
        for ii in range(len(points)):
            assert abs(points[ii] - test_dict["result"][ii]) < 1e-6

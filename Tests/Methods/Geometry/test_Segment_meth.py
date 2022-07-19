# -*- coding: utf-8 -*-
from pyleecan.Classes.Segment import Segment

from pyleecan.Methods.Geometry.Segment import (
    PointSegmentError,
    NbPointSegmentDError,
    AngleRotationSegmentError,
    PointTranslateSegmentError,
)
from numpy import pi, array, exp, sqrt
import pytest


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

split_half_test = list()
split_half_test.append(
    {"begin": 0, "end": 10 + 10j, "is_begin": True, "N_begin": 0, "N_end": 5 + 5j}
)
split_half_test.append(
    {"begin": -10, "end": 10, "is_begin": False, "N_begin": 0, "N_end": 10}
)
split_half_test.append(
    {
        "begin": 2 + 2j,
        "end": 1 + 1j,
        "is_begin": True,
        "N_begin": 2 + 2j,
        "N_end": 1.5 + 1.5j,
    }
)
split_half_test.append(
    {"begin": -2j, "end": -6j, "is_begin": False, "N_begin": -4j, "N_end": -6j}
)

is_on_test = list()
is_on_test.append({"begin": -2, "end": 2, "Z": 0, "result": True})
is_on_test.append({"begin": -2, "end": 2, "Z": 1j, "result": False})
is_on_test.append({"begin": -2, "end": 2, "Z": -1j, "result": False})
is_on_test.append({"begin": -2, "end": 2, "Z": -2, "result": True})
is_on_test.append({"begin": -2, "end": 2, "Z": 2, "result": True})
is_on_test.append({"begin": 2j, "end": 2, "Z": 1 + 1j, "result": True})

distance_test = list()
distance_test.append({"begin": -2, "end": 2, "Z": 0, "result": 0})
distance_test.append({"begin": -2, "end": 2, "Z": 1j, "result": 1})
distance_test.append({"begin": -2, "end": 2, "Z": -1j, "result": 1})
distance_test.append({"begin": -2, "end": 2, "Z": -2, "result": 0})
distance_test.append({"begin": -2, "end": 2, "Z": 2, "result": 0})
distance_test.append({"begin": 2j, "end": 2, "Z": 1 + 1j, "result": 0})
distance_test.append({"begin": 2j, "end": 2, "Z": 3 - 1j, "result": sqrt(2)})
distance_test.append({"begin": 1 + 0j, "end": 0 + 1j, "Z": 0 + 192j, "result": 191})


class Test_Segment_meth(object):
    """unittest for Segment methods"""

    def test_check(self):
        """Check that you can detect a one point segment"""
        segment = Segment(0, 0)
        with pytest.raises(PointSegmentError):
            segment.check()

    @pytest.mark.parametrize("test_dict", discretize_test)
    def test_dicretize(self, test_dict):
        """Check that you can discretize a segment"""
        segment = Segment(test_dict["begin"], test_dict["end"])

        result = segment.discretize(test_dict["nb_point"])

        assert result.size == test_dict["result"].size
        for i in range(0, result.size):
            assert abs(result[i] - test_dict["result"][i]) < DELTA

    def test_discretize_Point_error(self):
        """Check that dicretize can detect a one point segment"""
        segment = Segment(0, 0)
        with pytest.raises(PointSegmentError):
            segment.discretize(5)

    def test_discretize_Nb_error(self):
        """Check that you can detect a wrong argument"""
        segment = Segment(0, 10)
        with pytest.raises(NbPointSegmentDError):
            segment.discretize(-1)
        with pytest.raises(NbPointSegmentDError):
            segment.discretize("error ?")

    @pytest.mark.parametrize("test_dict", comp_length_test)
    def test_comp_length(self, test_dict):
        """Check that you the length return by comp_length is correct"""
        segment = Segment(test_dict["begin"], test_dict["end"])

        assert round(abs(segment.comp_length() - test_dict["length"]), 7) == 0

    def test_comp_length_Point_error(self):
        """Check that comp_length can detect a one point segment"""
        segment = Segment(0, 0)
        with pytest.raises(PointSegmentError):
            segment.comp_length()

    def test_get_middle(self):
        """Check that you can compute the middle of the segment"""
        segment = Segment(0, 10)
        result = segment.get_middle()
        expect = 5.0
        assert round(abs(abs(result - expect) - 0), 7) == 0

        segment = Segment(10, 10 * exp(1j * pi / 2))
        result = segment.get_middle()
        expect = 5 + 5j
        assert round(abs(abs(result - expect) - 0), 7) == 0

    def test_rotate(self):
        """Check that you can rotate the segment"""
        segment = Segment(0, 1)
        segment.rotate(pi / 2)
        expect_begin = 0
        expect_end = 1j
        assert round(abs(abs(expect_begin - segment.begin) - 0), 7) == 0
        assert round(abs(abs(expect_end - segment.end) - 0), 7) == 0

        segment = Segment(1 + 1j, 1)
        segment.rotate(-pi / 2)
        expect_begin = 1 - 1j
        expect_end = -1j
        assert round(abs(abs(expect_begin - segment.begin) - 0), 7) == 0
        assert round(abs(abs(expect_end - segment.end) - 0), 7) == 0

        with pytest.raises(AngleRotationSegmentError) as context:
            segment.rotate("error")

    def test_translate(self):
        """Check that you can translate the segment"""
        segment = Segment(0, 3j)
        segment.translate(2)
        expect_begin = 2
        expect_end = 2 + 3j
        assert round(abs(abs(expect_begin - segment.begin) - 0), 7) == 0
        assert round(abs(abs(expect_end - segment.end) - 0), 7) == 0

        segment = Segment(-2 + 1j, 2 + 3j)
        segment.translate(-2 - 3j)
        expect_begin = -4 - 2j
        expect_end = 0
        assert round(abs(abs(expect_begin - segment.begin) - 0), 7) == 0
        assert round(abs(abs(expect_end - segment.end) - 0), 7) == 0

        with pytest.raises(PointTranslateSegmentError) as context:
            segment.translate("error")

    @pytest.mark.parametrize("test_dict", split_half_test)
    def test_split_half(self, test_dict):
        """Check that the segment split is correct"""
        seg = Segment(begin=test_dict["begin"], end=test_dict["end"])
        seg.split_half(is_begin=test_dict["is_begin"])

        assert round(abs(seg.begin - test_dict["N_begin"]), 7) == 0
        assert round(abs(seg.end - test_dict["N_end"]), 7) == 0

    @pytest.mark.parametrize("test_dict", is_on_test)
    def test_is_on(self, test_dict):
        """Check that the segment is_on_line method is correct"""
        seg = Segment(begin=test_dict["begin"], end=test_dict["end"])
        result = seg.is_on_line(Z=test_dict["Z"])

        assert result == test_dict["result"]

    @pytest.mark.parametrize("test_dict", distance_test)
    def test_distance(self, test_dict):
        """Check that the segment comp_distance method is correct"""
        seg = Segment(begin=test_dict["begin"], end=test_dict["end"])
        result = seg.comp_distance(Z=test_dict["Z"])

        assert round(abs(result - test_dict["result"]), 7) == 0


if __name__ == "__main__":
    a = Test_Segment_meth()
    a.test_is_on(is_on_test[2])
    # for test_dict in is_on_test:
    #     a.test_is_on(test_dict)
    print("Done")

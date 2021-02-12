# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.Segment import Segment

from numpy import pi, sqrt, exp


# For AlmostEqual
DELTA = 1e-6

norm_list = list()

# 0) Segment on Ox
norm_list.append(
    {
        "test_obj": Segment(-1, 1),
        "result_0": (0, 1j * 2 / 3),
        "result_1": 1j * 2 / 3,
        "result_2": pi / 2,
    }
)
# 1) Segment diagonal X+,Y+
norm_list.append(
    {
        "test_obj": Segment(1, 1j),
        "result_0": (0.5 + 0.5j, (0.5 - 1 / 3) * (1 + 1j)),
        "result_1": -1 / 3 * (1 + 1j),
        "result_2": -3 * pi / 4,
    }
)
# 2) Reversed 1
norm_list.append(
    {
        "test_obj": Segment(1j, 1),
        "result_0": (0.5 + 0.5j, (0.5 + 1 / 3) * (1 + 1j)),
        "result_1": +1 / 3 * (1 + 1j),
        "result_2": pi / 4,
    }
)
# 3) Segment diagonal X-Y+
norm_list.append(
    {
        "test_obj": Segment(-1, 1j),
        "result_0": (-0.5 + 0.5j, (0.5 + 1 / 3) * (-1 + 1j)),
        "result_1": 1 / 3 * (-1 + 1j),
        "result_2": 3 * pi / 4,
    }
)
# 4) Reverse 3
norm_list.append(
    {
        "test_obj": Segment(1j, -1),
        "result_0": (-0.5 + 0.5j, (0.5 - 1 / 3) * (-1 + 1j)),
        "result_1": -1 / 3 * (-1 + 1j),
        "result_2": -pi / 4,
    }
)
# 5) Segment diagonal X- Y-
norm_list.append(
    {
        "test_obj": Segment(-1, -1j),
        "result_0": (-0.5 - 0.5j, (0.5 - 1 / 3) * (-1 - 1j)),
        "result_1": 1 / 3 * (1 + 1j),
        "result_2": pi / 4,
    }
)
# 6) Reversed 5
norm_list.append(
    {
        "test_obj": Segment(-1j, -1),
        "result_0": (-0.5 - 0.5j, (0.5 + 1 / 3) * (-1 - 1j)),
        "result_1": -1 / 3 * (1 + 1j),
        "result_2": -3 * pi / 4,
    }
)
# 7) Segment diagonal X+ Y-
norm_list.append(
    {
        "test_obj": Segment(-1j, 1),
        "result_0": (0.5 - 0.5j, (0.5 - 1 / 3) * (1 - 1j)),
        "result_1": -1 / 3 * (1 - 1j),
        "result_2": 3 * pi / 4,
    }
)
# 8) Reversed 7
norm_list.append(
    {
        "test_obj": Segment(1, -1j),
        "result_0": (0.5 - 0.5j, (0.5 + 1 / 3) * (1 - 1j)),
        "result_1": 1 / 3 * (1 - 1j),
        "result_2": -pi / 4,
    }
)


@pytest.mark.METHODS
class Test_Line_normal(object):
    """unittest for Line comp_normal method"""

    @pytest.mark.parametrize("test_dict", norm_list)
    def test_comp_normal(self, test_dict):
        """Check that the normal is computed correctly"""
        test_obj = test_dict["test_obj"]

        if "result_2" in test_dict:
            result = test_obj.comp_normal(return_type=2)
            assert isinstance(result, float)
            assert result == pytest.approx(test_dict["result_2"])
        if "result_1" in test_dict:
            result = test_obj.comp_normal(return_type=1)
            assert isinstance(result, complex)
            assert abs(result - test_dict["result_1"]) < DELTA
        if "result_0" in test_dict:
            result = test_obj.comp_normal(return_type=0)
            assert isinstance(result, tuple)
            assert len(result) == 2
            assert abs(result[0] - test_dict["result_0"][0]) < DELTA
            assert abs(result[1] - test_dict["result_0"][1]) < DELTA

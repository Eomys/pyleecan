# -*- coding: utf-8 -*-

from os.path import join
from numpy import pi, exp

import pytest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM57 import HoleM57
from pyleecan.Classes.Hole import Hole

DELTA = 1e-6
HoleM57_test = list()

test_obj = LamHole(is_internal=True, Rint=0.021, Rext=0.075, is_stator=False, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM57(
        Zh=8,
        W0=pi * 0.8,
        W1=10e-3,
        W2=0e-3,
        W3=5e-3,
        W4=10e-3,
        H1=3e-3,
        H2=5e-3,
    )
)
HoleM57_test.append(
    {
        "test_obj": test_obj,
    }
)


class Test_HoleM57_meth(object):
    """Test machine plot hole 57"""

    @pytest.mark.parametrize("test_dict", HoleM57_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.hole[0]._comp_point_coordinate()

        # Check width
        assert abs(point_dict["Z3"] - point_dict["Z2"]) == pytest.approx(
            test_obj.hole[0].W4
        )
        assert abs(point_dict["Z6"] - point_dict["Z7"]) == pytest.approx(
            test_obj.hole[0].W4
        )
        assert abs(point_dict["Z2"] - point_dict["Z9"]) == pytest.approx(
            test_obj.hole[0].W2
        )
        assert abs(point_dict["Z8"] - point_dict["Z7"]) == pytest.approx(
            test_obj.hole[0].W2
        )
        assert abs(
            point_dict["Z1"]
            - point_dict["Z1s"] * exp(-1j * 2 * pi / test_obj.hole[0].Zh)
        ) == pytest.approx(test_obj.hole[0].W3)
        assert abs(
            point_dict["Z8"]
            - point_dict["Z8s"] * exp(-1j * 2 * pi / test_obj.hole[0].Zh)
        ) == pytest.approx(test_obj.hole[0].W3)
        assert abs(point_dict["Z4"] - point_dict["Z4s"]) == pytest.approx(
            test_obj.hole[0].W1
        )
        assert abs(point_dict["Z5"] - point_dict["Z5s"]) == pytest.approx(
            test_obj.hole[0].W1
        )

        # Check height
        assert abs(point_dict["Z3"] - point_dict["Z6"]) == pytest.approx(
            test_obj.hole[0].H2
        )
        assert abs(point_dict["Z2"] - point_dict["Z7"]) == pytest.approx(
            test_obj.hole[0].H2
        )
        assert abs(point_dict["Z8"] - point_dict["Z9"]) == pytest.approx(
            test_obj.hole[0].H2
        )

    @pytest.mark.parametrize("test_dict", HoleM57_test)
    def test_comp_radius(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        Rmin, Rmax = test_obj.hole[0].comp_radius()

        # Check that the analytical method returns the same result as the numerical one
        Rmin_a, Rmax_a = Hole.comp_radius(test_obj.hole[0])

        a, b = Rmin, Rmin_a
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg
        a, b = Rmax, Rmax_a
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg


if __name__ == "__main__":
    a = Test_HoleM57_meth()
    for test_dict in HoleM57_test:
        a.test_comp_radius(test_dict)
    print("Done")

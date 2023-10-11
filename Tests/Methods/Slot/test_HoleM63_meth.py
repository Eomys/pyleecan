# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Hole import Hole
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM63 import HoleM63

from pyleecan.Classes.Magnet import Magnet
from numpy import exp, arcsin, ndarray, pi
import matplotlib.pyplot as plt

# For AlmostEqual
DELTA = 1e-4


holeM63_test = list()

test_obj = LamHole(Rint=0.03, Rext=0.12, is_stator=False, is_internal=True)
test_obj.hole = list()
test_obj.hole.append(HoleM63(Zh=4, W0=80e-3, H0=20e-3, H1=30e-3, top_flat=False))
holeM63_test.append(
    {
        "test_obj": test_obj,
        "carac": "all magnet",
        "Rmin_exp": 0.060622577482985496,
        "Rmax_exp": 0.09,
        "S_exp": 0.0021055711763162087,
        "hasmagnet_exp": False,
    }
)
# top_flat = True
test_obj = LamHole(is_internal=True, Rint=0.03, Rext=0.12, is_stator=False)
test_obj.hole = list()
test_obj.hole.append(HoleM63(Zh=4, W0=80e-3, H0=20e-3, H1=30e-3, top_flat=True))
holeM63_test.append(
    {
        "test_obj": test_obj,
        "carac": "all magnet",
        "Rmin_exp": 0.07,
        "Rmax_exp": 0.09848857801796104,
        "S_exp": 0.0015999999999999977,
        "hasmagnet_exp": False,
    }
)


class Test_HoleM63_meth(object):
    """pytest for holeB63 methods"""

    @pytest.mark.parametrize("test_dict", holeM63_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]

        point_dict = test_obj.hole[0]._comp_point_coordinate()
        Rbo = test_obj.hole[0].get_Rbo()

        # H0
        assert abs(point_dict["Z2"] - point_dict["Z1"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        assert abs(point_dict["Z3"] - point_dict["Z4"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        # W0
        assert abs(point_dict["Z3"] - point_dict["Z2"]) == pytest.approx(
            test_obj.hole[0].W0
        )
        assert abs(point_dict["Z4"] - point_dict["Z1"]) == pytest.approx(
            test_obj.hole[0].W0
        )
        # H1
        if not test_obj.hole[0].top_flat:
            assert abs(point_dict["Z3"]) == pytest.approx(Rbo - test_obj.hole[0].H1)
            assert abs(point_dict["Z2"]) == pytest.approx(Rbo - test_obj.hole[0].H1)
        else:
            assert abs(point_dict["Z3"].real) == pytest.approx(
                Rbo - test_obj.hole[0].H1
            )
            assert abs(point_dict["Z2"].real) == pytest.approx(
                Rbo - test_obj.hole[0].H1
            )

    @pytest.mark.parametrize("test_dict", holeM63_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"].copy()
        result = test_obj.hole[0].comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = f"Return {a} expected {b}"
        # assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Hole.comp_surface(test_obj.hole[0])
        msg = f"Return {a} expected {b}"
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", holeM63_test)
    def test_comp_radius(self, test_dict):
        """Check that the computation of the radius is correct"""
        test_obj = test_dict["test_obj"]
        Rmin, Rmax = test_obj.hole[0].comp_radius()

        Rmax_a = test_dict["Rmax_exp"]
        Rmin_a = test_dict["Rmin_exp"]
        a, b = Rmin, Rmin_a
        msg = f"For Rmin: Return {a} expected {b}"
        assert abs((a - b) / a - 0) < DELTA, msg
        a, b = Rmax, Rmax_a
        msg = f"For Rmax: Return {a} expected {b}"
        assert abs((a - b) / a - 0) < DELTA, msg

        Rmin_a, Rmax_a = Hole.comp_radius(test_obj.hole[0])
        a, b = Rmin, Rmin_a
        msg = f"For Rmin: Return {a} expected {b}"
        assert abs((a - b) / a - 0) < DELTA, msg

        a, b = Rmax, Rmax_a
        msg = f"For Rmax: Return {a} expected {b}"
        assert abs((a - b) / a - 0) < DELTA, msg


if __name__ == "__main__":
    a = Test_HoleM63_meth()
    for test_dict in holeM63_test:
        carac = test_dict["carac"]
        print("Test - %s - schematics" % carac)
        a.test_schematics(test_dict)
        print("Done - %s - schematics" % carac)
        print("Test - %s - comp_radius" % carac)
        a.test_comp_radius(test_dict)
        print("Done - %s - comp_radius" % carac)
        print("Test - %s - comp_surface" % carac)
        a.test_comp_surface(test_dict)
        print("Done - %s - comp_surface" % carac)
        print("Test - %s - comp_surface_mag" % carac)

    print("Done")

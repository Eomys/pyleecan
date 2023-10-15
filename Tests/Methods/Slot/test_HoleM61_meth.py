# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Hole import Hole
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM61 import HoleM61

from pyleecan.Classes.Magnet import Magnet
from numpy import exp, arcsin, ndarray, pi
import matplotlib.pyplot as plt

# For AlmostEqual
DELTA = 1e-4


HoleM61_test = list()

# No magnet case
test_obj = LamHole(Rint=0.03, Rext=0.12, is_stator=False, is_internal=True, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM61(
        Zh=4,
        W0=2e-2,
        W1=2e-2,
        W2=20e-3,
        W3=12e-3,
        H0=61e-3,
        H1=10e-3,
        H2=10e-3,
        magnet_0=None,
        magnet_1=None,
        magnet_2=None,
        magnet_3=None,
    )
)
HoleM61_test.append(
    {
        "test_obj": test_obj,
        "carac": "no magnet",
        "Rmin_exp": 0.05984145720150872,
        "Rmax_exp": 0.11,
        "S_exp": 0.001365343502693061,
        "SM_exp": 0,
        "hasmagnet_exp": False,
    }
)

# Tests with All magnets
test_obj = LamHole(is_internal=True, Rint=0.03, Rext=0.12, is_stator=False, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM61(
        Zh=4,
        W0=2e-2,
        W1=2e-2,
        W2=20e-3,
        W3=12e-3,
        H0=61e-3,
        H1=10e-3,
        H2=10e-3,
    )
)

HoleM61_test.append(
    {
        "test_obj": test_obj,
        "carac": "all magnets",
        "Rmin_exp": 0.05984145720150872,
        "Rmax_exp": 0.11,
        "S_exp": 0.0013668826437211773,
        "SM_exp": 0.0008,
        "hasmagnet_exp": True,
    }
)

# Tests with magnet_0 only
test_obj = LamHole(is_internal=True, Rint=0.03, Rext=0.12, is_stator=False, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM61(
        Zh=4,
        W0=2e-2,
        W1=20e-3,
        W2=15e-3,
        W3=12e-3,
        H0=61e-3,
        H1=10e-3,
        H2=10e-3,
        magnet_1=None,
        magnet_2=None,
        magnet_3=None,
    )
)

HoleM61_test.append(
    {
        "test_obj": test_obj,
        "carac": "magnet_0",
        "Rmin_exp": 0.05984145720150872,
        "Rmax_exp": 0.11,
        "S_exp": 0.0013668826437211769,
        "SM_exp": 0.00015,
        "hasmagnet_exp": True,
    }
)

# Tests with magnet_1 only
test_obj = LamHole(is_internal=True, Rint=0.03, Rext=0.12, is_stator=False, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM61(
        Zh=4,
        W0=2e-2,
        W1=2e-2,
        W2=20e-3,
        W3=12e-3,
        H0=61e-3,
        H1=10e-3,
        H2=10e-3,
        magnet_0=None,
        magnet_2=None,
        magnet_3=None,
    )
)

HoleM61_test.append(
    {
        "test_obj": test_obj,
        "carac": "magnet_1",
        "Rmin_exp": 0.05984145720150872,
        "Rmax_exp": 0.11,
        "S_exp": 0.0013653435026930684,
        "SM_exp": 0.0002,
        "hasmagnet_exp": True,
    }
)

# Tests with magnet_2 only
test_obj = LamHole(is_internal=True, Rint=0.03, Rext=0.12, is_stator=False, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM61(
        Zh=4,
        W0=2e-2,
        W1=2e-2,
        W2=20e-3,
        W3=12e-3,
        H0=61e-3,
        H1=10e-3,
        H2=10e-3,
        magnet_0=None,
        magnet_1=None,
        magnet_3=None,
    )
)

HoleM61_test.append(
    {
        "test_obj": test_obj,
        "carac": "magnet_2",
        "Rmin_exp": 0.05984145720150872,
        "Rmax_exp": 0.11,
        "S_exp": 0.001365343502693059,
        "SM_exp": 0.0002,
        "hasmagnet_exp": True,
    }
)


# Tests with magnet_3 only
test_obj = LamHole(is_internal=True, Rint=0.03, Rext=0.12, is_stator=False, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM61(
        Zh=4,
        W0=2e-2,
        W1=2e-2,
        W2=20e-3,
        W3=12e-3,
        H0=61e-3,
        H1=10e-3,
        H2=10e-3,
        magnet_0=None,
        magnet_1=None,
        magnet_2=None,
    )
)

HoleM61_test.append(
    {
        "test_obj": test_obj,
        "carac": "magnet_3",
        "Rmin_exp": 0.05984145720150872,
        "Rmax_exp": 0.11,
        "S_exp": 0.001365343502693063,
        "SM_exp": 0.0002,
        "hasmagnet_exp": True,
    }
)

# test Zh = 6
test_obj = LamHole(Rint=0.03, Rext=0.12, is_stator=False, is_internal=True, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM61(
        Zh=6,
        W0=10e-3,
        W1=10e-3,
        W2=10e-3,
        W3=12e-3,
        H0=61e-3,
        H1=10e-3,
        H2=10e-3,
    )
)
HoleM61_test.append(
    {
        "test_obj": test_obj,
        "carac": "all magnet",
        "Rmin_exp": 0.05921148537234985,
        "Rmax_exp": 0.11,
        "S_exp": 0.0012221775834963798,
        "SM_exp": 0.0004,
        "hasmagnet_exp": True,
    }
)


class Test_HoleM61_meth(object):
    """pytest for HoleM61 methods"""

    @pytest.mark.parametrize("test_dict", HoleM61_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]

        point_dict = test_obj.hole[0]._comp_point_coordinate()
        Rbo = test_obj.hole[0].get_Rbo()

        # Check height
        assert abs(point_dict["Z2"] - point_dict["Z1"]) == pytest.approx(
            test_obj.hole[0].H1
        )
        assert abs(point_dict["ZM2"] - point_dict["ZM1"]) == pytest.approx(
            test_obj.hole[0].H1
        )
        assert abs(point_dict["ZM3"] - point_dict["ZM4"]) == pytest.approx(
            test_obj.hole[0].H1
        )
        assert abs(point_dict["ZM5"] - point_dict["ZM8"]) == pytest.approx(
            test_obj.hole[0].H1
        )
        assert abs(point_dict["ZM6"] - point_dict["ZM7"]) == pytest.approx(
            test_obj.hole[0].H1
        )
        assert abs(point_dict["Z8"] - point_dict["Z7"]) == pytest.approx(
            test_obj.hole[0].H1
        )
        assert abs(point_dict["ZM10"] - point_dict["ZM9"]) == pytest.approx(
            test_obj.hole[0].H1
        )
        assert abs(point_dict["ZM11"] - point_dict["ZM12"]) == pytest.approx(
            test_obj.hole[0].H1
        )
        assert abs(point_dict["ZM13"] - point_dict["ZM16"]) == pytest.approx(
            test_obj.hole[0].H1
        )
        assert abs(point_dict["ZM14"] - point_dict["ZM15"]) == pytest.approx(
            test_obj.hole[0].H1
        )

        # Check width
        assert abs(point_dict["Z8"] - point_dict["Z2"]) == pytest.approx(
            test_obj.hole[0].W0
        )
        assert abs(point_dict["Z1"] - point_dict["Z7"]) == pytest.approx(
            test_obj.hole[0].W0
        )
        assert abs(point_dict["ZM2"] - point_dict["ZM10"]) == pytest.approx(
            test_obj.hole[0].W0
        )
        assert abs(point_dict["ZM1"] - point_dict["ZM9"]) == pytest.approx(
            test_obj.hole[0].W0
        )

        # Magnets dimensions w1
        assert abs(point_dict["ZM3"] - point_dict["ZM2"]) == pytest.approx(
            test_obj.hole[0].W1
        )
        assert abs(point_dict["ZM4"] - point_dict["ZM1"]) == pytest.approx(
            test_obj.hole[0].W1
        )
        assert abs(point_dict["ZM11"] - point_dict["ZM10"]) == pytest.approx(
            test_obj.hole[0].W1
        )
        assert abs(point_dict["ZM12"] - point_dict["ZM9"]) == pytest.approx(
            test_obj.hole[0].W1
        )

        # Magnets dimensions w2
        assert abs(point_dict["ZM6"] - point_dict["ZM5"]) == pytest.approx(
            test_obj.hole[0].W2
        )
        assert abs(point_dict["ZM7"] - point_dict["ZM8"]) == pytest.approx(
            test_obj.hole[0].W2
        )
        assert abs(point_dict["ZM13"] - point_dict["ZM14"]) == pytest.approx(
            test_obj.hole[0].W2
        )
        assert abs(point_dict["ZM16"] - point_dict["ZM15"]) == pytest.approx(
            test_obj.hole[0].W2
        )

        # Check W3
        sp = 2 * pi / test_obj.hole[0].Zh

        assert abs(
            point_dict["Z6"] - point_dict["Z12"] * exp(1j * sp)
        ) == pytest.approx(test_obj.hole[0].W3)
        assert abs(
            point_dict["Z5"] - point_dict["Z11"] * exp(1j * sp)
        ) == pytest.approx(test_obj.hole[0].W3)

        # Check H0
        assert abs(Rbo - point_dict["Z1"].real) == pytest.approx(test_obj.hole[0].H0)
        assert abs(Rbo - point_dict["Z6"].real) == pytest.approx(test_obj.hole[0].H0)
        assert abs(Rbo - point_dict["Z7"].real) == pytest.approx(test_obj.hole[0].H0)
        assert abs(Rbo - point_dict["Z12"].real) == pytest.approx(test_obj.hole[0].H0)
        assert abs(Rbo - point_dict["ZM4"].real) == pytest.approx(test_obj.hole[0].H0)
        assert abs(Rbo - point_dict["ZM1"].real) == pytest.approx(test_obj.hole[0].H0)
        assert abs(Rbo - point_dict["ZM9"].real) == pytest.approx(test_obj.hole[0].H0)
        assert abs(Rbo - point_dict["ZM12"].real) == pytest.approx(test_obj.hole[0].H0)

        # magnet height
        assert abs(point_dict["Z4"]) == pytest.approx(Rbo - test_obj.hole[0].H2)
        assert abs(point_dict["Z5"]) == pytest.approx(Rbo - test_obj.hole[0].H2)
        assert abs(point_dict["Z10"]) == pytest.approx(Rbo - test_obj.hole[0].H2)
        assert abs(point_dict["Z11"]) == pytest.approx(Rbo - test_obj.hole[0].H2)

    @pytest.mark.parametrize("test_dict", HoleM61_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = Hole.comp_surface(test_obj.hole[0])

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM61_test)
    def test_comp_surface_mag(self, test_dict):
        """Check that the computation of the magnet surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_surface_magnets()

        a = result
        b = test_dict["SM_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        if b == 0:
            assert a == b, msg
        else:
            assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM61_test)
    def test_comp_radius(self, test_dict):
        """Check that the computation of the radius is correct"""
        test_obj = test_dict["test_obj"]
        Rmin, Rmax = test_obj.hole[0].comp_radius()

        Rmax_a = test_dict["Rmax_exp"]
        Rmin_a = test_dict["Rmin_exp"]
        a, b = Rmin, Rmin_a
        msg = "For Rmin: Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg
        a, b = Rmax, Rmax_a
        msg = "For Rmax: Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        Rmin_a, Rmax_a = Hole.comp_radius(test_obj.hole[0])
        a, b = Rmin, Rmin_a
        msg = "For Rmin: Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg
        a, b = Rmax, Rmax_a
        msg = "For Rmax: Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_comp_surface_magnet_id(self):
        """Check that the computation of the magnet surface is correct"""
        test_obj = LamHole(
            Rint=45e-3 / 2, Rext=81.5e-3, is_stator=False, is_internal=True, L1=0.9
        )
        test_obj.hole = list()
        test_obj.hole.append(
            HoleM61(
                Zh=4,
                W0=2e-2,
                W1=20e-3,
                W2=40e-3,
                W3=12e-3,
                H0=61e-3,
                H1=10e-3,
                H2=10e-3,
            )
        )
        result = test_obj.hole[0].comp_surface_magnet_id(0)
        assert result == 0.0004
        result = test_obj.hole[0].comp_surface_magnet_id(1)
        assert result == 0.0002
        result = test_obj.hole[0].comp_surface_magnet_id(2)
        assert result == 0.0002
        result = test_obj.hole[0].comp_surface_magnet_id(3)
        assert result == 0.0004

    @pytest.mark.parametrize("test_dict", HoleM61_test)
    def test_has_magnet(self, test_dict):
        """Check that the return of has_magnet if correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].has_magnet()
        a = result
        b = test_dict["hasmagnet_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == b, msg


if __name__ == "__main__":
    a = Test_HoleM61_meth()
    for test_dict in HoleM61_test:
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
        a.test_comp_surface_mag(test_dict)
        print("Done - %s - comp_surface_mag" % carac)
        print("Test - %s - has_magnet" % carac)
        a.test_has_magnet(test_dict)
        print("Done - %s - has_magnet" % carac)
    print("Done")

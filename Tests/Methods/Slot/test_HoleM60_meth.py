# -*- coding: utf-8 -*-

from numpy import pi, angle
import pytest
from pyleecan.Classes.Hole import Hole
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM60 import HoleM60
from pyleecan.Functions.Geometry.inter_line_line import inter_line_line

HoleM60_test = list()
# Tests without magnet
test_obj = LamHole(is_internal=True, Rint=0.021, Rext=0.75, is_stator=False, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM60(
        Zh=4,
        W0=pi * 0.2,
        W1=1e-3,
        W2=15e-2,
        W3=5e-3,
        H0=3e-3,
        H1=5e-3,
        magnet_0=None,
        magnet_1=None,
    )
)

HoleM60_test.append(
    {
        "test_obj": test_obj,
        "carac": "no magnet",
        "Rmin_exp": 0.7067731287283922,
        "Rmax_exp": 0.7458565593569103,
        "S_exp": 0.0008961365913508546,
        "SM_exp": 0,
        "hasmagnet_exp": False,
    }
)

# Tests with both magnets
test_obj = LamHole(is_internal=True, Rint=0.021, Rext=0.75, is_stator=False, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM60(
        Zh=4,
        W0=pi * 0.4,
        W1=10e-3,
        W2=10e-2,
        W3=1e-3,
        H0=3e-3,
        H1=2e-3,
    )
)

HoleM60_test.append(
    {
        "test_obj": test_obj,
        "carac": "both magnets",
        "Rmin_exp": 0.7067731287283922,
        "Rmax_exp": 0.7458565593569103,
        "S_exp": 0.0005961365913508596,
        "SM_exp": 6e-5,
        "hasmagnet_exp": True,
    }
)

# Tests with magnet_0 only
test_obj = LamHole(is_internal=True, Rint=0.021, Rext=0.75, is_stator=False, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM60(
        Zh=4,
        W0=pi * 0.6,
        W1=10e-3,
        W2=10e-2,
        W3=5e-3,
        H0=6e-3,
        H1=5e-3,
        magnet_1=None,
    )
)

HoleM60_test.append(
    {
        "test_obj": test_obj,
        "carac": "magnet_0",
        "Rmin_exp": 0.7067731287283922,
        "Rmax_exp": 0.7458565593569103,
        "S_exp": 0.0011845463654034398,
        "SM_exp": 6e-05,
        "hasmagnet_exp": True,
    }
)

# Tests with magnet_1 only
test_obj = LamHole(is_internal=True, Rint=0.021, Rext=0.75, is_stator=False, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM60(
        Zh=4,
        W0=pi * 0.8,
        W1=10e-3,
        W2=10e-2,
        W3=5e-3,
        H0=3e-3,
        H1=5e-3,
        magnet_0=None,
    )
)

HoleM60_test.append(
    {
        "test_obj": test_obj,
        "carac": "magnet_1",
        "Rmin_exp": 0.7067731287283922,
        "Rmax_exp": 0.7458565593569103,
        "S_exp": 0.0005961365913508596,
        "SM_exp": 3e-5,
        "hasmagnet_exp": True,
    }
)

# For AlmostEqual
DELTA = 1e-4


class Test_HoleM60_meth(object):
    """Test machine plot hole 60"""

    @pytest.mark.parametrize("test_dict", HoleM60_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.hole[0]._comp_point_coordinate()
        # test_obj.plot()
        # test_obj.hole[0].plot()
        # plt.show()

        # Check width
        assert abs(point_dict["Z2"] - point_dict["Z1"]) == pytest.approx(
            test_obj.hole[0].W2 - test_obj.hole[0].H0
        )
        assert abs(point_dict["Z1s"] - point_dict["Z2s"]) == pytest.approx(
            test_obj.hole[0].W2 - test_obj.hole[0].H0
        )
        assert abs(point_dict["Z5"] - point_dict["Z4"]) == pytest.approx(
            test_obj.hole[0].W2 - test_obj.hole[0].H0
        )
        assert abs(point_dict["Z5s"] - point_dict["Z4s"]) == pytest.approx(
            test_obj.hole[0].W2 - test_obj.hole[0].H0
        )
        assert point_dict["Z1"].imag == pytest.approx(test_obj.hole[0].W3 / 2)
        assert abs(point_dict["Z1s"] - point_dict["Z1"]) == pytest.approx(
            test_obj.hole[0].W3
        )
        assert abs(point_dict["Z3"] - point_dict["Z6"]) == pytest.approx(
            test_obj.hole[0].W2
        )
        assert abs(point_dict["Z3s"] - point_dict["Z6s"]) == pytest.approx(
            test_obj.hole[0].W2
        )

        # Check height
        assert abs(point_dict["Z4"] - point_dict["Z2"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        assert abs(point_dict["Z4s"] - point_dict["Z2s"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        assert abs(point_dict["Z5"] - point_dict["Z1"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        assert abs(point_dict["Z5s"] - point_dict["Z1s"]) == pytest.approx(
            test_obj.hole[0].H0
        )

        assert abs(point_dict["Z3"]) == pytest.approx(
            test_obj.hole[0].get_Rbo() - test_obj.hole[0].H1
        )

        # Compute P
        Z = inter_line_line(
            point_dict["Z3"], point_dict["Z6"], point_dict["Z3s"], point_dict["Z6s"]
        )[0]
        assert abs(point_dict["Z"]) == pytest.approx(abs(Z))

        assert angle(point_dict["Z6"] - Z) == pytest.approx(test_obj.hole[0].W0 / 2)
        assert angle(point_dict["Z3"] - Z) == pytest.approx(test_obj.hole[0].W0 / 2)
        assert angle(point_dict["Z6s"] - Z) == pytest.approx(-test_obj.hole[0].W0 / 2)
        assert angle(point_dict["Z3s"] - Z) == pytest.approx(-test_obj.hole[0].W0 / 2)

        # Magnets dimensions
        assert abs(point_dict["ZM1"] - point_dict["ZM2"]) == pytest.approx(
            test_obj.hole[0].W1
        )
        assert abs(point_dict["ZM3"] - point_dict["ZM4"]) == pytest.approx(
            test_obj.hole[0].W1
        )
        assert abs(point_dict["ZM1s"] - point_dict["ZM2s"]) == pytest.approx(
            test_obj.hole[0].W1
        )
        assert abs(point_dict["ZM3s"] - point_dict["ZM4s"]) == pytest.approx(
            test_obj.hole[0].W1
        )

        assert abs(point_dict["ZM1"] - point_dict["ZM4"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        assert abs(point_dict["ZM3"] - point_dict["ZM2"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        assert abs(point_dict["ZM1s"] - point_dict["ZM4s"]) == pytest.approx(
            test_obj.hole[0].H0
        )
        assert abs(point_dict["ZM3s"] - point_dict["ZM2s"]) == pytest.approx(
            test_obj.hole[0].H0
        )

    @pytest.mark.parametrize("test_dict", HoleM60_test)
    def test_comp_radius(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        Rmin, Rmax = test_obj.hole[0].comp_radius()

        # Check that the analytical method returns the same result as the numerical one
        Rmin_a, Rmax_a = Hole.comp_radius(test_obj.hole[0])

        a, b = Rmin, Rmin_a
        msg = "For Rmin: Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg
        a, b = Rmax, Rmax_a
        msg = "For Rmax: Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM60_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

        # Check that the analytical method returns the same result as the numerical one
        b = Hole.comp_surface(test_obj.hole[0])
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == pytest.approx(b, rel=DELTA), msg

    @pytest.mark.parametrize("test_dict", HoleM60_test)
    def test_comp_surface_mag(self, test_dict):
        """Check that the computation of the magnet surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_surface_magnets()
        a = result
        b = test_dict["SM_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        if a != 0:
            assert abs((a - b) / a - 0) < DELTA, msg
        else:
            assert abs((a - b) - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM60_test)
    def test_has_magnet(self, test_dict):
        """Check that the return of has_magnet if correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].has_magnet()
        a = result
        b = test_dict["hasmagnet_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert a == b, msg


if __name__ == "__main__":
    a = Test_HoleM60_meth()
    for test_dict in HoleM60_test:
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

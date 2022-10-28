# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM52R import HoleM52R
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Methods.Slot.HoleM52R import (
    S52R_NoneError,
    S52R_R0CheckError,
    S52R_widthCheckError,
)

from numpy import exp, arcsin, ndarray, pi, angle

# For AlmostEqual
DELTA = 1e-6

HoleM52R_test = list()

test_obj = LamHole(is_internal=True, is_stator=False, hole=list(), Rext=0.1)
test_obj.hole = list()
test_obj.hole.append(HoleM52R(Zh=8, W0=30e-3, W1=1e-3, H0=12e-3, H1=18e-3, H2=2e-3))
HoleM52R_test.append(
    {
        "test_obj": test_obj,
        "S_exp": 572e-6,
        "SM_exp": 540e-6,
        "Rmin": 68.53323061e-3,
        "Rmax": 88e-3,
        "alpha": 0.365670274,
    }
)

HoleM52R_test_stator = list()

test_obj = LamHole(is_internal=True, is_stator=True, hole=list(), Rext=0.1)
test_obj.hole = list()
test_obj.hole.append(HoleM52R(Zh=8, W0=30e-3, W1=1e-3, H0=12e-3, H1=18e-3, H2=2e-3))
HoleM52R_test_stator.append(
    {
        "test_obj": test_obj,
        "S_exp": 572e-6,
        "SM_exp": 540e-6,
        "Rmin": 68.53323061e-3,
        "Rmax": 88e-3,
        "alpha": 0.365670274,
    }
)

HoleM52R_test_radius = list()

test_obj = LamHole(is_internal=True, is_stator=False, hole=list(), Rext=0.1)
test_obj.hole = list()
test_obj.hole.append(
    HoleM52R(Zh=8, W0=30e-3, W1=1e-3, H0=12e-3, H1=18e-3, H2=2e-3, R0=0.5e-3)
)
HoleM52R_test_radius.append(
    {
        "test_obj": test_obj,
        "S_exp": 572e-6 - 2 * (1 - pi * 0.5 ** 2) * 1e-6 / 4,
        "SM_exp": 540e-6,
        "Rmin": 68.53323061e-3,
        "Rmax": 88e-3,
        "alpha": 0.365670274,
    }
)


class Test_Hole52_meth(object):
    """pytest for holeB52 methods"""

    @pytest.mark.parametrize("test_dict", HoleM52R_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        hole = test_obj.hole[0]
        point_dict = hole._comp_point_coordinate()
        Z1 = point_dict["Z1"]
        Z2 = point_dict["Z2"]
        Z3 = point_dict["Z3"]
        Z4 = point_dict["Z4"]
        Z6 = point_dict["Z6"]
        Z7 = point_dict["Z7"]
        Z8 = point_dict["Z8"]
        Z9 = point_dict["Z9"]
        Z10 = point_dict["Z10"]
        Z11 = point_dict["Z11"]
        # Check H1
        assert abs(Z4 - Z11) == pytest.approx(hole.H1)
        assert abs(Z6 - Z10) == pytest.approx(hole.H1)
        # Check H2
        assert abs(Z3 - Z4) == pytest.approx(hole.H2)
        assert abs(Z6 - Z7) == pytest.approx(hole.H2)
        # Check W0
        assert abs(Z4 - Z6) == pytest.approx(hole.W0)
        assert abs(Z3 - Z7) == pytest.approx(hole.W0)
        assert abs(Z11 - Z10) == pytest.approx(hole.W0)
        # Check W1
        assert abs(Z2 - Z3) == pytest.approx(hole.W1)
        assert abs(Z7 - Z8) == pytest.approx(hole.W1)
        assert abs(Z11 - Z1) == pytest.approx(hole.W1)
        assert abs(Z10 - Z9) == pytest.approx(hole.W1)
        # Check H0
        assert abs(Z9) == pytest.approx(test_obj.get_Rbo() - hole.H0)
        assert abs(Z1) == pytest.approx(test_obj.get_Rbo() - hole.H0)

        # check alpha
        alpha = hole.comp_alpha()
        assert angle(Z1) - angle(Z9) == pytest.approx(alpha)

    @pytest.mark.parametrize("test_dict", HoleM52R_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM52R_test_radius)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM52R_test)
    def test_comp_surface_mag(self, test_dict):
        """Check that the computation of the magnet surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_surface_magnets()

        a = result
        b = test_dict["SM_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM52R_test)
    def test_comp_alpha(self, test_dict):
        """Check that the computation of the alpha is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_alpha()

        a = result
        b = test_dict["alpha"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM52R_test)
    def test_comp_radius(self, test_dict):
        """Check that the computation of the radius is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_radius()

        a = result[0]
        b = test_dict["Rmin"]
        msg = "For Rmin: Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        a = result[1]
        b = test_dict["Rmax"]
        msg = "For Rmax: Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM52R_test)
    def test_build_geometry_with_magnet(self, test_dict):
        """Check that the surf list is correct with magnet"""
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].build_geometry()
        assert len(result) == 3
        for surf in result:
            assert type(surf) == SurfLine

        assert result[0].label == "Rotor_HoleVoid_R0-T0-S0"
        assert len(result[0].line_list) == 4

        assert result[1].label == "Rotor_HoleMag_R0-T0-S0"
        assert len(result[1].line_list) == 4

        assert result[2].label == "Rotor_HoleVoid_R0-T1-S0"
        assert len(result[2].line_list) == 4

    @pytest.mark.parametrize("test_dict", HoleM52R_test)
    def test_build_geometry_no_magnet(self, test_dict):
        """Check that the surf list is correct without magnet"""
        test_obj = LamHole(init_dict=test_dict["test_obj"].as_dict())
        test_obj.hole[0].magnet_0 = None
        result = test_obj.hole[0].build_geometry()
        assert len(result) == 1
        for surf in result:
            assert type(surf) == SurfLine

        assert result[0].label == "Rotor_HoleVoid_R0-T0-S0"
        assert len(result[0].line_list) == 8

    @pytest.mark.parametrize("test_dict", HoleM52R_test_stator)
    def test_build_geometry_simplified_parallel(self, test_dict):
        """Check that the build geometry method works"""

        # is_simplified to True and magnetization Parallel

        test_obj = test_dict["test_obj"]
        test_obj.hole[0].magnet_0 = Magnet(type_magnetization=1)
        a = test_obj.hole[0].build_geometry(is_simplified=True)

        assert a[1].label == "Stator_HoleMag_R0-T0-S0"
        assert a[1].line_list[0] is not None
        assert a[1].line_list[1] is not None
        with pytest.raises(IndexError) as context:
            a[1].line_list[2]

    def test_check(self):
        """Check that the check function can raise error"""
        test_obj = LamHole(is_internal=True, is_stator=False, hole=list(), Rext=0.1)
        test_obj.hole = [HoleM52R(Zh=8, W0=None, W1=1e-3, H0=12e-3, H1=18e-3, H2=2e-3)]
        with pytest.raises(S52R_NoneError) as context:
            test_obj.hole[0].check()
        test_obj.hole = [HoleM52R(Zh=8, W0=30e-3, W1=None, H0=12e-3, H1=18e-3, H2=2e-3)]
        with pytest.raises(S52R_NoneError) as context:
            test_obj.hole[0].check()
        test_obj.hole = [HoleM52R(Zh=8, W0=30e-3, W1=1e-3, H0=None, H1=18e-3, H2=2e-3)]
        with pytest.raises(S52R_NoneError) as context:
            test_obj.hole[0].check()
        test_obj.hole = [HoleM52R(Zh=8, W0=30e-3, W1=1e-3, H0=12e-3, H1=None, H2=2e-3)]
        with pytest.raises(S52R_NoneError) as context:
            test_obj.hole[0].check()
        test_obj.hole = [HoleM52R(Zh=8, W0=30e-3, W1=1e-3, H0=12e-3, H1=18e-3, H2=None)]
        with pytest.raises(S52R_NoneError) as context:
            test_obj.hole[0].check()
        test_obj.hole = [
            HoleM52R(Zh=8, W0=30e-3, W1=1e-3, H0=12e-3, H1=18e-3, H2=2e-3, R0=2)
        ]
        with pytest.raises(S52R_R0CheckError) as context:
            test_obj.hole[0].check()
        test_obj.hole = [HoleM52R(Zh=8, W0=99e-3, W1=1e-3, H0=12e-3, H1=18e-3, H2=2e-3)]
        with pytest.raises(S52R_widthCheckError) as context:
            test_obj.hole[0].check()


if __name__ == "__main__":
    a = Test_Hole52_meth()
    a.test_schematics(HoleM52R_test[0])
    print("Done")

# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM53 import HoleM53
from pyleecan.Classes.Magnet import Magnet
from numpy import exp, arcsin, ndarray, pi

from pyleecan.Methods.Slot.HoleM53 import Slot53InterError

# For AlmostEqual
DELTA = 1e-6

HoleM53_test = list()
HoleM53_test_error = list()

# Two hole
test_obj = LamHole(is_internal=True, Rext=80.2e-3, Rint=0)
test_obj.hole = list()
test_obj.hole.append(
    HoleM53(
        Zh=8, H0=0.02, H1=0.001, H2=0.01, H3=0.003, W1=0.005, W2=0, W3=0.01, W4=0.78
    )
)
HoleM53_test.append(
    {
        "test_obj": test_obj,
        "S_exp": 3.63836e-4,
        "SM_exp": 0.0002,
        "Rmin": 5.8879558e-2,
        "Rmax": 7.92e-2,
        "W5": 7.78324e-3,
    }
)

# One hole
test_obj = LamHole(is_internal=True, Rext=80.2e-3, Rint=0)
test_obj.hole = list()
test_obj.hole.append(
    HoleM53(Zh=8, H0=0.02, H1=0.001, H2=0.01, H3=0.003, W1=0, W2=0, W3=0.01, W4=0.78)
)
HoleM53_test.append(
    {
        "test_obj": test_obj,
        "S_exp": 3.73158e-4,
        "SM_exp": 0.0002,
        "Rmin": 5.8523556e-2,
        "Rmax": 7.92e-2,
        "W5": 8.317707e-3,
    }
)

# Error test
test_obj = LamHole(is_internal=True, Rext=80.2e-3, Rint=0)
test_obj.hole = list()
test_obj.hole.append(
    HoleM53(Zh=8, H0=0.02, H1=0.001, H2=0.01, H3=0.003, W1=0, W2=0, W3=0.01, W4=0.78)
)
HoleM53_test_error.append(
    {
        "test_obj": test_obj,
        "S_exp": 3.73158e-4,
        "SM_exp": 0.0002,
        "Rmin": 5.8523556e-2,
        "Rmax": 7.92e-2,
        "W5": 8.317707e-3,
    }
)


@pytest.mark.METHODS
class Test_HoleM53_meth(object):
    """pytest for holeB53 methods"""

    @pytest.mark.parametrize("test_dict", HoleM53_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM53_test)
    def test_comp_surface_mag(self, test_dict):
        """Check that the computation of the magnet surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_surface_magnets()

        a = result
        b = test_dict["SM_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM53_test)
    def test_comp_radius(self, test_dict):
        """Check that the computation of the radius is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_radius()

        a = result[0]
        b = test_dict["Rmin"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        a = result[1]
        b = test_dict["Rmax"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM53_test)
    def test_comp_W5(self, test_dict):
        """Check that the computation of W5 iscorrect"""
        test_obj = test_dict["test_obj"]

        a = test_obj.hole[0].comp_W5()
        b = test_dict["W5"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        #  Test that Z11 = Zlist[0]

        test_obj2 = LamHole(is_internal=True, Rext=80.2e-3, Rint=0)
        test_obj2.hole = list()
        test_obj2.hole.append(
            HoleM53(
                Zh=8,
                H0=0.00000000000000000000002,
                H1=0.00000001,
                H2=0.01,
                H3=0.003,
                W1=0,
                W2=0,
                W3=0.01,
                W4=2.28,
            )
        )
        a = test_obj2.hole[0].comp_W5()
        assert -0.0014380265690122837 == a

    @pytest.mark.parametrize("test_dict", HoleM53_test)
    def test_build_geometry(self, test_dict):
        """Check that the build geometry method works"""

        # is_simplified to True and magnetization Parallel

        test_obj = test_dict["test_obj"]
        test_obj.hole[0].magnet_0 = Magnet(type_magnetization=1)
        test_obj.hole[0].magnet_1 = Magnet(type_magnetization=1)
        a = test_obj.hole[0].build_geometry(is_simplified=True)

        assert a[1].label == "HoleMagnet_Stator_Parallel_N_R0_T0_S0"
        assert a[1].line_list[0] is not None
        assert a[1].line_list[1] is not None
        with pytest.raises(IndexError) as context:
            a[1].line_list[2]

        if test_obj.hole[0].W1 > 0:
            assert a[4].label == "HoleMagnet_Stator_Parallel_N_R0_T1_S0"
            assert a[4].line_list[0] is not None
            assert a[4].line_list[1] is not None
            with pytest.raises(IndexError) as context:
                a[4].line_list[2]
        else:
            assert a[3].label == "HoleMagnet_Stator_Parallel_N_R0_T1_S0"
            assert a[3].line_list[0] is not None
            assert a[3].line_list[1] is not None
            with pytest.raises(IndexError) as context:
                a[3].line_list[2]

    @pytest.mark.parametrize("test_dict", HoleM53_test_error)
    def test_build_geometry_Z11_Z1_not_foundable(self, test_dict):
        """Check that the build geometry error works"""

        test_obj = test_dict["test_obj"]

        test_obj.hole[0] = HoleM53(
            Zh=8,
            H0=0.02,
            H1=0.001,
            H2=0.01,
            H3=0.003,
            W1=0.765149757,
            W2=0.32542,
            W3=0.0564,
            W4=0.324,
        )

        # Z11

        with pytest.raises(Slot53InterError) as context:
            test_obj.hole[0].build_geometry()

        test_obj.hole[0] = HoleM53(
            Zh=8,
            H0=50.02,
            H1=10.0054456451,
            H2=40.56456456401,
            H3=0.968464003,
            W1=10.0,
            W2=0.14540,
            W3=1.01546654654,
            W4=0.05144,
        )

        # Z1
        with pytest.raises(Slot53InterError) as context:
            test_obj.hole[0].build_geometry()

    @pytest.mark.parametrize("test_dict", HoleM53_test_error)
    def test_build_geometry_Z11_Z1(self, test_dict):
        """Check nothing it's just for the coverage"""

        test_obj = test_dict["test_obj"]
        test_obj.hole[0] = HoleM53(
            Zh=8, H0=0.02, H1=0.001, H2=0.01, H3=0.003, W1=0.005, W2=0, W3=0.01, W4=0.78
        )
        lst_pattern = test_obj.hole[0].build_geometry()

        # Z11 = Zlist[0]
        test_obj.hole[0] = HoleM53(
            Zh=8,
            H0=0.00000000000000000000002,
            H1=0.00000001,
            H2=0.01,
            H3=0.003,
            W1=0,
            W2=0,
            W3=0.01,
            W4=2.28,
        )
        lst1 = test_obj.hole[0].build_geometry()

        # Z1 = Zlist[0]
        test_obj.hole[0] = HoleM53(
            Zh=8,
            H0=0.00000000000000000000002,
            H1=0.00000001,
            H2=0.01,
            H3=0.003,
            W1=0,
            W2=0,
            W3=0.01,
            W4=4.78,
        )
        lst2 = test_obj.hole[0].build_geometry()

        assert len(lst1) != len(lst_pattern)
        assert len(lst2) != len(lst_pattern)

    def test_comp_surface_magnet_id(self):
        """check that id is 0"""
        hole = HoleM53(
            Zh=8, H0=0.02, H1=0.001, H2=0.01, H3=0.003, W1=0.005, W2=0, W3=0.01, W4=0.78
        )
        assert hole.comp_surface_magnet_id(2) == 0

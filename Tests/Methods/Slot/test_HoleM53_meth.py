# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM53 import HoleM53
from numpy import exp, arcsin, ndarray, pi

# For AlmostEqual
DELTA = 1e-6

HoleM53_test = list()

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


@pytest.mark.METHODS
class Test_HoleM53_meth(object):
    """pytest for holeB53 methods"""

    @pytest.mark.parametrize("test_dict", HoleM53_test)
    def test_comp_surface(self,test_dict):
        """Check that the computation of the surface is correct
            """
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a-0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM53_test)
    def test_comp_surface_mag(self,test_dict):
        """Check that the computation of the magnet surface is correct
            """
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_surface_magnets()

        a = result
        b = test_dict["SM_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a-0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM53_test)
    def test_comp_radius(self,test_dict):
        """Check that the computation of the radius is correct
            """
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_radius()

        a = result[0]
        b = test_dict["Rmin"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a-0) < DELTA, msg

        a = result[1]
        b = test_dict["Rmax"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a-0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", HoleM53_test)
    def test_comp_W5(self,test_dict):
        """Check that the computation of W5 iscorrect
            """
        test_obj = test_dict["test_obj"]
        
        a = test_obj.hole[0].comp_W5()
        b = test_dict["W5"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a-0) < DELTA, msg

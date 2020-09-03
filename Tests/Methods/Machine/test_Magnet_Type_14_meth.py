# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotMPolar import SlotMPolar
from pyleecan.Classes.MagnetType14 import MagnetType14
from numpy import pi, exp, sqrt
from pyleecan.Methods.Machine.Magnet.comp_height import comp_height
from pyleecan.Methods.Machine.Magnet.comp_surface import comp_surface

Mag14_test = list()
# Internal Slot inset
lam = LamSlotMag(Rint=40e-3, Rext=90e-3, is_internal=True)
lam.slot = SlotMPolar(Zs=4, W0=0.628, H0=0.02)
lam.slot.magnet = [MagnetType14(Lmag=0.5, Hmag=0.02, Wmag=0.628, Rtop=0.04)]
Mag14_test.append({"test_obj": lam, "S_exp": 9.022e-4, "Ao": 0.628, "H_exp": 0.02})

# Internal slot surface
lam = LamSlotMag(Rint=40e-3, Rext=90e-3, is_internal=True)
lam.slot = SlotMPolar(Zs=8, W0=0.628, H0=0)
lam.slot.magnet = [MagnetType14(Lmag=0.5, Hmag=0.02, Wmag=0.628, Rtop=0.05)]
Mag14_test.append({"test_obj": lam, "S_exp": 1.1089e-3, "Ao": 0.628, "H_exp": 0.02})

# For AlmostEqual
DELTA = 1e-4


@pytest.mark.METHODS

class Test_Magnet_Type_14_meth(object):
    """unittest for MagnetType14 methods
        """
    @pytest.mark.parametrize("test_dict", Mag14_test)
    def test_comp_surface(self,test_dict):
        """Check that the computation of the surface is correct
            """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a-0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", Mag14_test)
    def test_comp_height(self,test_dict):
        """Check that the computation of the height is correct
            """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a-0) < DELTA, msg

        # Compare numerical and analytical results
        b = comp_height(test_obj.slot.magnet[0])
        msg = "Analytical: " + str(a) + " Numerical " + str(b)
        assert abs((a - b) / a-0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", Mag14_test)
    def test_comp_angle_op(self,test_dict):
        """Check that the computation of the opening angle is correct
            """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_angle_opening()
        
        a = result
        b = test_dict["Ao"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a-0) < DELTA, msg

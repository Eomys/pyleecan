# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW15 import SlotW15
from numpy import ndarray, arcsin
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind

# For AlmostEqual
DELTA = 1e-4

slotW15_test = list()

# Outward Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW15(H0=5e-3, H1=5e-3, H2=20e-3, R1=4.5e-3, R2=4e-3, W0=5e-3, W3=10e-3)
slotW15_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.1010919e-4,
        "Aw": 0.10268530,
        "SW_exp": 3.8506988e-4,
        "H_exp": 0.03,
    }
)


@pytest.mark.METHODS
class Test_SlotW15_meth(object):
    """pytest for SlotW15 methods"""

    @pytest.mark.parametrize("test_dict", slotW15_test) 
    def test_comp_surface(self,test_dict):
        """Check that the computation of the surface is correct
            """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a-0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW15_test) 
    def test_comp_surface_wind(self,test_dict):
        """Check that the computation of the winding surface is correct
            """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_wind()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a-0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW15_test) 
    def test_comp_height(self,test_dict):
        """Check that the computation of the height is correct
            """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a-0) < DELTA, msg
        # Check that the analytical method returns the same result as the numerical one
        b = comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a-0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW15_test) 
    def test_comp_angle_opening(self,test_dict):
        """Check that the computation of the average opening angle iscorrect
            """
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a-0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW15_test) 
    def test_comp_angle_wind_eq(self,test_dict):
        """Check that the computation of the average angle is correct
            """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a-0) < DELTA, msg

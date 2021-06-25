# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW14 import SlotW14
from numpy import ndarray, arcsin
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods.Slot.SlotW14 import S14_Rbo1CheckError

# For AlmostEqual
DELTA = 1e-4

slotW14_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW14(H0=5e-3, H1=5e-3, H3=25e-3, W0=5e-3, W3=10e-3)
slotW14_test.append(
    {
        "test_obj": lam,
        "S_exp": 2.9443933e-4,
        "Aw": 0.08445503,
        "SW_exp": 2.28378e-4,
        "H_exp": 0.03486507,
    }
)

# Outward Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW14(H0=5e-3, H1=5e-3, H3=25e-3, W0=5e-3, W3=10e-3)
slotW14_test.append(
    {
        "test_obj": lam,
        "S_exp": 5.0790294e-4,
        "Aw": 0.108324,
        "SW_exp": 4.332517e-4,
        "H_exp": 0.03572334,
    }
)


class Test_SlotW14_meth(object):
    """pytest for SlotW14 methods"""

    @pytest.mark.parametrize("test_dict", slotW14_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()

        # Check width
        assert abs(point_dict["Z1"] - point_dict["Z9"]) == pytest.approx(
            test_obj.slot.W0
        )
        assert abs(point_dict["Z2"] - point_dict["Z8"]) == pytest.approx(
            test_obj.slot.W0
        )
        # Check height
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z2"].real - point_dict["Z3"].real) == pytest.approx(
            test_obj.slot.H1
        )
        assert abs(point_dict["Z3"] - point_dict["Z4"]) == pytest.approx(
            test_obj.slot.H3
        )
        assert abs(point_dict["Z9"] - point_dict["Z8"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z8"].real - point_dict["Z7"].real) == pytest.approx(
            test_obj.slot.H1
        )
        assert abs(point_dict["Z7"] - point_dict["Z6"]) == pytest.approx(
            test_obj.slot.H3
        )

    @pytest.mark.parametrize("test_dict", slotW14_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW14_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface_active(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW14_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW14_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW14_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_check(self):
        """Check that the check methods is correctly working"""
        lam = LamSlot(is_internal=False, Rint=0.1325)
        lam.slot = SlotW14(H0=5e-3, H1=5e-3, H3=25e-3, W0=5e-3, W3=10)

        with pytest.raises(S14_Rbo1CheckError) as context:
            lam.slot.check()

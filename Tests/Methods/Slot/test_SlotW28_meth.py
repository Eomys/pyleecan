# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW28 import SlotW28
from numpy import ndarray, arcsin, exp
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Segment import Segment
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.Slot.comp_surface_active import comp_surface_active
from pyleecan.Methods.Slot.SlotW28 import (
    S28_ZsCheckError,
    S28_RboW0CheckError,
    S28_R1R1CheckError,
)

# For AlmostEqual
DELTA = 1e-4

slotW28_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=84e-3)
lam.slot = SlotW28(Zs=42, W0=3.5e-3, H0=0.45e-3, R1=3.5e-3, H3=14e-3, W3=5e-3)
slotW28_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.1448e-4,
        "Ao": 0.0416696,
        "Aw": 0.107065,
        "SW_exp": 1.12862e-4,
        "H_exp": 2.0189e-2,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rint=85e-3)
lam.slot = SlotW28(Zs=18, W0=7e-3, R1=10e-3, H0=5e-3, H3=30e-3, W3=5e-3)
slotW28_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.8896e-3,
        "Ao": 0.082376,
        "Aw": 0.753692,
        "SW_exp": 1.855e-3,
        "H_exp": 6.2602e-2,
    }
)


@pytest.mark.METHODS
class Test_SlotW28_meth(object):
    """pytest for SlotW28 methods"""

    @pytest.mark.parametrize("test_dict", slotW28_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()

        # Check width
        assert abs(point_dict["Z1"] - point_dict["Z8"]) == pytest.approx(
            test_obj.slot.W0
        )
        assert abs(point_dict["Z2"] - point_dict["Z7"]) == pytest.approx(
            test_obj.slot.W0
        )
        # Check height
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z3"] - point_dict["Z4"]) == pytest.approx(
            test_obj.slot.H3
        )
        assert abs(point_dict["Z8"] - point_dict["Z7"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z5"] - point_dict["Z6"]) == pytest.approx(
            test_obj.slot.H3
        )

    @pytest.mark.parametrize("test_dict", slotW28_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW28_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface_active(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW28_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW28_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        b = test_dict["Ao"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW28_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_check(self):
        """Check that the check function is raising error"""
        lam = LamSlot(is_internal=True, Rext=84e-3)
        lam.slot = SlotW28(Zs=420, W0=3.5e-3, H0=0.45e-3, R1=3.5e-3, H3=14e-3, W3=5e-3)

        with pytest.raises(S28_ZsCheckError) as context:
            lam.slot.check()

        lam = LamSlot(is_internal=True, Rext=84e-3)
        lam.slot = SlotW28(Zs=420, W0=300.5, H0=0.45e-3, R1=3.5e-3, H3=14e-3, W3=5e-3)

        with pytest.raises(S28_RboW0CheckError) as context:
            lam.slot.check()

        # Test with Outwards and the error S28_R1R1CheckError to be sure that it works

        lam = LamSlot(
            is_internal=False, Rext=0.000000000000000000151, Rint=0.00000000000001256
        )
        lam.slot = SlotW28(Zs=1, W0=3.5e-53, H0=0, R1=30000000.5, H3=14e-3, W3=5e-3)

        with pytest.raises(S28_R1R1CheckError) as context:
            lam.slot.check()

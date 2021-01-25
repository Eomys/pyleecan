# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.SlotW26 import SlotW26
from numpy import ndarray, angle
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Slot import Slot

# For AlmostEqual
DELTA = 1e-4

slotW26_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1)
lam.slot = SlotW26(Zs=12, H0=10e-3, W0=10e-3, H1=0.025, R1=0.01, R2=0.0075)
slotW26_test.append(
    {
        "test_obj": lam,
        "S_exp": 7.7471e-4,
        "Ao": 0.10004,
        "Aw": 0.2362668,
        "SW_exp": 6.7387e-4,
        "H_exp": 5.1285e-2,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rint=0.1)
lam.slot = SlotW26(Zs=12, H0=10e-3, W0=10e-3, H1=0.025, R1=0.01, R2=0.0075)
slotW26_test.append(
    {
        "test_obj": lam,
        "S_exp": 7.73044e-4,
        "Ao": 0.10004,
        "Aw": 0.1254996,
        "SW_exp": 6.7387e-4,
        "H_exp": 5.103517e-2,
    }
)


@pytest.mark.METHODS
class Test_SlotW26_meth(object):
    """pytest for SlotW26 methods"""

    @pytest.mark.parametrize("test_dict", slotW26_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()

        assert angle(point_dict["Z1"]) < 0
        assert angle(point_dict["Z2"]) < 0
        assert angle(point_dict["Z3"]) < 0
        assert angle(point_dict["Z4"]) < 0
        assert angle(point_dict["Z5"]) > 0
        assert angle(point_dict["Z6"]) > 0
        assert angle(point_dict["Z7"]) > 0
        assert angle(point_dict["Z8"]) > 0
        # Check width
        assert abs(point_dict["Z1"] - point_dict["Z8"]) == pytest.approx(
            test_obj.slot.W0
        )
        assert abs(point_dict["Z2"] - point_dict["Z7"]) == pytest.approx(
            test_obj.slot.W0
        )
        assert abs(point_dict["Z4"] - point_dict["Z5"]) == pytest.approx(
            2 * test_obj.slot.R2
        )
        # Check height
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z3"].real - point_dict["Z4"].real) == pytest.approx(
            test_obj.slot.H1
        )
        assert abs(point_dict["Z8"] - point_dict["Z7"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z6"].real - point_dict["Z5"].real) == pytest.approx(
            test_obj.slot.H1
        )
        assert abs(point_dict["Zc1"] - point_dict["Zc2"]) == pytest.approx(
            test_obj.slot.H1
        )
        # Check radius
        assert abs(point_dict["Z2"] - point_dict["Zc1"]) == pytest.approx(
            test_obj.slot.R1
        )
        assert abs(point_dict["Z3"] - point_dict["Zc1"]) == pytest.approx(
            test_obj.slot.R1
        )
        assert abs(point_dict["Z7"] - point_dict["Zc1"]) == pytest.approx(
            test_obj.slot.R1
        )
        assert abs(point_dict["Z6"] - point_dict["Zc1"]) == pytest.approx(
            test_obj.slot.R1
        )
        assert abs(point_dict["Z4"] - point_dict["Zc2"]) == pytest.approx(
            test_obj.slot.R2
        )
        assert abs(point_dict["Z5"] - point_dict["Zc2"]) == pytest.approx(
            test_obj.slot.R2
        )

    @pytest.mark.parametrize("test_dict", slotW26_test)
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
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW26_test)
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
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW26_test)
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
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW26_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        b = test_dict["Ao"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW26_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_build_geometry_active(self):
        """Check if the build geometry of the winding works correctly"""
        lam = LamSlot(is_internal=True, Rext=0.1325)
        lam.slot = SlotW26(Zs=12, H0=10e-3, W0=10e-3, H1=0, R1=0.01, R2=0.0075)

        result = lam.slot.build_geometry()
        assert len(result) == 5

# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.Segment import Segment

from pyleecan.Classes.SlotW29 import SlotW29
from numpy import ndarray, arcsin, exp
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind

# For AlmostEqual
DELTA = 1e-4

slotW29_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW29(H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=20e-3)
slotW29_test.append(
    {
        "test_obj": lam,
        "S_exp": 6.340874e-4,
        "Ao": 0.10004,
        "Aw": 0.174118,
        "SW_exp": 6e-4,
        "H_exp": 3.26359e-2,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW29(H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=20e-3)
slotW29_test.append(
    {
        "test_obj": lam,
        "S_exp": 6.31912e-4,
        "Ao": 0.10004,
        "Aw": 0.133185,
        "SW_exp": 6e-4,
        "H_exp": 3.2667e-2,
    }
)


@pytest.mark.METHODS
class Test_SlotW29_meth(object):
    """pytest for SlotW29 methods"""

    @pytest.mark.parametrize("test_dict", slotW29_test)
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

    @pytest.mark.parametrize("test_dict", slotW29_test)
    def test_comp_surface_wind(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_wind()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface_wind(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW29_test)
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

    @pytest.mark.parametrize("test_dict", slotW29_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW29_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_build_geometry(self):
        """check that curve_list is correct"""
        test_obj = LamSlot(is_internal=False, Rint=1)
        test_obj.slot = SlotW29(W0=0.2, H0=0.1, W1=0.4, H1=0.1, H2=0.6, W2=0.6)

        # Rbo=1
        Z1 = exp(1j * float(arcsin(0.1)))

        Z2 = Z1 + 0.1
        Z3 = Z1 + 0.1 + 0.1j
        Z4 = Z1 + 0.2 + 0.1j
        Z5 = Z1 + 0.2 + 0.2j
        Z6 = Z1 + 0.8 + 0.2j
        Z7 = Z1 + 0.8 - 0.4j
        Z8 = Z1 + 0.2 - 0.4j
        Z9 = Z1 + 0.2 - 0.3j
        Z10 = Z1 + 0.1 - 0.3j
        Z11 = Z1 + 0.1 - 0.2j
        Z12 = Z1 - 0.2j

        [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12] = [
            Z12,
            Z11,
            Z10,
            Z9,
            Z8,
            Z7,
            Z6,
            Z5,
            Z4,
            Z3,
            Z2,
            Z1,
        ]
        curve_list = list()
        curve_list.append(Segment(Z1, Z2))
        curve_list.append(Segment(Z2, Z3))
        curve_list.append(Segment(Z3, Z4))
        curve_list.append(Segment(Z4, Z5))
        curve_list.append(Segment(Z5, Z6))
        curve_list.append(Segment(Z6, Z7))
        curve_list.append(Segment(Z7, Z8))
        curve_list.append(Segment(Z8, Z9))
        curve_list.append(Segment(Z9, Z10))
        curve_list.append(Segment(Z10, Z11))
        curve_list.append(Segment(Z11, Z12))

        result = test_obj.slot.build_geometry()
        assert len(result) == len(curve_list)
        for i in range(0, len(result)):
            a = result[i].begin
            b = curve_list[i].begin
            assert abs((a - b) / a - 0) < DELTA, (
                "Wrong build_geo (for begin point "
                + str(i)
                + " returned "
                + str(a)
                + ", expected "
                + str(b)
                + ")"
            )

            a = result[i].end
            b = curve_list[i].end
            assert abs((a - b) / a - 0) < DELTA, (
                "Wrong build_geo (for end point "
                + str(i)
                + " returned "
                + str(a)
                + ", expected "
                + str(b)
                + ")"
            )

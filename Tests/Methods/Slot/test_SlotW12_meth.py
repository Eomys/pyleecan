# -*- coding: utf-8 -*-
import pytest

from numpy import ndarray, arcsin, exp
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotW12 import SlotW12
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Arc3 import Arc3
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind

# For AlmostEqual
DELTA = 1e-4

slotW12_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW12(H0=1e-3, H1=6e-3, R1=0.5e-3, R2=2e-3)
slotW12_test.append(
    {
        "test_obj": lam,
        "S_exp": 3.91088e-5,
        "Aw": 0.0299276,
        "SW_exp": 3.028318e-5,
        "H_exp": 1.0015e-2,
    }
)

# Outward Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW12(H0=1e-3, H1=6e-3, R1=0.5e-3, R2=2e-3)
slotW12_test.append(
    {
        "test_obj": lam,
        "S_exp": 3.90283e-5,
        "Aw": 0.0273343,
        "SW_exp": 3.02831853e-5,
        "H_exp": 9.9849e-3,
    }
)


@pytest.mark.METHODS
class Test_SlotW12_meth(object):
    """pytest for SlotW12 methods"""

    @pytest.mark.parametrize("test_dict", slotW12_test)
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
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW12_test)
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
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW12_test)
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
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW12_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(2 * test_obj.slot.R2 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW12_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_build_geometry(self):
        """Check if the build_geometry of the slot is correct"""
        test_obj = SlotW12(H0=1e-3, H1=6e-3, R1=0.5e-3, R2=2e-3)
        lam = LamSlot(is_internal=True, slot=test_obj, Rext=1)

        # Rbo = 1
        Z1 = exp(-1j * float(arcsin(2e-3)))
        Z2 = Z1 - 1e-3
        Z3 = Z2 - 1e-3
        Z4 = Z3 - 6e-3
        # symetry
        Z5 = Z4.conjugate()
        Z6 = Z3.conjugate()
        Z7 = Z2.conjugate()
        Z8 = Z1.conjugate()

        # creation of the curve
        curve_list = list()
        curve_list.append(Segment(Z1, Z2))
        curve_list.append(Arc3(Z2, Z3, True))
        curve_list.append(Segment(Z3, Z4))
        curve_list.append(Arc3(Z4, Z5, True))
        curve_list.append(Segment(Z5, Z6))
        curve_list.append(Arc3(Z6, Z7, True))
        curve_list.append(Segment(Z7, Z8))

        result = test_obj.build_geometry()
        assert len(result) == len(curve_list)
        for i in range(0, len(result)):
            a = result[i].begin
            b = curve_list[i].begin
            assert abs((a - b) / a - 0) < DELTA

            a = result[i].end
            b = curve_list[i].end
            assert abs((a - b) / a - 0) < DELTA

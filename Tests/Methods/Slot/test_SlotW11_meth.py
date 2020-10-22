# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW11 import SlotW11
from numpy import ndarray, arcsin, exp, angle
from scipy.optimize import fsolve
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind
from pyleecan.Methods.Slot.SlotW11.check import S11_H1rCheckError

# For AlmostEqual
DELTA = 1e-6
slotW11_test = list()
slotW11_H1_rad_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW11(H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3, R1=5e-3)
slotW11_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.06857e-4,
        "Aw": 0.1086124,
        "SW_exp": 3.7427e-4,
        "H_exp": 3.263591e-2,
    }
)

# Outward Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW11(H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3, R1=5e-3)
slotW11_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.04682446e-4,
        "Aw": 0.0832448,
        "SW_exp": 3.7427e-04,
        "H_exp": 3.236711e-2,
    }
)
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW11(
    H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3, R1=5e-3, H1_is_rad=True
)
slotW11_H1_rad_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.04682446e-4,
        "Aw": 0.0832448,
        "SW_exp": 3.7427e-04,
        "H_exp": 3.236711e-2,
    }
)


@pytest.mark.METHODS
class Test_SlotW11_meth(object):
    """pytest for SlotW11 methods"""

    @pytest.mark.parametrize("test_dict", slotW11_test)
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

    @pytest.mark.parametrize("test_dict", slotW11_test)
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

    @pytest.mark.parametrize("test_dict", slotW11_test)
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

    @pytest.mark.parametrize("test_dict", slotW11_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW11_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW11_H1_rad_test)
    def test_comp_point_coordinate_error(self, test_dict):
        """Check that the error is well raised"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot._comp_point_coordinate()
        assert result == [
            (0.13236408123052115 - 0.006j),
            (0.13336408123052115 - 0.006j),
            (0.13336558123164616 - 0.007j),
            (0.15836558123164615 - 0.006j),
            (0.16336558123164616 - 0.001j),
            (0.16336558123164616 + 0.001j),
            (0.15836558123164615 + 0.006j),
            (0.13336558123164616 + 0.007j),
            (0.13336408123052115 + 0.006j),
            (0.13236408123052115 + 0.006j),
            1,
        ]

    def test_SlotW11_check(self):
        """Check if the error S11_H1rCheckError is correctly raised in the check method"""
        lam = LamSlot(is_internal=False, Rint=0.1325)
        lam.slot = SlotW11(
            H0=1e-3,
            H1=3,
            H2=30e-3,
            W0=12e-3,
            W1=14e-3,
            W2=12e-3,
            R1=5e-3,
            H1_is_rad=True,
        )

        with pytest.raises(S11_H1rCheckError) as context:
            lam.slot.check()

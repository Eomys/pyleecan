# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW23 import SlotW23
from numpy import ndarray, arcsin, pi
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind
from pyleecan.Methods.Slot.SlotW23.check import S23_H1rCheckError

# For AlmostEqual
DELTA = 1e-4

slotW23_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW23(
    H0=1e-3, H1=1.5e-3, H1_is_rad=False, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3
)
slotW23_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.2080459e-4,
        "Aw": 0.112537,
        "SW_exp": 3.8834260e-04,
        "H_exp": 0.032438,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW23(
    H0=1e-3, H1=1.5e-3, H1_is_rad=False, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3
)
slotW23_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.2116997e-4,
        "Aw": 0.086598,
        "SW_exp": 3.906568e-04,
        "H_exp": 0.032455,
    }
)

# Rad H1
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW23(
    H0=1e-3, H1=pi / 4, H1_is_rad=True, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3
)
slotW23_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.010646,
        "Aw": 0.013918,
        "SW_exp": 3.89935e-4,
        "H_exp": 0.81626,
    }
)


@pytest.mark.METHODS
class Test_SlotW23_meth(object):
    """pytest for SlotW23 methods"""

    @pytest.mark.parametrize("test_dict", slotW23_test)
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

    @pytest.mark.parametrize("test_dict", slotW23_test)
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

    @pytest.mark.parametrize("test_dict", slotW23_test)
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

    @pytest.mark.parametrize("test_dict", slotW23_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW23_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_comp_point_coordinate(self):
        """Check that comp_point_coordinate can compute W1 and W2 if cstt_tooth is true correct"""
        lam = LamSlot(is_internal=False, Rint=0.1325)
        lam.slot = SlotW23(
            H0=1e-3,
            H1=pi / 4,
            H1_is_rad=True,
            H2=30e-3,
            W0=12e-3,
            W1=14e-3,
            W2=12e-3,
            is_cstt_tooth=True,
        )
        result = lam.slot._comp_point_coordinate()
        assert result == [
            (0.13236408123052115 - 0.006j),
            (0.13336305542848736 - 0.006045283018867925j),
            (0.9187612188259356 - 0.07510509283990814j),
            (0.948647059768688 - 0.0777197651223379j),
            (0.948647059768688 + 0.0777197651223379j),
            (0.9187612188259356 + 0.07510509283990814j),
            (0.13336305542848736 + 0.006045283018867925j),
            (0.13236408123052115 + 0.006j),
        ]

    def test_check_error(self):
        """Check that the check method is correctly raising an error"""
        lam = LamSlot(is_internal=True, Rext=0.1325)
        lam.slot = SlotW23(Zs=69, H2=0.0015, W3=12e-3, H1_is_rad=True, H1=3.14)

        with pytest.raises(S23_H1rCheckError) as context:
            lam.slot.check()

    def test_get_surface_wind(self):
        """Check that the get_surface_wind works when stator = false"""
        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW23(
            H0=1e-3, H1=1.5e-3, H1_is_rad=False, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3
        )
        result = lam.slot.get_surface_wind()
        assert result.label == "Wind_Rotor_R0_T0_S0"
        assert len(result.get_lines()) == 4

    def test_comp_W(self):
        """Check that the computations of the Ws are right"""
        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW23(
            H0=1e-3, H1=1.5e-3, H1_is_rad=False, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3
        )
        lam.slot._comp_W()
        assert lam.slot.W1 == 0.012681779210634543
        assert lam.slot.W2 == 0.0074524346457750515

        lam = LamSlot(is_internal=False, Rext=0.1325, is_stator=False, Rint=0.154)
        lam.slot = SlotW23(
            H0=1e-3, H1=1.5e-3, H1_is_rad=False, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3
        )
        lam.slot._comp_W()
        assert lam.slot.W1 == 0.017303874301855315
        assert lam.slot.W2 == 0.022533218866714805

    def test_build_geometry_wind(self):
        """Check if the build geometry of the winding works correctly"""
        lam = LamSlot(is_internal=True, Rext=0.1325)
        lam.slot = SlotW23(
            H0=1e-3, H1=1.5e-3, H1_is_rad=False, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3
        )

        result = lam.slot.build_geometry_wind(Nrad=2, Ntan=4, is_simplified=True)
        a = result
        assert "Wind_Stator_R0_T0_S0" == a[0].label
        assert len(a) == 8

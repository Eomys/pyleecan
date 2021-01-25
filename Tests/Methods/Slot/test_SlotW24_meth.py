# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW24 import SlotW24
from numpy import ndarray, pi, exp
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods.Slot.SlotW24 import S24_HWCheckError

# For AlmostEqual
DELTA = 1e-4

slotW24_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW24(Zs=6, H2=30e-3, W3=12e-3)
slotW24_test.append(
    {
        "test_obj": lam,
        "S_exp": 3.327419e-3,
        "Ao": 0.9566,
        "Aw": 0.94497,
        "SW_exp": 3.327419e-3,
        "H_exp": 0.02996,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW24(Zs=6, H2=30e-3, W3=12e-3)
slotW24_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.26977e-3,
        "Ao": 0.9566,
        "Aw": 0.965887,
        "SW_exp": 4.26977e-3,
        "H_exp": 0.029974,
    }
)


@pytest.mark.METHODS
class Test_SlotW24_meth(object):
    """pytest for SlotW24 methods"""

    @pytest.mark.parametrize("test_dict", slotW24_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()

        assert point_dict["Z1"].imag < 0
        assert point_dict["Z2"].imag < 0
        assert point_dict["Z3"].imag > 0
        assert point_dict["Z4"].imag > 0

        # Check height
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.H2
        )
        assert abs(point_dict["Z3"] - point_dict["Z4"]) == pytest.approx(
            test_obj.slot.H2
        )
        # Check width
        assert (
            point_dict["Z1"] * exp(1j * pi / test_dict["test_obj"].slot.Zs)
        ).imag == pytest.approx(test_dict["test_obj"].slot.W3 / 2)
        assert (
            point_dict["Z2"] * exp(1j * pi / test_dict["test_obj"].slot.Zs)
        ).imag == pytest.approx(test_dict["test_obj"].slot.W3 / 2)

    @pytest.mark.parametrize("test_dict", slotW24_test)
    def test_build_geometry_active(self, test_dict):
        """Check that the active geometry is correctly split"""
        test_obj = test_dict["test_obj"]
        surf_list = test_obj.slot.build_geometry_active(Nrad=3, Ntan=2)

        # Check label
        assert surf_list[0].label == "Wind_Stator_R0_T0_S0"
        assert surf_list[1].label == "Wind_Stator_R1_T0_S0"
        assert surf_list[2].label == "Wind_Stator_R2_T0_S0"
        assert surf_list[3].label == "Wind_Stator_R0_T1_S0"
        assert surf_list[4].label == "Wind_Stator_R1_T1_S0"
        assert surf_list[5].label == "Wind_Stator_R2_T1_S0"
        # Check tangential position
        assert surf_list[0].point_ref.imag < 0
        assert surf_list[1].point_ref.imag < 0
        assert surf_list[2].point_ref.imag < 0
        assert surf_list[3].point_ref.imag > 0
        assert surf_list[4].point_ref.imag > 0
        assert surf_list[5].point_ref.imag > 0
        # Check radial position
        if test_obj.is_internal:
            # Tan=0
            assert surf_list[0].point_ref.real > surf_list[1].point_ref.real
            assert surf_list[1].point_ref.real > surf_list[2].point_ref.real
            # Tan=1
            assert surf_list[3].point_ref.real > surf_list[4].point_ref.real
            assert surf_list[4].point_ref.real > surf_list[5].point_ref.real
        else:
            # Tan=0
            assert surf_list[0].point_ref.real < surf_list[1].point_ref.real
            assert surf_list[1].point_ref.real < surf_list[2].point_ref.real
            # Tan=1
            assert surf_list[3].point_ref.real < surf_list[4].point_ref.real
            assert surf_list[4].point_ref.real < surf_list[5].point_ref.real

    @pytest.mark.parametrize("test_dict", slotW24_test)
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

    @pytest.mark.parametrize("test_dict", slotW24_test)
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

    @pytest.mark.parametrize("test_dict", slotW24_test)
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

    @pytest.mark.parametrize("test_dict", slotW24_test)
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

    @pytest.mark.parametrize("test_dict", slotW24_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_check_error(self):
        """Check that the check method is correctly raising an error"""
        lam = LamSlot(is_internal=True, Rext=0.1325)
        lam.slot = SlotW24(Zs=69, H2=0.0015, W3=12e-3)

        with pytest.raises(S24_HWCheckError) as context:
            lam.slot.check()

    def test_get_surface_active(self):
        """Check that the get_surface_active works when stator = false"""
        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW24(Zs=6, H2=30e-3, W3=12e-3)
        result = lam.slot.get_surface_active()
        assert result.label == "Wind_Rotor_R0_T0_S0"
        assert len(result.get_lines()) == 4

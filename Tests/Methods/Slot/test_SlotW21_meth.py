# -*- coding: utf-8 -*-
import pytest


from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.SlotW21 import SlotW21
from pyleecan.Classes.LamSlot import LamSlot
from numpy import ndarray, pi, arcsin, exp
from ddt import ddt, data
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.Slot.comp_surface_active import comp_surface_active
from pyleecan.Methods.Slot.SlotW21.check import S21_H1rCheckError

# For AlmostEqual
DELTA = 1e-4

slotW21_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1)
lam.slot = SlotW21(
    Zs=36, H0=3e-3, H1=0, H1_is_rad=False, H2=20e-3, W0=3e-3, W1=13e-3, W2=10e-3
)
slotW21_test.append(
    {
        "test_obj": lam,
        "S_exp": 2.390225015189331e-4,
        "Aw": 0.132201,
        "SW_exp": 2.3e-4,
        "H_exp": 2.3011250632883697e-2,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rint=0.1)
lam.slot = SlotW21(
    Zs=36, H0=3e-3, H1=0, H1_is_rad=False, H2=20e-3, W0=3e-3, W1=13e-3, W2=10e-3
)
slotW21_test.append(
    {
        "test_obj": lam,
        "S_exp": 2.3897749848106692e-4,
        "Aw": 0.10168861,
        "SW_exp": 2.3e-4,
        "H_exp": 2.30903427198e-2,
    }
)

# Rad H1
lam = LamSlot(is_internal=False, Rint=0.1)
lam.slot = SlotW21(
    Zs=36, H0=3e-3, H1=pi / 4, H1_is_rad=True, H2=20e-3, W0=3e-3, W1=13e-3, W2=10e-3
)
slotW21_test.append(
    {
        "test_obj": lam,
        "S_exp": 2.7897749848106692e-4,
        "Aw": 0.097386,
        "SW_exp": 2.3e-4,
        "H_exp": 2.8086e-2,
    }
)


@pytest.mark.METHODS
class Test_SlotW21_meth(object):
    """pytest for SlotW21 methods"""

    @pytest.mark.parametrize("test_dict", slotW21_test)
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
        assert abs(point_dict["Z3"] - point_dict["Z6"]) == pytest.approx(
            test_obj.slot.W1
        )
        assert abs(point_dict["Z4"] - point_dict["Z5"]) == pytest.approx(
            test_obj.slot.W2
        )
        # Check height
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z2"].real - point_dict["Z3"].real) == pytest.approx(
            test_obj.slot.get_H1()
        )
        assert abs(point_dict["Z3"].real - point_dict["Z4"].real) == pytest.approx(
            test_obj.slot.H2
        )

        assert abs(point_dict["Z8"] - point_dict["Z7"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z7"].real - point_dict["Z6"].real) == pytest.approx(
            test_obj.slot.get_H1()
        )
        assert abs(point_dict["Z6"].real - point_dict["Z5"].real) == pytest.approx(
            test_obj.slot.H2
        )

    @pytest.mark.parametrize("test_dict", slotW21_test)
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

    @pytest.mark.parametrize("test_dict", slotW21_test)
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

    @pytest.mark.parametrize("test_dict", slotW21_test)
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

    @pytest.mark.parametrize("test_dict", slotW21_test)
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

    @pytest.mark.parametrize("test_dict", slotW21_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1))
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW21_test)
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
        lam.slot = SlotW21(Zs=69, H2=0.0015, H1_is_rad=True, H1=3.14)

        with pytest.raises(S21_H1rCheckError) as context:
            lam.slot.check()

    def test_get_surface_active(self):
        """Check that the get_surface_active works when stator = false"""
        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW21(
            Zs=36, H0=3e-3, H1=0, H1_is_rad=False, H2=20e-3, W0=3e-3, W1=13e-3, W2=10e-3
        )
        result = lam.slot.get_surface_active()
        assert result.label == "Wind_Rotor_R0_T0_S0"
        assert len(result.get_lines()) == 4

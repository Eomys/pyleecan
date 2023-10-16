# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW16 import SlotW16
from numpy import ndarray, arcsin, pi, angle
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods.Slot.SlotW16 import S16OutterError
import matplotlib.pyplot as plt
from pyleecan.Classes.Arc1 import Arc1

# For AlmostEqual
DELTA = 1e-4

slotW16_test = list()
slotW16_wrong_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW16(Zs=8, H0=5e-3, H2=30e-3, R1=5e-3, W0=pi / 12, W3=10e-3)
slotW16_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.0029208336939601474,
        "Aw": 0.8150115827824299,
        "SW_exp": 0.0027506640918907002,
        "SO_exp": 0.000170169,
        "H_exp": 3.5e-2,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rext=0.1325, is_stator=False)
lam.slot = SlotW16(Zs=8, H0=5e-3, H2=30e-3, R1=5e-3, W0=pi / 12, W3=10e-3)
slotW16_wrong_test.append(
    {
        "test_obj": lam,
        "S_exp": 2.508259e-3,
        "Aw": 0.6927673,
        "SW_exp": 2.33808e-3,
        "SO_exp": 6.60596e-05,
        "H_exp": 3.5e-2,
    }
)

# Small H0/W0/R1
lam = LamSlot(is_internal=True, Rint=0.04, Rext=0.0746, is_stator=False)
lam.slot = SlotW16(Zs=76, H0=0.0008, H2=0.0172, R1=1e-6, W0=0.00001, W3=0.00299)
slotW16_test.append(
    {
        "test_obj": lam,
        "S_exp": 9.278655434664112e-05,
        "Aw": 0.08273823008510589,
        "SW_exp": 9.278596074664111e-05,
        "SO_exp": 5.935999999999972e-10,
        "H_exp": 0.018,
    }
)


class Test_SlotW16_meth(object):
    """pytest for SlotW16 methods"""

    @pytest.mark.parametrize("test_dict", slotW16_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()

        # Check width
        assert angle(point_dict["Z1"]) == pytest.approx(-test_obj.slot.W0 / 2)
        assert angle(point_dict["Z10"]) == pytest.approx(test_obj.slot.W0 / 2)
        assert abs(point_dict["Z1"]) == abs(point_dict["Z10"])

        assert angle(point_dict["Z2"]) == pytest.approx(-test_obj.slot.W0 / 2)
        assert angle(point_dict["Z9"]) == pytest.approx(test_obj.slot.W0 / 2)
        assert abs(point_dict["Z2"]) == abs(point_dict["Z9"])

        # Check height
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z10"] - point_dict["Z9"]) == pytest.approx(
            test_obj.slot.H0
        )
        # Check radius
        assert abs(point_dict["Z3"] - point_dict["Zc1"]) == pytest.approx(
            test_obj.slot.R1
        )
        assert abs(point_dict["Z4"] - point_dict["Zc1"]) == pytest.approx(
            test_obj.slot.R1
        )
        assert abs(point_dict["Z7"] - point_dict["Zc2"]) == pytest.approx(
            test_obj.slot.R1
        )
        assert abs(point_dict["Z8"] - point_dict["Zc2"]) == pytest.approx(
            test_obj.slot.R1
        )

    @pytest.mark.parametrize("test_dict", slotW16_test)
    def test_build_geometry_active(self, test_dict):
        """Check that the active geometry is correctly split"""
        test_obj = test_dict["test_obj"]
        surf_list = test_obj.slot.build_geometry_active(Nrad=3, Ntan=2)

        if test_obj.is_stator == False:
            # Check label
            assert surf_list[0].label == "Rotor_Winding_R0-T0-S0"
            assert surf_list[1].label == "Rotor_Winding_R1-T0-S0"
            assert surf_list[2].label == "Rotor_Winding_R2-T0-S0"
            assert surf_list[3].label == "Rotor_Winding_R0-T1-S0"
            assert surf_list[4].label == "Rotor_Winding_R1-T1-S0"
            assert surf_list[5].label == "Rotor_Winding_R2-T1-S0"
        else:
            # Check label
            assert surf_list[0].label == "Stator_Winding_R0-T0-S0"
            assert surf_list[1].label == "Stator_Winding_R1-T0-S0"
            assert surf_list[2].label == "Stator_Winding_R2-T0-S0"
            assert surf_list[3].label == "Stator_Winding_R0-T1-S0"
            assert surf_list[4].label == "Stator_Winding_R1-T1-S0"
            assert surf_list[5].label == "Stator_Winding_R2-T1-S0"
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

    @pytest.mark.parametrize("test_dict", slotW16_test)
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

    @pytest.mark.parametrize("test_dict", slotW16_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW16_test)
    def test_comp_surface_opening(self, test_dict):
        """Check that the computation of the opening surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_opening()

        a = result
        b = test_dict["SO_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface_opening(test_obj.slot, Ndisc=400)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW16_test)
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

    @pytest.mark.parametrize("test_dict", slotW16_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == test_obj.slot.W0
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW16_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW16_wrong_test)
    def test_comp_point_coordinate_error(self, test_dict):
        """Check that the error is well raised"""
        test_obj = test_dict["test_obj"]

        with pytest.raises(S16OutterError) as context:
            test_obj.slot._comp_point_coordinate()

    def test_get_surface_X(self):
        """Check that the get_surface_X works when stator = false"""
        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW16(Zs=8, H0=5e-3, H2=30e-3, R1=5e-3, W0=pi / 12, W3=10e-3)
        result = lam.slot.get_surface_active()
        assert result.label == "Rotor_Winding_R0-T0-S0"
        assert len(result.get_lines()) == 8
        assert result.is_inside(result.point_ref)

        result = lam.slot.get_surface_opening()
        assert len(result) == 1
        assert result[0].label == "Rotor_SlotOpening_R0-T0-S0"
        assert len(result[0].get_lines()) == 4
        assert result[0].is_inside(result[0].point_ref)

        result = lam.slot.get_surface()
        assert len(result.get_lines()) == 10
        assert result.is_inside(result.point_ref)


if __name__ == "__main__":
    a = Test_SlotW16_meth()
    for ii, test_dict in enumerate(slotW16_test):
        print("Running test for Slot[" + str(ii) + "]")
        a.test_schematics(test_dict)
        a.test_comp_surface(test_dict)
        a.test_comp_surface_active(test_dict)
        a.test_comp_surface_opening(test_dict)
        a.test_comp_height(test_dict)
        a.test_build_geometry_active(test_dict)
        a.test_comp_angle_opening(test_dict)
        a.test_comp_angle_active_eq(test_dict)
        print("Done")

# -*- coding: utf-8 -*-
import pytest
from os.path import join, isfile
from os import remove
from pyleecan.Classes.SlotCirc import SlotCirc
from numpy import ndarray, pi, exp
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods.Slot.SlotCirc import SlotCheckError
import matplotlib.pyplot as plt
from pyleecan.Functions.load import load
from Tests import save_load_path

# For AlmostEqual
DELTA = 1e-4

slotCirc_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rint=0.1325, Rext=0.2)
lam.slot = SlotCirc(Zs=6, H0=30e-3, W0=12e-3, is_H0_bore=False)
slotCirc_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.00075558,
        "Ao": 0.0600090036,
        "Aw": 0.13576,
        "SW_exp": 0.00075558,
        "H_exp": 0.03009,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotCirc(Zs=6, H0=30e-3, W0=12e-3, is_H0_bore=False)
slotCirc_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.00075377,
        "Ao": 0.090597,
        "Aw": 0.1711986,
        "SW_exp": 0.00075377,
        "H_exp": 0.029864,
    }
)

# H0 < W0/2 internal
lam = LamSlot(is_internal=True, Rext=0.0592, Rint=0.0215)
lam.slot = SlotCirc(Zs=8, H0=0.00021, W0=0.008, is_H0_bore=False)
slotCirc_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.8423274e-06,
        "Ao": 0.135238,
        "Aw": 0.090392,
        "SW_exp": 1.8423274e-06,
        "H_exp": 0.000345289,
    }
)

# H0 < W0/2 external
lam = LamSlot(is_internal=False, Rint=0.0592, Rext=0.075)
lam.slot = SlotCirc(Zs=8, H0=0.00035, W0=0.008, is_H0_bore=False)
slotCirc_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.1478116e-06,
        "Ao": 0.13523817,
        "Aw": 0.09013827,
        "SW_exp": 1.1478116e-06,
        "H_exp": 0.0002147,
    }
)

#############
# Same 4 cases with is_H0_bore=True
#############
# Internal Slot
lam = LamSlot(is_internal=True, Rint=0.1325, Rext=0.2)
lam.slot = SlotCirc(Zs=6, H0=30e-3, W0=12e-3, is_H0_bore=True)
slotCirc_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.00075132,
        "Ao": 0.0600090036,
        "Aw": 0.135373,
        "SW_exp": 0.00075132,
        "H_exp": 0.03,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotCirc(Zs=6, H0=30e-3, W0=12e-3, is_H0_bore=True)
slotCirc_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.0007602278,
        "Ao": 0.090597,
        "Aw": 0.1718029,
        "SW_exp": 0.0007602278,
        "H_exp": 0.03,
    }
)

# H0 < W0/2 internal
lam = LamSlot(is_internal=True, Rext=0.0592, Rint=0.0215)
lam.slot = SlotCirc(Zs=8, H0=0.00021, W0=0.008, is_H0_bore=True)
slotCirc_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.1201928e-06,
        "Ao": 0.135238,
        "Aw": 0.0902657,
        "SW_exp": 1.1201928e-06,
        "H_exp": 0.00021,
    }
)

# H0 < W0/2 external
lam = LamSlot(is_internal=False, Rint=0.0592, Rext=0.075)
lam.slot = SlotCirc(Zs=8, H0=0.00035, W0=0.008, is_H0_bore=True)
slotCirc_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.874104913e-06,
        "Ao": 0.13523817,
        "Aw": 0.090182,
        "SW_exp": 1.874104913e-06,
        "H_exp": 0.00035,
    }
)

###################
# Check Convertion should not change geometry
###################
Conv_test = slotCirc_test[0].copy()
Conv_test["test_obj"] = Conv_test["test_obj"].copy()
Conv_test["test_obj"].slot.convert_to_H0_bore()
slotCirc_test.append(Conv_test)

Conv_test = slotCirc_test[1].copy()
Conv_test["test_obj"] = Conv_test["test_obj"].copy()
Conv_test["test_obj"].slot.convert_to_H0_bore()
slotCirc_test.append(Conv_test)


# python -m pytest ./Tests/Methods/Slot/test_SlotCirc_meth.py
class Test_SlotCirc_meth(object):
    """pytest for SlotCirc methods"""

    @pytest.mark.parametrize("test_dict", slotCirc_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()
        line_dict = test_obj.slot._comp_line_dict()

        assert point_dict["Z1"].imag < 0
        assert point_dict["Z2"].imag > 0
        assert point_dict["ZM"].imag == 0

        # Check schematics
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.W0
        )
        if test_obj.slot.is_H0_bore:
            assert abs(point_dict["ZM"] - test_obj.get_Rbo()) == pytest.approx(
                test_obj.slot.H0
            )
        else:
            assert abs(point_dict["Z2"].real - point_dict["ZM"]) == pytest.approx(
                test_obj.slot.H0
            )
            assert abs(point_dict["Z1"].real - point_dict["ZM"]) == pytest.approx(
                test_obj.slot.H0
            )
        # Two different computation methods
        assert abs(line_dict["M-2"].get_begin() - point_dict["ZM"]) == pytest.approx(0)

    @pytest.mark.parametrize("test_dict", slotCirc_test)
    def test_build_geometry_active(self, test_dict):
        """Check that the active geometry is correctly split"""
        test_obj = test_dict["test_obj"]
        surf_list = test_obj.slot.build_geometry_active(Nrad=3, Ntan=2)

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

    @pytest.mark.parametrize("test_dict", slotCirc_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "For Surface: Return " + str(a) + " expected " + str(b)
        # print(msg)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface(test_obj.slot, Ndisc=400)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotCirc_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SW_exp"]
        msg = "For Surface active: Return " + str(a) + " expected " + str(b)
        # print(msg)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface_active(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotCirc_test)
    def test_comp_surface_opening(self, test_dict):
        """Check that the computation of the opening surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_opening()
        assert result == 0

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface_opening(test_obj.slot, Ndisc=400)
        assert b == 0

    @pytest.mark.parametrize("test_dict", slotCirc_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "For Height: Return " + str(a) + " expected " + str(b)
        # print(msg)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotCirc_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        b = test_dict["Ao"]
        msg = "For Angle Op: Return " + str(a) + " expected " + str(b)
        # print(msg)
        assert abs((a - b) / a - 0) < DELTA, msg
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotCirc_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "For angle active: Return " + str(a) + " expected " + str(b)
        # print(msg)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_get_surface_X(self):
        """Check that the get_surface_X works when stator = false"""
        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotCirc(Zs=6, H0=30e-3, W0=12e-3)
        result = lam.slot.get_surface_active()
        assert result.label == "Rotor_Winding_R0-T0-S0"
        assert len(result.get_lines()) == 3
        assert result.is_inside(result.point_ref)

        result = lam.slot.get_surface_opening()
        assert len(result) == 0

        result = lam.slot.get_surface()
        assert len(result.get_lines()) == 3
        assert result.is_inside(result.point_ref)


if __name__ == "__main__":
    a = Test_SlotCirc_meth()
    # a.test_comp_surface(slotCirc_test[2])
    a.test_build_geometry_active(slotCirc_test[6])
    for ii, test_dict in enumerate(slotCirc_test):
        print("Running test for Slot[" + str(ii) + "]")
        # a.test_check_retro(test_dict)
        # a.test_schematics(test_dict)
        # a.test_comp_surface(test_dict)
        # a.test_comp_surface_active(test_dict)
        # a.test_comp_surface_opening(test_dict)
        # a.test_comp_height(test_dict)
        a.test_build_geometry_active(test_dict)
        # a.test_comp_angle_opening(test_dict)
        # a.test_comp_angle_active_eq(test_dict)
    a.test_get_surface_X()
    print("Done")

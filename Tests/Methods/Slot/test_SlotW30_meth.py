# -*- coding: utf-8 -*-
from tkinter import S
import pytest

from pyleecan.Classes.SlotW30 import SlotW30
from numpy import ndarray, arcsin, exp, pi
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Slot import Slot

# For AlmostEqual
DELTA = 1e-4

slotW30_test = list()

# Outward Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW30(H0=5e-3, H1=20e-3, R1=4.5e-3, R2=4e-3, W0=5e-3, W3=10e-3)
slotW30_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.0003248119953235181,
        "Aw": 0.101630141234976,
        "SW_exp": 0.00029989062007,
        "SO_exp": 2.49213752500043e-05,
        "H_exp": 0.025040196456158986,
    }
)

# Internal Slot
lam = LamSlot(is_internal=True, Rint=0.1325)
lam.slot = SlotW30(H0=5e-3, H1=20e-3, R1=4.5e-3, R2=4e-3, W0=5e-3, W3=10e-3)
slotW30_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.003255087,
        "Aw": 0.163963806301649,
        "SW_exp": 0.0032300767363885,
        "SO_exp": 2.5010416686198074e-05,
        "H_exp": 0.025003125004882887,
    }
)


class Test_SlotW30_meth(object):
    """pytest for SlotW30 methods"""

    @pytest.mark.parametrize("test_dict", slotW30_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()

        # Check width
        assert abs(point_dict["Z1"] - point_dict["Z12"]) == pytest.approx(
            test_obj.slot.W0
        )
        assert abs(point_dict["Z2"] - point_dict["Z11"]) == pytest.approx(
            test_obj.slot.W0
        )
        # Check height
        assert abs(point_dict["Z2"] - point_dict["Z1"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z12"] - point_dict["Z11"]) == pytest.approx(
            test_obj.slot.H0
        )

        assert abs(point_dict["Z7"].real - point_dict["Z6"].real) == pytest.approx(0)

        Z11 = point_dict["Z11"].real
        Z7 = point_dict["Z7"].real
        msg = f"{Z7 -Z11} is different H1 : {test_obj.slot.H1}"
        assert abs((point_dict["Z7"].real - point_dict["Z11"].real)) == pytest.approx(
            test_obj.slot.H1
        ), msg

        # Check radius
        assert abs(point_dict["Z3"] - point_dict["Zc1"]) - test_obj.slot.R1 < 1e-6
        assert abs(point_dict["Z4"] - point_dict["Zc1"]) - test_obj.slot.R1 < 1e-6
        assert abs(point_dict["Z10"] - point_dict["Zc4"]) - test_obj.slot.R1 < 1e-6
        assert abs(point_dict["Z9"] - point_dict["Zc4"]) - test_obj.slot.R1 < 1e-6
        assert abs(point_dict["Z5"] - point_dict["Zc2"]) - test_obj.slot.R2 < 1e-6
        assert abs(point_dict["Z6"] - point_dict["Zc2"]) - test_obj.slot.R2 < 1e-6
        assert abs(point_dict["Z7"] - point_dict["Zc3"]) - test_obj.slot.R2 < 1e-6
        assert abs(point_dict["Z8"] - point_dict["Zc3"]) - test_obj.slot.R2 < 1e-6

        sp = 2 * pi / test_obj.slot.Zs
        a = point_dict["Z9"]
        b = exp(1j * sp) * point_dict["Z4"]
        assert abs(a - b) == pytest.approx(test_obj.slot.W3)

        a = point_dict["Z8"]
        b = exp(1j * sp) * point_dict["Z5"]
        assert abs(a - b) == pytest.approx(test_obj.slot.W3)

    @pytest.mark.parametrize("test_dict", slotW30_test)
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

    @pytest.mark.parametrize("test_dict", slotW30_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW30_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW30_test)
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

    @pytest.mark.parametrize("test_dict", slotW30_test)
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

    @pytest.mark.parametrize("test_dict", slotW30_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()

        if test_obj.is_internal == False:
            assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW30_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_get_surface_X(self):
        """Check that the get_surface_active works when stator = false"""
        lam = LamSlot(is_internal=False, Rint=0.3164, Rext=0.1325, is_stator=False)
        lam.slot = SlotW30(H0=0.3084, H1=20e-3, R1=0.30648, R2=4e-3, W0=5e-3, W3=10e-3)
        result = lam.slot.get_surface_active()
        assert result.label == "Rotor_Winding_R0-T0-S0"
        assert len(result.get_lines()) == 10

        result = lam.slot.get_surface_opening()
        assert len(result) == 1
        assert result[0].label == "Rotor_SlotOpening_R0-T0-S0"
        assert len(result[0].get_lines()) == 4

        # result = lam.slot.get_surface()
        # assert len(result.get_lines()) == 12


if __name__ == "__main__":
    a = Test_SlotW30_meth()
    a.test_get_surface_X()
    for ii, test_dict in enumerate(slotW30_test):
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

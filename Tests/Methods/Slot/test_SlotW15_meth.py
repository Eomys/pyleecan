# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW15 import SlotW15
from numpy import arcsin, exp, pi
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods.Slot.SlotW15 import S15InnerError

# For AlmostEqual
DELTA = 1e-4

slotW15_test = list()
slotW15_wrong_test = list()

# Outward Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW15(H0=5e-3, H1=5e-3, H2=20e-3, R1=4.5e-3, R2=4e-3, W0=5e-3, W3=10e-3)
slotW15_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.1010919e-4,
        "Aw": 0.10268530,
        "SW_exp": 3.8506988e-4,
        "SO_exp": 2.5039310e-05,
        "H_exp": 0.03,
    }
)

# Internal Slot
lam = LamSlot(is_internal=True, Rint=0.1325)
lam.slot = SlotW15(H0=5e-3, H1=5e-3, H2=20e-3, R1=4.5e-3, R2=4e-3, W0=5e-3, W3=10e-3)
slotW15_wrong_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.1010919e-4,
        "Aw": 0.10268530,
        "SW_exp": 3.8506988e-4,
        "SO_exp": 6.60596e-05,
        "H_exp": 0.03,
    }
)


class Test_SlotW15_meth(object):
    """pytest for SlotW15 methods"""

    @pytest.mark.parametrize("test_dict", slotW15_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()

        # Check width
        assert abs(point_dict["Z1"] - point_dict["Z13"]) == pytest.approx(
            test_obj.slot.W0
        )
        assert abs(point_dict["Z2"] - point_dict["Z12"]) == pytest.approx(
            test_obj.slot.W0
        )
        # Check height
        assert abs(
            test_obj.slot.get_Rbo() * exp(1j * 0) - point_dict["Z2"].real
        ) == pytest.approx(test_obj.slot.H0)
        assert abs(
            test_obj.slot.get_Rbo() * exp(1j * 0) - point_dict["Z12"].real
        ) == pytest.approx(test_obj.slot.H0)

        assert abs(point_dict["Z2"].real - point_dict["Zc1"].real) == pytest.approx(
            test_obj.slot.H1
        )
        assert abs(point_dict["Z12"].real - point_dict["Zc4"].real) == pytest.approx(
            test_obj.slot.H1
        )
        assert abs(point_dict["Z7"] - point_dict["Zc1"].real) == pytest.approx(
            test_obj.slot.H2
        )
        assert abs(point_dict["Z7"] - point_dict["Zc4"].real) == pytest.approx(
            test_obj.slot.H2
        )
        # Check radius
        assert abs(point_dict["Z3"] - point_dict["Zc1"]) == pytest.approx(
            test_obj.slot.R1
        )
        assert abs(point_dict["Z4"] - point_dict["Zc1"]) == pytest.approx(
            test_obj.slot.R1
        )
        assert abs(point_dict["Z11"] - point_dict["Zc4"]) == pytest.approx(
            test_obj.slot.R1
        )
        assert abs(point_dict["Z10"] - point_dict["Zc4"]) == pytest.approx(
            test_obj.slot.R1
        )
        assert abs(point_dict["Z5"] - point_dict["Zc2"]) == pytest.approx(
            test_obj.slot.R2
        )
        assert abs(point_dict["Z6"] - point_dict["Zc2"]) == pytest.approx(
            test_obj.slot.R2
        )
        assert abs(point_dict["Z9"] - point_dict["Zc3"]) == pytest.approx(
            test_obj.slot.R2
        )
        assert abs(point_dict["Z8"] - point_dict["Zc3"]) == pytest.approx(
            test_obj.slot.R2
        )

        sp = 2 * pi / test_obj.slot.Zs
        a = point_dict["Z9"]
        b = exp(1j * sp) * point_dict["Z5"]
        assert abs(a - b) == pytest.approx(test_obj.slot.W3)

        a = point_dict["Z10"]
        b = exp(1j * sp) * point_dict["Z4"]
        assert abs(a - b) == pytest.approx(test_obj.slot.W3)

        # check Zc3, Z8 and (0,0) are align
        ya = point_dict["Zc3"].imag
        xa = point_dict["Zc3"].real

        yb = point_dict["Z8"].imag
        xb = point_dict["Z8"].real

        a = (ya - yb) / (xa - xb)

        assert abs(a) == pytest.approx(ya / xa)
        assert abs(a) == pytest.approx(yb / xb)

    @pytest.mark.parametrize("test_dict", slotW15_test)
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

    @pytest.mark.parametrize("test_dict", slotW15_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW15_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW15_test)
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

    @pytest.mark.parametrize("test_dict", slotW15_test)
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

    @pytest.mark.parametrize("test_dict", slotW15_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW15_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW15_wrong_test)
    def test_comp_point_coordinate_error(self, test_dict):
        """Check that the error is well raised"""
        test_obj = test_dict["test_obj"]

        with pytest.raises(S15InnerError) as context:
            test_obj.slot._comp_point_coordinate()

    def test_get_surface_X(self):
        """Check that the get_surface_active works when stator = false"""
        lam = LamSlot(is_internal=False, Rint=0.3164, Rext=0.1325, is_stator=False)
        lam.slot = SlotW15(
            H0=0.1584, H1=5e-3, H2=20e-3, R1=0.15648, R2=4e-3, W0=5e-3, W3=10e-3
        )
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
    a = Test_SlotW15_meth()
    a.test_get_surface_X()
    for ii, test_dict in enumerate(slotW15_test):
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

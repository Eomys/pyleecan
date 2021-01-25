# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW27 import SlotW27
from numpy import ndarray, arcsin, exp
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Segment import Segment
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.Slot.comp_surface_active import comp_surface_active
from pyleecan.Methods.Slot.SlotW27 import S27_W03CheckError

# For AlmostEqual
DELTA = 1e-4

slotW27_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1)
lam.slot = SlotW27(
    Zs=12, H0=10e-3, W0=10e-3, H1=0.03, W1=0.02, H2=0.02, W2=0.03, W3=0.02
)
slotW27_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.3508e-3,
        "Ao": 0.10004,
        "Aw": 0.3853569,
        "SW_exp": 1.25e-3,
        "H_exp": 6.0125e-2,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rint=0.1)
lam.slot = SlotW27(
    Zs=12, H0=10e-3, W0=10e-3, H1=0.03, W1=0.02, H2=0.02, W2=0.03, W3=0.02
)
slotW27_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.34916e-3,
        "Ao": 0.10004,
        "Aw": 0.184928,
        "SW_exp": 1.25e-3,
        "H_exp": 6.0187e-2,
    }
)


@pytest.mark.METHODS
class Test_SlotW27_meth(object):
    """pytest for SlotW27 methods"""

    @pytest.mark.parametrize("test_dict", slotW27_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]
        point_dict = test_obj.slot._comp_point_coordinate()

        # Check width
        assert abs(point_dict["Z1"] - point_dict["Z10"]) == pytest.approx(
            test_obj.slot.W0
        )
        assert abs(point_dict["Z2"] - point_dict["Z9"]) == pytest.approx(
            test_obj.slot.W0
        )
        assert abs(point_dict["Z3"] - point_dict["Z8"]) == pytest.approx(
            test_obj.slot.W1
        )
        assert abs(point_dict["Z4"] - point_dict["Z7"]) == pytest.approx(
            test_obj.slot.W2
        )
        assert abs(point_dict["Z5"] - point_dict["Z6"]) == pytest.approx(
            test_obj.slot.W3
        )
        # Check height
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z2"].real - point_dict["Z4"].real) == pytest.approx(
            test_obj.slot.H1
        )
        assert abs(point_dict["Z3"].real - point_dict["Z4"].real) == pytest.approx(
            test_obj.slot.H1
        )
        assert abs(point_dict["Z4"].real - point_dict["Z5"].real) == pytest.approx(
            test_obj.slot.H2
        )
        assert abs(point_dict["Z10"] - point_dict["Z9"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z9"].real - point_dict["Z7"].real) == pytest.approx(
            test_obj.slot.H1
        )
        assert abs(point_dict["Z8"].real - point_dict["Z7"].real) == pytest.approx(
            test_obj.slot.H1
        )
        assert abs(point_dict["Z7"].real - point_dict["Z6"].real) == pytest.approx(
            test_obj.slot.H2
        )

    @pytest.mark.parametrize("test_dict", slotW27_test)
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

    @pytest.mark.parametrize("test_dict", slotW27_test)
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

    @pytest.mark.parametrize("test_dict", slotW27_test)
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

    @pytest.mark.parametrize("test_dict", slotW27_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        b = test_dict["Ao"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW27_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()
        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_build_geometry(self):
        """Check if the curve_list is correct"""
        test_obj = SlotW27(
            Zs=6, H0=0.05, W0=30e-3, H1=0.125, W1=0.06, H2=0.05, W2=0.09, W3=0.04
        )
        lam = LamSlot(is_internal=False, slot=test_obj, Rint=1)

        Z1 = exp(1j * float(arcsin(30e-3 / 2.0)))
        Z2 = Z1 + 0.05
        Z3 = Z2 + ((0.06 - 30e-3) / 2.0) * 1j
        Z4 = Z3 + 0.125 + ((0.09 - 0.06) / 2.0) * 1j
        Z5 = Z4 + 0.05 + ((0.04 - 0.09) / 2.0) * 1j
        Z6 = Z5.conjugate()
        Z7 = Z4.conjugate()
        Z8 = Z3.conjugate()
        Z9 = Z2.conjugate()
        Z10 = Z1.conjugate()

        [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10] = [
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

        result = test_obj.build_geometry()
        assert len(result) == len(curve_list)
        for i in range(0, len(result)):
            a = result[i].begin
            b = curve_list[i].begin
            assert abs((a - b) / a - 0) < DELTA

            a = result[i].end
            b = curve_list[i].end
            assert abs((a - b) / a - 0) < DELTA

    def test_check(self):
        """Check that the check function is raising error"""

        test_obj = SlotW27(
            Zs=6, H0=0.05, W0=0.01, H1=0.125, W1=0.04, H2=0.05, W2=0.05, W3=0.00015
        )

        with pytest.raises(S27_W03CheckError) as context:
            test_obj.check()

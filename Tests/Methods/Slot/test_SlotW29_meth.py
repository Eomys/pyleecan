# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.Segment import Segment

from pyleecan.Classes.SlotW29 import SlotW29
from numpy import ndarray, arcsin, exp
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Slot import Slot

from pyleecan.Functions.load import load
from os.path import join
from pyleecan.definitions import DATA_DIR

# For AlmostEqual
DELTA = 1e-4

slotW29_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW29(H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=20e-3)
slotW29_test.append(
    {
        "test_obj": lam,
        "S_exp": 6.340874e-4,
        "Ao": 0.10004,
        "Aw": 0.174118,
        "SO_exp": 3.408746e-05,
        "SW_exp": 6e-4,
        "H_exp": 3.26359e-2,
    }
)

# External Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW29(H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=20e-3)
slotW29_test.append(
    {
        "test_obj": lam,
        "S_exp": 6.31912e-4,
        "Ao": 0.10004,
        "Aw": 0.133185,
        "SO_exp": 3.191253e-05,
        "SW_exp": 6e-4,
        "H_exp": 3.2667e-2,
    }
)

# Internal Slot but W1>W2
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW29(H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=20e-3, W2=14e-3)
slotW29_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.630874e-4,
        "Ao": 0.10004,
        "Aw": 0.1218831,
        "SO_exp": 4.3087461745e-05,
        "SW_exp": 0.00042,
        "H_exp": 3.26359e-2,
    }
)

# Internal Slot with wedge_type = 1
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW29(
    H0=1e-3,
    H1=1.5e-3,
    H2=30e-3,
    W0=12e-3,
    W1=14e-3,
    W2=20e-3,
    wedge_type=1,
)
slotW29_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.00063408746174,
        "Ao": 0.10004,
        "Aw": 0.17411883,
        "SO_exp": 1.3087461745489922e-05,
        "SW_exp": 6e-4,
        "H_exp": 0.0326359,
        "SWedge_exp": 2.1e-05,
    }
)

# Outward Slot with wedge_type = 1
lam = LamSlot(
    is_internal=False,
    Rint=0.1325,
)
lam.slot = SlotW29(
    H0=1e-3,
    H1=1.5e-3,
    H2=30e-3,
    W0=12e-3,
    W1=14e-3,
    W2=20e-3,
    wedge_type=1,
)
slotW29_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.000631912538,
        "Ao": 0.10004,
        "Aw": 0.133185,
        "SO_exp": 1.0912538254510078e-05,
        "SW_exp": 6e-4,
        "H_exp": 3.2667e-2,
        "SWedge_exp": 2.1e-05,
    }
)


class Test_SlotW29_meth(object):
    """pytest for SlotW29 methods"""

    @pytest.mark.parametrize("test_dict", slotW29_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"].copy()
        point_dict = test_obj.slot._comp_point_coordinate()

        # Check width
        assert abs(point_dict["Z1"] - point_dict["Z12"]) == pytest.approx(
            test_obj.slot.W0
        )
        assert abs(point_dict["Z2"] - point_dict["Z11"]) == pytest.approx(
            test_obj.slot.W0
        )
        assert abs(point_dict["Z3"] - point_dict["Z10"]) == pytest.approx(
            test_obj.slot.W1
        )
        assert abs(point_dict["Z4"] - point_dict["Z9"]) == pytest.approx(
            test_obj.slot.W1
        )
        assert abs(point_dict["Z5"] - point_dict["Z8"]) == pytest.approx(
            test_obj.slot.W2
        )
        assert abs(point_dict["Z6"] - point_dict["Z7"]) == pytest.approx(
            test_obj.slot.W2
        )
        # Check height
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z3"] - point_dict["Z4"]) == pytest.approx(
            test_obj.slot.H1
        )
        assert abs(point_dict["Z5"] - point_dict["Z6"]) == pytest.approx(
            test_obj.slot.H2
        )
        assert abs(point_dict["Z12"] - point_dict["Z11"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z10"] - point_dict["Z9"]) == pytest.approx(
            test_obj.slot.H1
        )
        assert abs(point_dict["Z7"] - point_dict["Z8"]) == pytest.approx(
            test_obj.slot.H2
        )

    @pytest.mark.parametrize("test_dict", slotW29_test)
    def test_build_geometry_active(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"].copy()
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

    @pytest.mark.parametrize("test_dict", slotW29_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"].copy()
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW29_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"].copy()
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface_active(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW29_test)
    def test_comp_surface_opening(self, test_dict):
        """Check that the computation of the opening surface is correct"""
        test_obj = test_dict["test_obj"].copy()
        result = test_obj.slot.comp_surface_opening()

        a = result
        b = test_dict["SO_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_surface_opening(test_obj.slot, Ndisc=400)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW29_test)
    def test_comp_surface_wedge(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"].copy()
        slot = test_obj.slot

        if test_obj.slot.wedge_type == 1:
            M400 = load(join(DATA_DIR, "Material", "M400-50A.json"))
            slot.wedge_mat = M400
            result = test_obj.slot.comp_surface_wedge()

            a = result
            b = test_dict["SWedge_exp"]
            msg = "Return " + str(a) + " expected " + str(b)
            assert abs((a - b) / a - 0) < DELTA, msg

            # Check that the analytical method returns the same result as the numerical one
            b = Slot.comp_surface_wedges(test_obj.slot)
            msg = "Return " + str(a) + " expected " + str(b)
            assert abs((a - b) / a - 0) < 1e-5, msg

        if test_obj.slot.wedge_type == 0:
            M400 = load(join(DATA_DIR, "Material", "M400-50A.json"))
            slot.wedge_mat = M400
            result = test_obj.slot.comp_surface_wedge()

            a = result
            b = test_dict["SO_exp"]
            msg = "Return " + str(a) + " expected " + str(b)
            assert abs((a - b) / a - 0) < DELTA, msg

            # Check that the analytical method returns the same result as the numerical one
            b = Slot.comp_surface_wedges(test_obj.slot)
            msg = "Return " + str(a) + " expected " + str(b)
            assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW29_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct"""
        test_obj = test_dict["test_obj"].copy()
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW29_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"].copy()
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW29_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"].copy()
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_build_geometry(self):
        """check that curve_list is correct"""
        test_obj = LamSlot(is_internal=False, Rint=1)
        test_obj.slot = SlotW29(W0=0.2, H0=0.1, W1=0.4, H1=0.1, H2=0.6, W2=0.6)

        # Rbo=1
        Z1 = exp(1j * float(arcsin(0.1)))

        Z2 = Z1 + 0.1
        Z3 = Z1 + 0.1 + 0.1j
        Z4 = Z1 + 0.2 + 0.1j
        Z5 = Z1 + 0.2 + 0.2j
        Z6 = Z1 + 0.8 + 0.2j
        Z7 = Z1 + 0.8 - 0.4j
        Z8 = Z1 + 0.2 - 0.4j
        Z9 = Z1 + 0.2 - 0.3j
        Z10 = Z1 + 0.1 - 0.3j
        Z11 = Z1 + 0.1 - 0.2j
        Z12 = Z1 - 0.2j

        [Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12] = [
            Z12,
            Z11,
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
        curve_list.append(Segment(Z10, Z11))
        curve_list.append(Segment(Z11, Z12))

        result = test_obj.slot.build_geometry()
        assert len(result) == len(curve_list)
        for i in range(0, len(result)):
            a = result[i].begin
            b = curve_list[i].begin
            assert abs((a - b) / a - 0) < DELTA, (
                "Wrong build_geo (for begin point "
                + str(i)
                + " returned "
                + str(a)
                + ", expected "
                + str(b)
                + ")"
            )

            a = result[i].end
            b = curve_list[i].end
            assert abs((a - b) / a - 0) < DELTA, (
                "Wrong build_geo (for end point "
                + str(i)
                + " returned "
                + str(a)
                + ", expected "
                + str(b)
                + ")"
            )

    def test_get_surface_X(self):
        """Check that the get_surface_X works when stator = false"""
        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW29(H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=20e-3)
        result = lam.slot.get_surface_active()
        assert result.label == "Rotor_Winding_R0-T0-S0"
        assert len(result.get_lines()) == 6
        assert result.is_inside(result.point_ref)

        result = lam.slot.get_surface_opening()
        assert len(result) == 1
        assert result[0].label == "Rotor_SlotOpening_R0-T0-S0"
        assert len(result[0].get_lines()) == 8
        assert result[0].is_inside(result[0].point_ref)

        result = lam.slot.get_surface()
        assert len(result.get_lines()) == 12
        assert result.is_inside(result.point_ref)


if __name__ == "__main__":
    a = Test_SlotW29_meth()
    for ii, test_dict in enumerate(slotW29_test):
        print("Running test for Slot[" + str(ii) + "]")
        a.test_schematics(test_dict)
        a.test_comp_surface(test_dict)
        a.test_comp_surface_active(test_dict)
        a.test_comp_surface_opening(test_dict)
        a.test_comp_height(test_dict)
        a.test_build_geometry_active(test_dict)
        a.test_comp_angle_opening(test_dict)
        a.test_comp_angle_active_eq(test_dict)
        a.test_comp_surface_wedge(test_dict)
        print("Done")

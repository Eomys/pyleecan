# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW14 import SlotW14
from numpy import arcsin, pi
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods.Slot.SlotW14 import S14_Rbo1CheckError

from pyleecan.Functions.load import load
from os.path import join
from pyleecan.definitions import DATA_DIR

# For AlmostEqual
DELTA = 1e-4

slotW14_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW14(
    H0=5e-3,
    H1=5e-3,
    H3=25e-3,
    W0=5e-3,
    W3=10e-3,
    H1_is_rad=False,
)
slotW14_test.append(
    {
        "test_obj": lam,
        "S_exp": 2.9443933e-4,
        "Aw": 0.08445503,
        "SW_exp": 2.28378e-4,
        "SO_exp": 6.60596e-05,
        "H_exp": 0.03486507,
    }
)

# Outward Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW14(
    H0=5e-3,
    H1=5e-3,
    H3=25e-3,
    W0=5e-3,
    W3=10e-3,
    wedge_type=0,
    H1_is_rad=False,
)
slotW14_test.append(
    {
        "test_obj": lam,
        "S_exp": 5.0790294e-4,
        "Aw": 0.108324,
        "SW_exp": 4.332517e-4,
        "SO_exp": 7.4651234e-05,
        "H_exp": 0.03572334,
    }
)

# H1 rad
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW14(
    H0=5e-3,
    H1=0.01,
    H3=25e-3,
    W0=5e-3,
    W3=10e-3,
    wedge_type=0,
    H1_is_rad=True,
)
slotW14_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.00043629885867586983,
        "Aw": 0.10630161,
        "SW_exp": 0.0004109465804555589,
        "SO_exp": 2.5352278220310933e-05,
        "H_exp": 0.0307307210,
    }
)

lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW14(
    H0=5e-3,
    H1=0,
    H3=25e-3,
    W0=5e-3,
    W3=10e-3,
    wedge_type=0,
    H1_is_rad=True,
)
slotW14_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.00043566418141197945,
        "Aw": 0.10628246802,
        "SW_exp": 0.0004107428061619,
        "SO_exp": 2.4921375250004305e-05,
        "H_exp": 0.0306850757,
    }
)

lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW14(
    H0=5e-3,
    H1=pi / 4,
    H3=25e-3,
    W0=5e-3,
    W3=10e-3,
    wedge_type=1,
    H1_is_rad=True,
)
slotW14_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.0005073025572861639,
        "Aw": 0.1083080950696,
        "SW_exp": 0.00043306999862850,
        "SO_exp": 2.49213752500043e-05,
        "H_exp": 0.03568270305258159,
        "SWedge_exp": 4.931118340765717e-05,
    }
)


lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW14(
    H0=5e-3,
    H1=5e-3,
    H3=25e-3,
    W0=5e-3,
    W3=10e-3,
    wedge_type=1,
    H1_is_rad=False,
)
slotW14_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.00029443833868045136,
        "Aw": 0.08445503,
        "SW_exp": 2.28378e-4,
        "SO_exp": 2.5078624749995704e-05,
        "H_exp": 0.03486507,
        "SWedge_exp": 4.098099249328862e-05,
    }
)

# Outward Slot
lam = LamSlot(
    is_internal=False,
    Rint=0.1325,
)
lam.slot = SlotW14(
    H0=5e-3,
    H1=5e-3,
    H3=25e-3,
    W0=5e-3,
    W3=10e-3,
    wedge_type=1,
    H1_is_rad=False,
)
slotW14_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.0005079029472254,
        "Aw": 0.108324,
        "SW_exp": 4.332517e-4,
        "SO_exp": 2.49213752500043e-05,
        "H_exp": 0.03572334,
        "SWedge_exp": 4.972985884588103e-05,
    }
)


class Test_SlotW14_meth(object):
    """pytest for SlotW14 methods"""

    @pytest.mark.parametrize("test_dict", slotW14_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"].copy()
        point_dict = test_obj.slot._comp_point_coordinate()

        # Check width
        assert abs(point_dict["Z1"] - point_dict["Z9"]) == pytest.approx(
            test_obj.slot.W0
        )
        assert abs(point_dict["Z2"] - point_dict["Z8"]) == pytest.approx(
            test_obj.slot.W0
        )
        # Check height
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.H0
        )

        assert abs(point_dict["Z2"].real - point_dict["Z3"].real) == pytest.approx(
            test_obj.slot.get_H1()
        )
        assert abs(point_dict["Z3"] - point_dict["Z4"]) == pytest.approx(
            test_obj.slot.H3
        )
        assert abs(point_dict["Z9"] - point_dict["Z8"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z8"].real - point_dict["Z7"].real) == pytest.approx(
            test_obj.slot.get_H1()
        )
        assert abs(point_dict["Z7"] - point_dict["Z6"]) == pytest.approx(
            test_obj.slot.H3
        )

    @pytest.mark.parametrize("test_dict", slotW14_test)
    def test_build_geometry_active(self, test_dict):
        """Check that the active geometry is correctly split"""
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

    @pytest.mark.parametrize("test_dict", slotW14_test)
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
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW14_test)
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

    @pytest.mark.parametrize("test_dict", slotW14_test)
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
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW14_test)
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

    @pytest.mark.parametrize("test_dict", slotW14_test)
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
        assert abs((a - b) / a - 0) < 1e-5, msg

    @pytest.mark.parametrize("test_dict", slotW14_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"].copy()
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW14_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"].copy()
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_check(self):
        """Check that the check methods is correctly working"""
        lam = LamSlot(is_internal=False, Rint=0.1325)
        lam.slot = SlotW14(H0=5e-3, H1=5e-3, H3=25e-3, W0=5e-3, W3=10)

        with pytest.raises(S14_Rbo1CheckError) as context:
            lam.slot.check()

    def test_get_H1(self):
        """check conversion of H1"""

        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW14(
            H0=1e-3,
            H1=pi / 4,
            H1_is_rad=True,
            W0=12e-3,
            W3=10e-3,
        )

        a = lam.slot.get_H1()
        b = 0.0004373180612594603
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW14(
            H0=1e-3,
            H1=0,
            H1_is_rad=True,
            W0=12e-3,
            W3=10e-3,
        )

        a = lam.slot.get_H1()
        b = 0
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b)) < DELTA, msg


if __name__ == "__main__":
    a = Test_SlotW14_meth()
    for ii, test_dict in enumerate(slotW14_test):
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
        a.test_get_H1()
        print("Done")

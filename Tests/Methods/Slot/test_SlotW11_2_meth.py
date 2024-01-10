# -*- coding: utf-8 -*-
import pytest

from pyleecan.Classes.SlotW11_2 import SlotW11_2
from numpy import arcsin, exp, pi
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods.Slot.SlotW11_2 import S11_2_H1rCheckError, S11_2_R1CheckError


# For AlmostEqual
DELTA = 1e-6
SlotW11_2_test = list()

# Internal Slot / H1m / Cst slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW11_2(
    H0=1e-3,
    H1=1.5e-3,
    H1_is_rad=False,
    H2=30e-3,
    W0=12e-3,
    W1=14e-3,
    W2=12e-3,
    is_cstt_tooth=False,
    R1=5e-3,
)
SlotW11_2_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.0004068558,
        "Aw": 0.108611951225,
        "SO_exp": 3.258746174548993e-05,
        "SW_exp": 0.090597018,
        "H_exp": 0.03263591876947885,
    }
)

# Internal Slot / H1m / Cst slot/ R1*2 == W2 (round top)
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW11_2(
    H0=1e-3,
    H1=1.5e-3,
    H1_is_rad=False,
    H2=30e-3,
    W0=12e-3,
    W1=14e-3,
    W2=12e-3,
    is_cstt_tooth=False,
    R1=6e-3,
)
SlotW11_2_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.0004011338271489,
        "Aw": 0.10695143,
        "SO_exp": 3.258746174548993e-05,
        "SW_exp": 0.09059701805,
        "H_exp": 0.03263591876947885,
    }
)

# External Slot  / H1m / Cst slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW11_2(
    H0=1e-3,
    H1=1.5e-3,
    H1_is_rad=False,
    H2=30e-3,
    W0=12e-3,
    W1=14e-3,
    W2=12e-3,
    is_cstt_tooth=False,
    R1=5e-3,
)
SlotW11_2_test.append(
    {
        "test_obj": lam,
        "S_exp": 4.046824e-4,
        "Aw": 0.083244699,
        "SO_exp": 3.0412538254510085e-05,
        "SW_exp": 0.0905970180,
        "H_exp": 0.032367202959,
    }
)

# External Slot /Rad H1
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW11_2(
    H0=1e-3,
    H1=pi / 4,
    H1_is_rad=True,
    H2=30e-3,
    W0=12e-3,
    W1=14e-3,
    W2=12e-3,
    is_cstt_tooth=False,
    R1=5e-3,
)
SlotW11_2_test.append(
    {
        "test_obj": lam,
        "S_exp": 3.981824e-4,
        "Aw": 0.08352335186,
        "SO_exp": 2.3912538254510076e-05,
        "SW_exp": 0.090597018056,
        "H_exp": 0.03186721292,
    }
)

# Internal Slot / H1m  / Cst tooth
lam_CT = LamSlot(is_internal=True, Rext=0.1325)
lam_CT.slot = SlotW11_2(
    H0=1e-3,
    H1=1.5e-3,
    H1_is_rad=False,
    H2=30e-3,
    W0=12e-3,
    W1=None,
    W2=None,
    W3=10e-3,
    is_cstt_tooth=True,
    R1=1e-3,
)
Lam_CT_surf = 0.000333289388
SlotW11_2_test.append(
    {
        "test_obj": lam_CT,
        "S_exp": Lam_CT_surf,
        "Aw": 0.0875461964,
        "SO_exp": 3.16119853732e-05,
        "SW_exp": 0.0905970180566,
        "H_exp": 0.03263591,
    }
)

# External Slot / H1 rad  / Cst tooth
lam_CT = LamSlot(is_internal=False, Rint=0.1325)
lam_CT.slot = SlotW11_2(
    Zs=12,
    H0=20e-3,
    W0=30e-3,
    H1=pi / 4,
    H1_is_rad=True,
    H2=80e-3,
    W1=None,
    W2=None,
    W3=20e-3,
    is_cstt_tooth=True,
    R1=1e-3,
)


Lam_CT_surf = 0.0082260530
SlotW11_2_test.append(
    {
        "test_obj": lam_CT,
        "S_exp": Lam_CT_surf,
        "Aw": 0.422066929,
        "SO_exp": 0.0011572004684,
        "SW_exp": 0.22690152563,
        "H_exp": 0.116852241277,
    }
)


class Test_SlotW11_2_meth(object):
    """pytest for SlotW11_2 methods"""

    @pytest.mark.parametrize("test_dict", SlotW11_2_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"].copy()
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
        assert abs(point_dict["Z4c"] - point_dict["Z7c"]) == pytest.approx(
            test_obj.slot.W2
        )
        # Check height
        assert abs(point_dict["Z1"] - point_dict["Z2"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z2"].real - point_dict["Z3"].real) == pytest.approx(
            test_obj.slot.get_H1()
        )
        assert abs(point_dict["Z3"].real - point_dict["Z4c"].real) == pytest.approx(
            test_obj.slot.H2 - test_obj.slot.R1
        )
        assert abs(point_dict["Z3"].real - point_dict["Z5"].real) == pytest.approx(
            test_obj.slot.H2
        )
        assert abs(point_dict["Z10"] - point_dict["Z9"]) == pytest.approx(
            test_obj.slot.H0
        )
        assert abs(point_dict["Z9"].real - point_dict["Z8"].real) == pytest.approx(
            test_obj.slot.get_H1()
        )
        assert abs(point_dict["Z8"].real - point_dict["Z7c"].real) == pytest.approx(
            test_obj.slot.H2 - test_obj.slot.R1
        )
        assert abs(point_dict["Z8"].real - point_dict["Z6"].real) == pytest.approx(
            test_obj.slot.H2
        )
        if test_obj.slot.is_cstt_tooth:
            sp = 2 * pi / test_obj.slot.Zs

            a = point_dict["Z3"]
            b = exp(-1j * sp) * point_dict["Z8"]
            msg = "Return " + str(abs((a - b))) + " expected " + str(test_obj.slot.W3)
            assert (abs((a - b)) - test_obj.slot.W3) < DELTA, msg

            a = point_dict["Z4"]
            b = exp(-1j * sp) * point_dict["Z7"]
            msg = "Return " + str(abs((a - b))) + " expected " + str(test_obj.slot.W3)
            assert (abs((a - b)) - test_obj.slot.W3) < DELTA, msg

    @pytest.mark.parametrize("test_dict", SlotW11_2_test)
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

    @pytest.mark.parametrize("test_dict", SlotW11_2_test)
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

    @pytest.mark.parametrize("test_dict", SlotW11_2_test)
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

    @pytest.mark.parametrize("test_dict", SlotW11_2_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"].copy()
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * arcsin(test_obj.slot.W0 / (2 * 0.1325))
        # Check that the analytical method returns the same result as the numerical one
        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", SlotW11_2_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"].copy()
        result = Slot.comp_angle_opening(test_obj.slot)

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", SlotW11_2_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"].copy()
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", SlotW11_2_test)
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

    def test_SlotW11_2_check(self):
        """Check if the error S11_H1rCheckError is correctly raised in the check method"""
        lam = LamSlot(is_internal=False, Rint=0.1325)
        lam.slot = SlotW11_2(
            H0=1e-3,
            H1=3,
            H2=30e-3,
            W0=12e-3,
            W1=14e-3,
            W2=12e-3,
            R1=5e-3,
            H1_is_rad=True,
        )

        with pytest.raises(S11_2_H1rCheckError) as context:
            lam.slot.check()

        lam.slot.R1 = 0
        with pytest.raises(S11_2_R1CheckError) as context:
            lam.slot.check()

    def test_comp_W(self):
        """Check that the computations of the Ws are right"""
        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW11_2(
            H0=1e-3,
            H1=1.5e-3,
            H1_is_rad=False,
            H2=30e-3,
            W0=12e-3,
            W3=10e-3,
            R1=1e-3,
            is_cstt_tooth=True,
        )
        lam.slot._comp_W()
        assert lam.slot.W1 == 0.012699364837066218
        assert lam.slot.W2 == 0.007610745213606121

        lam = LamSlot(is_internal=False, Rext=0.1325, is_stator=False, Rint=0.154)
        lam.slot = SlotW11_2(
            H0=1e-3,
            H1=1.5e-3,
            H1_is_rad=False,
            H2=30e-3,
            W0=12e-3,
            W3=10e-3,
            R1=1e-3,
            is_cstt_tooth=True,
        )
        lam.slot._comp_W()
        assert lam.slot.W1 == 0.017332085329084986
        assert lam.slot.W2 == 0.022399646484284684

    def test_comp_surface_change_W3(self):
        # Check surface, change, W3, check surface again
        test_obj = lam_CT.copy()

        assert test_obj.slot.W1 is None
        assert test_obj.slot.W2 is None
        result = test_obj.slot.comp_surface()
        assert test_obj.slot.W1 is not None
        assert test_obj.slot.W2 is not None

        a = result
        b = Lam_CT_surf
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # change W3
        W2 = test_obj.slot.W2
        W1 = test_obj.slot.W1
        test_obj.slot.W3 = test_obj.slot.W3 / 2
        assert test_obj.slot.W2 != W2
        assert test_obj.slot.W1 != W1

        result = test_obj.slot.comp_surface()

        # Check if methods constant thooth change surface
        c = result
        b = Slot.comp_surface(test_obj.slot)
        msg = "Error if " + str(c) + " and " + str(b) + "are equal"
        assert Lam_CT_surf != b, msg

        # Check that the analytical method returns the same result as the numerical one
        msg = "Return " + str(c) + " expected " + str(b)
        assert abs((c - b) / c - 0) < DELTA, msg

    def test_get_H1(self):
        """check conversion of H1"""

        lam = LamSlot(is_internal=True, Rext=0.1325, is_stator=False)
        lam.slot = SlotW11_2(
            H0=1e-3,
            H1=pi / 4,
            H1_is_rad=True,
            H2=30e-3,
            W0=12e-3,
            W3=10e-3,
            R1=1e-3,
            is_cstt_tooth=True,
        )

        a = lam.slot.get_H1()
        b = 0.0005362698781809228
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        lam = LamSlot(is_internal=False, Rext=0.1325, is_stator=False, Rint=0.154)
        lam.slot = SlotW11_2(
            H0=1e-3,
            H1=pi / 4,
            H1_is_rad=True,
            H2=30e-3,
            W0=12e-3,
            W1=20e-3,
            W2=10e-3,
            R1=1e-3,
            is_cstt_tooth=False,
        )

        a = lam.slot.get_H1()
        b = 0.004
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg


if __name__ == "__main__":
    a = Test_SlotW11_2_meth()
    for ii, test_dict in enumerate(SlotW11_2_test):
        print("Running test for Slot[" + str(ii) + "]")
        a.test_schematics(test_dict)
        a.test_comp_surface(test_dict)
        a.test_comp_surface_opening(test_dict)
        a.test_comp_height(test_dict)
        a.test_build_geometry_active(test_dict)
        a.test_comp_angle_opening(test_dict)
        a.test_comp_angle_active_eq(test_dict)
        a.test_comp_surface_change_W3()
    print("Done")

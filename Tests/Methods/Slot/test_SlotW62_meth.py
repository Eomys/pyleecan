# -*- coding: utf-8 -*-
import pytest


from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotW62 import SlotW62
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods.Slot.SlotW62 import (
    S62_InnerCheckError,
    S62_WindError,
    S62_WindHError,
    S62_W0Error,
    S62_W1Error,
    S62_W2Error,
    S62_H1Error,
    S62_H2Error,
)


# For AlmostEqual
DELTA = 1e-5

slotW62_test = list()


# Internal Slot
lam = LamSlot(
    Rint=0.135,
    Rext=0.3,
    is_internal=True,
    is_stator=False,
)
lam.slot = SlotW62(
    Zs=12,
    H0=70e-3,
    W0=50e-3,
    H1=30e-3,
    W1=120e-3,
    W2=15e-3,
    H2=40e-3,
    W3=10e-3,
    H3=12e-3,
)
slotW62_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.0060191044069,
        "Aw": 0.13918306,
        "SW_exp": 0.0012,
        "H_exp": 0.104456536,
        "Ao": 0.120882934017,
    }
)


# W3 and H3 = 0
lam = LamSlot(
    Rint=0.135,
    Rext=0.3,
    is_internal=True,
    is_stator=False,
)
lam.slot = SlotW62(
    Zs=12,
    H0=70e-3,
    W0=50e-3,
    H1=30e-3,
    W1=120e-3,
    W2=15e-3,
    H2=40e-3,
    W3=0,
    H3=0,
)
slotW62_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.0060191044069,
        "Aw": 0.13918306,
        "SW_exp": 0.0012,
        "H_exp": 0.104456536,
        "Ao": 0.120882934017,
    }
)


# H0 = H2 + H3
lam = LamSlot(
    Rint=0.135,
    Rext=0.3,
    is_internal=True,
    is_stator=False,
)
lam.slot = SlotW62(
    Zs=12,
    H0=70e-3,
    W0=50e-3,
    H1=30e-3,
    W1=120e-3,
    W2=15e-3,
    H2=40e-3,
    W3=20e-3,
    H3=30e-3,
)
slotW62_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.0060191044069,
        "Aw": 0.13918306,
        "SW_exp": 0.0012,
        "H_exp": 0.104456536,
        "Ao": 0.120882934017,
    }
)


# W1 < W0
lam = LamSlot(
    Rint=0.135,
    Rext=0.3,
    is_internal=True,
    is_stator=False,
)
lam.slot = SlotW62(
    Zs=12,
    H0=70e-3,
    W0=50e-3,
    H1=30e-3,
    W1=40e-3,
    W2=15e-3,
    H2=40e-3,
    W3=20e-3,
    H3=30e-3,
)
slotW62_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.008330411950,
        "Aw": 0.13581162,
        "SW_exp": 0.0012,
        "H_exp": 0.099105794,
        "Ao": 0.39016647,
    }
)

# W1 = W0
lam = LamSlot(
    Rint=0.135,
    Rext=0.3,
    is_internal=True,
    is_stator=False,
)
lam.slot = SlotW62(
    Zs=12,
    H0=70e-3,
    W0=50e-3,
    H1=30e-3,
    W1=50e-3,
    W2=15e-3,
    H2=40e-3,
    W3=20e-3,
    H3=30e-3,
)
slotW62_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.00805273,
        "Aw": 0.13604142,
        "SW_exp": 0.0012,
        "H_exp": 0.099478938,
        "Ao": 0.3567386,
    }
)


class Test_SlotW62_meth(object):
    """pytest for SlotW62 methods"""

    @pytest.mark.parametrize("test_dict", slotW62_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        b = Slot.comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW62_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        if result != 0:
            a = result
            b = test_dict["SW_exp"]
            msg = "Return " + str(a) + " expected " + str(b)
            assert abs((a - b) / a - 0) < DELTA, msg
        else:
            a = result
            b = test_dict["SW_exp"]
            msg = "Return " + str(a) + " expected " + str(b)
            assert a == b, msg

    @pytest.mark.parametrize("test_dict", slotW62_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        b = Slot.comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW62_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect"""
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()

        b = test_dict["Ao"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW62_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        if result != 0:
            a = result
            b = test_dict["Aw"]
            msg = "Return " + str(a) + " expected " + str(b)
            assert abs((a - b) / a - 0) < DELTA, msg
        else:
            a = result
            b = test_dict["Aw"]
            msg = "Return " + str(a) + " expected " + str(b)
            assert a == b, msg

    @pytest.mark.parametrize("test_dict", slotW62_test)
    def test_build_geometry_active_is_stator_true(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.build_geometry_active(Nrad=1, Ntan=2)
        a = result
        assert "Rotor_Winding_R0-T0-S0" == a[0].label

    @pytest.mark.parametrize("test_dict", slotW62_test)
    def test_build_geometry_active_error(self, test_dict):
        """Check that the ERROR is raised"""

        test_obj = test_dict["test_obj"]

        with pytest.raises(S62_WindError) as context:
            test_obj.slot.build_geometry_active(Nrad=0, Ntan=0)

    @pytest.mark.parametrize("test_dict", slotW62_test)
    def test_check_Inner_error(self, test_dict):
        """Check that the ERROR is raised"""

        test_obj = test_dict["test_obj"].copy()

        test_obj.is_internal = False
        with pytest.raises(S62_InnerCheckError) as context:
            test_obj.slot.check()

    def test_SlotW62_check_S62_W0Error(self):
        """Check if the error S62_W0Error is correctly raised in the check method"""
        lam = LamSlot(
            Rint=0.135,
            Rext=0.3,
            is_internal=True,
            is_stator=False,
        )
        lam.slot = SlotW62(
            Zs=12,
            H0=70e-3,
            W0=0,
            H1=30e-3,
            W1=120e-3,
            W2=15e-3,
            H2=40e-3,
            W3=10e-3,
            H3=12e-3,
        )

        with pytest.raises(S62_W0Error) as context:
            lam.slot.check()

    def test_SlotW62_check_S62_W1Error(self):
        """Check if the error S62_W1Error is correctly raised in the check method"""
        lam = LamSlot(
            Rint=0.135,
            Rext=0.3,
            is_internal=True,
            is_stator=False,
        )
        lam.slot = SlotW62(
            Zs=12,
            H0=70e-3,
            W0=70e-3,
            H1=30e-3,
            W1=0,
            W2=15e-3,
            H2=40e-3,
            W3=10e-3,
            H3=12e-3,
        )

        with pytest.raises(S62_W1Error) as context:
            lam.slot.check()

    def test_SlotW62_check_S62_W2Error(self):
        """Check if the error S62_W2Error is correctly raised in the check method"""
        lam = LamSlot(
            Rint=0.135,
            Rext=0.3,
            is_internal=True,
            is_stator=False,
        )
        lam.slot = SlotW62(
            Zs=12,
            H0=70e-3,
            W0=70e-3,
            H1=30e-3,
            W1=120e-3,
            W2=0,
            H2=40e-3,
            W3=10e-3,
            H3=12e-3,
        )

        with pytest.raises(S62_W2Error) as context:
            lam.slot.check()

    def test_SlotW62_check_S62_H1Error(self):
        """Check if the error S62_H1Error is correctly raised in the check method"""
        lam = LamSlot(
            Rint=0.135,
            Rext=0.3,
            is_internal=True,
            is_stator=False,
        )
        lam.slot = SlotW62(
            Zs=12,
            H0=70e-3,
            W0=70e-3,
            H1=0,
            W1=120e-3,
            W2=15e-3,
            H2=40e-3,
            W3=10e-3,
            H3=12e-3,
        )

        with pytest.raises(S62_H1Error) as context:
            lam.slot.check()

    def test_SlotW62_check_S62_H2Error(self):
        """Check if the error S62_H2Error is correctly raised in the check method"""
        lam = LamSlot(
            Rint=0.135,
            Rext=0.3,
            is_internal=True,
            is_stator=False,
        )
        lam.slot = SlotW62(
            Zs=12,
            H0=70e-3,
            W0=70e-3,
            H1=30e-3,
            W1=120e-3,
            W2=15e-3,
            H2=0,
            W3=10e-3,
            H3=12e-3,
        )

        with pytest.raises(S62_H2Error) as context:
            lam.slot.check()

    def test_SlotW62_check_S62_WindHError(self):
        """Check if the error S62_WindHError is correctly raised in the check method"""
        lam = LamSlot(
            Rint=0.135,
            Rext=0.3,
            is_internal=True,
            is_stator=False,
        )
        lam.slot = SlotW62(
            Zs=12,
            H0=20e-3,
            W0=70e-3,
            H1=30e-3,
            W1=120e-3,
            W2=15e-3,
            H2=40e-3,
            W3=10e-3,
            H3=12e-3,
        )

        with pytest.raises(S62_WindHError) as context:
            lam.slot.check()


if __name__ == "__main__":
    a = Test_SlotW62_meth()
    lam.slot.plot()
    for test_dict in slotW62_test:
        a.test_comp_height(test_dict)
        a.test_comp_angle_opening(test_dict)
    print("Done")

# -*- coding: utf-8 -*-
import pytest


from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotW63 import SlotW63
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods.Slot.SlotW63 import (
    S63_InnerCheckError,
    S63_WindError,
    S63_W0CheckError,
    S63_H0CheckError,
)


# For AlmostEqual
DELTA = 1e-5

slotW63_test = list()


# Internal Slot
lam = LamSlot(
    Rint=0.135,
    Rext=0.3,
    is_internal=True,
    is_stator=False,
)
lam.slot = SlotW63(
    Zs=12,
    H0=30e-3,
    W0=30e-3,
    H1=0.78539,
    W1=80e-3,
    H2=40e-3,
    W2=15e-3,
)

slotW63_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.00699400,
        "Aw": 0.2880486802351,
        "SW_exp": 0.0012,
        "H_exp": 0.09361730554,
        "Ao": 0.256135596778,
    }
)

# H1=0
lam = LamSlot(
    Rint=0.135,
    Rext=0.3,
    is_internal=True,
    is_stator=False,
)
lam.slot = SlotW63(
    Zs=12,
    H0=30e-3,
    W0=30e-3,
    H1=0,
    W1=80e-3,
    H2=40e-3,
    W2=15e-3,
)

slotW63_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.0059996,
        "Aw": 0.325341262,
        "SW_exp": 0.0012,
        "H_exp": 0.0765421,
        "Ao": 0.256135596778,
    }
)

# W2=0
lam = LamSlot(
    Rint=0.135,
    Rext=0.3,
    is_internal=True,
    is_stator=False,
)
lam.slot = SlotW63(
    Zs=12,
    H0=10e-3,
    W0=30e-3,
    H1=0.78539,
    W1=80e-3,
    H2=40e-3,
    W2=0,
)

# H2=0 and W2=0
lam = LamSlot(
    Rint=0.135,
    Rext=0.3,
    is_internal=True,
    is_stator=False,
)
lam.slot = SlotW63(
    Zs=12,
    H0=10e-3,
    W0=30e-3,
    H1=0.78539,
    W1=80e-3,
    H2=0,
    W2=0,
)

slotW63_test.append(
    {
        "test_obj": lam,
        "S_exp": 0.0034841,
        "Aw": 0.360020758,
        "SW_exp": 0.0012,
        "H_exp": 0.03566175,
        "Ao": 0.256135596778,
    }
)


class Test_SlotW63_meth(object):
    """pytest for SlotW63 methods"""

    @pytest.mark.parametrize("test_dict", slotW63_test)
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

    @pytest.mark.parametrize("test_dict", slotW63_test)
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

    @pytest.mark.parametrize("test_dict", slotW63_test)
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

    @pytest.mark.parametrize("test_dict", slotW63_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW63_test)
    def test_build_geometry_active_is_stator_true(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.build_geometry_active(Nrad=1, Ntan=2)
        a = result
        assert "Rotor_Winding_R0-T0-S0" == a[0].label

    @pytest.mark.parametrize("test_dict", slotW63_test)
    def test_build_geometry_active_error(self, test_dict):
        """Check that the ERROR is raised"""

        test_obj = test_dict["test_obj"]

        with pytest.raises(S63_WindError) as context:
            test_obj.slot.build_geometry_active(Nrad=0, Ntan=0)

    @pytest.mark.parametrize("test_dict", slotW63_test)
    def test_check_Inner_error(self, test_dict):
        """Check that the ERROR is raised"""

        test_obj = test_dict["test_obj"].copy()

        test_obj.is_internal = False
        with pytest.raises(S63_InnerCheckError) as context:
            test_obj.slot.check()

    @pytest.mark.parametrize("test_dict", slotW63_test)
    def test_get_surfaces(self, test_dict):
        test_obj = test_dict["test_obj"]
        Sact = test_obj.slot.build_geometry_active(Nrad=1, Ntan=2)
        Sfull = test_obj.slot.get_surface()
        Sop = test_obj.slot.get_surface_opening()
        if len(Sact) == 2:
            assert len(Sop) == 1
            S1 = Sact[0].comp_surface() + Sact[1].comp_surface() + Sop[0].comp_surface()
            S2 = Sfull.comp_surface()
        if len(Sact) == 1:
            assert len(Sop) == 1
            S1 = Sact[0].comp_surface() + Sop[0].comp_surface()
            S2 = Sfull.comp_surface()
        msg = "Act+Op=" + str(S1) + ", Full=" + str(S2)
        assert abs((S1 - S2) / S1) < DELTA, msg

    def test_SlotW63_check_S63_W0CheckError(self):
        """Check if the error S63_W0CheckError is correctly raised in the check method"""
        lam = LamSlot(
            Rint=0.135,
            Rext=0.3,
            is_internal=True,
            is_stator=False,
        )
        lam.slot = SlotW63(
            Zs=12,
            H0=30e-3,
            W0=30e-3,
            H1=0.78539,
            W1=20e-3,
            H2=40e-3,
            W2=15e-3,
        )

        with pytest.raises(S63_W0CheckError) as context:
            lam.slot.check()

    def test_SlotW63_check_S63_H0CheckError(self):
        """Check if the error S63_H0CheckError is correctly raised in the check method"""
        lam = LamSlot(
            Rint=0.135,
            Rext=0.3,
            is_internal=True,
            is_stator=False,
        )
        lam.slot = SlotW63(
            Zs=12,
            H0=0,
            W0=30e-3,
            H1=0.78539,
            W1=70e-3,
            H2=40e-3,
            W2=15e-3,
        )

        with pytest.raises(S63_H0CheckError) as context:
            lam.slot.check()

    def test_SlotW63_check_S63_W0CheckError(self):
        """Check if the error S63_H0CheckError is correctly raised in the check method"""
        lam = LamSlot(
            Rint=0.135,
            Rext=0.3,
            is_internal=True,
            is_stator=False,
        )
        lam.slot = SlotW63(
            Zs=12,
            H0=30e-3,
            W0=0,
            H1=0.78539,
            W1=70e-3,
            H2=40e-3,
            W2=15e-3,
        )

        with pytest.raises(S63_W0CheckError) as context:
            lam.slot.check()


if __name__ == "__main__":
    a = Test_SlotW63_meth()
    for test_dict in slotW63_test:
        a.test_build_geometry_active_error(test_dict)
        a.test_comp_height(test_dict)
        a.test_comp_angle_opening(test_dict)
        a.test_comp_surface(test_dict)
        a.test_get_surfaces(test_dict)
    print("Done")

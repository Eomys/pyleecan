# -*- coding: utf-8 -*-
import pytest


from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotW61 import SlotW61
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods.Slot.SlotW61 import (
    S61_InnerCheckError,
    S61_WindError,
    S61_WindWError,
)


# For AlmostEqual
DELTA = 1e-5

slotW61_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW61(
    Zs=12,
    W0=15e-3,
    W1=40e-3,
    W2=12.5e-3,
    H0=15e-3,
    H1=20e-3,
    H2=25e-3,
    H3=0,
    H4=0,
    W3=0,
)
slotW61_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.69308e-3,
        "Aw": 0.29889,
        "SW_exp": 6.875e-4,
        "H_exp": 5.9942749e-2,
        "Ao": 0.41033,
    }
)

# Internal Slot small wind
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW61(
    Zs=12,
    W0=15e-3,
    W1=40e-3,
    W2=12.5e-3,
    H0=15e-3,
    H1=20e-3,
    H2=25e-3,
    H3=1e-3,
    H4=2e-3,
    W3=3e-3,
)
slotW61_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.69308e-3,
        "Aw": 0.2419425,
        "SW_exp": 4.73e-4,
        "H_exp": 5.9942749e-2,
        "Ao": 0.41033,
    }
)


class Test_SlotW61_meth(object):
    """pytest for SlotW61 methods"""

    @pytest.mark.parametrize("test_dict", slotW61_test)
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

    @pytest.mark.parametrize("test_dict", slotW61_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the winding surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW61_test)
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

    @pytest.mark.parametrize("test_dict", slotW61_test)
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

    @pytest.mark.parametrize("test_dict", slotW61_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW61_test)
    def test_build_geometry_active_is_stator_true(self, test_dict):
        """Check that the computation of the average angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.build_geometry_active(Nrad=1, Ntan=2)
        a = result
        assert "Stator_Winding_R0-T0-S0" == a[0].label

    @pytest.mark.parametrize("test_dict", slotW61_test)
    def test_build_geometry_active_error(self, test_dict):
        """Check that the ERROR is raised"""

        test_obj = test_dict["test_obj"]

        with pytest.raises(S61_WindError) as context:
            test_obj.slot.build_geometry_active(Nrad=0, Ntan=0)

    @pytest.mark.parametrize("test_dict", slotW61_test)
    def test_check_Inner_error(self, test_dict):
        """Check that the ERROR is raised"""

        test_obj = test_dict["test_obj"].copy()

        test_obj.is_internal = False
        with pytest.raises(S61_InnerCheckError) as context:
            test_obj.slot.check()

    @pytest.mark.parametrize("test_dict", slotW61_test)
    def test_get_surfaces(self, test_dict):
        """Checks that the surfaces are correct"""
        test_obj = test_dict["test_obj"]
        Sact = test_obj.slot.build_geometry_active(Nrad=1, Ntan=2)
        Sfull = test_obj.slot.get_surface()
        Sop = test_obj.slot.get_surface_opening()

        # Sop[0].plot()
        assert len(Sact) == 2
        assert len(Sop) == 1
        S1 = Sact[0].comp_surface() + Sact[1].comp_surface() + Sop[0].comp_surface()
        S2 = Sfull.comp_surface()

        msg = "Act+Op=" + str(S1) + ", Full=" + str(S2)
        assert abs((S1 - S2) / S1) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW61_test)
    def test_check_Wind_error(self, test_dict):
        """Check that the ERROR is raised"""

        test_obj = test_dict["test_obj"].copy()

        test_obj.slot.W3 = 50
        test_obj.is_internal = True
        with pytest.raises(S61_WindWError) as context:
            test_obj.slot.check()


if __name__ == "__main__":
    a = Test_SlotW61_meth()
    for test_dict in slotW61_test:
        a.test_get_surfaces(test_dict)
    print("Done")

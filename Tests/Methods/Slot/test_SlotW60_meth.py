# -*- coding: utf-8 -*-
import pytest
from numpy import pi

from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotW60 import SlotW60
from pyleecan.Classes.Slot import Slot
from pyleecan.Methods.Slot.SlotW60 import (
    S60_InnerCheckError,
    S60_RCheckError,
    S60_WindWError,
    S60_WindError,
)

# For AlmostEqual
DELTA = 1e-5

slotW60_test = list()

# Internal Slot Full winding
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW60(
    Zs=12, W1=25e-3, W2=12.5e-3, H1=20e-3, H2=20e-3, R1=0.1, H3=0, H4=0, W3=0
)
slotW60_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.5792e-3,
        "Aw": 0.119451,
        "SW_exp": 2.5e-4,
        "H_exp": 0.0405716,
    }
)

# Internal Slot, R1=Rbo + small winding in all direction
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW60(
    Zs=12,
    W1=25e-3,
    W2=12.5e-3,
    H1=20e-3,
    H2=20e-3,
    R1=0.1325,
    H3=2e-3,
    H4=1e-3,
    W3=2e-3,
)
slotW60_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.572921e-3,
        "Aw": 0.0780255,
        "SW_exp": 1.445e-4,
        "H_exp": 0.0403786,
    }
)


class Test_SlotW60_meth(object):
    """pytest for SlotW60 methods"""

    @pytest.mark.parametrize("test_dict", slotW60_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct

        Parameters
        ----------
        test_dict :


        Returns
        -------

        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        b = Slot.comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW60_test)
    def test_comp_surface_active(self, test_dict):
        """Check that the computation of the winding surface is correct

        Parameters
        ----------
        test_dict :


        Returns
        -------

        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_active()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW60_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct

        Parameters
        ----------
        test_dict :


        Returns
        -------

        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        b = Slot.comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW60_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect

        Parameters
        ----------
        test_dict :


        Returns
        -------

        """
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        assert a == 2 * pi / test_obj.slot.Zs

        b = Slot.comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW60_test)
    def test_comp_angle_active_eq(self, test_dict):
        """Check that the computation of the average angle is correct

        Parameters
        ----------
        test_dict :


        Returns
        -------

        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_active_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", slotW60_test)
    def test_build_geometry_active_is_stator_true(self, test_dict):
        """Check that the computation of the average angle is correct"""

        test_obj = test_dict["test_obj"]

        result = test_obj.slot.build_geometry_active(Nrad=1, Ntan=2)
        a = result
        assert "Stator_Winding_R0-T0-S0" == a[0].label

    @pytest.mark.parametrize("test_dict", slotW60_test)
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

    @pytest.mark.parametrize("test_dict", slotW60_test)
    def test_build_geometry_error(self, test_dict):
        """Check that the ERROR is raised"""

        test_obj = test_dict["test_obj"]

        with pytest.raises(S60_WindError) as context:
            test_obj.slot.build_geometry_active(Nrad=0, Ntan=0)

    def test_check(self):
        """Check that the check methods is correctly working"""
        lam = LamSlot(is_internal=False, Rext=0.1325)
        lam.slot = SlotW60(
            Zs=12,
            W1=25e-3,
            W2=12.5e-3,
            H1=20e-3,
            H2=20e-3,
            R1=0.1325,
            H3=2e-3,
            H4=1e-3,
            W3=2e-3,
        )

        with pytest.raises(S60_InnerCheckError) as context:
            lam.slot.check()

        lam = LamSlot(is_internal=True, Rext=0.1325)
        lam.slot = SlotW60(
            Zs=12,
            W1=25e-3,
            W2=12.5e-3,
            H1=20e-3,
            H2=20e-3,
            R1=0.919325,
            H3=2e-3,
            H4=1e-3,
            W3=2e-3,
        )
        with pytest.raises(S60_RCheckError) as context:
            lam.slot.check()

        lam.slot = SlotW60(
            Zs=12,
            W1=25e-3,
            W2=12.5e-3,
            H1=20e-3,
            H2=20e-3,
            R1=0.1325,
            H3=2e-3,
            H4=1e-3,
            W3=2,
        )
        with pytest.raises(S60_WindWError) as context:
            lam.slot.check()


if __name__ == "__main__":
    a = Test_SlotW60_meth()
    for test_dict in slotW60_test:
        a.test_get_surfaces(test_dict)
    print("Done")
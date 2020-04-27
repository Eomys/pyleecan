# -*- coding: utf-8 -*-
from unittest import TestCase
from ddt import ddt, data


from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotW61 import SlotW61
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening

# For AlmostEqual
DELTA = 1e-5

SlotW61_test = list()

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
SlotW61_test.append(
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
SlotW61_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.69308e-3,
        "Aw": 0.2419425,
        "SW_exp": 4.73e-4,
        "H_exp": 5.9942749e-2,
        "Ao": 0.41033,
    }
)


@ddt
class test_SlotW61_meth(TestCase):
    """unittest for SlotW61 methods"""

    @data(*SlotW61_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

        b = comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*SlotW61_test)
    def test_comp_surface_wind(self, test_dict):
        """Check that the computation of the winding surface is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_wind()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*SlotW61_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

        b = comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*SlotW61_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect
        """
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        b = test_dict["Ao"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*SlotW61_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

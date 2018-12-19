# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 13:51:53 2014

@author: pierre_b
"""
from unittest import TestCase
from ddt import ddt, data
from numpy import pi

from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotW60 import SlotW60
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening

# For AlmostEqual
DELTA = 1e-5

SlotW60_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW60(
    Zs=12, W1=25e-3, W2=12.5e-3, H1=20e-3, H2=20e-3, R1=0.1, H3=0, H4=0, W3=0
)
SlotW60_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.5792e-3,
        "Aw": 0.119451,
        "SW_exp": 2.5e-4,
        "H_exp": 0.0405716,
    }
)

# Internal Slot, R1=Rbo
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
SlotW60_test.append(
    {
        "test_obj": lam,
        "S_exp": 1.572921e-3,
        "Aw": 0.0780255,
        "SW_exp": 1.445e-4,
        "H_exp": 0.0403786,
    }
)


@ddt
class test_SlotW60_meth(TestCase):
    """unittest for SlotW60 methods"""

    @data(*SlotW60_test)
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
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

        b = comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*SlotW60_test)
    def test_comp_surface_wind(self, test_dict):
        """Check that the computation of the winding surface is correct

        Parameters
        ----------
        test_dict :
            

        Returns
        -------

        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_wind()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*SlotW60_test)
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
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

        b = comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*SlotW60_test)
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
        self.assertEqual(a, 2 * pi / test_obj.slot.Zs)

        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*SlotW60_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct

        Parameters
        ----------
        test_dict :
            

        Returns
        -------

        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

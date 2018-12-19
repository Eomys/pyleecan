# -*- coding: utf-8 -*-
"""
@date Created on Tue Feb 02 11:31:45 2016
@copyright (C) 2015-2016 EOMYS ENGINEERING.
@author pierre_b
"""

from unittest import TestCase
from ddt import ddt, data

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM52 import HoleM52
from numpy import exp, arcsin, ndarray, pi

# For AlmostEqual
DELTA = 1e-6

HoleM52_test = list()

test_obj = LamHole(is_internal=True, is_stator=False, hole=list(), Rext=0.1)
test_obj.hole = list()
test_obj.hole.append(HoleM52(Zh=8, W0=30e-3, W3=15e-3, H0=12e-3, H1=18e-3, H2=2e-3))
HoleM52_test.append(
    {
        "test_obj": test_obj,
        "S_exp": 8.059458e-4,
        "SM_exp": 5.4e-4,
        "Rmin": 6.587571e-2,
        "Rmax": 8.8e-2,
        "W1": 4.9971e-3,
        "alpha": 0.614736,
    }
)


@ddt
class test_holeB52_meth(TestCase):
    """unittest for holeB52 methods"""

    @data(*HoleM52_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*HoleM52_test)
    def test_comp_surface_mag(self, test_dict):
        """Check that the computation of the magnet surface is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_surface_magnets()

        a = result
        b = test_dict["SM_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*HoleM52_test)
    def test_comp_alpha(self, test_dict):
        """Check that the computation of the alpha is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_alpha()

        a = result
        b = test_dict["alpha"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*HoleM52_test)
    def test_comp_W1(self, test_dict):
        """Check that the computation of W1 is correct
        """
        test_obj = test_dict["test_obj"]

        a = test_obj.hole[0].comp_W1()
        b = test_dict["W1"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*HoleM52_test)
    def test_comp_radius(self, test_dict):
        """Check that the computation of the radius is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_radius()

        a = result[0]
        b = test_dict["Rmin"]
        msg = "For Rmin: Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

        a = result[1]
        b = test_dict["Rmax"]
        msg = "For Rmax: Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*HoleM52_test)
    def test_build_geometry_with_magnet(self, test_dict):
        """Check that the surf list is correct with magnet
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].build_geometry()

        self.assertEquals(len(result), 3)
        for surf in result:
            self.assertTrue(type(surf) == SurfLine)

        self.assertEqual(result[0].label, "Air")
        self.assertEquals(len(result[0].line_list), 4)

        self.assertEqual(result[1].label, "MagnetR_N_R0_T0_S0")
        self.assertEquals(len(result[1].line_list), 4)

        self.assertEqual(result[2].label, "Air")
        self.assertEquals(len(result[2].line_list), 4)

    @data(*HoleM52_test)
    def test_build_geometry_no_magnet(self, test_dict):
        """Check that the surf list is correct without magnet
        """
        test_obj = LamHole(init_dict=test_dict["test_obj"].as_dict())
        test_obj.hole[0].magnet_0 = None
        result = test_obj.hole[0].build_geometry()

        self.assertEquals(len(result), 1)
        for surf in result:
            self.assertTrue(type(surf) == SurfLine)

        self.assertEqual(result[0].label, "Air")
        self.assertEquals(len(result[0].line_list), 8)

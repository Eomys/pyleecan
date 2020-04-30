# -*- coding: utf-8 -*-

from unittest import TestCase
from ddt import ddt, data

from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM51 import HoleM51
from numpy import exp, arcsin, ndarray, pi

# For AlmostEqual
DELTA = 1e-4

HoleM51_test = list()

test_obj = LamHole(
    Rint=45e-3 / 2, Rext=81.5e-3, is_stator=False, is_internal=True, L1=0.9
)
test_obj.hole = list()
test_obj.hole.append(
    HoleM51(
        Zh=8,
        W0=0.016,
        W1=pi / 6,
        W2=0.004,
        W3=0.01,
        W4=0.002,
        W5=0.01,
        W6=0.002,
        W7=0.01,
        H0=0.01096,
        H1=0.0015,
        H2=0.0055,
    )
)
HoleM51_test.append(
    {
        "test_obj": test_obj,
        "S_exp": 2.917e-4,
        "SM_exp": 1.65e-4,
        "Rmin": 0.06504,
        "Rmax": 0.08,
        "W": 41.411e-3,
        "alpha": 0.487367,
    }
)


@ddt
class test_holeM51_meth(TestCase):
    """unittest for holeB51 methods"""

    @data(*HoleM51_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*HoleM51_test)
    def test_comp_surface_mag(self, test_dict):
        """Check that the computation of the magnet surface is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_surface_magnets()

        a = result
        b = test_dict["SM_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*HoleM51_test)
    def test_comp_alpha(self, test_dict):
        """Check that the computation of the alpha is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].comp_alpha()

        a = result
        b = test_dict["alpha"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*HoleM51_test)
    def test_comp_width(self, test_dict):
        """Check that the computation of width is correct
        """
        test_obj = test_dict["test_obj"]

        a = test_obj.hole[0].comp_width()
        b = test_dict["W"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*HoleM51_test)
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

    @data(*HoleM51_test)
    def test_build_geometry_with_magnet(self, test_dict):
        """Check that the surf list is correct with magnet
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.hole[0].build_geometry()

        self.assertEqual(len(result), 7)
        for surf in result:
            self.assertTrue(type(surf) == SurfLine)

        self.assertEqual(result[0].label[:5], "Hole_")
        self.assertEqual(result[0].label[-9:], "_R0_T0_S0")
        self.assertEqual(len(result[0].line_list), 4)

        self.assertEqual(result[1].label[:11], "HoleMagnet_")
        self.assertEqual(result[1].label[-11:], "_N_R0_T0_S0")
        self.assertEqual(len(result[1].line_list), 4)

        self.assertEqual(result[2].label[:5], "Hole_")
        self.assertEqual(result[2].label[-9:], "_R0_T1_S0")
        self.assertEqual(len(result[2].line_list), 6)

        self.assertEqual(result[3].label[:11], "HoleMagnet_")
        self.assertEqual(result[3].label[-11:], "_N_R0_T1_S0")
        self.assertEqual(len(result[3].line_list), 4)

        self.assertEqual(result[4].label[:5], "Hole_")
        self.assertEqual(result[4].label[-9:], "_R0_T2_S0")
        self.assertEqual(len(result[4].line_list), 6)

        self.assertEqual(result[5].label[:11], "HoleMagnet_")
        self.assertEqual(result[5].label[-11:], "_N_R0_T2_S0")
        self.assertEqual(len(result[5].line_list), 4)

        self.assertEqual(result[6].label[:5], "Hole_")
        self.assertEqual(result[6].label[-9:], "_R0_T3_S0")
        self.assertEqual(len(result[6].line_list), 4)

    @data(*HoleM51_test)
    def test_build_geometry_no_magnet(self, test_dict):
        """Check that the surf list is correct without magnet
        """
        test_obj = LamHole(init_dict=test_dict["test_obj"].as_dict())
        test_obj.hole[0].magnet_0 = None
        test_obj.hole[0].magnet_1 = None
        test_obj.hole[0].magnet_2 = None
        result = test_obj.hole[0].build_geometry()

        self.assertEqual(len(result), 1)
        for surf in result:
            self.assertTrue(type(surf) == SurfLine)

        self.assertEqual(result[0].label[:5], "Hole_")
        self.assertEqual(result[0].label[-9:], "_R0_T0_S0")
        self.assertEqual(len(result[0].line_list), 8)

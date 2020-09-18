# -*- coding: utf-8 -*-

from unittest import TestCase

from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.MagnetType10 import MagnetType10

# For AlmostEqual
DELTA = 1e-4


class unittest_HoleM50_meth(TestCase):
    """unittest for HoleM50 methods"""

    def test_comp_alpha(self):
        """Check that the computation of the alpha is correct"""
        test_obj = LamHole(is_internal=True, Rext=0.075)
        test_obj.hole = list()
        test_obj.hole.append(
            HoleM50(
                Zh=8,
                W0=50e-3,
                W1=2e-3,
                W2=1e-3,
                W3=1e-3,
                W4=20.6e-3,
                H0=17.3e-3,
                H1=1.25e-3,
                H2=0.5e-3,
                H3=6.8e-3,
            )
        )
        result = test_obj.hole[0].comp_alpha()

        a = result
        b = 0.45304022
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)

    def test_comp_magnet_surface(self):
        """Check that the computation of the magnet surface"""
        test_obj = LamHole(is_internal=True, Rext=0.075)
        test_obj.hole = list()
        test_obj.hole.append(
            HoleM50(
                Zh=8,
                W0=50e-3,
                W1=2e-3,
                W2=1e-3,
                W3=1e-3,
                W4=20.6e-3,
                H0=17.3e-3,
                H1=1.25e-3,
                H2=0.5e-3,
                H3=6.8e-3,
            )
        )
        result = test_obj.hole[0].comp_surface_magnets()

        a = result
        b = 1.4008e-4 * 2
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)

    def test_comp_surface(self):
        """Check that the computation of the slot surface is correct"""
        test_obj = LamHole(is_internal=True, Rext=0.075)
        test_obj.hole = list()
        test_obj.hole.append(
            HoleM50(
                Zh=8,
                W0=50e-3,
                W1=2e-3,
                W2=1e-3,
                W3=1e-3,
                W4=20.6e-3,
                H0=17.3e-3,
                H1=1.25e-3,
                H2=0.5e-3,
                H3=6.8e-3,
            )
        )
        result = test_obj.hole[0].comp_surface()
        a = result
        b = 3.77977e-04
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)

    def test_comp_W5(self):
        """Check that the computation of W5 is correct"""
        test_obj = LamHole(is_internal=True, Rext=0.075)
        test_obj.hole = list()
        test_obj.hole.append(
            HoleM50(
                Zh=8,
                W0=50e-3,
                W1=2e-3,
                W2=1e-3,
                W3=1e-3,
                W4=20.6e-3,
                H0=17.3e-3,
                H1=1.25e-3,
                H2=0.5e-3,
                H3=6.8e-3,
            )
        )
        result = test_obj.hole[0].comp_W5()

        a = result
        b = 5.09275e-3
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)

    def test_build_geometry_two_hole_no_mag(self):
        """check that curve_list is correct (two holes no magnet)"""
        test_obj = LamHole(is_internal=True, Rext=0.075)
        test_obj.hole = list()
        test_obj.hole.append(
            HoleM50(
                Zh=8,
                W0=50e-3,
                W1=2e-3,
                W2=1e-3,
                W3=1e-3,
                W4=20.6e-3,
                H0=17.3e-3,
                H1=1.25e-3,
                H2=0.5e-3,
                H3=6.8e-3,
                H4=1e-3,
                magnet_0=None,
                magnet_1=None,
            )
        )

        result = test_obj.hole[0].build_geometry()

        self.assertEqual(len(result), 2)
        for surf in result:
            self.assertTrue(type(surf) is SurfLine)

        self.assertEqual(result[0].label[:4], "Hole")
        self.assertEqual(result[0].label[-9:], "_R0_T0_S0")
        self.assertEqual(len(result[0].line_list), 11)

        self.assertEqual(result[1].label[:4], "Hole")
        self.assertEqual(result[1].label[-9:], "_R0_T1_S0")
        self.assertEqual(len(result[1].line_list), 11)

    def test_build_geometry_one_hole_no_mag(self):
        """check that curve_list is correct (one hole no mag)"""
        test_obj = LamHole(is_internal=True, Rext=0.075)
        test_obj.hole = list()
        test_obj.hole.append(
            HoleM50(
                Zh=8,
                W0=52e-3,
                W1=0,
                W2=1e-3,
                W3=1e-3,
                W4=20.6e-3,
                H0=17.3e-3,
                H1=1.25e-3,
                H2=0.5e-3,
                H3=6.8e-3,
                H4=0,
                magnet_0=None,
                magnet_1=None,
            )
        )

        result = test_obj.hole[0].build_geometry()
        self.assertEqual(len(result), 1)
        for surf in result:
            self.assertTrue(type(surf) is SurfLine)

        self.assertEqual(result[0].label[:4], "Hole")
        self.assertEqual(result[0].label[-9:], "_R0_T0_S0")
        self.assertEqual(len(result[0].line_list), 16)

    def test_build_geometry_one_hole_with_magnet(self):
        """check that curve_list is correct (one hole)"""
        test_obj = LamHole(is_internal=True, Rext=0.075)
        test_obj.hole = list()
        test_obj.hole.append(
            HoleM50(
                Zh=8,
                W0=52e-3,
                W1=0,
                W2=1e-3,
                W3=1e-3,
                W4=20.6e-3,
                H0=17.3e-3,
                H1=1.25e-3,
                H2=0.5e-3,
                H3=6.8e-3,
                H4=0,
                magnet_0=MagnetType10(Wmag=0.01, Hmag=0.02),
            )
        )

        result = test_obj.hole[0].build_geometry()
        self.assertEqual(len(result), 5)
        for surf in result:
            self.assertTrue(type(surf) is SurfLine)

        self.assertEqual(result[0].label[:5], "Hole_")
        self.assertEqual(result[0].label[-9:], "_R0_T0_S0")
        self.assertEqual(len(result[0].line_list), 5)

        self.assertEqual(result[1].label[:11], "HoleMagnet_")
        self.assertEqual(result[1].label[-11:], "_N_R0_T0_S0")
        self.assertEqual(len(result[1].line_list), 6)

        self.assertEqual(result[2].label[:5], "Hole_")
        self.assertEqual(result[2].label[-9:], "_R0_T1_S0")
        self.assertEqual(len(result[2].line_list), 6)

        self.assertEqual(result[3].label[:11], "HoleMagnet_")
        self.assertEqual(result[3].label[-11:], "_N_R0_T1_S0")
        self.assertEqual(len(result[3].line_list), 6)

        self.assertEqual(result[4].label[:5], "Hole_")
        self.assertEqual(result[4].label[-9:], "_R0_T2_S0")
        self.assertEqual(len(result[4].line_list), 5)

    def test_build_geometry_two_hole_with_magnet(self):
        """check that curve_list is correct (one hole)"""
        test_obj = LamHole(is_internal=True, is_stator=False, Rext=0.075)
        test_obj.hole = list()
        test_obj.hole.append(
            HoleM50(
                Zh=8,
                W0=50e-3,
                W1=2e-3,
                W2=1e-3,
                W3=1e-3,
                W4=20.6e-3,
                H0=17.3e-3,
                H1=1.25e-3,
                H2=0.5e-3,
                H3=6.8e-3,
                H4=1e-3,
                magnet_0=MagnetType10(Wmag=0.01, Hmag=0.02),
            )
        )

        result = test_obj.hole[0].build_geometry()
        self.assertEqual(len(result), 6)
        for surf in result:
            self.assertTrue(type(surf) is SurfLine)

        self.assertEqual(result[0].label[:5], "Hole_")
        self.assertEqual(result[0].label[-9:], "_R0_T0_S0")
        self.assertEqual(len(result[0].line_list), 7)

        self.assertEqual(result[1].label[:11], "HoleMagnet_")
        self.assertEqual(result[1].label[-11:], "_N_R0_T0_S0")
        self.assertEqual(len(result[1].line_list), 6)

        self.assertEqual(result[2].label[:5], "Hole_")
        self.assertEqual(result[2].label[-9:], "_R0_T1_S0")
        self.assertEqual(len(result[2].line_list), 4)

        self.assertEqual(result[3].label[:5], "Hole_")
        self.assertEqual(result[3].label[-9:], "_R0_T2_S0")
        self.assertEqual(len(result[3].line_list), 4)

        self.assertEqual(result[4].label[:11], "HoleMagnet_")
        self.assertEqual(result[4].label[-11:], "_N_R0_T1_S0")
        self.assertEqual(len(result[4].line_list), 6)

        self.assertEqual(result[5].label[:5], "Hole_")
        self.assertEqual(result[5].label[-9:], "_R0_T3_S0")
        self.assertEqual(len(result[5].line_list), 7)

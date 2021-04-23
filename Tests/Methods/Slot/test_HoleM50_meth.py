# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Magnet import Magnet

# For AlmostEqual
DELTA = 1e-4


class Test_HoleM50_meth(object):
    """pytest for HoleM50 methods"""

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
        assert abs((a - b) / a - 0) < DELTA

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
        assert abs((a - b) / a - 0) < DELTA

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
        b = 3.7803e-04
        assert abs((a - b) / a - 0) < DELTA

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
        assert abs((a - b) / a - 0) < DELTA

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

        assert len(result) == 2
        for surf in result:
            assert type(surf) is SurfLine

        assert "Hole_" in result[0].label
        assert "R0_T0_S0" in result[0].label
        assert len(result[0].line_list) == 11

        assert "Hole_" in result[1].label
        assert "R0_T1_S0" in result[1].label
        assert len(result[1].line_list) == 11

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
        assert len(result) == 1
        for surf in result:
            assert type(surf) is SurfLine

        assert "Hole_" in result[0].label
        assert "R0_T0_S0" in result[0].label
        assert len(result[0].line_list) == 16

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
                magnet_0=Magnet(),
            )
        )

        result = test_obj.hole[0].build_geometry()
        assert len(result) == 5
        for surf in result:
            assert type(surf) is SurfLine

        assert "Hole_" in result[0].label
        assert "R0_T0_S0" in result[0].label
        assert len(result[0].line_list) == 5

        assert "HoleMagnet_" in result[1].label
        assert "_N_R0_T0_S0" in result[1].label
        assert len(result[1].line_list) == 6

        assert "Hole_" in result[2].label
        assert "R0_T1_S0" in result[2].label
        assert len(result[2].line_list) == 6

        assert "HoleMagnet_" in result[3].label
        assert "_N_R0_T1_S0" in result[3].label
        assert len(result[3].line_list) == 6

        assert "Hole_" in result[4].label
        assert "R0_T2_S0" in result[4].label
        assert len(result[4].line_list) == 5

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
                magnet_0=Magnet(),
            )
        )
        result = test_obj.hole[0].build_geometry()
        assert len(result) == 6
        for surf in result:
            assert type(surf) is SurfLine

        assert "Hole_" in result[0].label
        assert "_R0_T0_S0" in result[0].label
        assert len(result[0].line_list) == 7
        assert "HoleMagnet_" in result[1].label
        assert "_N_R0_T0_S0" in result[1].label
        assert len(result[1].line_list) == 6
        assert "Hole_" in result[2].label
        assert "_R0_T1_S0" in result[2].label
        assert len(result[2].line_list) == 4
        assert "Hole_" in result[3].label
        assert "_R0_T2_S0" in result[3].label
        assert len(result[3].line_list) == 4
        assert "HoleMagnet_" in result[4].label
        assert "_N_R0_T1_S0" in result[4].label
        assert len(result[4].line_list) == 6
        assert "Hole_" in result[5].label
        assert "_R0_T3_S0" in result[5].label
        assert len(result[5].line_list) == 7

    def test_build_geometry_two_hole_with_magnet_is_simplified(self):
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
                magnet_0=Magnet(),
            )
        )
        result = test_obj.hole[0].build_geometry(is_simplified=True)
        assert len(result) == 6
        for surf in result:
            assert type(surf) is SurfLine

        assert "Hole_" in result[0].label
        assert "_R0_T0_S0" in result[0].label
        assert len(result[0].line_list) == 7
        assert "HoleMagnet_" in result[1].label
        assert "_N_R0_T0_S0" in result[1].label
        assert len(result[1].line_list) == 2
        assert "Hole_" in result[2].label
        assert "_R0_T1_S0" in result[2].label
        assert len(result[2].line_list) == 4
        assert "Hole_" in result[3].label
        assert "_R0_T2_S0" in result[3].label
        assert len(result[3].line_list) == 4
        assert "HoleMagnet_" in result[4].label
        assert "_N_R0_T1_S0" in result[4].label
        assert len(result[4].line_list) == 2
        assert "Hole_" in result[5].label
        assert "_R0_T3_S0" in result[5].label
        assert len(result[5].line_list) == 7

    def test_comp_radius_mid_yoke(self):
        test_obj = LamHole(is_internal=True, is_stator=False, Rext=0.325, Rint=0.032121)
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
            )
        )
        assert test_obj.comp_radius_mid_yoke() == 0.1661908960397621

        test_obj = LamHole(
            is_internal=False, is_stator=False, Rext=0.325, Rint=0.032121
        )
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
            )
        )
        # Hole is defined on Rext, so mid yoke is around Rext, Rext H1
        assert test_obj.comp_radius_mid_yoke() == 0.324375

    def test_comp_surface_magnet_id(self):
        """check that id is 0"""
        hole = HoleM50(
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
        assert hole.comp_surface_magnet_id(3) == 0

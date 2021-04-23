# -*- coding: utf-8 -*-
import pytest
from pyleecan.Classes.Trapeze import Trapeze
from pyleecan.Classes.Segment import Segment
from mock import MagicMock
from numpy import pi

from pyleecan.definitions import config_dict


class Test_Trapeze_meth(object):
    """Unittest for the Trapeze methods"""

    def test_rotate(self):
        """Check that you can rotate the trapeze"""
        surface = Trapeze(point_ref=1j, label="test", height=6, W2=6, W1=3)
        surface.rotate(pi / 2)
        expected = -1
        assert round(abs(abs(surface.point_ref - expected) - 0), 7) == 0

    def test_comp_length(self):
        """Check that you can compute the length of the trapeze"""
        surface = Trapeze(point_ref=1j, label="test", height=6, W2=6, W1=3)
        surface.get_lines = MagicMock(return_value=[Segment(begin=0, end=1)])
        length = surface.comp_length()
        expected = 1
        assert length == expected

    def test_translate(self):
        """Check that you can translate the Trapeze"""
        surface = Trapeze(point_ref=1j, label="test", height=6, W2=6, W1=3)
        surface.translate(-2)
        expected = -2 + 1j
        assert round(abs(abs(surface.point_ref - expected) - 0), 7) == 0

    def test_get_lines(self):
        """Check that you get the correct lines to draw the trapeze"""
        surface = Trapeze(point_ref=1j, label="test", height=6, W2=6, W1=3)
        lines = surface.get_lines()
        cpt_Segment = 0
        for line in lines:
            assert type(line) in [Segment]
            cpt_Segment += 1
        assert cpt_Segment == 4

    def test_get_patches(self):
        """Check that you get the correct color to draw the Polygon"""
        surface = Trapeze(point_ref=1j, label="test", height=6, W2=6, W1=3)
        result = surface.get_patches(is_edge_only=True)
        assert result[0].get_facecolor() == (0.0, 0.0, 0.0, 0.0)
        assert result[0].get_edgecolor() == (1.0, 0.0, 0.0, 1.0)

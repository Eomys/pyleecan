# -*- coding: utf-8 -*-
import pytest
from mock import MagicMock
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Arc2 import Arc2
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from numpy import pi

@pytest.mark.METHODS
class Test_SurfLine_meth(object):
    """Unittest for SurfLine methods"""

    def test_comp_length(self):
        """Check that you can compute the length of the Surface
            """
        line1 = Arc1(begin=1, end=1j, radius=1)
        line1.comp_length = MagicMock(return_value=1)
        line2 = Arc2(begin=1, center=0, angle=pi / 2)
        line2.comp_length = MagicMock(return_value=1)
        line3 = Segment(begin=1j, end=0)
        line3.comp_length = MagicMock(return_value=1)
        
        surface = SurfLine(line_list=[line1, line2, line3], label="test", point_ref=0)
        length = surface.comp_length()
        line1.comp_length.assert_called_once()
        line2.comp_length.assert_called_once()
        line3.comp_length.assert_called_once()
        assert round(abs(abs(length - 3)-0), 7) == 0

    def test_rotate(self):
        """Check that you can rotate the surface
            """
        line1 = Arc1(begin=1, end=1j, radius=1)
        line2 = Arc2(begin=1, center=0, angle=pi / 2)
        line3 = Segment(begin=1j, end=0)
        surface = SurfLine(line_list=[line1, line2, line3], label="test", point_ref=0)
        surface.rotate(pi / 2)
        assert round(abs(abs(line1.begin - 1j)-0), 7) == 0
        assert round(abs(abs(line1.end + 1)-0), 7) == 0
        assert round(abs(abs(line2.begin - 1j)-0), 7) == 0
        assert round(abs(line2.center-0), 7) == 0
        assert round(abs(abs(line3.begin + 1)-0), 7) == 0
        assert round(abs(line3.end-0), 7) == 0

    def test_translate(self):
        """Check that you can rotate the surface
            """
        line1 = Arc1(begin=1, end=1j, radius=1)
        line2 = Arc2(begin=1, center=0, angle=pi / 2)
        line3 = Segment(begin=1j, end=0)
        surface = SurfLine(line_list=[line1, line2, line3], label="test", point_ref=0)
        surface.translate(1j)
        assert round(abs(abs(line1.begin - 1j)-1), 7) == 0
        assert round(abs(line1.end-2j), 7) == 0
        assert round(abs(abs(line2.begin - 1j)-1), 7) == 0
        assert round(abs(abs(line2.center - 1j)-0), 7) == 0
        assert round(abs(abs(line3.begin - 2j)-0), 7) == 0
        assert round(abs(line3.end-1j), 7) == 0

# -*- coding: utf-8 -*-
from pyleecan.Classes.PolarArc import PolarArc
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment
from numpy import pi
from mock import MagicMock

import pytest

# Dictionary to test rotate
rotate_test = list()
rotate_test.append({"ref": 1, "angle": pi / 4, "H": 2, "alpha": pi / 2, "exp_ref": 1j})
rotate_test.append({"ref": 1j, "angle": pi / 4, "H": 2, "alpha": -pi / 2, "exp_ref": 1})
rotate_test.append(
    {"ref": 1 + 1j, "angle": pi / 2, "H": 1, "alpha": pi / 2, "exp_ref": -1 + 1j}
)

# Dictionary to test translate
translate_test = list()
translate_test.append(
    {"ref": 1, "angle": pi / 4, "H": 2, "delta": 1j, "exp_ref": 1 + 1j}
)
translate_test.append(
    {"ref": 1j, "angle": pi / 4, "H": 2, "delta": -2, "exp_ref": -2 + 1j}
)
translate_test.append(
    {"ref": 1 + 1j, "angle": pi / 2, "H": 1, "delta": 1 + 1j, "exp_ref": 2 + 2j}
)

@pytest.mark.METHODS
class Test_PolarArc_meth(object):
    """Unittest for PolarArc methods"""

    @pytest.mark.parametrize("test_dict", rotate_test)
    def test_rotate(self,test_dict):
        """Check that you can rotate the polararc
            """
        surface = PolarArc(    
            label="test",    
            point_ref=test_dict["ref"],    
            angle=test_dict["angle"],    
            height=test_dict["H"],    
        )
        surface.rotate(test_dict["alpha"])

        assert round(abs(abs(surface.point_ref - test_dict["exp_ref"])-0), 7) == 0
        assert round(abs(abs(surface.angle - test_dict["angle"])-0), 7) == 0
        assert round(abs(abs(surface.height - test_dict["H"])-0), 7) == 0

    @pytest.mark.parametrize("test_dict", translate_test)
    def test_translate(self,test_dict):
        """Check that you can translate the polararc
            """
        surface = PolarArc(    
            label="test",    
            point_ref=test_dict["ref"],    
            angle=test_dict["angle"],    
            height=test_dict["H"],    
        )
        surface.translate(test_dict["delta"])

        assert round(abs(abs(surface.point_ref - test_dict["exp_ref"])-0), 7) == 0
        assert round(abs(abs(surface.angle - test_dict["angle"])-0), 7) == 0
        assert round(abs(abs(surface.height - test_dict["H"])-0), 7) == 0

    def test_get_lines(self):
        """Check that you get the correct lines to drow the polar arc
            """
        surface = PolarArc(label="test", point_ref=0, angle=pi / 4, height=2)
        lines = surface.get_lines()
        cpt_Arc1 = 0
        cpt_Segment = 0
        for line in lines:
            assert type(line) in [Arc1, Segment]
            if isinstance(line, Arc1):
                cpt_Arc1 += 1
            elif isinstance(line, Segment):
                cpt_Segment += 1
        assert cpt_Arc1== 2
        assert cpt_Segment==2

    def test_comp_length(self):
        """Check that you can compute the length of the polar arc
            """
        surface = PolarArc(label="test", point_ref=1, angle=pi / 4, height=2)
        surface.get_lines = MagicMock(return_value=[Segment(begin=0, end=1)])
        length = surface.comp_length()
        expected = 1
        assert round(abs(abs(length - expected)-0), 7) == 0

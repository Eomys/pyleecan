# -*- coding: utf-8 -*-

import pytest
from numpy import pi

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.CondType12 import CondType12
from Tests.Validation.Machine.IPMSM_A import IPMSM_A


def test_resistance():
    """Check that resistance computation is correct
    """
    result = IPMSM_A.stator.comp_resistance_wind()
    assert result == pytest.approx(0.035951, abs=0.00001)


def test_DQ_axis_rotor():
    """Check that the DQ axis are correct for the rotor
    """
    d_axis = IPMSM_A.rotor.comp_angle_d_axis()
    assert d_axis == pytest.approx(pi / 8, abs=0.0001)

    q_axis = IPMSM_A.rotor.comp_angle_q_axis()
    assert q_axis == pytest.approx(2 * pi / 8, abs=0.0001)


def test_DQ_axis_stator():
    """Check that the DQ axis are correct for the stator
    """
    d_axis = IPMSM_A.stator.comp_angle_d_axis()
    assert d_axis == pytest.approx(1.31, abs=0.001)

    q_axis = IPMSM_A.stator.comp_angle_q_axis()
    assert q_axis == pytest.approx(1.31 + pi / 8, abs=0.0001)


def test_comp_rot_dir():
    """Check that the computation of the rot dir is correct
    """
    rot_dir = IPMSM_A.stator.comp_rot_dir()
    assert rot_dir == 1

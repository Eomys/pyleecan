# -*- coding: utf-8 -*-

import pytest
from numpy import pi
from os.path import join
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.CondType12 import CondType12
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


@pytest.fixture(scope="module")
def Toyota_Prius():
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    return Toyota_Prius


@pytest.mark.IPMSM
class Test_Electrical(object):
    def test_resistance(self, Toyota_Prius):
        """Check that resistance computation is correct"""
        result = Toyota_Prius.stator.comp_resistance_wind()
        assert result == pytest.approx(0.035951, abs=0.00001)

    def test_DQ_axis_rotor(self, Toyota_Prius):
        """Check that the DQ axis are correct for the rotor"""
        d_axis = Toyota_Prius.rotor.comp_angle_d_axis()
        assert d_axis == pytest.approx(pi / 8, abs=0.0001)

        q_axis = Toyota_Prius.rotor.comp_angle_q_axis()
        assert q_axis == pytest.approx(2 * pi / 8, abs=0.0001)

    def test_DQ_axis_stator(self, Toyota_Prius):
        """Check that the DQ axis are correct for the stator"""
        d_axis = Toyota_Prius.stator.comp_angle_d_axis()
        assert d_axis == pytest.approx(1.3086, abs=0.001)

        q_axis = Toyota_Prius.stator.comp_angle_q_axis()
        assert q_axis == pytest.approx(1.3086 + pi / 8, abs=0.0001)

    def test_comp_rot_dir(self, Toyota_Prius):
        """Check that the computation of the rot dir is correct"""
        rot_dir = Toyota_Prius.stator.comp_rot_dir()
        assert rot_dir == -1

    def test_comp_rot_dir_reverse_wind(self, Toyota_Prius):
        """Check that the computation of the rot dir is correct when reversing the winding"""
        IPMSM_B = Toyota_Prius.copy()
        IPMSM_B.stator.winding.is_reverse_wind = (
            not IPMSM_B.stator.winding.is_reverse_wind
        )
        rot_dir = IPMSM_B.stator.comp_rot_dir()
        assert rot_dir == 1

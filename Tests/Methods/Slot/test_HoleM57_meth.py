# -*- coding: utf-8 -*-

from os.path import join
from numpy import pi

import pytest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.HoleM57 import HoleM57

HoleM57_test = list()

test_obj = LamHole(is_internal=True, Rint=0.021, Rext=0.075, is_stator=False, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM57(
        Zh=8,
        W0=pi * 0.8,
        W1=10e-3,
        W2=0e-3,
        W3=5e-3,
        W4=10e-3,
        H1=3e-3,
        H2=5e-3,
    )
)
HoleM57_test.append(
    {
        "test_obj": test_obj,
    }
)


@pytest.mark.METHODS
class Test_HoleM57_meth(object):
    """Test machine plot hole 57"""

    @pytest.mark.parametrize("test_dict", HoleM57_test)
    def test_build_geometry_magnet_0_and_1(self, test_dict):
        """Test build_geometry with both magnet"""

        result1 = test_obj.hole[0].build_geometry()
        assert result1[1].label == "Magnet_Rotor_N_R0_T0_S0"
        assert result1[3].point_ref == (
            0.05300650262595291 + 0.02768664153388476j
        )  # SurfLine #6
        assert (
            result1[4].label == "Magnet_Rotor_N_R0_T1_S0"
        )  # Label SurfLine #5 at 5th position

        test_obj.hole[0].W1 = 0

        result2 = test_obj.hole[0].build_geometry()
        assert (
            result2[3].point_ref != result1[3].point_ref
        )  # SurfLine #6 absent when W1 == 0
        assert result2[3].label == result1[4].label  # Same label of S5

    @pytest.mark.parametrize("test_dict", HoleM57_test)
    def test_build_geometry_simplified(self, test_dict):
        """Test build_geometry with both magnet and simplified"""

        test_obj.hole[0].W1 = 10e-3

        result1 = test_obj.hole[0].build_geometry(is_simplified=True)
        assert result1[1].label == "Magnet_Rotor_N_R0_T0_S0"
        assert result1[3].point_ref == (
            0.05300650262595291 + 0.02768664153388476j
        )  # SurfLine #6
        assert (
            result1[4].label == "Magnet_Rotor_N_R0_T1_S0"
        )  # SurfLine #5 at 5th position

        test_obj.hole[0].W1 = 0

        result2 = test_obj.hole[0].build_geometry(is_simplified=True)
        assert (
            result2[3].point_ref != result1[3].point_ref
        )  # SurfLine #6 absent when W1 == 0
        assert (
            result2[3].label == result1[4].label
        )  # SurfLine #5 at 4th position like the #5 at 5th positio

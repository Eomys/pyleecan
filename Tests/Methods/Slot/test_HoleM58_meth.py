# -*- coding: utf-8 -*-

from os.path import join
from numpy import pi

import pytest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.Magnet import Magnet
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.HoleM58 import HoleM58

HoleM58_test = list()

test_obj = LamHole(is_internal=True, Rint=0.021, Rext=0.075, is_stator=False, L1=0.7)
test_obj.hole = list()
test_obj.hole.append(
    HoleM58(
        Zh=8,
        W0=20e-3,
        W1=16e-3,
        W2=2e-3,
        W3=2 * pi / 8 * 0.6,
        H0=15e-3,
        H1=5e-3,
        H2=5e-3,
        R0=1e-3,
    )
)
HoleM58_test.append(
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


class Test_HoleM58_meth(object):
    """Test machine plot hole 58"""

    @pytest.mark.parametrize("test_dict", HoleM58_test)
    def test_magnet_None(self, test_dict):
        """Magnet None"""

        test_obj.hole[0].magnet_0 = None
        result = test_obj.hole[0].build_geometry()
        assert "Hole_Rotor_R0_T0_S0" == result[0].label

    @pytest.mark.parametrize("test_dict", HoleM58_test)
    def test_magnet_Parallel(self, test_dict):
        """Type Magnetization Parallel"""

        test_obj.hole[0].magnet_0 = Magnet(type_magnetization=1)
        result = test_obj.hole[0].build_geometry()
        assert result[1].label == "HoleMagnet_Rotor_Parallel_N_R0_T0_S0"

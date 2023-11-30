# -*- coding: utf-8 -*-

from os.path import join
from numpy import pi

import pytest

from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.Hole import Hole
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
        "Rmin": 0.055,
        "Rmax": 0.07,
        "W": 41.411e-3,
        "alpha": 0.487367,
    }
)

# For AlmostEqual
DELTA = 1e-3


class Test_HoleM58_meth(object):
    """Test machine plot hole 58"""

    @pytest.mark.parametrize("test_dict", HoleM58_test)
    def test_schematics(self, test_dict):
        """Check that the schematics is correct"""
        test_obj = test_dict["test_obj"]

        point_dict = test_obj.hole[0]._comp_point_coordinate()
        Rbo = test_obj.hole[0].get_Rbo()

        # W0
        assert abs(point_dict["Z2"] - point_dict["Z11"]) == pytest.approx(
            test_obj.hole[0].W0
        )
        assert abs(point_dict["Z8"] - point_dict["Z5"]) == pytest.approx(
            test_obj.hole[0].W0
        )

        # W1
        assert abs(point_dict["Z12"] - point_dict["Z1"]) == pytest.approx(
            test_obj.hole[0].W1
        )
        assert abs(point_dict["Z6"] - point_dict["Z7"]) == pytest.approx(
            test_obj.hole[0].W1
        )

        # W2
        assert abs(point_dict["Z2"] - point_dict["Z1"]) == pytest.approx(
            test_obj.hole[0].W2
        )
        assert abs(point_dict["Z6"] - point_dict["Z5"]) == pytest.approx(
            test_obj.hole[0].W2
        )

        # H2
        assert abs(point_dict["Z2"] - point_dict["Z5"]) == pytest.approx(
            test_obj.hole[0].H2
        )
        assert abs(point_dict["Z6"] - point_dict["Z1"]) == pytest.approx(
            test_obj.hole[0].H2
        )
        assert abs(point_dict["Z12"] - point_dict["Z7"]) == pytest.approx(
            test_obj.hole[0].H2
        )

        # R0
        assert abs(point_dict["Z4"] - point_dict["Zc1"]) == pytest.approx(
            test_obj.hole[0].R0
        )
        assert abs(point_dict["Z3"] - point_dict["Zc1"]) == pytest.approx(
            test_obj.hole[0].R0
        )
        assert abs(point_dict["Z10"] - point_dict["Zc2"]) == pytest.approx(
            test_obj.hole[0].R0
        )
        assert abs(point_dict["Z9"] - point_dict["Zc2"]) == pytest.approx(
            test_obj.hole[0].R0
        )

        assert abs(point_dict["Zc1"]) == pytest.approx(
            Rbo - test_obj.hole[0].R0 - test_obj.hole[0].H1
        )
        assert abs(point_dict["Zc2"]) == pytest.approx(
            Rbo - test_obj.hole[0].R0 - test_obj.hole[0].H1
        )

    @pytest.mark.parametrize("test_dict", HoleM58_test)
    def test_magnet_None(self, test_dict):
        """Magnet None"""

        test_obj.hole[0].magnet_0 = None
        result = test_obj.hole[0].build_geometry()
        assert result[0].label == "Rotor_HoleVoid_R0-T0-S0"

    @pytest.mark.parametrize("test_dict", HoleM58_test)
    def test_magnet_Parallel(self, test_dict):
        """Type Magnetization Parallel"""

        test_obj.hole[0].magnet_0 = Magnet(type_magnetization=1)
        result = test_obj.hole[0].build_geometry()
        assert result[1].label == "Rotor_HoleMag_R0-T0-S0"

    @pytest.mark.parametrize("test_dict", HoleM58_test)
    def test_comp_radius(self, test_dict):
        """Check that comp_radius return the correct result (analytical+num)"""
        test_obj = test_dict["test_obj"]
        Rmin, Rmax = test_obj.hole[0].comp_radius()

        Rmax_a = test_dict["Rmax"]
        Rmin_a = test_dict["Rmin"]
        a, b = Rmin, Rmin_a
        msg = f"For Rmin: Return {a} expected {b}"
        assert abs((a - b) / a - 0) < DELTA, msg
        a, b = Rmax, Rmax_a
        msg = f"For Rmax: Return {a} expected {b}"
        assert abs((a - b) / a - 0) < DELTA, msg

        Rmin_a, Rmax_a = Hole.comp_radius(test_obj.hole[0])
        a, b = Rmin, Rmin_a
        msg = f"For Rmin: Return {a} expected {b}"
        assert abs((a - b) / a - 0) < DELTA, msg

        a, b = Rmax, Rmax_a
        msg = f"For Rmax: Return {a} expected {b}"
        assert abs((a - b) / a - 0) < DELTA, msg


if __name__ == "__main__":
    a = Test_HoleM58_meth()
    for test_dict in HoleM58_test:
        a.test_schematics(test_dict)
        a.test_magnet_None(test_dict)
        a.test_magnet_Parallel(test_dict)
    print("Done")

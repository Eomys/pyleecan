# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotMPolar import SlotMPolar
from pyleecan.Classes.MagnetType15 import MagnetType15
from numpy import pi, exp, sqrt, arcsin
from pyleecan.Methods.Machine.Magnet.comp_height import comp_height
from pyleecan.Methods.Machine.Magnet.comp_surface import comp_surface
from pyleecan.Methods import ParentMissingError

mm = 1e-3


def comp_surface_analytical(slot):
    """compute the magnet surface analytically
    based on integration of magnet height over magnet (half) width
    magnet height: h(y) = sqrt(Rtop**2 - y**2) + x0 - sqrt(Rbottom**2 - y**2)
    """
    Z1, _ = slot.get_point_bottom()
    Rbottom = abs(Z1)
    Rtop = slot.magnet[0].Rtop
    Wmag = slot.magnet[0].Wmag
    Hmag = slot.magnet[0].Hmag

    x0 = Rbottom + Hmag - Rtop  #  reference point, i.e. center of top curve
    w = Wmag / 2

    s0 = x0 * w
    s1 = w / 2 * sqrt(Rtop ** 2 - w ** 2) + Rtop ** 2 / 2 * arcsin(w / Rtop)
    s2 = w / 2 * sqrt(Rbottom ** 2 - w ** 2) + Rbottom ** 2 / 2 * arcsin(w / Rbottom)

    surf = 2 * (s1 + s0 - s2)

    return surf


Mag15_test = list()
# Internal Slot inset magnet with same top and bottom radius
lam = LamSlotMag(Rint=40 * mm, Rext=110 * mm, is_internal=True)
lam.slot = SlotMPolar(Zs=4, W0=80 * pi / 180, H0=10 * mm)
lam.slot.magnet = [
    MagnetType15(Lmag=500 * mm, Hmag=20 * mm, Wmag=100 * mm, Rtop=100 * mm)
]
Mag15_test.append({"test_obj": lam, "Ao": 2 * arcsin(50 / 100), "H_exp": 20 * mm})

# Internal Slot inset magnet with same top and bottom radius
lam = LamSlotMag(Rint=40 * mm, Rext=110 * mm, is_internal=True)
lam.slot = SlotMPolar(Zs=4, W0=80 * pi / 180, H0=20 * mm)
lam.slot.magnet = [
    MagnetType15(Lmag=500 * mm, Hmag=20 * mm, Wmag=100 * mm, Rtop=100 * mm)
]
Mag15_test.append({"test_obj": lam, "Ao": 2 * arcsin(50 / 90), "H_exp": 20 * mm})

# Internal slot surface magnet with same top and bottom radius
lam = LamSlotMag(Rint=40 * mm, Rext=100 * mm, is_internal=True)
lam.slot = SlotMPolar(Zs=4, W0=80 * pi / 180, H0=0 * mm)
lam.slot.magnet = [
    MagnetType15(Lmag=500 * mm, Hmag=20 * mm, Wmag=100 * mm, Rtop=100 * mm)
]
Mag15_test.append({"test_obj": lam, "Ao": 2 * arcsin(50 / 100), "H_exp": 20 * mm})

# Internal slot surface magnet with different top and bottom radius
lam = LamSlotMag(Rint=40 * mm, Rext=100 * mm, is_internal=True)
lam.slot = SlotMPolar(Zs=4, W0=80 * pi / 180, H0=0 * mm)
lam.slot.magnet = [
    MagnetType15(Lmag=500 * mm, Hmag=20 * mm, Wmag=100 * mm, Rtop=65 * mm)
]
Mag15_test.append({"test_obj": lam, "Ao": 2 * arcsin(50 / 100), "H_exp": 20 * mm})

# For AlmostEqual
DELTA = 1e-4


@pytest.mark.METHODS
@pytest.mark.DEV
class Test_Magnet_Type_15_meth(object):
    """unittest for MagnetType15 methods"""

    @pytest.mark.parametrize("test_dict", Mag15_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_surface()

        a = result
        b = comp_surface_analytical(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", Mag15_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Compare numerical and analytical results
        b = comp_height(test_obj.slot.magnet[0])
        msg = "Analytical: " + str(a) + " Numerical " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", Mag15_test)
    def test_comp_angle_op(self, test_dict):
        """Check that the computation of the opening angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_angle_opening()

        a = result
        b = test_dict["Ao"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_build_geometry(self):
        """check that curve_list is correct"""

        with pytest.raises(ParentMissingError) as context:
            MagnetType15(Lmag=0.5, Hmag=0.02, Wmag=0.04, Rtop=0.04).build_geometry()

        lam = LamSlotMag(Rint=40 * mm, Rext=90 * mm, is_internal=True)
        lam.slot = SlotMPolar(Zs=4, W0=80 * pi / 180, H0=20 * mm)
        lam.slot.magnet = [
            MagnetType15(Lmag=500 * mm, Hmag=20 * mm, Wmag=100 * mm, Rtop=100 * mm)
        ]

        surface = lam.slot.magnet[0].build_geometry(is_simplified=True)

        assert len(surface) == 1
        assert surface[0].label == "MagnetRotorRadial_N_R0_T0_S0"

        lam = LamSlotMag(Rint=40e-3, Rext=90e-3, is_internal=True)
        lam.slot = SlotMPolar(Zs=4, W0=80 * pi / 180, H0=10 * mm)
        lam.slot.magnet = [
            MagnetType15(Lmag=500 * mm, Hmag=20 * mm, Wmag=100 * mm, Rtop=100 * mm)
        ]

        surface = lam.slot.magnet[0].build_geometry(is_simplified=True)

        assert len(surface) == 1
        assert surface[0].label == "MagnetRotorRadial_N_R0_T0_S0"

# -*- coding: utf-8 -*-

import pytest

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment

from pyleecan.Classes.MagnetType11 import MagnetType11
from pyleecan.Classes.LamSlotMag import LamSlotMag

from pyleecan.Classes.SlotMPolar import SlotMPolar
from numpy import pi, exp, angle, array
from pyleecan.Methods.Machine.Magnet.comp_surface import comp_surface

from pyleecan.Methods import ParentMissingError

Mag11_test = list()
# Internal Slot surface
lam = LamSlotMag(is_internal=True, Rext=0.5)
lam.slot = SlotMPolar(H0=0, W0=pi / 4, Zs=4)
lam.slot.magnet = [MagnetType11(Hmag=1, Wmag=pi / 4)]
Mag11_test.append({"test_obj": lam, "S_exp": 0.78539616, "Ao": pi / 4, "H_exp": 1})

# Internal Slot inset
lam = LamSlotMag(is_internal=True, Rext=0.5)
lam.slot = SlotMPolar(H0=40e-3, W0=pi / 4, Zs=4)
lam.slot.magnet = [MagnetType11(Hmag=20e-3, Wmag=pi / 4)]
Mag11_test.append({"test_obj": lam, "S_exp": 7.3827e-3, "Ao": pi / 4, "H_exp": 20e-3})

# Outward Slot inset
lam = LamSlotMag(is_internal=False, Rext=0.1325)
lam.slot = SlotMPolar(H0=5e-3, W0=pi / 10, Zs=8)
lam.slot.magnet = [MagnetType11(Hmag=8e-3, Wmag=pi / 12)]
Mag11_test.append({"test_obj": lam, "S_exp": 2.09439e-6, "Ao": pi / 12, "H_exp": 8e-3})

# For AlmostEqual
DELTA = 1e-4


@pytest.mark.METHODS
class Test_Magnet_Type_11_meth(object):
    """unittest for MagnetType11 methods"""

    @pytest.mark.parametrize("test_dict", Mag11_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

        # Compare numerical and analytical results
        b = comp_surface(test_obj.slot.magnet[0])
        msg = "Analytical: " + str(a) + " Numerical " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", Mag11_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    @pytest.mark.parametrize("test_dict", Mag11_test)
    def test_comp_angle_op(self, test_dict):
        """Check that the computation of the opening angle is correct"""
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.magnet[0].comp_angle_opening()

        a = result
        b = test_dict["Ao"]
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < DELTA, msg

    def test_build_geometry_out(self):
        """check that curve_list is correct (outwards magnet)"""
        lam = LamSlotMag(
            Rint=40e-3,
            Rext=90e-3,
            is_internal=False,
            is_stator=False,
            L1=0.45,
            Nrvd=1,
            Wrvd=0.05,
        )
        magnet = [MagnetType11(Wmag=pi / 10, Hmag=0.2)]
        lam.slot = SlotMPolar(Zs=8, W0=pi / 10, H0=0.2, magnet=magnet)
        test_obj = lam.slot.magnet[0]
        Z1 = (40e-3 + 0.2) * exp(-1j * pi / 10 / 2)
        Z2 = (40e-3 + 0.2) * exp(1j * pi / 10 / 2)

        Z = abs(Z1)

        Z3 = (Z - 0.2) * exp(1j * angle(Z1))
        Z4 = (Z - 0.2) * exp(1j * angle(Z2))

        # # Creation of curve
        curve_list = list()
        curve_list.append(Segment(Z1, Z3))
        curve_list.append(Arc1(Z3, Z4, abs(Z3)))
        curve_list.append(Segment(Z4, Z2))
        curve_list.append(Arc1(Z2, Z1, -abs(Z2)))

        surface = test_obj.build_geometry()
        result = surface[0].get_lines()
        for i in range(0, len(result)):
            a = result[i].begin
            b = curve_list[i].begin
            assert abs((a - b) / a - 0) < DELTA

            a = result[i].end
            b = curve_list[i].end
            assert abs((a - b) / a - 0) < DELTA

    def test_build_geometry_in(self):
        """check that curve_list is correct (inwards magnet)"""
        lam = LamSlotMag(
            Rint=40e-1,
            Rext=90e-1,
            is_internal=True,
            is_stator=False,
            L1=0.45,
            Nrvd=1,
            Wrvd=0.05,
        )
        magnet = [MagnetType11(Wmag=pi / 10, Hmag=0.2)]
        lam.slot = SlotMPolar(Zs=8, W0=pi / 10, H0=0.2, magnet=magnet)
        test_obj = lam.slot.magnet[0]
        Z1 = (90e-1 - 0.2) * exp(-1j * pi / 10 / 2)
        Z2 = (90e-1 - 0.2) * exp(1j * pi / 10 / 2)

        Z = abs(Z1)

        Z3 = (Z + 0.2) * exp(1j * angle(Z1))
        Z4 = (Z + 0.2) * exp(1j * angle(Z2))

        # # Creation of curve
        curve_list = list()
        curve_list.append(Segment(Z1, Z3))
        curve_list.append(Arc1(Z3, Z4, abs(Z3)))
        curve_list.append(Segment(Z4, Z2))
        curve_list.append(Arc1(Z2, Z1, -abs(Z2)))

        surface = test_obj.build_geometry()
        result = surface[0].get_lines()
        for i in range(0, len(result)):
            a = result[i].begin
            b = curve_list[i].begin
            assert abs((a - b) / a - 0) < DELTA

            a = result[i].end
            b = curve_list[i].end
            assert abs((a - b) / a - 0) < DELTA

    def test_comp_point_coordinate_error(self):
        """check that comp_point_coordinate is correct (throwing error)"""
        magnet = MagnetType11(Wmag=pi / 10, Hmag=0.2)
        with pytest.raises(ParentMissingError) as context:
            magnet._comp_point_coordinate()

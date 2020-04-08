# -*- coding: utf-8 -*-
from unittest import TestCase
from ddt import ddt, data

from numpy import ndarray, arcsin, exp
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotW12 import SlotW12
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Arc3 import Arc3
from pyleecan.Methods.Slot.Slot.comp_height import comp_height
from pyleecan.Methods.Slot.Slot.comp_surface import comp_surface
from pyleecan.Methods.Slot.Slot.comp_angle_opening import comp_angle_opening
from pyleecan.Methods.Slot.SlotWind.comp_surface_wind import comp_surface_wind

# For AlmostEqual
DELTA = 1e-4

slotW12_test = list()

# Internal Slot
lam = LamSlot(is_internal=True, Rext=0.1325)
lam.slot = SlotW12(H0=1e-3, H1=6e-3, R1=0.5e-3, R2=2e-3)
slotW12_test.append(
    {
        "test_obj": lam,
        "S_exp": 3.91088e-5,
        "Aw": 0.0299276,
        "SW_exp": 3.028318e-5,
        "H_exp": 1.0015e-2,
    }
)

# Outward Slot
lam = LamSlot(is_internal=False, Rint=0.1325)
lam.slot = SlotW12(H0=1e-3, H1=6e-3, R1=0.5e-3, R2=2e-3)
slotW12_test.append(
    {
        "test_obj": lam,
        "S_exp": 3.90283e-5,
        "Aw": 0.0273343,
        "SW_exp": 3.02831853e-5,
        "H_exp": 9.9849e-3,
    }
)


@ddt
class test_SlotW12_meth(TestCase):
    """unittest for SlotW12 methods"""

    @data(*slotW12_test)
    def test_comp_surface(self, test_dict):
        """Check that the computation of the surface is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface()

        a = result
        b = test_dict["S_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)
        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=1e-5, msg=msg)

    @data(*slotW12_test)
    def test_comp_surface_wind(self, test_dict):
        """Check that the computation of the winding surface is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_surface_wind()

        a = result
        b = test_dict["SW_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)
        # Check that the analytical method returns the same result as the numerical one
        b = comp_surface_wind(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=1e-5, msg=msg)

    @data(*slotW12_test)
    def test_comp_height(self, test_dict):
        """Check that the computation of the height is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_height()

        a = result
        b = test_dict["H_exp"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)
        # Check that the analytical method returns the same result as the numerical one
        b = comp_height(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=1e-5, msg=msg)

    @data(*slotW12_test)
    def test_comp_angle_opening(self, test_dict):
        """Check that the computation of the average opening angle iscorrect
        """
        test_obj = test_dict["test_obj"]
        a = test_obj.slot.comp_angle_opening()
        self.assertEqual(a, 2 * arcsin(2 * test_obj.slot.R2 / (2 * 0.1325)))
        # Check that the analytical method returns the same result as the numerical one
        b = comp_angle_opening(test_obj.slot)
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    @data(*slotW12_test)
    def test_comp_angle_wind_eq(self, test_dict):
        """Check that the computation of the average angle is correct
        """
        test_obj = test_dict["test_obj"]
        result = test_obj.slot.comp_angle_wind_eq()

        a = result
        b = test_dict["Aw"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, delta=DELTA, msg=msg)

    def test_build_geometry(self):
        """Check if the build_geometry of the slot is correct
        """
        test_obj = SlotW12(H0=1e-3, H1=6e-3, R1=0.5e-3, R2=2e-3)
        lam = LamSlot(is_internal=True, slot=test_obj, Rext=1)

        # Rbo = 1
        Z1 = exp(-1j * float(arcsin(2e-3)))
        Z2 = Z1 - 1e-3
        Z3 = Z2 - 1e-3
        Z4 = Z3 - 6e-3
        # symetry
        Z5 = Z4.conjugate()
        Z6 = Z3.conjugate()
        Z7 = Z2.conjugate()
        Z8 = Z1.conjugate()

        # creation of the curve
        curve_list = list()
        curve_list.append(Segment(Z1, Z2))
        curve_list.append(Arc3(Z2, Z3, True))
        curve_list.append(Segment(Z3, Z4))
        curve_list.append(Arc3(Z4, Z5, True))
        curve_list.append(Segment(Z5, Z6))
        curve_list.append(Arc3(Z6, Z7, True))
        curve_list.append(Segment(Z7, Z8))

        result = test_obj.build_geometry()
        self.assertEqual(len(result), len(curve_list))
        for i in range(0, len(result)):
            a = result[i].begin
            b = curve_list[i].begin
            self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)

            a = result[i].end
            b = curve_list[i].end
            self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)

    def test_build_geometry_wind(self):
        """Check if the build_geometry_wind works correctly
        """

        test_obj = SlotW12(H0=1e-3, H1=6e-3, R1=0.5e-3, R2=2e-3)
        lam = LamSlot(is_internal=True, slot=test_obj, Rext=1)

        # Rbo = 1
        Z1 = exp(-1j * float(arcsin(2e-3)))
        Z2 = Z1 - 1e-3
        Z3 = Z2 - 1e-3
        Z4 = Z3 - 6e-3
        # symetry
        Z5 = Z4.conjugate()
        Z6 = Z3.conjugate()
        Z7 = Z2.conjugate()
        Z8 = Z1.conjugate()

        Ztan1 = Z3.real
        Ztan2 = Z4.real - 2e-3

        Zrad2 = Z6 - (6e-3 + 2e-3) / 2
        Zrad1 = Z3 - (6e-3 + 2e-3) / 2

        Zmid = (Ztan1 + Ztan2) / 2

        expected = list()

        # part(0,0)
        curve_list = list()
        curve_list.append(Segment(Z3, Ztan1))
        curve_list.append(Segment(Ztan1, Zmid))
        curve_list.append(Segment(Zmid, Zrad1))
        curve_list.append(Segment(Zrad1, Z3))
        point_ref = (Z3 + Ztan1 + Zmid + Zrad1) / 4
        surface = SurfLine(
            line_list=curve_list, point_ref=point_ref, label="WindS_R0_T0_S0"
        )
        expected.append(surface)

        # part (1,0)
        curve_list = list()
        curve_list.append(Segment(Zrad1, Zmid))
        curve_list.append(Segment(Zmid, Ztan2))
        curve_list.append(Arc1(Ztan2, Z4, 2e-3))
        curve_list.append(Segment(Z4, Zrad1))
        point_ref = (Z4 + Ztan2 + Zmid + Zrad1) / 4
        surface = SurfLine(
            line_list=curve_list, point_ref=point_ref, label="WindS_R1_T0_S0"
        )
        expected.append(surface)

        # part(0, 1)

        curve_list = list()
        curve_list.append(Segment(Ztan1, Z6))
        curve_list.append(Segment(Z6, Zrad2))
        curve_list.append(Segment(Zrad2, Zmid))
        curve_list.append(Segment(Zmid, Ztan1))
        point_ref = (Z6 + Ztan1 + Zmid + Zrad2) / 4
        surface = SurfLine(
            line_list=curve_list, point_ref=point_ref, label="WindS_R0_T1_S0"
        )
        expected.append(surface)

        # part(1, 1)
        curve_list = list()
        curve_list.append(Segment(Zmid, Zrad2))
        curve_list.append(Segment(Zrad2, Z5))
        curve_list.append(Arc1(Z5, Ztan2, 2e-3))
        curve_list.append(Segment(Ztan2, Zmid))
        point_ref = (Z5 + Ztan2 + Zmid + Zrad2) / 4
        surface = SurfLine(
            line_list=curve_list, point_ref=point_ref, label="WindS_R1_T1_S0"
        )
        expected.append(surface)

        result = test_obj.build_geometry_wind(Nrad=2, Ntan=2)
        self.assertEqual(len(result), len(expected))
        for i in range(0, len(result)):
            self.assertEqual(len(result[i].line_list), len(expected[i].line_list))
            for jj in range(len(result[i].line_list)):
                a = result[i].line_list[jj].begin
                b = expected[i].line_list[jj].begin
                self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)

                a = result[i].line_list[jj].end
                b = expected[i].line_list[jj].end
                self.assertAlmostEqual((a - b) / a, 0, delta=DELTA)

            self.assertTrue(result[i].label == expected[i].label)

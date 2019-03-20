# -*- coding: utf-8 -*-

from unittest import TestCase, skip

from ddt import ddt, data
from mock import MagicMock
from numpy import array, pi, zeros

from pyleecan.Classes.Machine import Machine
from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.HoleM50 import HoleM50
from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.Shaft import Shaft

# For AlmostEqual
DELTA = 1e-4

M_test = list()
test_obj = Machine()
test_obj.rotor = LamHole(
    is_internal=True, Rint=0.021, Rext=0.075, is_stator=False, L1=0.7, Nrvd=0, Kf1=0.95
)
test_obj.rotor.hole = list()
test_obj.rotor.hole.append(
    HoleM50(
        Zh=8,
        W0=50e-3,
        W1=2e-3,
        W2=1e-3,
        W3=1e-3,
        W4=20.6e-3,
        H0=17.3e-3,
        H1=1.25e-3,
        H2=0.5e-3,
        H3=6.8e-3,
        H4=0,
    )
)
test_obj.rotor.hole[0].magnet_0.Lmag = 0.3
test_obj.rotor.hole[0].magnet_1.Lmag = 0.5
test_obj.rotor.hole[0].magnet_0.mat_type.struct.rho = 1000
test_obj.rotor.hole[0].magnet_1.mat_type.struct.rho = 1000
test_obj.rotor.axial_vent = list()
test_obj.rotor.axial_vent.append(VentilationCirc(Zh=8, Alpha0=0, D0=5e-3, H0=40e-3))
test_obj.rotor.axial_vent.append(
    VentilationCirc(Zh=8, Alpha0=pi / 8, D0=7e-3, H0=40e-3)
)
test_obj.rotor.mat_type.struct.rho = 7600
test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=1.2)
test_obj.shaft.mat_type.struct.rho = 5000
test_obj.stator = Lamination(
    Rint=0.078, Rext=0.104, is_internal=False, is_stator=True, L1=0.8, Nrvd=0, Kf1=0.95
)
test_obj.stator.axial_vent.append(
    VentilationPolar(Zh=8, H0=0.08, D0=0.01, W1=pi / 8, Alpha0=pi / 8)
)
test_obj.stator.axial_vent.append(
    VentilationPolar(Zh=8, H0=0.092, D0=0.01, W1=pi / 8, Alpha0=0)
)
test_obj.stator.mat_type.struct.rho = 8000
test_obj.frame = Frame(Rint=0.104, Rext=0.114, Lfra=1)
test_obj.frame.mat_type.struct.rho = 4000

M_test.append(
    {
        "test_obj": test_obj,
        "Mfra": 4000 * pi * (0.114 ** 2 - 0.104 ** 2),
        "Msha": 5000 * 1.2 * pi * 0.021 ** 2,
    }
)
M_test[-1]["rotor"] = {
    "Slam": 1.2797e-2,
    "Svent": 8 * pi * (2.5e-3 ** 2 + 3.5e-3 ** 2),
    "Smag": 6.8e-3 * 20.6e-3 * 2 * 8,
}
M_test[-1]["rotor"]["Vlam"] = M_test[-1]["rotor"]["Slam"] * 0.7
M_test[-1]["rotor"]["Vvent"] = M_test[-1]["rotor"]["Svent"] * 0.7
M_test[-1]["rotor"]["Vmag"] = M_test[-1]["rotor"]["Smag"] * 0.4
M_test[-1]["Mrot"] = (
    M_test[-1]["rotor"]["Vmag"] * 1000 + M_test[-1]["rotor"]["Vlam"] * 7600 * 0.95
)

M_test[-1]["stator"] = {"Slam": 9.1483e-3, "Svent": 5.7177e-3}
M_test[-1]["stator"]["Vlam"] = M_test[-1]["stator"]["Slam"] * 0.8
M_test[-1]["stator"]["Vvent"] = M_test[-1]["stator"]["Svent"] * 0.8
M_test[-1]["Msta"] = M_test[-1]["stator"]["Vlam"] * 8000 * 0.95

M_test[-1]["Mmach"] = (
    M_test[-1]["Mrot"] + M_test[-1]["Msta"] + M_test[-1]["Mfra"] + M_test[-1]["Msha"]
)


@ddt
class test_comp_mass_meth(TestCase):
    """unittest for comp_mass (and volume and surface) methods"""

    @data(*M_test)
    def test_comp_surface_rotor(self, test_dict):
        """Check that the computation of the surface is correct
        """
        result = test_obj.rotor.comp_surfaces()

        a = result["Slam"]
        b = test_dict["rotor"]["Slam"]
        msg = "For Slam, Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

        a = result["Svent"]
        b = test_dict["rotor"]["Svent"]
        msg = "For Svent, Return " + str(a) + " expected " + str(b)
        if b == 0:
            self.assertEqual(a, b, msg=msg)
        else:
            self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

        if "Smag" in result.keys():
            a = result["Smag"]
            b = test_dict["rotor"]["Smag"]
            msg = "For Smag, Return " + str(a) + " expected " + str(b)
            self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

    @data(*M_test)
    def test_comp_surface_stator(self, test_dict):
        """Check that the computation of the surface is correct
        """
        result = test_obj.stator.comp_surfaces()

        a = result["Slam"]
        b = test_dict["stator"]["Slam"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

        a = result["Svent"]
        b = test_dict["stator"]["Svent"]
        msg = "Return " + str(a) + " expected " + str(b)
        if b == 0:
            self.assertEqual(a, b, msg=msg)
        else:
            self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

        if "Smag" in result.keys():
            a = result["Smag"]
            b = test_dict["stator"]["Smag"]
            msg = "Return " + str(a) + " expected " + str(b)
            self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

    @data(*M_test)
    def test_comp_volume_rotor(self, test_dict):
        """Check that the computation of the volume is correct
        """
        result = test_obj.rotor.comp_volumes()

        a = result["Vlam"]
        b = test_dict["rotor"]["Vlam"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

        a = result["Vvent"]
        b = test_dict["rotor"]["Vvent"]
        msg = "Return " + str(a) + " expected " + str(b)
        if b == 0:
            self.assertEqual(a, b, msg=msg)
        else:
            self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

        if "Vmag" in result.keys():
            a = result["Vmag"]
            b = test_dict["rotor"]["Vmag"]
            msg = "Return " + str(a) + " expected " + str(b)
            self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

    @data(*M_test)
    def test_comp_volume_stator(self, test_dict):
        """Check that the computation of the volume is correct
        """
        result = test_obj.stator.comp_volumes()

        a = result["Vlam"]
        b = test_dict["stator"]["Vlam"]
        msg = "Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

        a = result["Vvent"]
        b = test_dict["stator"]["Vvent"]
        msg = "Return " + str(a) + " expected " + str(b)
        if b == 0:
            self.assertEqual(a, b, msg=msg)
        else:
            self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

        if "Vmag" in result.keys():
            a = result["Vmag"]
            b = test_dict["stator"]["Vmag"]
            msg = "Return " + str(a) + " expected " + str(b)
            self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

    @data(*M_test)
    def test_comp_mass(self, test_dict):
        """Check that the computation of the mass is correct
        """
        result = test_obj.comp_masses()

        a = result["Mfra"]
        b = test_dict["Mfra"]
        msg = "Mfra, Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

        a = result["Msha"]
        b = test_dict["Msha"]
        msg = "Msha, Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

        a = result["Mrot"]["Mtot"]
        b = test_dict["Mrot"]
        msg = "Mrot, Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

        a = result["Msta"]["Mtot"]
        b = test_dict["Msta"]
        msg = "Msta, Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

        a = result["Mmach"]
        b = test_dict["Mmach"]
        msg = "Mmach, Return " + str(a) + " expected " + str(b)
        self.assertAlmostEqual((a - b) / a, 0, msg=msg, delta=DELTA)

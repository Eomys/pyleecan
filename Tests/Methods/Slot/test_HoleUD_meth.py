# -*- coding: utf-8 -*-

from os.path import isfile, join
import pytest

from pyleecan.Classes.HoleUD import HoleUD
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.MagnetType10 import MagnetType10
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load

# For AlmostEqual
DELTA = 1e-4

mach_path = join(DATA_DIR, "Machine", "IPMSM_A.json")
if isfile(mach_path):
    IPMSM_A = load(mach_path)

    surf_list = IPMSM_A.rotor.hole[0].build_geometry()
    magnet_dict = {
        "magnet_0": IPMSM_A.rotor.hole[0].magnet_0,
        "magnet_1": IPMSM_A.rotor.hole[0].magnet_1,
    }

    HUD = HoleUD(Zh=4, surf_list=surf_list, magnet_dict=magnet_dict)

    IPMSM_B = IPMSM_A.copy()
    IPMSM_B.rotor.hole[0] = HUD

@pytest.mark.METHODS
class Test_HoleUD_meth(object):
    def test_comp_magnet_surface(self):
        """Check that the computation of the magnet surface"""
        exp = IPMSM_A.rotor.hole[0].comp_surface_magnets()
        result = IPMSM_B.rotor.hole[0].comp_surface_magnets()

        assert exp == pytest.approx(result, rel=0.01)


    def test_comp_surface(self):
        """Check that the computation of the slot surface is correct"""
        exp = IPMSM_A.rotor.hole[0].comp_surface()
        result = IPMSM_B.rotor.hole[0].comp_surface()

        assert exp == pytest.approx(result, rel=0.01)


    def test_build_geometry_no_mag(self):
        """check that curve_list is correct (Remove magnet)"""
        assert IPMSM_B.rotor.hole[0].magnet_dict["magnet_0"] is not None
        assert IPMSM_B.rotor.hole[0].magnet_dict["magnet_1"] is not None
        IPMSM_B.rotor.hole[0].remove_magnet()
        assert IPMSM_B.rotor.hole[0].magnet_dict["magnet_0"] is None
        assert IPMSM_B.rotor.hole[0].magnet_dict["magnet_1"] is None

        surf_list = IPMSM_B.rotor.hole[0].build_geometry()

        assert len(surf_list) == 5
        for ii, surf in enumerate(surf_list):
            assert type(surf) is SurfLine
            assert surf.label == "Hole_Rotor_R0_T" + str(ii) + "_S0"

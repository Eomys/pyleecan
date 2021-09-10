# -*- coding: utf-8 -*-

from os.path import join
import pytest

from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Methods.Slot.VentilationCirc import CircleBuildGeometryError
from pyleecan.Classes.Hole import Hole

"""unittest for VentilationCirc"""


class Test_VentilationCirc(object):
    @pytest.fixture
    def vent(self):
        """Run at the begining of every test to setup the VentilationCirc"""
        test_obj = VentilationCirc(Zh=8, Alpha0=0, D0=5e-3, H0=40e-3)
        lam = Lamination(is_stator=True, axial_vent=[test_obj])

        return test_obj

    def test_build_geometry_errors(self, vent):
        """Test that build_geometry can raise some errors"""
        with pytest.raises(CircleBuildGeometryError) as context:
            vent.build_geometry(alpha="dz")
        with pytest.raises(CircleBuildGeometryError) as context:
            vent.build_geometry(alpha=1, delta="dz")

    def test_build_geometry(self, vent):
        """Test that build_geometry works"""
        result = vent.build_geometry()

        assert len(result) == 1

    def test_comp_surface(self, vent):
        """Check that the computation of the surface is correct"""
        # Check that the analytical method returns the same result as the numerical one
        a = vent.comp_surface()
        b = Hole.comp_surface(vent)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < 1e-4, msg

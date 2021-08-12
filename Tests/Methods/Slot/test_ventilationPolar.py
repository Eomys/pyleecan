# -*- coding: utf-8 -*-

from os.path import join
import pytest
from numpy import pi

from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Methods.Slot.VentilationPolar import PolarArcBuildGeometryError
from pyleecan.Classes.Hole import Hole

"""unittest for VentilationPolar"""


class Test_VentilationPolar(object):
    @pytest.fixture
    def vent(self):
        """Run at the begining of every test to setup the VentilationPolar"""
        test_obj = VentilationPolar(Zh=8, H0=0.08, D0=0.01, W1=pi / 8, Alpha0=pi / 8)
        lam = Lamination(is_stator=True, axial_vent=[test_obj])

        return test_obj

    def test_build_geometry_errors(self, vent):
        """Test that build_geometry can raise some errors"""
        with pytest.raises(PolarArcBuildGeometryError) as context:
            vent.build_geometry(alpha="dz")
        with pytest.raises(PolarArcBuildGeometryError) as context:
            vent.build_geometry(alpha=1, delta="dz")

    def test_comp_surface(self, vent):
        """Check that the computation of the surface is correct"""
        # Check that the analytical method returns the same result as the numerical one
        a = vent.comp_surface()
        b = Hole.comp_surface(vent)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < 1e-4, msg

# -*- coding: utf-8 -*-

from os.path import join
import pytest
from numpy import pi

from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.Methods.Slot.VentilationTrap import TrapezeBuildGeometryError
from pyleecan.Classes.Hole import Hole

"""unittest for VentilationTrap"""


class Test_VentilationTrap(object):
    @pytest.fixture
    def vent(self):
        """Run at the begining of every test to setup the VentilationTrap"""
        test_obj = VentilationTrap(
            Zh=6, Alpha0=pi / 6, W1=30e-3, W2=60e-3, D0=0.05, H0=0.3
        )
        lam = Lamination(is_stator=True, axial_vent=[test_obj])

        return test_obj

    def test_build_geometry_errors(self, vent):
        """Test that build_geometry can raise some errors"""
        with pytest.raises(TrapezeBuildGeometryError) as context:
            vent.build_geometry(alpha="dz")
        with pytest.raises(TrapezeBuildGeometryError) as context:
            vent.build_geometry(alpha=1, delta="dz")

    def test_comp_surface(self, vent):
        """Check that the computation of the surface is correct"""
        # Check that the analytical method returns the same result as the numerical one
        a = vent.comp_surface()
        b = Hole.comp_surface(vent)
        msg = "Return " + str(a) + " expected " + str(b)
        assert abs((a - b) / a - 0) < 1e-4, msg

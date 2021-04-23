# -*- coding: utf-8 -*-

from os.path import join
import pytest
from numpy import pi

from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.Methods.Slot.VentilationTrap import TrapezeBuildGeometryError


"""unittest for VentilationTrap"""


class Test_VentilationTrap(object):
    @pytest.fixture
    def vent(self):
        """Run at the begining of every test to setup the VentilationTrap"""
        test_obj = VentilationTrap(
            Zh=6, Alpha0=pi / 6, W1=30e-3, W2=60e-3, D0=0.05, H0=0.3
        )

        return test_obj

    def test_build_geometry_errors(self, vent):
        """Test that build_geometry can raise some errors"""
        with pytest.raises(TrapezeBuildGeometryError) as context:
            vent.build_geometry(sym=0.2)
        with pytest.raises(TrapezeBuildGeometryError) as context:
            vent.build_geometry(sym=1, alpha="dz")
        with pytest.raises(TrapezeBuildGeometryError) as context:
            vent.build_geometry(sym=1, alpha=1, delta="dz")

    def test_build_geometry(self, vent):
        """Test that build_geometry works"""
        result = vent.build_geometry()

        assert len(result) == 6

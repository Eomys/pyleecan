# -*- coding: utf-8 -*-

from os.path import join
import pytest

from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Methods.Slot.VentilationCirc import CircleBuildGeometryError


"""unittest for VentilationCirc"""


class Test_VentilationCirc(object):
    @pytest.fixture
    def vent(self):
        """Run at the begining of every test to setup the VentilationCirc"""
        test_obj = VentilationCirc(Zh=8, Alpha0=0, D0=5e-3, H0=40e-3)

        return test_obj

    def test_build_geometry_errors(self, vent):
        """Test that build_geometry can raise some errors"""
        with pytest.raises(CircleBuildGeometryError) as context:
            vent.build_geometry(sym=0.2)
        with pytest.raises(CircleBuildGeometryError) as context:
            vent.build_geometry(sym=1, alpha="dz")
        with pytest.raises(CircleBuildGeometryError) as context:
            vent.build_geometry(sym=1, alpha=1, delta="dz")

    def test_build_geometry(self, vent):
        """Test that build_geometry works"""
        result = vent.build_geometry()

        assert len(result) == 8

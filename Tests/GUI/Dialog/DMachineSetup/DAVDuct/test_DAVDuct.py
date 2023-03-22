# -*- coding: utf-8 -*-

import sys
import matplotlib.pyplot as plt
import pytest
from PySide2 import QtWidgets

from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.GUI.Dialog.DMachineSetup.DAVDuct.DAVDuct import DAVDuct
from pyleecan.GUI.Dialog.DMachineSetup.DAVDuct.PVentCirc.PVentCirc import (
    PVentCirc,
)
from pyleecan.GUI.Dialog.DMachineSetup.DAVDuct.PVentPolar.PVentPolar import (
    PVentPolar,
)
from pyleecan.GUI.Dialog.DMachineSetup.DAVDuct.PVentTrap.PVentTrap import (
    PVentTrap,
)
from Tests.GUI.Dialog.DMachineSetup.DAVDuct import (
    VENT_CIRC_INDEX,
    VENT_POLAR_INDEX,
    VENT_TRAP_INDEX,
)


class TestDAVDuct(object):
    """Test that the widget DAVDuct behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        print("\nStart Test TestDAVDuct")
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    def setup_method(self):
        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        self.test_obj = Lamination(Rint=0.1, Rext=1, is_stator=True, is_internal=True)
        self.test_obj.axial_vent.append(
            VentilationCirc(Zh=8, H0=10e-3, D0=40e-3, Alpha0=0)
        )
        self.test_obj.axial_vent.append(
            VentilationCirc(Zh=9, H0=20e-3, D0=50e-3, Alpha0=0)
        )

        self.widget = DAVDuct(self.test_obj)
        self.widget.is_test = True
        self.widget.tab_vent.widget(0).is_test = True

    @pytest.mark.Vent
    def test_init_all_type(self):
        """Check that you can combine several kind of ventilations"""
        test_obj = Lamination(Rint=0.1, Rext=1, is_stator=True, is_internal=True)
        test_obj.axial_vent.append(VentilationCirc(Zh=8, H0=10e-3, D0=40e-3, Alpha0=0))
        test_obj.axial_vent.append(
            VentilationTrap(Zh=4, H0=24e-3, D0=34e-3, W1=44e-3, W2=54e-3, Alpha0=0)
        )
        test_obj.axial_vent.append(
            VentilationPolar(Zh=3, H0=23e-3, D0=33e-3, W1=43e-3, Alpha0=0)
        )

        self.widget = DAVDuct(test_obj)

        assert self.widget.tab_vent.count() == 3
        assert self.widget.tab_vent.currentIndex() == 0

        # First set
        assert type(self.widget.tab_vent.widget(0).w_vent) == PVentCirc
        assert (
            self.widget.tab_vent.widget(0).c_vent_type.currentIndex() == VENT_CIRC_INDEX
        )
        assert self.widget.tab_vent.widget(0).w_vent.si_Zh.value() == 8

        # 2nd set
        assert type(self.widget.tab_vent.widget(1).w_vent) == PVentTrap
        assert (
            self.widget.tab_vent.widget(1).c_vent_type.currentIndex() == VENT_TRAP_INDEX
        )
        assert self.widget.tab_vent.widget(1).w_vent.si_Zh.value() == 4

        # 3rd set
        assert type(self.widget.tab_vent.widget(2).w_vent) == PVentPolar
        assert (
            self.widget.tab_vent.widget(2).c_vent_type.currentIndex()
            == VENT_POLAR_INDEX
        )
        assert self.widget.tab_vent.widget(2).w_vent.si_Zh.value() == 3


if __name__ == "__main__":
    a = TestDAVDuct()
    a.setup_class()
    a.setup_method()
    a.test_init_all_type()
    a.teardown_class()
    print("Done")

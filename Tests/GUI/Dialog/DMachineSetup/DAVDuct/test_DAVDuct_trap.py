# -*- coding: utf-8 -*-

import sys

import pytest
from qtpy import QtWidgets
from qtpy.QtWidgets import QTabBar

from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.GUI.Dialog.DMachineSetup.DAVDuct.DAVDuct import DAVDuct
from pyleecan.GUI.Dialog.DMachineSetup.DAVDuct.PVentTrap.PVentTrap import (
    PVentTrap,
)
from Tests.GUI.Dialog.DMachineSetup.DAVDuct import VENT_TRAP_INDEX
from numpy import pi


class TestDAVDuctTrap(object):
    """Test that the widget DAVDuct behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = Lamination(Rint=0.1, Rext=1, is_stator=True, is_internal=True)
        test_obj.axial_vent.append(
            VentilationTrap(Zh=4, H0=24e-3, D0=34e-3, W1=44e-3, W2=54e-3, Alpha0=0)
        )
        test_obj.axial_vent.append(
            VentilationTrap(Zh=4, H0=25e-3, D0=35e-3, W1=45e-3, W2=55e-3, Alpha0=0)
        )

        widget = DAVDuct(test_obj)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    @pytest.mark.Vent
    def test_init_trap(self, setup):
        """Check that the Widget initialise for trap ventilations"""
        # Init the widget with Polar vent

        setup["test_obj"].axial_vent = [
            VentilationTrap(Zh=4, H0=24e-3, D0=34e-3, W1=44e-3, W2=54e-3, Alpha0=0)
        ]
        setup["widget"] = DAVDuct(setup["test_obj"])

        assert setup["widget"].tab_vent.count() == 1
        assert setup["widget"].tab_vent.currentIndex() == 0

        # First set
        assert type(setup["widget"].tab_vent.widget(0).w_vent) == PVentTrap
        assert (
            setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex()
            == VENT_TRAP_INDEX
        )
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 4
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_H0.value() == 24e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_D0.value() == 34e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_W1.value() == 44e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_W2.value() == 54e-3
        assert setup["widget"].tab_vent.widget(0).lf_Alpha0.value() == 0

        # Set Values
        setup["widget"].tab_vent.widget(0).w_vent.si_Zh.setValue(12)
        setup["widget"].tab_vent.widget(0).w_vent.lf_H0.setValue(12e-3)
        setup["widget"].tab_vent.widget(0).w_vent.lf_D0.setValue(42e-3)
        setup["widget"].tab_vent.widget(0).w_vent.lf_W1.setValue(45e-3)
        setup["widget"].tab_vent.widget(0).w_vent.lf_W2.setValue(55e-3)
        setup["widget"].tab_vent.widget(0).lf_Alpha0.setValue(0.3)
        # Raise signal to update object
        setup["widget"].tab_vent.widget(0).w_vent.lf_H0.editingFinished.emit()
        setup["widget"].tab_vent.widget(0).w_vent.lf_D0.editingFinished.emit()
        setup["widget"].tab_vent.widget(0).w_vent.lf_W1.editingFinished.emit()
        setup["widget"].tab_vent.widget(0).w_vent.lf_W2.editingFinished.emit()
        setup["widget"].tab_vent.widget(0).lf_Alpha0.editingFinished.emit()
        # Check changes
        assert setup["widget"].lam.axial_vent[0].Zh == 12
        assert setup["widget"].lam.axial_vent[0].H0 == 12e-3
        assert setup["widget"].lam.axial_vent[0].D0 == 42e-3
        assert setup["widget"].lam.axial_vent[0].W1 == 45e-3
        assert setup["widget"].lam.axial_vent[0].W2 == 55e-3
        assert setup["widget"].lam.axial_vent[0].Alpha0 == 0.3

        # Check set Alpha0 in [deg]
        setup["widget"].tab_vent.widget(0).c_Alpha0_unit.setCurrentIndex(1)
        assert setup["widget"].tab_vent.widget(0).c_Alpha0_unit.currentText() == "[°]"
        setup["widget"].tab_vent.widget(0).lf_Alpha0.setValue(18)
        assert (
            setup["widget"].tab_vent.widget(0).lf_Alpha0.text() == "18"
        )  # check validator top
        setup["widget"].tab_vent.widget(0).lf_Alpha0.editingFinished.emit()
        assert setup["widget"].lam.axial_vent[0].Alpha0 == pi / 10

    @pytest.mark.Vent
    def test_add_trap(self, setup):
        """Test that you can add trap ventilation"""
        setup["widget"].b_new.clicked.emit()

        assert setup["widget"].tab_vent.count() == 3
        assert setup["widget"].tab_vent.currentIndex() == 0

        # First set
        assert type(setup["widget"].tab_vent.widget(0).w_vent) == PVentTrap
        assert (
            setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex()
            == VENT_TRAP_INDEX
        )
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 4
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_H0.value() == 24e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_D0.value() == 34e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_W1.value() == 44e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_W2.value() == 54e-3
        assert setup["widget"].tab_vent.widget(0).lf_Alpha0.value() == 0

        # Second set
        assert type(setup["widget"].tab_vent.widget(1).w_vent) == PVentTrap
        assert (
            setup["widget"].tab_vent.widget(1).c_vent_type.currentIndex()
            == VENT_TRAP_INDEX
        )
        assert setup["widget"].tab_vent.widget(1).w_vent.si_Zh.value() == 4
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_H0.value() == 25e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_D0.value() == 35e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_W1.value() == 45e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_W2.value() == 55e-3
        assert setup["widget"].tab_vent.widget(1).lf_Alpha0.value() == 0

        # Third set
        setup["widget"].tab_vent.widget(2).c_vent_type.setCurrentIndex(VENT_TRAP_INDEX)
        assert type(setup["widget"].tab_vent.widget(2).w_vent) == PVentTrap
        assert (
            setup["widget"].tab_vent.widget(2).c_vent_type.currentIndex()
            == VENT_TRAP_INDEX
        )
        assert setup["widget"].tab_vent.widget(2).w_vent.si_Zh.value() == 8
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_H0.value() == None
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_D0.value() == None
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_W1.value() == None
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_W2.value() == None
        assert setup["widget"].tab_vent.widget(2).lf_Alpha0.value() == 0

    @pytest.mark.Vent
    def test_remove_trap(self, setup):
        """Test that you can remove trap ventilation"""
        b_remove = (
            setup["widget"]
            .tab_vent.tabBar()
            .tabButton(setup["widget"].tab_vent.count() - 1, QTabBar.RightSide)
        )
        b_remove.clicked.emit()
        assert setup["widget"].tab_vent.count() == 1
        assert setup["widget"].tab_vent.currentIndex() == 0

        # First set
        assert type(setup["widget"].tab_vent.widget(0).w_vent) == PVentTrap
        assert (
            setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex()
            == VENT_TRAP_INDEX
        )
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 4
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_H0.value() == 24e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_D0.value() == 34e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_W1.value() == 44e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_W2.value() == 54e-3
        assert setup["widget"].tab_vent.widget(0).lf_Alpha0.value() == 0

    @pytest.mark.Vent
    def test_check_PVentTrap(self, setup):
        """Test that check of PVentTrap"""
        VentilationTrap(Zh=4, H0=24e-3, D0=34e-3, W1=44e-3, W2=54e-3, Alpha0=0)

        lam = Lamination(Rint=0.1, Rext=1, is_stator=True, is_internal=True)
        vent = VentilationTrap(
            Zh=4, H0=24e-3, D0=34e-3, W1=44e-3, W2=54e-3, Alpha0=None
        )
        assert PVentTrap(vent=vent, lam=lam).check() is None
        assert vent.Alpha0 == 0  # check set default value to 0

        vent = VentilationTrap(Zh=4, H0=24e-3, D0=34e-3, W1=44e-3, W2=None, Alpha0=0)
        assert PVentTrap(vent=vent, lam=lam).check() == "You must set W2 !"

        vent = VentilationTrap(Zh=4, H0=24e-3, D0=34e-3, W1=None, W2=54e-3, Alpha0=0)
        assert PVentTrap(vent=vent, lam=lam).check() == "You must set W1 !"

        vent = VentilationTrap(Zh=4, H0=24e-3, D0=None, W1=44e-3, W2=54e-3, Alpha0=0)
        assert PVentTrap(vent=vent, lam=lam).check() == "You must set D0 !"

        vent = VentilationTrap(Zh=4, H0=None, D0=34e-3, W1=44e-3, W2=54e-3, Alpha0=0)
        assert PVentTrap(vent=vent, lam=lam).check() == "You must set H0 !"

        pvent = PVentTrap(vent=vent, lam=lam)
        pvent.vent.Zh = None
        assert pvent.check() == "You must set Zh !"

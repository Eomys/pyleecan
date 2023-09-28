# -*- coding: utf-8 -*-

import sys

import pytest
from PySide2 import QtWidgets
from PySide2.QtWidgets import QTabBar

from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.GUI.Dialog.DMachineSetup.DAVDuct.DAVDuct import DAVDuct
from pyleecan.GUI.Dialog.DMachineSetup.DAVDuct.PVentPolar.PVentPolar import (
    PVentPolar,
)
from Tests.GUI.Dialog.DMachineSetup.DAVDuct import VENT_POLAR_INDEX
from numpy import pi


class TestDAVDuctPolar(object):
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
            VentilationPolar(Zh=1, H0=21e-3, D0=31e-3, W1=41e-3, Alpha0=0)
        )
        test_obj.axial_vent.append(
            VentilationPolar(Zh=2, H0=22e-3, D0=32e-3, W1=42e-3, Alpha0=0)
        )

        widget = DAVDuct(test_obj)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    @pytest.mark.Vent
    def test_init_polar(self, setup):
        """Check that the Widget initialise for polar ventilations"""
        # Init the widget with Polar vent
        vent = list()
        vent.append(VentilationPolar(Zh=1, H0=21e-3, D0=31e-3, W1=41e-3, Alpha0=0))
        vent.append(VentilationPolar(Zh=2, H0=22e-3, D0=32e-3, W1=42e-3, Alpha0=0))
        vent.append(VentilationPolar(Zh=3, H0=23e-3, D0=33e-3, W1=43e-3, Alpha0=0))

        setup["test_obj"].axial_vent = vent
        setup["widget"] = DAVDuct(setup["test_obj"])

        assert setup["widget"].tab_vent.count() == 3
        assert setup["widget"].tab_vent.currentIndex() == 0

        # First set
        assert type(setup["widget"].tab_vent.widget(0).w_vent) == PVentPolar
        assert (
            setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex()
            == VENT_POLAR_INDEX
        )
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 1
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_H0.value() == 21e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_D0.value() == 31e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_W1.value() == 41e-3
        assert setup["widget"].tab_vent.widget(0).lf_Alpha0.value() == 0

        # 2nd set
        assert type(setup["widget"].tab_vent.widget(1).w_vent) == PVentPolar
        assert (
            setup["widget"].tab_vent.widget(1).c_vent_type.currentIndex()
            == VENT_POLAR_INDEX
        )
        assert setup["widget"].tab_vent.widget(1).w_vent.si_Zh.value() == 2
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_H0.value() == 22e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_D0.value() == 32e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_W1.value() == 42e-3
        assert setup["widget"].tab_vent.widget(1).lf_Alpha0.value() == 0

        # 3rd set
        assert type(setup["widget"].tab_vent.widget(2).w_vent) == PVentPolar
        assert (
            setup["widget"].tab_vent.widget(2).c_vent_type.currentIndex()
            == VENT_POLAR_INDEX
        )
        assert setup["widget"].tab_vent.widget(2).w_vent.si_Zh.value() == 3
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_H0.value() == 23e-3
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_D0.value() == 33e-3
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_W1.value() == 43e-3
        assert setup["widget"].tab_vent.widget(2).lf_Alpha0.value() == 0

        # Set Values
        setup["widget"].tab_vent.widget(1).w_vent.si_Zh.setValue(9)
        setup["widget"].tab_vent.widget(1).w_vent.lf_H0.setValue(33e-3)
        setup["widget"].tab_vent.widget(1).w_vent.lf_D0.setValue(44e-3)
        setup["widget"].tab_vent.widget(1).w_vent.lf_W1.setValue(55e-3)
        setup["widget"].tab_vent.widget(1).lf_Alpha0.setValue(0.4)
        # Raise signal to update object
        setup["widget"].tab_vent.widget(1).w_vent.lf_H0.editingFinished.emit()
        setup["widget"].tab_vent.widget(1).w_vent.lf_D0.editingFinished.emit()
        setup["widget"].tab_vent.widget(1).w_vent.lf_W1.editingFinished.emit()
        setup["widget"].tab_vent.widget(1).lf_Alpha0.editingFinished.emit()
        # Check changes
        assert setup["widget"].lam.axial_vent[1].Zh == 9
        assert setup["widget"].lam.axial_vent[1].H0 == 33e-3
        assert setup["widget"].lam.axial_vent[1].D0 == 44e-3
        assert setup["widget"].lam.axial_vent[1].W1 == 55e-3
        assert setup["widget"].lam.axial_vent[1].Alpha0 == 0.4
        # Check set Alpha0 in [deg]
        setup["widget"].tab_vent.widget(0).c_Alpha0_unit.setCurrentIndex(1)
        assert setup["widget"].tab_vent.widget(0).c_Alpha0_unit.currentText() == "[°]"
        setup["widget"].tab_vent.widget(0).lf_Alpha0.setValue(18)
        assert (
            setup["widget"].tab_vent.widget(0).lf_Alpha0.text() == "18"
        )  # check validator top
        setup["widget"].tab_vent.widget(0).lf_Alpha0.editingFinished.emit()
        assert setup["widget"].lam.axial_vent[0].Alpha0 == pi / 10

        # Check set W1 in [deg]
        setup["widget"].tab_vent.widget(0).w_vent.c_W1_unit.setCurrentIndex(1)
        assert (
            setup["widget"].tab_vent.widget(0).w_vent.c_W1_unit.currentText() == "[°]"
        )
        setup["widget"].tab_vent.widget(0).w_vent.lf_W1.setValue(9)
        assert (
            setup["widget"].tab_vent.widget(0).w_vent.lf_W1.text() == "9"
        )  # check validator top
        setup["widget"].tab_vent.widget(0).w_vent.lf_W1.editingFinished.emit()
        assert setup["widget"].lam.axial_vent[0].W1 == pi / 20

    @pytest.mark.Vent
    def test_add_polar(self, setup):
        """Test that you can add polar ventilation"""
        setup["widget"].b_new.clicked.emit()

        assert setup["widget"].tab_vent.count() == 3
        assert setup["widget"].tab_vent.currentIndex() == 0

        # First set
        assert type(setup["widget"].tab_vent.widget(0).w_vent) == PVentPolar
        assert (
            setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex()
            == VENT_POLAR_INDEX
        )
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 1
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_H0.value() == 21e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_D0.value() == 31e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_W1.value() == 41e-3
        assert setup["widget"].tab_vent.widget(0).lf_Alpha0.value() == 0

        # Second set
        assert type(setup["widget"].tab_vent.widget(1).w_vent) == PVentPolar
        assert (
            setup["widget"].tab_vent.widget(1).c_vent_type.currentIndex()
            == VENT_POLAR_INDEX
        )
        assert setup["widget"].tab_vent.widget(1).w_vent.si_Zh.value() == 2
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_H0.value() == 22e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_D0.value() == 32e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_W1.value() == 42e-3
        assert setup["widget"].tab_vent.widget(1).lf_Alpha0.value() == 0

        # Third set
        setup["widget"].tab_vent.widget(2).c_vent_type.setCurrentIndex(VENT_POLAR_INDEX)
        assert type(setup["widget"].tab_vent.widget(2).w_vent) == PVentPolar
        assert (
            setup["widget"].tab_vent.widget(2).c_vent_type.currentIndex()
            == VENT_POLAR_INDEX
        )
        assert setup["widget"].tab_vent.widget(2).w_vent.si_Zh.value() == 8
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_H0.value() == None
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_D0.value() == None
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_W1.value() == None
        assert setup["widget"].tab_vent.widget(2).lf_Alpha0.value() == 0

    @pytest.mark.Vent
    def test_remove_polar(self, setup):
        """Test that you can remove polar ventilation"""
        b_remove = (
            setup["widget"]
            .tab_vent.tabBar()
            .tabButton(setup["widget"].tab_vent.count() - 1, QTabBar.RightSide)
        )
        b_remove.clicked.emit()
        assert setup["widget"].tab_vent.count() == 1
        assert setup["widget"].tab_vent.currentIndex() == 0

        assert type(setup["widget"].tab_vent.widget(0).w_vent) == PVentPolar
        assert (
            setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex()
            == VENT_POLAR_INDEX
        )
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 1
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_H0.value() == 21e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_D0.value() == 31e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_W1.value() == 41e-3
        assert setup["widget"].tab_vent.widget(0).lf_Alpha0.value() == 0

    @pytest.mark.Vent
    def test_check_PVentPolar(self, setup):
        """Test that check of PVentPolar"""
        lam = Lamination(Rint=0.1, Rext=1, is_stator=True, is_internal=True)
        vent = VentilationPolar(Zh=1, H0=21e-3, D0=31e-3, W1=41e-3, Alpha0=None)
        assert PVentPolar(vent=vent, lam=lam).check() is None
        assert vent.Alpha0 == 0  # check set default value to 0

        vent = VentilationPolar(Zh=1, H0=21e-3, D0=31e-3, W1=None, Alpha0=0)
        assert PVentPolar(vent=vent, lam=lam).check() == "You must set W1 !"

        vent = VentilationPolar(Zh=1, H0=21e-3, D0=None, W1=41e-3, Alpha0=0)
        assert PVentPolar(vent=vent, lam=lam).check() == "You must set D0 !"

        vent = VentilationPolar(Zh=1, H0=None, D0=31e-3, W1=41e-3, Alpha0=0)
        assert PVentPolar(vent=vent, lam=lam).check() == "You must set H0 !"

        pvent = PVentPolar(vent=vent, lam=lam)
        pvent.vent.Zh = None
        assert pvent.check() == "You must set Zh !"

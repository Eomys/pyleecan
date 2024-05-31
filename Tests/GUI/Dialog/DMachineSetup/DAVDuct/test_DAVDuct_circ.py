# -*- coding: utf-8 -*-

import sys

import pytest
from qtpy import QtWidgets
from qtpy.QtWidgets import QTabBar

from pyleecan.Classes.Lamination import Lamination
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.GUI.Dialog.DMachineSetup.DAVDuct.DAVDuct import DAVDuct
from pyleecan.GUI.Dialog.DMachineSetup.DAVDuct.PVentCirc.PVentCirc import (
    PVentCirc,
)
from Tests.GUI.Dialog.DMachineSetup.DAVDuct import VENT_CIRC_INDEX
from numpy import pi


class TestDAVDuctCirc(object):
    """Test that the widget DAVDuct behave like it should"""

    @pytest.fixture
    def setup(self):
        """Run at the begining of every test to setup the gui"""

        if not QtWidgets.QApplication.instance():
            self.app = QtWidgets.QApplication(sys.argv)
        else:
            self.app = QtWidgets.QApplication.instance()

        test_obj = Lamination(Rint=0.1, Rext=1, is_stator=True, is_internal=True)
        test_obj.axial_vent.append(VentilationCirc(Zh=8, H0=10e-3, D0=40e-3, Alpha0=0))
        test_obj.axial_vent.append(VentilationCirc(Zh=9, H0=20e-3, D0=50e-3, Alpha0=0))

        widget = DAVDuct(test_obj)

        yield {"widget": widget, "test_obj": test_obj}

        self.app.quit()

    @pytest.mark.Vent
    def test_init_circ(self, setup):
        """Check that the Widget initialise for circular ventilations"""
        assert setup["widget"].tab_vent.count() == 2
        assert setup["widget"].tab_vent.currentIndex() == 0

        # First set
        assert type(setup["widget"].tab_vent.widget(0).w_vent) == PVentCirc
        assert (
            setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex()
            == VENT_CIRC_INDEX
        )
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 8
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_H0.value() == 10e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_D0.value() == 40e-3
        assert setup["widget"].tab_vent.widget(0).lf_Alpha0.value() == 0

        # Second set
        assert type(setup["widget"].tab_vent.widget(1).w_vent) == PVentCirc
        assert (
            setup["widget"].tab_vent.widget(1).c_vent_type.currentIndex()
            == VENT_CIRC_INDEX
        )
        assert setup["widget"].tab_vent.widget(1).w_vent.si_Zh.value() == 9
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_H0.value() == 20e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_D0.value() == 50e-3
        assert setup["widget"].tab_vent.widget(1).lf_Alpha0.value() == 0

        # Set Values
        setup["widget"].tab_vent.widget(0).w_vent.si_Zh.setValue(10)
        setup["widget"].tab_vent.widget(0).w_vent.lf_H0.setValue(11e-3)
        setup["widget"].tab_vent.widget(0).w_vent.lf_D0.setValue(41e-3)
        setup["widget"].tab_vent.widget(0).lf_Alpha0.setValue(0.2)
        # Raise signal to update object
        setup["widget"].tab_vent.widget(0).w_vent.lf_H0.editingFinished.emit()
        setup["widget"].tab_vent.widget(0).w_vent.lf_D0.editingFinished.emit()
        setup["widget"].tab_vent.widget(0).lf_Alpha0.editingFinished.emit()
        # Check changes
        assert setup["widget"].lam.axial_vent[0].Zh == 10
        assert setup["widget"].lam.axial_vent[0].H0 == 11e-3
        assert setup["widget"].lam.axial_vent[0].D0 == 41e-3
        assert setup["widget"].lam.axial_vent[0].Alpha0 == 0.2
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
    def test_add_circ(self, setup):
        """Test that you can add circ ventilation"""
        setup["widget"].b_new.clicked.emit()

        assert setup["widget"].tab_vent.count() == 3
        assert setup["widget"].tab_vent.currentIndex() == 0

        # First set
        assert type(setup["widget"].tab_vent.widget(0).w_vent) == PVentCirc
        assert (
            setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex()
            == VENT_CIRC_INDEX
        )
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 8
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_H0.value() == 10e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_D0.value() == 40e-3
        assert setup["widget"].tab_vent.widget(0).lf_Alpha0.value() == 0

        # Second set
        assert type(setup["widget"].tab_vent.widget(1).w_vent) == PVentCirc
        assert (
            setup["widget"].tab_vent.widget(1).c_vent_type.currentIndex()
            == VENT_CIRC_INDEX
        )
        assert setup["widget"].tab_vent.widget(1).w_vent.si_Zh.value() == 9
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_H0.value() == 20e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_D0.value() == 50e-3
        assert setup["widget"].tab_vent.widget(1).lf_Alpha0.value() == 0

        # Third set
        assert type(setup["widget"].tab_vent.widget(2).w_vent) == PVentCirc
        assert (
            setup["widget"].tab_vent.widget(2).c_vent_type.currentIndex()
            == VENT_CIRC_INDEX
        )
        assert setup["widget"].tab_vent.widget(2).w_vent.si_Zh.value() == 8
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_H0.value() == None
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_D0.value() == None
        assert setup["widget"].tab_vent.widget(2).lf_Alpha0.value() == 0

    @pytest.mark.Vent
    def test_remove_circ(self, setup):
        """Test that you can remove circ ventilation"""

        b_remove = (
            setup["widget"]
            .tab_vent.tabBar()
            .tabButton(setup["widget"].tab_vent.count() - 1, QTabBar.RightSide)
        )
        b_remove.clicked.emit()
        assert setup["widget"].tab_vent.count() == 1
        assert setup["widget"].tab_vent.currentIndex() == 0

        # First set
        assert type(setup["widget"].tab_vent.widget(0).w_vent) == PVentCirc
        assert (
            setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex()
            == VENT_CIRC_INDEX
        )
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 8
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_H0.value() == 10e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_D0.value() == 40e-3
        assert setup["widget"].tab_vent.widget(0).lf_Alpha0.value() == 0

    @pytest.mark.Vent
    def test_check_PVentCirc(self, setup):
        """Test that check of PVentCirc"""
        lam = Lamination(Rint=0.1, Rext=1, is_stator=True, is_internal=True)
        vent = VentilationCirc(Zh=8, H0=10e-3, D0=40e-3, Alpha0=None)
        assert PVentCirc(vent=vent, lam=lam).check() is None
        assert vent.Alpha0 == 0  # check set default value to 0

        vent = VentilationCirc(Zh=8, H0=10e-3, D0=None, Alpha0=None)
        assert PVentCirc(vent=vent, lam=lam).check() == "You must set D0 !"

        vent = VentilationCirc(Zh=8, H0=None, D0=None, Alpha0=None)
        assert PVentCirc(vent=vent, lam=lam).check() == "You must set H0 !"

        pvent = PVentCirc(vent=vent, lam=lam)
        pvent.vent.Zh = None
        assert pvent.check() == "You must set Zh !"

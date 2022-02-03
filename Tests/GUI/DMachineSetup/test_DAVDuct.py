# -*- coding: utf-8 -*-

import sys

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
import pytest


class TestDAVDuct(object):
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

    def test_init_circ(self, setup):
        """Check that the Widget initialise for circular ventilations"""
        assert setup["widget"].tab_vent.count() == 2
        assert setup["widget"].tab_vent.currentIndex() == 0

        # First set
        assert type(setup["widget"].tab_vent.widget(0).w_vent) == PVentCirc
        assert setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex() == 0
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 8
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_H0.value() == 10e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_D0.value() == 40e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_Alpha0.value() == 0

        # Second set
        assert type(setup["widget"].tab_vent.widget(1).w_vent) == PVentCirc
        assert setup["widget"].tab_vent.widget(1).c_vent_type.currentIndex() == 0
        assert setup["widget"].tab_vent.widget(1).w_vent.si_Zh.value() == 9
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_H0.value() == 20e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_D0.value() == 50e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_Alpha0.value() == 0

        # Set Values
        setup["widget"].tab_vent.widget(0).w_vent.si_Zh.setValue(10)
        setup["widget"].tab_vent.widget(0).w_vent.lf_H0.setValue(11e-3)
        setup["widget"].tab_vent.widget(0).w_vent.lf_D0.setValue(41e-3)
        setup["widget"].tab_vent.widget(0).w_vent.lf_Alpha0.setValue(0.2)
        # Raise signal to update object
        setup["widget"].tab_vent.widget(0).w_vent.si_Zh.editingFinished.emit()
        setup["widget"].tab_vent.widget(0).w_vent.lf_H0.editingFinished.emit()
        setup["widget"].tab_vent.widget(0).w_vent.lf_D0.editingFinished.emit()
        setup["widget"].tab_vent.widget(0).w_vent.lf_Alpha0.editingFinished.emit()
        # Check changes
        assert setup["widget"].lam.axial_vent[0].Zh == 10
        assert setup["widget"].lam.axial_vent[0].H0 == 11e-3
        assert setup["widget"].lam.axial_vent[0].D0 == 41e-3
        assert setup["widget"].lam.axial_vent[0].Alpha0 == 0.2

    def test_init_trap(self, setup):
        """Check that the Widget initialise for polar ventilations"""
        # Init the widget with Polar vent

        setup["test_obj"].axial_vent = [
            VentilationTrap(Zh=4, H0=24e-3, D0=34e-3, W1=44e-3, W2=54e-3, Alpha0=0)
        ]
        setup["widget"] = DAVDuct(setup["test_obj"])

        assert setup["widget"].tab_vent.count() == 1
        assert setup["widget"].tab_vent.currentIndex() == 0

        # First set
        assert type(setup["widget"].tab_vent.widget(0).w_vent) == PVentTrap
        assert setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex() == 1
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 4
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_H0.value() == 24e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_D0.value() == 34e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_W1.value() == 44e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_W2.value() == 54e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_Alpha0.value() == 0

        # Set Values
        setup["widget"].tab_vent.widget(0).w_vent.si_Zh.setValue(12)
        setup["widget"].tab_vent.widget(0).w_vent.lf_H0.setValue(12e-3)
        setup["widget"].tab_vent.widget(0).w_vent.lf_D0.setValue(42e-3)
        setup["widget"].tab_vent.widget(0).w_vent.lf_W1.setValue(45e-3)
        setup["widget"].tab_vent.widget(0).w_vent.lf_W2.setValue(55e-3)
        setup["widget"].tab_vent.widget(0).w_vent.lf_Alpha0.setValue(0.3)
        # Raise signal to update object
        setup["widget"].tab_vent.widget(0).w_vent.si_Zh.editingFinished.emit()
        setup["widget"].tab_vent.widget(0).w_vent.lf_H0.editingFinished.emit()
        setup["widget"].tab_vent.widget(0).w_vent.lf_D0.editingFinished.emit()
        setup["widget"].tab_vent.widget(0).w_vent.lf_W1.editingFinished.emit()
        setup["widget"].tab_vent.widget(0).w_vent.lf_W2.editingFinished.emit()
        setup["widget"].tab_vent.widget(0).w_vent.lf_Alpha0.editingFinished.emit()
        # Check changes
        assert setup["widget"].lam.axial_vent[0].Zh == 12
        assert setup["widget"].lam.axial_vent[0].H0 == 12e-3
        assert setup["widget"].lam.axial_vent[0].D0 == 42e-3
        assert setup["widget"].lam.axial_vent[0].W1 == 45e-3
        assert setup["widget"].lam.axial_vent[0].W2 == 55e-3
        assert setup["widget"].lam.axial_vent[0].Alpha0 == 0.3

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
        assert setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex() == 2
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 1
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_H0.value() == 21e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_D0.value() == 31e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_W1.value() == 41e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_Alpha0.value() == 0

        # 2nd set
        assert type(setup["widget"].tab_vent.widget(1).w_vent) == PVentPolar
        assert setup["widget"].tab_vent.widget(1).c_vent_type.currentIndex() == 2
        assert setup["widget"].tab_vent.widget(1).w_vent.si_Zh.value() == 2
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_H0.value() == 22e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_D0.value() == 32e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_W1.value() == 42e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_Alpha0.value() == 0

        # 3rd set
        assert type(setup["widget"].tab_vent.widget(2).w_vent) == PVentPolar
        assert setup["widget"].tab_vent.widget(2).c_vent_type.currentIndex() == 2
        assert setup["widget"].tab_vent.widget(2).w_vent.si_Zh.value() == 3
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_H0.value() == 23e-3
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_D0.value() == 33e-3
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_W1.value() == 43e-3
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_Alpha0.value() == 0

        # Set Values
        setup["widget"].tab_vent.widget(1).w_vent.si_Zh.setValue(9)
        setup["widget"].tab_vent.widget(1).w_vent.lf_H0.setValue(33e-3)
        setup["widget"].tab_vent.widget(1).w_vent.lf_D0.setValue(44e-3)
        setup["widget"].tab_vent.widget(1).w_vent.lf_W1.setValue(55e-3)
        setup["widget"].tab_vent.widget(1).w_vent.lf_Alpha0.setValue(0.4)
        # Raise signal to update object
        setup["widget"].tab_vent.widget(1).w_vent.si_Zh.editingFinished.emit()
        setup["widget"].tab_vent.widget(1).w_vent.lf_H0.editingFinished.emit()
        setup["widget"].tab_vent.widget(1).w_vent.lf_D0.editingFinished.emit()
        setup["widget"].tab_vent.widget(1).w_vent.lf_W1.editingFinished.emit()
        setup["widget"].tab_vent.widget(1).w_vent.lf_Alpha0.editingFinished.emit()
        # Check changes
        assert setup["widget"].lam.axial_vent[1].Zh == 9
        assert setup["widget"].lam.axial_vent[1].H0 == 33e-3
        assert setup["widget"].lam.axial_vent[1].D0 == 44e-3
        assert setup["widget"].lam.axial_vent[1].W1 == 55e-3
        assert setup["widget"].lam.axial_vent[1].Alpha0 == 0.4

    def test_init_all_type(self, setup):
        """Check that you can combine several kind of ventilations"""
        test_obj = Lamination(Rint=0.1, Rext=1, is_stator=True, is_internal=True)
        test_obj.axial_vent.append(VentilationCirc(Zh=8, H0=10e-3, D0=40e-3, Alpha0=0))
        test_obj.axial_vent.append(
            VentilationTrap(Zh=4, H0=24e-3, D0=34e-3, W1=44e-3, W2=54e-3, Alpha0=0)
        )
        test_obj.axial_vent.append(
            VentilationPolar(Zh=3, H0=23e-3, D0=33e-3, W1=43e-3, Alpha0=0)
        )
        setup["widget"] = DAVDuct(test_obj)

        assert setup["widget"].tab_vent.count() == 3
        assert setup["widget"].tab_vent.currentIndex() == 0

        # First set
        assert type(setup["widget"].tab_vent.widget(0).w_vent) == PVentCirc
        assert setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex() == 0
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 8

        # 2nd set
        assert type(setup["widget"].tab_vent.widget(1).w_vent) == PVentTrap
        assert setup["widget"].tab_vent.widget(1).c_vent_type.currentIndex() == 1
        assert setup["widget"].tab_vent.widget(1).w_vent.si_Zh.value() == 4

        # 3rd set
        assert type(setup["widget"].tab_vent.widget(2).w_vent) == PVentPolar
        assert setup["widget"].tab_vent.widget(2).c_vent_type.currentIndex() == 2
        assert setup["widget"].tab_vent.widget(2).w_vent.si_Zh.value() == 3

    def test_add_circ(self, setup):
        """Test that you can add circ ventilation"""
        setup["widget"].b_new.clicked.emit()

        assert setup["widget"].tab_vent.count() == 3
        assert setup["widget"].tab_vent.currentIndex() == 0

        # First set
        assert type(setup["widget"].tab_vent.widget(0).w_vent) == PVentCirc
        assert setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex() == 0
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 8
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_H0.value() == 10e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_D0.value() == 40e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_Alpha0.value() == 0

        # Second set
        assert type(setup["widget"].tab_vent.widget(1).w_vent) == PVentCirc
        assert setup["widget"].tab_vent.widget(1).c_vent_type.currentIndex() == 0
        assert setup["widget"].tab_vent.widget(1).w_vent.si_Zh.value() == 9
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_H0.value() == 20e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_D0.value() == 50e-3
        assert setup["widget"].tab_vent.widget(1).w_vent.lf_Alpha0.value() == 0

        # Third set
        assert type(setup["widget"].tab_vent.widget(2).w_vent) == PVentCirc
        assert setup["widget"].tab_vent.widget(2).c_vent_type.currentIndex() == 0
        assert setup["widget"].tab_vent.widget(2).w_vent.si_Zh.value() == 8
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_H0.value() == None
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_D0.value() == None
        assert setup["widget"].tab_vent.widget(2).w_vent.lf_Alpha0.value() == None

    def test_remove_circ(self, setup):
        """Test that you can remove circ ventilation"""
        setup["widget"].b_remove.clicked.emit()
        assert setup["widget"].tab_vent.count() == 1
        assert setup["widget"].tab_vent.currentIndex() == 0

        # First set
        assert type(setup["widget"].tab_vent.widget(0).w_vent) == PVentCirc
        assert setup["widget"].tab_vent.widget(0).c_vent_type.currentIndex() == 0
        assert setup["widget"].tab_vent.widget(0).w_vent.si_Zh.value() == 8
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_H0.value() == 10e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_D0.value() == 40e-3
        assert setup["widget"].tab_vent.widget(0).w_vent.lf_Alpha0.value() == 0

    def test_check_PVentCirc(self, setup):
        """Test that check of PVentCirc"""
        lam = Lamination(Rint=0.1, Rext=1, is_stator=True, is_internal=True)
        vent = VentilationCirc(Zh=8, H0=10e-3, D0=40e-3, Alpha0=None)
        assert PVentCirc(vent=vent, lam=lam).check() == "You must set Alpha0 !"

        vent = VentilationCirc(Zh=8, H0=10e-3, D0=None, Alpha0=None)
        assert PVentCirc(vent=vent, lam=lam).check() == "You must set D0 !"

        vent = VentilationCirc(Zh=8, H0=None, D0=None, Alpha0=None)
        assert PVentCirc(vent=vent, lam=lam).check() == "You must set H0 !"

        pvent = PVentCirc(vent=vent, lam=lam)
        pvent.vent.Zh = None
        assert pvent.check() == "You must set Zh !"

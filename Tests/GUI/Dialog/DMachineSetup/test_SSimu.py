# -*- coding: utf-8 -*-

import sys
from os.path import join
import pytest
from numpy import pi
from numpy.testing import assert_almost_equal

import numpy as np
from PySide2 import QtWidgets
from PySide2.QtTest import QTest


from pyleecan.GUI.Dialog.DMachineSetup.SSimu.SSimu import SSimu

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.LossFEA import LossFEA
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.OPdq import OPdq


class TestSSimu(object):
    """Test that the widget SSimu behave like it should"""

    @classmethod
    def setup_class(cls):
        """Start the app for the test"""
        if not QtWidgets.QApplication.instance():
            cls.app = QtWidgets.QApplication(sys.argv)
        else:
            cls.app = QtWidgets.QApplication.instance()

    def setup_method(self):
        """Create widget before each test"""
        self.machine = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
        self.widget = SSimu(machine=self.machine, material_dict=None, is_stator=None)

        self.simu = Simu1(machine=self.machine)
        self.simu.mag = MagFEMM(
            is_periodicity_a=False,
            is_periodicity_t=False,
            nb_worker=4,
            is_get_meshsolution=True,
            is_periodicity_rotor=True,
            is_calc_torque_energy=False,
            T_mag=20,
        )
        self.simu.input = InputCurrent(
            Nt_tot=365,
            Na_tot=2,
            OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
            is_periodicity_t=True,
            is_periodicity_a=True,
        )
        self.simu.loss = LossFEA(Trot=125, Tsta=124)

    @classmethod
    def teardown_class(cls):
        """Exit the app after the test"""
        cls.app.quit()

    @pytest.mark.SSimu
    @pytest.mark.IPMSM
    def test_init(self):
        """Check that the Widget init is correct"""
        assert isinstance(self.widget.simu.mag, MagFEMM)
        assert self.widget.lf_N0.value() == 1000
        assert self.widget.lf_I1.value() == 0  # Id
        assert self.widget.lf_I1.value() == 0  # Iq
        assert self.widget.lf_T_mag.value() == 20

    # @pytest.mark.SSimu
    # @pytest.mark.IPMSM
    # def test_set_value(self):
    #     """Check that you can set simu for simu"""

    #     self.simu = Simu1(machine=self.machine)
    #     self.simu.mag = MagFEMM(
    #         is_periodicity_a=False,
    #         is_periodicity_t=False,
    #         nb_worker=4,
    #         is_get_meshsolution=True,
    #         is_periodicity_rotor=True,
    #         is_calc_torque_energy=False,
    #         T_mag=17,
    #     )
    #     self.simu.input = InputCurrent(
    #         Nt_tot=365,
    #         Na_tot=2,
    #         OP=OPdq(N0=4000, Id_ref=0, Iq_ref=np.sqrt(2)),
    #         is_periodicity_t=True,
    #         is_periodicity_a=True,
    #     )
    #     self.simu.loss = LossFEA(Trot=125, Tsta=124)

    #     self.widget = SSimu(self.machine, material_dict=None, is_stator=None)

    #     assert not self.widget.is_per_a.isChecked()
    #     assert not self.widget.is_per_t.isChecked()

    #     assert isinstance(self.widget.simu.mag, MagFEMM)
    #     assert self.widget.lf_N0.value() == 4000
    #     assert self.widget.lf_I1.value() == 2.5  # Id
    #     assert self.widget.lf_I1.value() == 1.414  # Iq
    #     assert self.widget.lf_T_mag.value() == 17

    #     assert self.widget.lf_Trot.value() == 125
    #     assert self.widget.lf_Tsta.value() == 124

    #     assert self.widget.si_Na_tot.value() == 365
    #     assert self.widget.si_Nt_tot.value() == 2
    #     assert self.widget.si_nb_worker.value() == 4

    #     self.widget.is_losses.setChecked(True)
    #     self.widget.is_mesh_sol.setChecked(True)

    #     assert self.widget.is_losses.isChecked()
    #     assert self.widget.is_mesh_sol.isChecked()

    def test_set_N0(self):
        """Check that the Widget allow to update No"""
        self.widget.lf_N0.clear()  # Clear the field before writing
        QTest.keyClicks(self.widget.lf_N0, "4000")
        self.widget.lf_N0.editingFinished.emit()  # To trigger the slot

        assert self.widget.lf_N0.value() == 4000
        assert self.widget.simu.input.OP.N0 == 4000

    # continuepour Id, Iq....


if __name__ == "__main__":
    a = TestSSimu()
    a.setup_class()
    a.setup_method()
    a.test_init()
    a.test_set_N0()
    # a.test_set_value()

    print("Done")

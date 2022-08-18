from datetime import datetime
from logging import getLogger
from multiprocessing import cpu_count
from os.path import join

from PySide2.QtCore import Qt, Signal
from PySide2.QtWidgets import QMessageBox, QWidget

from .....Classes._FEMMHandler import _FEMMHandler
from .....Classes.InputCurrent import InputCurrent
from .....Classes.MachineWRSM import MachineWRSM
from .....Classes.MachineIPMSM import MachineIPMSM
from .....Classes.MachineSIPMSM import MachineSIPMSM
from .....Classes.MagFEMM import MagFEMM
from .....Classes.OPdq import OPdq
from .....Classes.OPdqf import OPdqf
from .....Classes.Simu1 import Simu1
from .....GUI import gui_option
from .....GUI.Dialog.DMachineSetup.SSimu.Gen_SSimu import Gen_SSimu
from .....loggers import GUI_LOG_NAME


class SSimu(Gen_SSimu, QWidget):
    """Step to define and run a simulation"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()  # No used here
    # Information for DMachineSetup nav
    step_name = "FEMM Simulation"

    def __init__(self, machine, material_dict, is_stator):
        """Initialize the GUI according to machine

        Parameters
        ----------
        self : SSimu
            A SSimu widget
        machine : Machine
            current machine to edit
        material_dict: dict
            Materials dictionary (library + machine)
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor (unused)
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Saving arguments
        self.machine = machine
        self.material_dict = material_dict

        # Plot the machine
        try:
            self.machine.plot(
                fig=self.w_viewer.fig,
                ax=self.w_viewer.axes,
                sym=1,
                alpha=0,
                delta=0,
                is_show_fig=False,
                is_clean_plot=True,
                is_max_sym=True,
            )
        except Exception as e:
            err_msg = "Error while plotting machine in Simulation Step:\n" + str(e)
            getLogger(GUI_LOG_NAME).error(err_msg)
            QMessageBox().critical(
                self,
                self.tr("Error"),
                err_msg,
            )
        self.w_viewer.draw()

        # Adapt OP widgets to machine type
        self.in_I3.setHidden(not isinstance(self.machine, MachineWRSM))
        self.lf_I3.setHidden(not isinstance(self.machine, MachineWRSM))
        self.unit_I3.setHidden(not isinstance(self.machine, MachineWRSM))
        if self.machine.is_synchronous():
            self.in_I1.setText("Id:")
            self.in_I2.setText("Iq:")
            self.unit_I2.setText("[Arms]")
        else:
            self.in_I1.setText("I0:")
            self.in_I2.setText("Phi0:")
            self.unit_I2.setText("[rad]")
        self.unit_I1.setText("[Arms]")
        hide_mag = not isinstance(self.machine, (MachineIPMSM, MachineSIPMSM))
        self.in_T_mag.setHidden(hide_mag)
        self.lf_T_mag.setHidden(hide_mag)
        self.unit_T_mag.setHidden(hide_mag)

        # Init default simulation to edit
        self.simu = Simu1(name="FEMM_" + self.machine.name, machine=self.machine)
        p = self.machine.get_pole_pair_number()
        Zs = self.machine.stator.slot.Zs
        self.simu.input = InputCurrent(Na_tot=2 * 3 * 5 * 7 * p, Nt_tot=10 * Zs * p)
        if isinstance(self.machine, MachineWRSM):
            self.simu.input.OP = OPdqf(N0=1000, Id_ref=0, Iq_ref=0, If_ref=5)
        else:
            self.simu.input.OP = OPdq(N0=1000, Id_ref=0, Iq_ref=0)
        self.simu.mag = MagFEMM(
            Kmesh_fineness=1,
            is_periodicity_a=True,
            is_periodicity_t=True,
            T_mag=20,
            nb_worker=cpu_count(),
        )
        self.simu.force = None

        # Init widget according to defaut simulation
        self.lf_N0.setValue(self.simu.input.OP.N0)
        self.lf_I1.setValue(0)
        self.lf_I2.setValue(0)
        self.lf_I3.setValue(5)  # Hidden if not used
        self.lf_T_mag.setValue(self.simu.mag.T_mag)
        self.si_Na_tot.setValue(self.simu.input.Na_tot)
        self.si_Nt_tot.setValue(self.simu.input.Nt_tot)
        self.is_per_a.setChecked(True)
        self.is_per_t.setChecked(True)
        self.lf_Kmesh.setValue(1)
        self.si_nb_worker.setValue(self.simu.mag.nb_worker)

        # Setup path result selection
        self.w_path_result.obj = None
        self.w_path_result.param_name = None
        self.w_path_result.verbose_name = "Result folder"
        self.w_path_result.extension = None
        self.w_path_result.is_file = False
        self.w_path_result.update()

        # Connecting the signal
        self.lf_N0.editingFinished.connect(self.set_N0)
        self.lf_I1.editingFinished.connect(self.set_Id_Iq)
        self.lf_I2.editingFinished.connect(self.set_Id_Iq)
        self.lf_I3.editingFinished.connect(self.set_I3)
        self.lf_T_mag.editingFinished.connect(self.set_T_mag)
        self.si_Na_tot.editingFinished.connect(self.set_Na_tot)
        self.si_Nt_tot.editingFinished.connect(self.set_Nt_tot)
        self.is_per_a.toggled.connect(self.set_per_a)
        self.is_per_t.toggled.connect(self.set_per_t)
        self.lf_Kmesh.editingFinished.connect(self.set_Kmesh)
        self.si_nb_worker.editingFinished.connect(self.set_nb_worker)

        self.b_next.clicked.connect(self.run)

    def run(self):
        """Run the current simulation"""
        if self.w_path_result.get_path() is None:
            QMessageBox().critical(
                self, self.tr("Error"), "Please select a result folder"
            )
            return
        # Setup result folder
        now = datetime.now()
        time_str = now.strftime("%Y_%m_%d %Hh%Mmin%Ss")
        self.simu.path_result = join(
            self.w_path_result.get_path(), time_str + "_" + self.simu.name
        )
        # Save simu for reference
        self.simu.save(join(self.simu.path_result, self.simu.name + ".json"))
        # Check FEMM installation
        try:
            femm = _FEMMHandler()
            femm.openfemm(1)  # 1 == open in background, 0 == open normally
            femm.closefemm()
        except Exception as e:
            msgBox = QMessageBox()
            msgBox.setTextFormat(Qt.RichText)
            msgBox.warning(
                None,
                "Warning",
                "This pyleecan simulation requires FEMM Software (Finite Element Method Magnetics), its installer can be dowloaded from <a href='https://www.femm.info/wiki/Download'>https://www.femm.info/wiki/Download</a>.",
                QMessageBox.Ok,
            )
            return
        # Run simulation
        try:
            out = self.simu.run()
        except Exception as e:
            err_msg = "Error while running simulation:\n" + str(e)
            QMessageBox().critical(self, self.tr("Error"), err_msg)
            self.simu.get_logger().error(err_msg)
        # Save results
        out.save(join(self.simu.path_result, "Result.h5"))

    def set_N0(self):
        """Update N0 according to the widget"""
        self.simu.input.OP.N0 = self.lf_N0.value()

    def set_Id_Iq(self):
        """Update Id/Iq according to the widget"""
        if self.machine.is_synchronous():
            self.simu.input.OP.Id_ref = self.lf_I1.value()
            self.simu.input.OP.Iq_ref = self.lf_I2.value()
        else:
            self.simu.input.OP.set_Id_Iq(I0=self.lf_I1.value(), Phi0=self.lf_I2.value())

    def set_I3(self):
        """Update If according to the widget"""
        self.simu.input.OP.If = self.lf_I3.value()

    def set_T_mag(self):
        """Update T_mag according to the widget"""
        self.simu.mag.T_mag = self.lf_T_mag.value()

    def set_Na_tot(self):
        """Update Na_tot according to the widget"""
        self.simu.input.Na_tot = self.si_Na_tot.value()

    def set_Nt_tot(self):
        """Update Nt_tot according to the widget"""
        self.simu.input.Nt_tot = self.si_Nt_tot.value()

    def set_per_a(self):
        """Update is_per_a according to the widget"""
        self.simu.mag.is_periodicity_a = self.is_per_a.isChecked()

    def set_per_t(self):
        """Update is_per_t according to the widget"""
        self.simu.mag.is_periodicity_t = self.is_per_t.isChecked()

    def set_Kmesh(self):
        """Update Kmesh according to the widget"""
        self.simu.mag.Kmesh_fineness = self.lf_Kmesh.value()

    def set_nb_worker(self):
        """Update nb_worker according to the widget"""
        self.simu.mag.nb_worker = self.si_nb_worker.value()
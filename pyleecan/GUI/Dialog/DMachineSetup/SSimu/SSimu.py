from datetime import datetime
from logging import getLogger
from multiprocessing import cpu_count
from os.path import join

from qtpy.QtCore import Qt, Signal
from qtpy.QtWidgets import QMessageBox, QWidget

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
from .....definitions import config_dict
from .....Functions.init_environment import save_config_dict
from .....Functions.GUI.log_error import log_error
from .....Classes.LossFEA import LossFEA


class SSimu(Gen_SSimu, QWidget):
    """Step to define and run a simulation"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()  # No used here
    # Information for DMachineSetup nav
    step_name = "FEMM Simulation"

    def __init__(self, machine, material_dict, is_stator, test_config_dict=None):
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
        test_config_dict : None
            To overwritte the current config_dict (for testing only)
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Saving arguments
        self.machine = machine
        self.material_dict = material_dict
        self.last_out = None  # To store the last output for tests
        self.test_err_msg = None  # For test of popup
        self.test_config_dict = test_config_dict  # to avoid saving config dict in test

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
            self.test_err_msg = (
                "Error while plotting machine in Simulation Step:\n" + str(e)
            )
            log_error(
                self,
                self.test_err_msg,
                self.simu.get_logger(),
                is_popup=False,
                is_warning=False,
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
        self.simu.input = InputCurrent(Na_tot=2 * 2 * 3 * 5 * 7 * p, Nt_tot=10 * Zs)
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
        self.le_name.setText(self.simu.name)

        # Setup path result selection
        self.w_path_result.obj = None
        self.w_path_result.param_name = None
        self.w_path_result.verbose_name = "Results folder"
        self.w_path_result.extension = None
        self.w_path_result.is_file = False
        self.w_path_result.update()
        if self.test_config_dict is not None:
            if "MAIN" in test_config_dict and "RESULT_DIR" in test_config_dict["MAIN"]:
                self.w_path_result.set_path_txt(test_config_dict["MAIN"]["RESULT_DIR"])
        elif "MAIN" in config_dict and "RESULT_DIR" in config_dict["MAIN"]:
            self.w_path_result.set_path_txt(config_dict["MAIN"]["RESULT_DIR"])

        # setup Losses Model
        if isinstance(self.machine, MachineSIPMSM) or isinstance(
            self.machine, MachineIPMSM
        ):
            self.g_losses_model.show()

        else:
            self.g_losses_model.hide()

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

        self.is_mesh_sol.toggled.connect(self.set_mesh_sol)
        self.g_losses_model.toggled.connect(self.set_g_losses_model)
        self.lf_Tsta.editingFinished.connect(self.set_Tsta)
        self.lf_Trot.editingFinished.connect(self.set_Trot)

        self.b_next.clicked.connect(self.run)

    def run(self):
        """Run the current simulation"""
        if self.w_path_result.get_path() in [None, ""]:
            QMessageBox().critical(
                self, self.tr("Error"), "Please select a result folder"
            )
            return
        if self.test_config_dict is None:
            config_dict["MAIN"]["RESULT_DIR"] = self.w_path_result.get_path()
            save_config_dict(config_dict)
        else:
            self.test_config_dict["MAIN"]["RESULT_DIR"] = self.w_path_result.get_path()

        if self.le_name.text() in [None, ""]:
            QMessageBox().critical(
                self, self.tr("Error"), "Please set a simulation name"
            )
            return
        self.simu.name = self.le_name.text()
        # Setup result folder
        now = datetime.now()
        time_str = now.strftime("%Y_%m_%d-%Hh%Mmin%Ss")
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
            self.test_err_msg = "Error while running simulation:\n" + str(e)
            log_error(
                self,
                self.test_err_msg,
                self.simu.get_logger(),
                is_popup=False,
                is_warning=False,
            )
        # Store output for test
        self.last_out = out
        # Save results
        try:
            out.save(join(self.simu.path_result, "Result.h5"))
            out.export_to_mat(join(self.simu.path_result, "Result.mat"))
        except Exception as e:
            self.test_err_msg = "Error while saving results:\n" + str(e)
            log_error(
                self,
                self.test_err_msg,
                self.simu.get_logger(),
                is_popup=False,
                is_warning=False,
            )
        # Machine
        out.simu.machine.plot(
            is_max_sym=self.simu.mag.is_periodicity_a,
            is_clean_plot=True,
            is_show_fig=False,
            save_path=join(self.simu.path_result, out.simu.machine.name + ".png"),
        )
        p = self.machine.get_pole_pair_number()
        # Torque Time
        try:
            out.mag.Tem.plot_2D_Data(
                "time",
                is_show_fig=False,
                save_path=join(self.simu.path_result, "torque as fct of time.png"),
            )
        except Exception as e:
            self.test_err_msg = "Error while plotting torque as fct of time: " + str(e)
            log_error(
                self,
                self.test_err_msg,
                self.simu.get_logger(),
                is_popup=False,
                is_warning=False,
            )
        # Torque FFT
        try:
            out.mag.Tem.plot_2D_Data(
                "freqs->elec_order=[0,15]",
                is_show_fig=False,
                save_path=join(self.simu.path_result, "torque FFT over freq.png"),
            )
        except Exception as e:
            self.test_err_msg = "Error while plotting torque FFT over freq: " + str(e)
            log_error(
                self,
                self.test_err_msg,
                self.simu.get_logger(),
                is_popup=False,
                is_warning=False,
            )
        # Flux
        try:
            out.mag.B.plot_2D_Data(
                "time",
                is_show_fig=False,
                save_path=join(self.simu.path_result, "flux as fct of time.png"),
            )
            out.mag.B.plot_2D_Data(
                "angle{°}",
                is_show_fig=False,
                save_path=join(self.simu.path_result, "flux as fct of angle.png"),
            )
            out.mag.B.plot_2D_Data(
                "freqs->elec_order=[0,15]",
                is_show_fig=False,
                save_path=join(self.simu.path_result, "flux FFT over freq.png"),
            )
            out.mag.B.plot_2D_Data(
                "wavenumber=[0," + str(int(25 * p)) + "]",
                is_show_fig=False,
                save_path=join(self.simu.path_result, "flux FFT over wavenumber.png"),
            )
            # out.mag.B.plot_3D_Data(
            #     "time",
            #     "angle{°}",
            #     component_list=["radial"],
            #     is_2D_view=True,
            #     is_show_fig=False,
            #     save_path=join(
            #         self.simu.path_result, "flux as fct of time and angle.png"
            #     ),
            # )
            out.mag.B.plot_3D_Data(
                "freqs->elec_order=[0,10]",
                "wavenumber->space_order=[-10,10]",
                N_stem=50,
                is_2D_view=True,
                is_show_fig=False,
                save_path=join(self.simu.path_result, "flux 3D FFT.png"),
            )
        except Exception as e:
            self.test_err_msg = "Error while plotting flux:\n" + str(e)
            log_error(
                self,
                self.test_err_msg,
                self.simu.get_logger(),
                is_popup=False,
                is_warning=False,
            )
        # Phi_wind_stator
        try:
            out.mag.Phi_wind_stator.plot_2D_Data(
                "time",
                "phase[0]",
                is_show_fig=False,
                save_path=join(self.simu.path_result, "Stator winding flux.png"),
            )
        except Exception as e:
            self.test_err_msg = "Error while plotting Stator winding flux:\n" + str(e)
            log_error(
                self,
                self.test_err_msg,
                self.simu.get_logger(),
                is_popup=False,
                is_warning=False,
            )

        # mag mesh solution
        if self.simu.mag.is_get_meshsolution:
            try:
                out.plot_B_mesh(
                    is_show_fig=False,
                    is_2D=True,
                    clim=[0, 3],
                    save_path=(join(self.simu.path_result, "B_meshsolution.png")),
                )
            except Exception as e:
                self.test_err_msg = f"Error while plotting B meshsolution : {e}"
                log_error(
                    self,
                    self.test_err_msg,
                    self.simu.mag.get_logger(),
                    is_popup=False,
                    is_warning=False,
                )

            # save mesh
            try:
                out.mag.meshsolution.export_to_mat(
                    save_path=(join(self.simu.path_result, "MagMeshSolution.mat")),
                )
            except Exception as e:
                self.test_err_msg = "Error while saving mesh solution: " + str(e)
                log_error(
                    self,
                    self.test_err_msg,
                    self.simu.get_logger(),
                    is_popup=False,
                    is_warning=False,
                )
            # save mesh file vtk
            try:
                out.mag.meshsolution.mesh.save_vtk(
                    save_path=(join(self.simu.path_result, "MagMesh.vtk")),
                )
            except Exception as e:
                self.test_err_msg = "Error while saving mesh : " + str(e)
                log_error(
                    self,
                    self.test_err_msg,
                    self.simu.get_logger(),
                    is_popup=False,
                    is_warning=False,
                )

        # Losses
        if self.simu.loss is not None:
            try:
                out.loss.plot_losses(
                    is_show_fig=False,
                    save_path=(join(self.simu.path_result, "Losses.png")),
                )
            except Exception as e:
                self.test_err_msg = "Error while plotting Losses: " + str(e)
                log_error(
                    self,
                    self.test_err_msg,
                    self.simu.get_logger(),
                    is_popup=False,
                    is_warning=False,
                )

            # Overall on stator
            try:
                out.loss["overall"].plot_mesh(
                    group_names=["stator core", "stator winding"],
                    save_path=(
                        join(self.simu.path_result, "Losses_meshsolution_stator.png")
                    ),
                )
            except Exception as e:
                self.test_err_msg = (
                    "Error while plotting Losses meshsolution (Overall on stator): "
                    + str(e)
                )
                log_error(
                    self,
                    self.test_err_msg,
                    self.simu.get_logger(),
                    is_popup=False,
                    is_warning=False,
                )

            # rotor core with magnets
            try:
                out.loss["overall"].plot_mesh(
                    group_names=["rotor core", "rotor magnets"],
                    save_path=(
                        join(self.simu.path_result, "Losses_meshsolution_rotor.png")
                    ),
                )
            except Exception as e:
                self.test_err_msg = (
                    "Error while plotting Losses meshsolution (rotor core with magnets): "
                    + str(e)
                )
                log_error(
                    self,
                    self.test_err_msg,
                    self.simu.get_logger(),
                    is_popup=False,
                    is_warning=False,
                )

        # Done
        self.test_err_msg = (
            "Simulation "
            + self.simu.name
            + " is finished.\nResults available at "
            + self.simu.path_result
        )
        QMessageBox().information(
            self,
            self.tr("Simlation finished"),
            self.test_err_msg,
        )

    def set_N0(self):
        """Update N0 according to the widget"""
        self.simu.input.OP.N0 = self.lf_N0.value()

    def set_Id_Iq(self):
        """Update Id/Iq according to the widget"""
        if self.machine.is_synchronous():
            self.simu.input.OP.Id_ref = self.lf_I1.value()
            self.simu.input.OP.Iq_ref = self.lf_I2.value()
        else:
            self.simu.input.OP.set_I0_Phi0(
                I0=self.lf_I1.value(), Phi0=self.lf_I2.value()
            )

    def set_I3(self):
        """Update If according to the widget"""
        self.simu.input.OP.If_ref = self.lf_I3.value()

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

    def set_g_losses_model(self):
        """Update g_losses_model according to the widget"""
        if self.g_losses_model.isChecked():
            self.simu.loss = LossFEA()
            self.simu.loss.is_get_meshsolution = True
            self.simu.mag.is_get_meshsolution = True
            self.simu.mag.is_save_meshsolution_as_file = True

            self.is_mesh_sol.setChecked(True)
            self.is_mesh_sol.setDisabled(True)

        else:
            self.simu.loss = None
            self.is_mesh_sol.setDisabled(False)

    def set_Tsta(self):
        """Update lf_Tsta according to the widget"""
        self.simu.loss.Tsta = self.lf_Tsta.value()

    def set_Trot(self):
        """Update lf_Tsta according to the widget"""
        self.simu.loss.Trot = self.lf_Trot.value()

    def set_mesh_sol(self):
        """Update is_mesh_sol according to the widget"""
        if self.is_mesh_sol.isChecked():
            self.simu.mag.is_get_meshsolution = True
            self.simu.mag.is_save_meshsolution_as_file = True
        else:
            self.simu.mag.is_get_meshsolution = False
            self.simu.mag.is_save_meshsolution_as_file = False

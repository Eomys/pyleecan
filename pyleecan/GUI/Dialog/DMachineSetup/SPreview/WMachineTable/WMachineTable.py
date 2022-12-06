from logging import getLogger
from os.path import join

from PySide2.QtWidgets import QFileDialog, QTableWidgetItem, QWidget, QMessageBox

from ......Classes._FEMMHandler import _FEMMHandler
from ......Classes.Output import Output
from ......Classes.InputCurrent import InputCurrent
from ......Classes.Simu1 import Simu1
from ......Classes.OPdq import OPdq
from ......Classes.OPslip import OPslip
from ......Classes.InputCurrent import InputCurrent
from ......definitions import config_dict
from ......loggers import GUI_LOG_NAME
from ......Functions.GUI.log_error import log_error
from ......Functions.FEMM.update_FEMM_simulation import update_FEMM_simulation
from ......Functions.FEMM.draw_FEMM import draw_FEMM
from ......Functions.Plot.set_plot_gui_icon import set_plot_gui_icon
from ......GUI.Dialog.DMachineSetup.SPreview.WMachineTable.Ui_WMachineTable import (
    Ui_WMachineTable,
)
from ......Methods.Simulation.MagElmer import MagElmer_BP_dict

try:
    from ......Functions.GMSH.draw_GMSH import draw_GMSH
except Exception as e:
    draw_GMSH = e
try:
    from pyleecan.Functions.GMSH.gen_3D_mesh import gen_3D_mesh
except Exception as e:
    gen_3D_mesh = e


class WMachineTable(Ui_WMachineTable, QWidget):
    """Table to display the main paramaters of the machine"""

    def __init__(self, parent=None):
        """Initialize the GUI

        Parameters
        ----------
        self : SWindCond
            A SWindCond widget
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self, parent)
        self.setupUi(self)

        self.machine = None

        # Connect the widget
        self.b_mmf.clicked.connect(self.plot_mmf)
        self.b_FEMM.clicked.connect(self.draw_FEMM)
        if isinstance(draw_GMSH, Exception):
            self.b_GMSH.setEnabled(False)
            self.b_GMSH.setWhatsThis(str(draw_GMSH))
            self.b_GMSH.setToolTip(str(draw_GMSH))

            self.b_GMSH_3D.setEnabled(False)
            self.b_GMSH_3D.setWhatsThis(str(gen_3D_mesh))
            self.b_GMSH_3D.setToolTip(str(gen_3D_mesh))
        else:
            self.b_GMSH.clicked.connect(self.draw_GMSH)
            self.b_GMSH_3D.clicked.connect(self.draw_GMSH_3D)
        self.b_plot_machine.clicked.connect(self.plot_machine)

    def update_tab(self, machine):
        """Update the table to match the machine

        Parameters
        ----------
        self : WMachineTable
            A WMachineTable object
        """

        self.machine = machine
        desc_dict = self.machine.comp_desc_dict()

        self.tab_param.clear()
        # Set header
        self.tab_param.setColumnCount(2)
        item = QTableWidgetItem("Name")
        self.tab_param.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem("Value")
        self.tab_param.setHorizontalHeaderItem(1, item)
        # Set containt
        for ii, desc in enumerate(desc_dict):
            if desc["value"] is not None:
                self.tab_param.insertRow(ii)
                self.tab_param.setItem(ii, 0, QTableWidgetItem(desc["verbose"]))
                if desc["type"] is float:
                    txt = format(desc["value"], ".4g")
                else:
                    txt = str(desc["value"])
                if desc["unit"] not in ["", None]:
                    txt += " " + desc["unit"]
                self.tab_param.setItem(ii, 1, QTableWidgetItem(txt))

    def plot_mmf(self):
        """Plot the unit mmf of the stator"""
        try:
            if self.machine is not None:
                self.machine.stator.plot_mmf_unit()
                set_plot_gui_icon()
        except Exception as e:
            err_msg = "Error while plotting Stator mmf unit:\n" + str(e)
            log_error(self, err_msg)

    def plot_machine(self):
        """Plot the machine"""
        if self.machine is not None:
            self.machine.plot()
        set_plot_gui_icon()

    def draw_FEMM(self):
        """Draw the Machine in FEMM"""

        save_file_path = self.get_save_path(ext=".fem", file_type="FEMM (*.fem)")
        # Avoid bug due to user closing the popup witout selecting a file
        if save_file_path is [None, ""]:
            return

        try:
            femm = _FEMMHandler()

            # Periodicity
            sym, is_antiper = self.machine.comp_periodicity_spatial()
            if is_antiper:
                sym *= 2
            # Set Current (constant J in a layer)
            S_slot = self.machine.stator.slot.comp_surface_active()
            (Nrad, Ntan) = self.machine.stator.winding.get_dim_wind()
            Ntcoil = self.machine.stator.winding.Ntcoil
            Sphase = S_slot / (Nrad * Ntan)
            J = 5e6
            if self.machine.is_synchronous():
                OP = OPdq(felec=60)
                OP.set_Id_Iq(Id=0, Iq=J * Sphase / Ntcoil)
            else:
                OP = OPslip(felec=60)
                OP.set_Id_Iq(Id=J * Sphase / Ntcoil, Iq=0)

            output = Output(
                simu=Simu1(
                    machine=self.machine,
                    input=InputCurrent(OP=OP, Nt_tot=20, Na_tot=200),
                )
            )

            # Generate time and phase vectors in OutElec
            output.simu.input.gen_input()

            # Get current values for given OP
            Is = output.elec.get_Is().values

            # Divide phase current by the number of parallel circuit per phase of winding
            stator = self.machine.stator
            if hasattr(stator.winding, "Npcp") and stator.winding.Npcp is not None:
                Npcp = stator.winding.Npcp
            else:
                Npcp = 1
            Is /= Npcp

            # Get rotor angular position in degress
            angle_rotor = output.elec.axes_dict["time"].get_values(
                normalization="angle_rotor"
            )
            # Draw the machine
            FEMM_dict = draw_FEMM(
                femm,
                output,
                is_mmfr=True,
                is_mmfs=True,
                sym=sym,
                is_antiper=is_antiper,
                type_calc_leakage=0,
                path_save=None,
                is_sliding_band=True,
                is_fast_draw=True,
            )
            # Set the current
            update_FEMM_simulation(
                femm=femm,
                FEMM_dict=FEMM_dict,
                is_sliding_band=True,
                is_internal_rotor=self.machine.rotor.is_internal,
                angle_rotor=angle_rotor,
                Is=Is,
                Ir=None,
                ii=0,
            )
            femm.mi_saveas(save_file_path)  # Save
        except Exception as e:
            err_msg = (
                "Error while drawing machine "
                + self.machine.name
                + " in FEMM:\n"
                + str(e)
            )
            log_error(self, err_msg)
        femm.closefemm()

    def draw_GMSH(self):
        save_file_path = self.get_save_path(ext=".msh", file_type="GMSH (*.msh)")
        # Avoid bug due to user closing the popup witout selecting a file
        if save_file_path is [None, ""]:
            return
        # Create the Simulation
        try:
            mySimu = Simu1(name="test_gmsh_ipm", machine=self.machine)
            myResults = Output(simu=mySimu)
            sym, is_antiper = self.machine.comp_periodicity_spatial()
            if is_antiper:
                sym *= 2
            draw_GMSH(
                output=myResults,
                sym=sym,
                boundary_prop=MagElmer_BP_dict,
                is_lam_only_S=False,
                is_lam_only_R=False,
                user_mesh_dict=None,
                is_sliding_band=True,
                is_airbox=True,
                path_save=save_file_path,
            )
        except Exception as e:
            err_msg = (
                "Error while drawing machine "
                + self.machine.name
                + " in GMSH:\n"
                + str(e)
            )
            log_error(self, err_msg)

    def draw_GMSH_3D(self):
        save_file_path = self.get_save_path(ext="_stator.msh", file_type="GMSH (*.msh)")
        # Avoid bug due to user closing the popup witout selecting a file
        if save_file_path is [None, ""]:
            return
        try:
            gen_3D_mesh(
                lamination=self.machine.stator,
                save_path=save_file_path,
                mesh_size=(self.machine.stator.Rext - self.machine.stator.Rint) / 20,
                Nlayer=20,
                display=False,
            )
        except Exception as e:
            err_msg = (
                "Error while drawing machine "
                + self.machine.name
                + " in GMSH:\n"
                + str(e)
            )
            log_error(self, err_msg)

    def get_save_path(self, ext=".fem", file_type="FEMM (*.fem)"):
        machine_path = config_dict["MAIN"]["MACHINE_DIR"]
        # Ask the user to select a .fem file to save
        if self.machine.name in ["", None]:
            return QFileDialog.getSaveFileName(
                self, self.tr("Save file"), machine_path, file_type
            )[0]
        else:
            def_path = join(machine_path, self.machine.name + ext)
            return QFileDialog.getSaveFileName(
                self, self.tr("Save file"), def_path, file_type
            )[0]

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QMessageBox, QWidget, QListView

from numpy import pi

from .....GUI.Dialog.DMachineSetup.SSkew.Ui_SSkew import Ui_SSkew
from .....GUI.Tools.FloatEdit import FloatEdit
from .....Classes.Skew import Skew

from .....Methods.Machine.Skew import TYPE_SKEW_LIST


class SSkew(Ui_SSkew, QWidget):
    """Step to setup the main lamination parameters"""

    # Signal to DMachineSetup to know that the save popup is needed
    saveNeeded = Signal()
    # Information for the DMachineSetup nav
    step_name = "Skew"

    def __init__(self, machine, material_dict, is_stator=False):
        """Initialize the widget according to machine

        Parameters
        ----------
        self : SSkew
            A SSkew widget
        machine : Machine
            current machine to edit
        material_dict: dict
            Materials dictionary (library + machine)
        is_stator : bool
            To adapt the GUI to set either the stator or the rotor
        """

        # Build the interface according to the .ui file
        QWidget.__init__(self)
        self.setupUi(self)

        # Init widget
        sp_retain = self.label_deg.sizePolicy()
        sp_retain.setRetainSizeWhenHidden(True)
        self.label_deg.setSizePolicy(sp_retain)
        sp_retain = self.tab_angle.sizePolicy()
        sp_retain.setRetainSizeWhenHidden(True)
        self.tab_angle.setSizePolicy(sp_retain)
        self.label_deg.hide()
        self.in_slot_pitch.hide()
        self.tab_angle.hide()
        sp_retain = self.sb_nslice.sizePolicy()
        sp_retain.setRetainSizeWhenHidden(True)
        self.sb_nslice.setSizePolicy(sp_retain)
        sp_retain = self.label_segments.sizePolicy()
        sp_retain.setRetainSizeWhenHidden(True)
        self.label_segments.setSizePolicy(sp_retain)

        listView = QListView(self.cb_type)
        self.cb_type.setView(listView)

        listView = QListView(self.cb_step)
        self.cb_step.setView(listView)

        # Init machine properties
        self.machine = machine
        self.material_dict = material_dict
        self.is_stator = is_stator
        if "PMSM" in self.machine.get_machine_type():
            self.is_PMSM = True
            Zs = self.machine.stator.get_Zs()
            self.type_skew_list = TYPE_SKEW_LIST
        else:
            self.is_PMSM = False
            Zs = self.machine.rotor.get_Zs()
            self.type_skew_list = [TYPE_SKEW_LIST[0]]
        self.slot_pitch = 360 / Zs
        self.label_deg.setText("[°]")

        # Get lamination
        if is_stator:
            lam = self.machine.stator
        else:
            lam = self.machine.rotor

        if lam.skew is not None:
            # Init with skew data already existing in lamination
            self.g_activate.setChecked(True)

            if lam.skew.type_skew not in self.type_skew_list:
                QMessageBox().critical(
                    self,
                    self.tr("Error"),
                    self.tr(
                        "Error while loading skew in current machine: unknown skew type"
                    ),
                )

            self.skew_object = lam.skew
            self.is_step = lam.skew.is_step
            self.type_skew = lam.skew.type_skew

            if self.is_step:
                self.Nslice = lam.skew.Nstep
            else:
                self.Nslice = 2

            if self.type_skew != "user-defined":
                self.rate = lam.skew.rate
            else:
                self.rate = 1
                self.tab_angle.clear()
                self.set_table()
            self.lf_angle.setValue(self.rate * self.slot_pitch)
            self.activate_skew()

        else:
            # Init default parameters in case skew is activated
            self.skew_object = None
            self.rate = 1
            self.type_skew = "linear"
            if self.is_PMSM:
                self.Nslice = 3
                self.is_step = True
            else:
                self.Nslice = 2
                self.is_step = False

            self.g_activate.setChecked(False)

        self.cb_step.setCurrentIndex(not self.is_step)
        self.cb_type.setCurrentIndex(self.type_skew_list.index(self.type_skew))
        self.sb_nslice.setValue(self.Nslice)
        self.lf_angle.setValue(self.rate * self.slot_pitch)
        self.update_angle_deg()

        self.update_hide()

        # Connecting the signals
        self.g_activate.toggled.connect(self.activate_skew)
        self.cb_type.currentIndexChanged.connect(self.set_type)
        self.cb_step.currentIndexChanged.connect(self.set_step)
        self.sb_nslice.valueChanged.connect(self.set_Nslice)
        self.lf_angle.editingFinished.connect(self.set_rate)

    def activate_skew(self):
        """Activate skewing setup"""

        if self.g_activate.isChecked():
            # Calculate skew set up by default
            self.comp_skew()
        else:
            # Remove skew from lamination
            if self.is_stator:
                self.machine.stator.skew = None
            else:
                self.machine.rotor.skew = None
            self.skew_object = None

        self.update_hide()

        self.saveNeeded.emit()

    def update_hide(self):
        """Hide / show widget depending on parameters"""

        if self.g_activate.isChecked():

            # Show common widgets
            self.cb_type.show()
            self.cb_step.show()

            if self.is_step:
                self.cb_type.setEnabled(True)
            else:
                self.cb_type.setEnabled(False)

            if self.is_PMSM:
                self.cb_step.setEnabled(True)
            else:
                self.cb_step.setEnabled(False)

            self.cb_step.setCurrentIndex(not self.is_step)
            self.cb_type.setCurrentIndex(self.type_skew_list.index(self.type_skew))

            self.w_viewer.show()
            self.in_type.show()
            self.in_step.show()
            self.tab_angle.show()

            if self.is_step:
                # step skew
                self.sb_nslice.setEnabled(True)
                self.sb_nslice.setValue(self.Nslice)
                self.sb_nslice.show()
                self.label_segments.show()
            else:
                # continuous skew
                self.sb_nslice.setEnabled(False)
                size = self.sb_nslice.sizePolicy()
                size.setRetainSizeWhenHidden(False)
                self.sb_nslice.setSizePolicy(size)
                self.sb_nslice.hide()
                size = self.label_segments.sizePolicy()
                size.setRetainSizeWhenHidden(False)
                self.label_segments.setSizePolicy(size)
                self.label_segments.hide()

            if self.type_skew == "user-defined":
                self.lf_angle.setEnabled(False)
                self.lf_angle.hide()
                self.label_rate.hide()
                self.label_deg.hide()
                self.in_slot_pitch.hide()

            else:
                self.lf_angle.setEnabled(True)
                self.lf_angle.setValue(self.rate * self.slot_pitch)
                self.lf_angle.show()
                self.update_angle_deg()
                self.label_deg.show()
                self.in_slot_pitch.show()
                self.label_rate.show()

        else:
            # Hide all widgets
            self.cb_step.hide()
            self.cb_type.hide()
            size = self.sb_nslice.sizePolicy()
            size.setRetainSizeWhenHidden(False)
            self.sb_nslice.setSizePolicy(size)
            self.sb_nslice.hide()
            self.lf_angle.hide()
            self.in_type.hide()
            self.in_step.hide()
            size = self.label_segments.sizePolicy()
            size.setRetainSizeWhenHidden(False)
            self.label_segments.setSizePolicy(size)
            self.label_segments.hide()
            self.label_rate.hide()
            self.label_deg.hide()
            self.in_slot_pitch.hide()
            self.tab_angle.hide()
            self.w_viewer.axes.clear()
            self.w_viewer.draw()
            self.w_viewer.hide()

    def set_step(self):
        """Set step/continuous"""

        self.is_step = self.cb_step.currentIndex() == 0

        self.check_values()

        self.comp_skew()

        self.saveNeeded.emit()

    def set_type(self):
        """Set skew widget"""

        self.type_skew = self.type_skew_list[self.cb_type.currentIndex()]

        self.check_values()

        self.comp_skew()

        self.saveNeeded.emit()

    def set_Nslice(self):
        """Set number of slices"""

        self.Nslice = self.sb_nslice.value()

        self.check_values()

        self.comp_skew()

        self.saveNeeded.emit()

    def check_values(self):
        """Check if values are consistent"""

        if not self.is_step:
            # Continuous skew can only be linear
            self.type_skew = "linear"
            self.cb_type.setCurrentIndex(self.type_skew_list.index(self.type_skew))

        if self.type_skew in ["vshape", "zig-zag"] and self.Nslice < 3:
            self.Nslice = 3
            self.sb_nslice.setValue(self.Nslice)

        elif self.type_skew == "user-defined":
            self.tab_angle.clear()
            self.skew_object = None
            self.set_table()

        self.update_hide()

    def set_rate(self):
        """Set rate in slot pitch"""

        self.rate = self.lf_angle.value() / self.slot_pitch

        self.update_angle_deg()

        self.comp_skew()
        self.saveNeeded.emit()

    def update_angle_deg(self):
        """Set angle label in °"""

        if self.is_PMSM:
            lam_name = "Stator "
        else:
            lam_name = "Rotor "
        self.in_slot_pitch.setText(
            lam_name
            + "slot pitch ="
            + format(self.slot_pitch, ".2g")
            + " [°] / Skew rate = "
            + format(self.rate * 100, ".3g")
            + "%"
        )

    def set_table(self):
        """Fill angle table"""

        if self.is_step:
            # stepped skew
            Nlines = self.Nslice  # +1
        else:
            # continuous skew
            Nlines = 2  # +1

        self.tab_angle.clear()
        self.tab_angle.setRowCount(Nlines)
        self.tab_angle.setColumnCount(1)
        self.tab_angle.setVerticalHeaderLabels(
            [str(i + 1) for i in range(Nlines - 1)]  # + ["unit"]
        )
        self.tab_angle.setHorizontalHeaderLabels(["Skew Angles [°]"])

        if self.skew_object is None:
            angle_list = [0 for ii in range(self.Nslice)]
        else:
            angle_list = self.skew_object.angle_list

        for ii in range(Nlines):
            widget = FloatEdit()
            widget.setValue(angle_list[ii] * 180 / pi)
            if self.type_skew == "user-defined":
                widget.editingFinished.connect(self.comp_skew)
            else:
                widget.setEnabled(False)
            self.tab_angle.setCellWidget(
                ii,
                0,
                widget,
            )
        # combobox = QComboBox()
        # listView = QListView(combobox)
        # combobox.setView(listView)
        # combobox.addItems(["rad", "°"])
        # combobox.setCurrentIndex(1)
        # combobox.setEnabled(False)
        # self.tab_angle.setCellWidget(
        #     Nlines - 1,
        #     0,
        #     combobox,
        # )

    def comp_skew(self):
        """Compute skew"""

        is_step = self.is_step
        rate = self.rate
        Nslices = self.Nslice
        type_skew = self.type_skew

        angle_list = None
        if type_skew == "user-defined":
            Nlines = self.tab_angle.rowCount()
            if Nlines > 0:
                angle_list = list()
                for ii in range(Nlines):
                    wid = self.tab_angle.cellWidget(
                        ii,
                        0,
                    )
                    if wid.value() is not None:
                        angle_list.append(wid.value() * pi / 180)
                    else:
                        angle_list.append(0)
                # wid = self.tab_angle.cellWidget(
                #     Nlines - 1,
                #     0,
                # )
                # if wid.currentIndex() == 1:
                #     angle_list = [a * pi / 180 for a in angle_list]

        angle_overall = (
            self.lf_angle.value() * pi / 180
            if self.lf_angle.value() is not None
            else None
        )
        self.skew_object = Skew(
            type_skew=self.type_skew,
            is_step=is_step,
            angle_overall=angle_overall,
            rate=rate,
            Nstep=Nslices,
            angle_list=angle_list,
            z_list=None,
        )

        if self.is_stator:
            self.machine.stator.skew = self.skew_object
        else:
            self.machine.rotor.skew = self.skew_object

        try:
            self.skew_object.comp_angle()
        except Exception as e:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr("Error while calculating skew angle:\n" + str(e)),
            )

        self.update_graph()
        if self.type_skew != "user-defined":
            self.set_table()

    def update_graph(self):
        """Plot the skew"""

        self.w_viewer.axes.clear()

        # Plot the skew in the viewer fig
        try:
            self.machine.rotor.skew.plot(fig=self.w_viewer.fig, ax=self.w_viewer.axes)
        except Exception as e:
            QMessageBox().critical(
                self,
                self.tr("Error"),
                self.tr("Error while plotting skew:\n" + str(e)),
            )

        # Update the Graph
        # self.w_viewer.fig.set_size_inches(8, 4)
        self.w_viewer.draw()

    def emit_save(self):
        self.saveNeeded.emit()

    @staticmethod
    def check(lamination):
        """Check that the current machine have all the needed field set

        Parameters
        ----------
        lamination : Lamination
            Lamination to check

        Returns
        -------
        error : str
            Error message (return None if no error)
        """

        pass

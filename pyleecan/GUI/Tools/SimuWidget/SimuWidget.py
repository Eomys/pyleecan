from os import getcwd, rename, remove
from os.path import join, dirname, abspath, split
from re import match
import pathlib
from PySide2.QtWidgets import QDialog, QFileDialog, QMessageBox
from ....GUI.Tools.SimuWidget.Ui_SimuWidget import Ui_SimuWidget



class SimuWidget(Ui_SimuWidget, QDialog):
    def __init__(self):
        """
        WGuiOption enable to modify some option in the GUI such as:
            - units
            - material library folder

        Parameters:
        machine_setup: DMachineSetup
            Machine widget
        matlib : MatLib
            Material Library
        """
        QDialog.__init__(self)
        self.setupUi(self)


        #RadioButtons Kies Simulatie box
        self.FindNom.toggled.connect(self.findnom)
        self.SpecificRPM.toggled.connect(self.specrpm)
        self.TorqueSlip.toggled.connect(self.torqueslip)

        # Input RadioButtons
        self.TorqueBullet.toggled.connect(self.torquebullet)
        self.PowerBullet.toggled.connect(self.powerbullet)

        # Motorchoise
        self.Open.clicked.connect(self.open)

        # Simulation
        self.Start.clicked.connect(self.start)


    def start(self):
        if self.check():
            if self.FindNom.isChecked():
                if self.TorqueBullet.isChecked():
                    self.NomTorque()
                else:
                    self.NomPower()

            if self.TorqueSlip.isChecked():
                self.TorqueSlip()

            if self.SpecificRPM.isChecked():
                self.SpecSpeed()

    def NomTorque(self):
        pass
        #from pyleecan.SCIM.NomPowSimu import NomPowSimu
        

        
    def NomPower(self):
        pass
        #from pyleecan.SCIM.SCIMSimu import SCIMSimu
        

    def TorqueSlip(self):
        pass
        #from pyleecan.SCIM.TorqueSlipSim import TorqueSlipSim
        #TorqueSlipSim(self.MachineFile(), int(self.VoltageInput.text()), int(self.FreqInput.text()))
        
    def SpecSpeed(self):
        from pyleecan.SCIM.SCIMSimu import SCIMSimu

        freq = int(self.FreqInput.text())
        speed = int(self.RPMInput.text())
        #convert to slip
        slip = 0.05#1 - speed*SCIM.get_pole_pair_number()/(60*freq)
        U = int(self.VoltageInput.text())
        out, para = SCIMSimu("SCIM_010.json", 50, slip, 400)

    def MachineFile(self):
        string = self.Motor.text()
        comp = string.split("/")
        return comp[len(comp)-1]
        

    def check(self):
        checked = True
        return True


        if not ".json" in self.Motor.text() :
            self.error("Motor is not a .json file")

        if self.Motor.text() == "":
            self.error("Choose a motor file")

        try:
            x = int(self.VoltageInput.text())
        except ValueError:
            self.error("Voltage is not a number")
            checked = False

        try:
            x = int(self.FreqInput.text())
        except ValueError:
            self.error("Frequency is not a number")
            checked = False

        if self.RPMInput.isEnabled() == True:
            try:
                x = int(self.RPMInput.text())
            except ValueError:
                self.error("Speed is not a number")
                checked = False

        if self.TorqueInput.isEnabled() == True:
            try:
                x = int(self.TorqueInput.text())
            except ValueError:
                self.error("Torque is not a number")
                checked = False

        if self.PowerInput.isEnabled() == True:
            try:
                x = int(self.PowerInput.text())
            except ValueError:
                self.error("Power is not a number")
                checked = False

        return checked

    def error(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(text)
        x = msg.exec_()


    def open(self):
        Motorpath = str(pathlib.Path(__file__).parent.parent.parent.parent.absolute()) + "\\Data\\Machine"
        file = QFileDialog.getOpenFileName(self, 'Open file', Motorpath, "JSON File (*.json)")
        self.Motor.setText(str(file[0]))


    def powerbullet(self):
        self.PowerInput.setEnabled(True)
        self.TorqueInput.setEnabled(False)

    def torquebullet(self):
        self.PowerInput.setEnabled(False)
        self.TorqueInput.setEnabled(True)

    def findnom(self):
        self.TorqueBullet.setChecked(True)
        self.TorqueBullet.setEnabled(True)
        self.TorqueInput.setEnabled(True)
        self.PowerBullet.setEnabled(True)
        self.PowerInput.setEnabled(False)
        self.RPMInput.setEnabled(False)

    def specrpm(self):
        self.TorqueBullet.setEnabled(False)
        self.TorqueInput.setEnabled(False)
        self.PowerBullet.setEnabled(False)
        self.PowerInput.setEnabled(False)
        self.RPMInput.setEnabled(True)

    def torqueslip(self):
        self.TorqueBullet.setEnabled(False)
        self.TorqueInput.setEnabled(False)
        self.PowerBullet.setEnabled(False)
        self.PowerInput.setEnabled(False)
        self.RPMInput.setEnabled(False)

from PySide2.QtCore import QSize
from PySide2.QtWidgets import QGroupBox, QLabel, QVBoxLayout, QWidget

from ......GUI import gui_option


class WCondOut(QGroupBox):
    """Setup of QGroupBox for output for Winding Conductor"""

    def __init__(self, parent=None):
        """Initialize the widget"""

        QGroupBox.__init__(self, parent)
        # Set main widget
        self.u = gui_option.unit
        self.setTitle(self.tr("Output"))
        self.setMinimumSize(QSize(200, 0))
        self.setObjectName("g_output")
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName("layout")
        # The widget is composed of several QLabel in a vertical layout
        self.out_Sslot = QLabel(self)
        self.out_Sslot.setObjectName("out_Sslot")
        self.out_Sslot.setToolTip("Slot surface")
        self.layout.addWidget(self.out_Sslot)

        self.out_Saslot = QLabel(self)
        self.out_Saslot.setObjectName("out_Saslot")
        self.out_Saslot.setToolTip("Slot active surface")
        self.layout.addWidget(self.out_Saslot)

        self.out_Sact = QLabel(self)
        self.out_Sact.setObjectName("out_Sact")
        self.out_Sact.setToolTip("Conductor active surface")
        self.layout.addWidget(self.out_Sact)

        self.out_Ncps = QLabel(self)
        self.out_Ncps.setObjectName("out_Ncps")
        self.out_Ncps.setToolTip("Number of conductors per slot")
        self.layout.addWidget(self.out_Ncps)

        self.out_K = QLabel(self)
        self.out_K.setObjectName("out_K")
        self.out_K.setToolTip("Conductor active surface over total slot active surface")
        self.layout.addWidget(self.out_K)

        self.out_MLT = QLabel(self)
        self.out_MLT.setObjectName("out_MLT")
        self.layout.addWidget(self.out_MLT)
        self.out_MLT.setToolTip("Mean Length Turn")

        self.out_Mwind = QLabel(self)
        self.out_Mwind.setObjectName("out_Mwind")
        self.layout.addWidget(self.out_Mwind)
        self.out_Mwind.setToolTip("Total winding mass [kg]")

        self.out_Rwind = QLabel(self)
        self.out_Rwind.setObjectName("out_Rwind")
        self.layout.addWidget(self.out_Rwind)
        self.out_Rwind.setToolTip("Phase winding resistance at 20°C")

        self.out_RwindLL = QLabel(self)
        self.out_RwindLL.setObjectName("out_RwindLL")
        self.layout.addWidget(self.out_RwindLL)
        self.out_RwindLL.setToolTip("Line-to-line winding resistance at 20°C")

    def comp_output(self):
        """Update the Output with the computed values

        Parameters
        ----------
        self : WCondOut
            A WCondOut object
        """

        obj = self
        while not hasattr(obj.parent(), "lam") or obj.parent() is None:
            obj = obj.parent()
        parent = obj.parent()
        lam = parent.lam

        Sslot_txt = self.tr("Slot surface: ")
        Saslot_txt = self.tr("Slot active surface: ")
        Sa_txt = self.tr("Conductor active surface: ")
        Ncps_txt = self.tr("Conductors per slot: ")
        K_txt = self.tr("Fill factor: ")
        MLT_txt = "Mean Length Turn: "
        Mwind_txt = "Winding mass: "
        Rwind_txt = "Phase resistance at 20°C: "
        RwindLL_txt = "Line-to-line resistance at 20°C: "

        # Compute all the needed output as string
        try:
            Sslot = format(self.u.get_m2(lam.slot.comp_surface()), ".4g")
        except Exception:  # Unable to compute the slot surface
            Sslot = "?"
        try:
            Saslot = format(self.u.get_m2(lam.slot.comp_surface_active()), ".4g")
        except Exception:  # Unable to compute the slot active surface
            Saslot = "?"
        try:
            Sact = format(
                self.u.get_m2(lam.winding.conductor.comp_surface_active()), ".4g"
            )
        except Exception:  # Unable to compute the conductor active surface
            Sact = "?"
        try:
            Ncps = str(int(lam.winding.comp_Ncps()))
        except Exception:  # Unable to compute the number of conductors per slot
            Ncps = "?"
        try:
            K = "%.2f" % (lam.comp_fill_factor() * 100)
        except Exception:  # Unable to compute the fill factor (Not set)
            K = "?"
        try:
            MLT = format(self.u.get_m(lam.comp_lengths_winding()["MLT"]), ".4g")
        except Exception:  # Unable to compute MLT
            MLT = "?"
        try:
            Mwind = format(lam.comp_masses()["Mwind"], ".4g")
        except Exception:  # Unable to compute MLT
            Mwind = "?"
        try:
            Rwind = format(lam.comp_resistance_wind(T=20), ".2g")
            RwindLL = format(
                2 * lam.comp_resistance_wind(T=20), ".2g"
            )  # *2 for star connection, *2/3 for delta connection /!\
        except Exception:  # Unable to compute MLT
            Rwind = "?"
            RwindLL = "?"

        # Update the GUI to display the Output
        self.out_Sslot.setText(Sslot_txt + Sslot + " [" + self.u.get_m2_name() + "]")
        self.out_Saslot.setText(Saslot_txt + Saslot + " [" + self.u.get_m2_name() + "]")
        self.out_Sact.setText(Sa_txt + Sact + " [" + self.u.get_m2_name() + "]")
        self.out_Ncps.setText(Ncps_txt + Ncps)
        self.out_K.setText(K_txt + K + " %")
        self.out_MLT.setText(MLT_txt + MLT + " [" + self.u.get_m_name() + "]")
        self.out_Mwind.setText(Mwind_txt + Mwind + " [kg]")
        self.out_Rwind.setText(Rwind_txt + Rwind + " [Ohm]")
        self.out_RwindLL.setText(RwindLL_txt + RwindLL + " [Ohm]")

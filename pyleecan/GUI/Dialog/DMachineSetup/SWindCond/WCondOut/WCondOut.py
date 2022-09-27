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
        self.out_H = QLabel(self)
        self.out_H.setObjectName("out_H")
        self.layout.addWidget(self.out_H)

        self.out_W = QLabel(self)
        self.out_W.setObjectName("out_W")
        self.layout.addWidget(self.out_W)

        self.out_S = QLabel(self)
        self.out_S.setObjectName("out_S")
        self.layout.addWidget(self.out_S)

        self.out_Sact = QLabel(self)
        self.out_Sact.setObjectName("out_Sact")
        self.out_Sact.setToolTip("Conductor active surface")
        self.layout.addWidget(self.out_Sact)

        self.out_K = QLabel(self)
        self.out_K.setObjectName("out_K")
        self.out_K.setToolTip("Conductor active surface over total slot active surface")
        self.layout.addWidget(self.out_K)

        self.out_MLT = QLabel(self)
        self.out_MLT.setObjectName("out_MLT")
        self.layout.addWidget(self.out_MLT)
        self.out_MLT.setToolTip("Mean Length Turn")

        self.out_Rwind = QLabel(self)
        self.out_Rwind.setObjectName("out_Rwind")
        self.layout.addWidget(self.out_Rwind)
        self.out_Rwind.setToolTip("Phase winding resistance at 20°C")

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

        H_txt = self.tr("Hcond = ")
        W_txt = self.tr("Wcond = ")
        S_txt = self.tr("Scond = ")
        Sa_txt = self.tr("Scond_active = ")
        if lam.is_stator:
            K_txt = self.tr("Ksfill = ")
        else:
            K_txt = self.tr("Krfill = ")
        MLT_txt = "Mean Length Turn = "
        Rwind_txt = "Rwind 20°C = "

        # We compute the output only if the conductor is correctly set
        if parent.check(lam) is None:
            # Compute all the needed output as string
            H = format(self.u.get_m(lam.winding.conductor.comp_height()), ".4g")
            W = format(self.u.get_m(lam.winding.conductor.comp_width()), ".4g")
            S = format(self.u.get_m2(lam.winding.conductor.comp_surface()), ".4g")
            Sact = format(
                self.u.get_m2(lam.winding.conductor.comp_surface_active()), ".4g"
            )
            try:
                K = "%.2f" % (lam.comp_fill_factor() * 100)
            except Exception:  # Unable to compute the fill factor (Not set)
                K = "?"

            try:
                MLT = format(self.u.get_m(lam.comp_lengths_winding()["MLT"]), ".4g")
            except Exception:  # Unable to compute MLT
                MLT = "?"
            try:
                Rwind = format(lam.comp_resistance_wind(T=20), ".4g")
            except Exception:  # Unable to compute MLT
                Rwind = "?"

            # Update the GUI to display the Output
            self.out_H.setText(H_txt + H + " [" + self.u.get_m_name() + "]")
            self.out_W.setText(W_txt + W + " [" + self.u.get_m_name() + "]")
            self.out_S.setText(S_txt + S + " [" + self.u.get_m2_name() + "]")
            self.out_Sact.setText(Sa_txt + Sact + " [" + self.u.get_m2_name() + "]")
            self.out_K.setText(K_txt + K + " %")
            self.out_MLT.setText(MLT_txt + MLT + " [" + self.u.get_m_name() + "]")
            self.out_Rwind.setText(Rwind_txt + Rwind + " [Ohm]")
        else:
            # We can't compute the output => We erase the previous version
            # (that way the user know that something is wrong)
            self.out_H.setText(H_txt + "?")
            self.out_W.setText(W_txt + "?")
            self.out_S.setText(S_txt + "?")
            self.out_Sact.setText(Sa_txt + "?")
            self.out_K.setText(K_txt + "? %")
            self.out_MLT.setText(MLT_txt + "?")
            self.out_Rwind.setText(Rwind_txt + "?")

        if parent is not None:
            if parent.g_ins.isChecked():
                self.out_H.show()
                self.out_W.show()
                self.out_S.show()
            else:
                self.out_H.hide()
                self.out_W.hide()
                self.out_S.hide()

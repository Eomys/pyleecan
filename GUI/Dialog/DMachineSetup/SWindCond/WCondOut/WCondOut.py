from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QGroupBox, QLabel, QVBoxLayout, QWidget

from pyleecan.GUI import gui_option


class WCondOut(QGroupBox):
    """Setup of QGroupBox for output for Winding Conductor
    """

    def __init__(self, parent=None):
        """Initialize the widget
        """

        QWidget.__init__(self, parent)
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
        self.layout.addWidget(self.out_Sact)

        self.out_K = QLabel(self)
        self.out_K.setObjectName("out_K")
        self.layout.addWidget(self.out_K)

    def comp_output(self):
        """Update the Output with the computed values

        Parameters
        ----------
        self : WCondOut
            A WCondOut object
        """

        lam = self.parent().lam
        H_txt = self.tr("Hcond = ")
        W_txt = self.tr("Wcond = ")
        S_txt = self.tr("Scond = ")
        Sa_txt = self.tr("Scond_active = ")
        if lam.is_stator:
            K_txt = self.tr("Ksfill = ")
        else:
            K_txt = self.tr("Krfill = ")
        # We compute the output only if the slot is correctly set
        if self.parent().check() is None:
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

            # Update the GUI to display the Output
            self.out_H.setText(H_txt + H + " " + self.u.get_m_name())
            self.out_W.setText(W_txt + W + " " + self.u.get_m_name())
            self.out_S.setText(S_txt + S + " " + self.u.get_m2_name())
            self.out_Sact.setText(Sa_txt + Sact + " " + self.u.get_m2_name())
            self.out_K.setText(K_txt + K + " %")
        else:
            # We can't compute the output => We erase the previous version
            # (that way the user know that something is wrong)
            self.out_H.setText(H_txt + "?")
            self.out_W.setText(W_txt + "?")
            self.out_S.setText(S_txt + "?")
            self.out_Sact.setText(Sa_txt + "?")
            self.out_K.setText(K_txt + "? %")

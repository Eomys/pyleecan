from qtpy.QtCore import QSize
from qtpy.QtWidgets import QGroupBox, QLabel, QVBoxLayout, QWidget

from ......GUI import gui_option


class WBarOut(QGroupBox):
    """Setup of QGroupBox for output for Winding Slot"""

    def __init__(self, parent=None):
        """Initialize the widget"""
        # Main widget setup
        QGroupBox.__init__(self, parent)
        self.u = gui_option.unit
        self.setTitle(self.tr("Output"))
        self.setMinimumSize(QSize(200, 0))
        self.setObjectName("g_output")
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName("layout")

        # The widget is composed of 3 QLabel in a vertical layout
        self.out_Sbar = QLabel(self)
        self.out_Sbar.setObjectName("out_Sbar")
        self.layout.addWidget(self.out_Sbar)

        self.out_Sslot = QLabel(self)
        self.out_Sslot.setObjectName("out_Sslot")
        self.layout.addWidget(self.out_Sslot)

        self.out_ratio = QLabel(self)
        self.out_ratio.setMinimumSize(QSize(140, 0))
        self.out_ratio.setObjectName("out_ratio")
        self.layout.addWidget(self.out_ratio)

    def comp_output(self):
        """Update the Output text with the computed values

        Parameters
        ----------
        self : WBarOut
            A WBarOut object
        """

        # For readibility
        obj = self.parent().machine.rotor.winding.conductor

        # Update Bar surface if possible
        txt_Sbar = self.tr("Sbar: ")
        try:
            Sbar = format(self.u.get_m2(obj.comp_surface_active()), ".4g")
            self.out_Sbar.setText(txt_Sbar + Sbar + " [" + self.u.get_m2_name() + "]")
        except Exception:
            self.out_Sbar.setText(txt_Sbar + "?")
        # Update Slot surface if possible
        txt_Sslot = self.tr("Sslot: ")
        try:
            Sslot = format(
                self.u.get_m2(self.parent().machine.rotor.slot.comp_surface()), ".4g"
            )
            self.out_Sslot.setText(
                txt_Sslot + Sslot + " [" + self.u.get_m2_name() + "]"
            )
        except Exception:
            self.out_Sslot.setText(txt_Sslot + " ?")
        # Update ratio if possible
        txt_ratio = self.tr("Sbar / Sslot: ")
        try:
            ratio = "%.4g" % (float(Sbar) / float(Sslot) * 100)
            self.out_ratio.setText(txt_ratio + ratio + " [%]")
        except Exception:
            self.out_ratio.setText(txt_ratio + "?")

from PySide2.QtCore import QSize
from PySide2.QtWidgets import QGroupBox, QLabel, QVBoxLayout, QWidget

from ......GUI import gui_option


class WBoreOut(QGroupBox):
    """Setup of QGroupBox for output for Bore shape"""

    def __init__(self, parent=None):
        """Initialize the widget"""

        QGroupBox.__init__(self, parent)
        # Set main widget
        self.setTitle(self.tr("Output"))
        self.setMinimumSize(QSize(200, 0))
        self.setObjectName("g_output")
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName("layout")
        # The widget is composed of several QLabel in a vertical layout
        self.out_Rmin = QLabel(self)
        self.out_Rmin.setObjectName("out_Rmin")
        self.layout.addWidget(self.out_Rmin)

        self.out_surface = QLabel(self)
        self.out_surface.setObjectName("out_surface")
        self.layout.addWidget(self.out_surface)

    def comp_output(self):
        """Update the Output with the computed values

        Parameters
        ----------
        self : WBoreOut
            A WBoreOut object
        """

        obj = self
        while not hasattr(obj.parent(), "lamination") or obj.parent() is None:
            obj = obj.parent()
        parent = obj.parent()
        lam = parent.lamination

        if lam.is_stator:
            lam_name = "Stator"
        else:
            lam_name = "Rotor"

        R_txt = self.tr("Min Radius: ")
        S_txt = self.tr(lam_name + " surface: ")

        if parent.check(lam) is None:
            # Compute all the needed output as string
            Rmin = format(gui_option.unit.get_m(lam.bore.comp_Rmin()), ".4g")
            S = format(gui_option.unit.get_m2(lam.comp_surfaces()["Slam"]), ".4g")

            # Update the GUI to display the Output
            self.out_Rmin.setText(
                R_txt + Rmin + " [" + gui_option.unit.get_m_name() + "]"
            )
            self.out_surface.setText(
                S_txt + S + " [" + gui_option.unit.get_m2_name() + "]"
            )
        else:
            # We can't compute the output => We erase the previous version
            # (that way the user know that something is wrong)
            self.out_Rmin.setText(R_txt + "?")
            self.out_surface.setText(S_txt + "?")

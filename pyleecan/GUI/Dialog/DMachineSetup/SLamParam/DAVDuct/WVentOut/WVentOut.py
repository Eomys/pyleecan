from numpy import pi
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QGroupBox, QLabel, QVBoxLayout, QWidget

from .......Classes.Lamination import Lamination
from .......GUI import gui_option


class WVentOut(QGroupBox):
    """Setup of QGroupBox for output for Ventilation"""

    def __init__(self, parent=None):
        """Initialize the widget"""

        QGroupBox.__init__(self, parent)
        # Init the main widget
        self.u = gui_option.unit
        self.setTitle(self.tr("Output"))
        self.setMinimumSize(QSize(300, 0))
        self.setObjectName("g_output")
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName("layout")

        # The widget is composed of several QLabel in a vertical layout
        self.out_Rint = QLabel(self)
        self.out_Rint.setObjectName("out_Rint")
        self.layout.addWidget(self.out_Rint)

        self.out_Rext = QLabel(self)
        self.out_Rext.setObjectName("out_Rext")
        self.layout.addWidget(self.out_Rext)

        self.out_lam_surface = QLabel(self)
        self.out_lam_surface.setObjectName("out_lam_surface")
        self.layout.addWidget(self.out_lam_surface)

        self.out_lam_vent_surface = QLabel(self)
        self.out_lam_vent_surface.setObjectName("out_lam_vent_surface")
        self.layout.addWidget(self.out_lam_vent_surface)

        self.out_vent_surf = QLabel(self)
        self.out_vent_surf.setObjectName("out_vent_surf")
        self.layout.addWidget(self.out_vent_surf)

        # self.layout.addWidget(self)

    def comp_output(self):
        """Update the Output group according to the current value

        Parameters
        ----------
        self : WVentOut
            A WVentOut object
        """

        if hasattr(self.parent(), "lam"):
            lam = self.parent().lam
        else:  # For VentUD
            lam = self.parent().parent().parent().parent().lam

        # Lamination output
        Rint = format(self.u.get_m(lam.Rint), ".4g")
        self.out_Rint.setText(
            self.tr("Lam. internal radius: ") + Rint + " " + self.u.get_m_name()
        )

        Rext = format(self.u.get_m(lam.Rext), ".4g")
        self.out_Rext.setText(
            self.tr("Lam. external radius: ") + Rext + " " + self.u.get_m_name()
        )
        Slam = format(self.u.get_m2(pi * (lam.Rext ** 2 - lam.Rint ** 2)), ".4g")
        self.out_lam_surface.setText(
            self.tr("Lam. surface (no slot, no vent): ")
            + Slam
            + " "
            + self.u.get_m2_name()
        )
        # Ventilation output
        try:
            lam = Lamination(Rext=lam.Rext, Rint=lam.Rint)

            lam.axial_vent = self.parent().lam.axial_vent
            Svent = format(self.u.get_m2(lam.comp_surface_axial_vent()), ".4g")
        except Exception:
            Svent = 0
            self.out_lam_vent_surface.setText(
                self.tr("Lam. surface (no slot, with vent): ?")
            )
            self.out_vent_surf.setText(self.tr("Vent surface: ?"))
        if Svent != 0:
            Slv = format(float(Slam) - float(Svent), ".4g")
            self.out_lam_vent_surface.setText(
                self.tr("Lam. surface (no slot, with vent): ")
                + Slv
                + " "
                + self.u.get_m2_name()
            )
            self.out_vent_surf.setText(
                self.tr("Vent surface: ") + Svent + " " + self.u.get_m2_name()
            )

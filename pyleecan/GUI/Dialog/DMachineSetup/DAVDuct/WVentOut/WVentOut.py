from numpy import pi
from PySide2.QtCore import QSize
from PySide2.QtWidgets import QGroupBox, QLabel, QVBoxLayout, QWidget

from ......Classes.Lamination import Lamination
from ......GUI import gui_option


class WVentOut(QGroupBox):
    """Setup of QGroupBox for output for Ventilation"""

    def __init__(self, parent=None):
        """Initialize the widget"""

        QGroupBox.__init__(self, parent)
        # Init the main widget
        self.u = gui_option.unit
        self.setTitle(self.tr("Output"))
        self.setMinimumSize(QSize(200, 0))
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

        self.out_sp = QLabel(self)
        self.out_sp.setObjectName("out_sp")
        self.layout.addWidget(self.out_sp)
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
            vent = self.parent().vent
        else:  # For VentUD
            lam = self.parent().parent().parent().parent().lam
            vent = self.parent().parent().parent().parent().vent

        # Lamination output
        lam_name = lam.get_label(is_add_id=False)
        Rint = format(self.u.get_m(lam.Rint), ".4g")
        self.out_Rint.setText(
            lam_name + ".Rint: " + Rint + " [" + self.u.get_m_name() + "]"
        )

        Rext = format(self.u.get_m(lam.Rext), ".4g")
        self.out_Rext.setText(
            lam_name + ".Rext: " + Rext + " [" + self.u.get_m_name() + "]"
        )

        if vent.Zh not in [None, 0]:
            sp_txt = (
                format(pi / vent.Zh, ".4g")
                + " [rad], "
                + format(180 / vent.Zh, ".4g")
                + " [°]"
            )
        else:
            sp_txt = "?"
        self.out_sp.setText("pi / Zh : " + sp_txt)

        Slam = pi * (lam.Rext ** 2 - lam.Rint ** 2)
        Slam_txt = format(self.u.get_m2(Slam), ".4g")
        self.out_lam_surface.setText(
            "Active surface: " + Slam_txt + " [" + self.u.get_m2_name() + "]"
        )
        self.out_lam_vent_surface.hide()

        # Ventilation output
        try:
            Svent = lam.comp_surface_axial_vent()
        except Exception:
            Svent = 0

        if Svent != 0:
            Slv = format(self.u.get_m2(float(Slam) - float(Svent)), ".4g")
            Svent = format(self.u.get_m2(float(Svent)), ".4g")
            self.out_lam_surface.setText(
                self.tr("Active surface: ") + Slv + " [" + self.u.get_m2_name() + "]"
            )
            self.out_vent_surf.setText(
                self.tr("Cooling surface: ") + Svent + " [" + self.u.get_m2_name() + "]"
            )
        else:
            self.out_vent_surf.setText(self.tr("Cooling surface: ?"))

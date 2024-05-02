from qtpy.QtCore import QSize
from qtpy.QtWidgets import QGroupBox, QLabel, QVBoxLayout, QWidget

from ......GUI import gui_option


class WWSlotOut(QGroupBox):
    """Setup of QGroupBox for output for Winding Slot"""

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
        self.out_Wlam = QLabel(self)
        self.out_Wlam.setObjectName("out_Wlam")
        self.layout.addWidget(self.out_Wlam)

        self.out_slot_height = QLabel(self)
        self.out_slot_height.setObjectName("out_slot_height")
        self.layout.addWidget(self.out_slot_height)

        self.out_yoke_height = QLabel(self)
        self.out_yoke_height.setObjectName("out_yoke_height")
        self.layout.addWidget(self.out_yoke_height)

        self.out_wind_surface = QLabel(self)
        self.out_wind_surface.setObjectName("out_wind_surface")
        self.layout.addWidget(self.out_wind_surface)

        self.out_tot_surface = QLabel(self)
        self.out_tot_surface.setObjectName("out_tot_surface")
        self.layout.addWidget(self.out_tot_surface)

        self.out_op_angle = QLabel(self)
        self.out_op_angle.setObjectName("out_op_angle")
        self.layout.addWidget(self.out_op_angle)

        # self.layout.addWidget(self)

    def comp_output(self):
        """Update the Output with the computed values

        Parameters
        ----------
        self : WWSlotOut
            A WWSlotOut object
        """

        obj = self
        while not hasattr(obj.parent(), "lamination") or obj.parent() is None:
            obj = obj.parent()
        parent = obj.parent()
        lam = parent.lamination
        if hasattr(parent, "is_notch"):
            is_notch = parent.is_notch
        else:
            is_notch = False

        if lam.is_stator:
            lam_name = "Stator"
        else:
            lam_name = "Rotor"

        if is_notch:
            AO_txt = self.tr("Opening angle: ")
            WS_txt = ""
            self.out_wind_surface.hide()
            TS_txt = self.tr("Notch surface: ")
            SH_txt = self.tr("Notch height: ")
            YH_txt = ""
            self.out_yoke_height.hide()
        else:
            AO_txt = self.tr("Opening angle: ")
            WS_txt = self.tr("Active surface: ")
            TS_txt = self.tr("Slot surface: ")
            SH_txt = self.tr("Slot height: ")
            YH_txt = self.tr("Yoke height: ")

        Wlam = format(gui_option.unit.get_m(lam.Rext - lam.Rint), ".4g")
        self.out_Wlam.setText(
            self.tr(lam_name + " width: ")
            + Wlam
            + " ["
            + gui_option.unit.get_m_name()
            + "]"
        )
        check = False
        try:
            parent.check(lam)
            if parent.check(lam) is None:
                check = True
        except:
            check = False
        if check:
            # Compute all the needed output as string
            w_surf = format(
                gui_option.unit.get_m2(lam.slot.comp_surface_active()), ".4g"
            )
            tot_surf = format(gui_option.unit.get_m2(lam.slot.comp_surface()), ".4g")
            op_angle = "%.4g" % lam.slot.comp_angle_opening()
            slot_height = format(gui_option.unit.get_m(lam.slot.comp_height()), ".4g")
            yoke_height = format(gui_option.unit.get_m(lam.comp_height_yoke()), ".4g")

            # Update the GUI to display the Output
            self.out_wind_surface.setText(
                WS_txt + w_surf + " [" + gui_option.unit.get_m2_name() + "]"
            )
            self.out_tot_surface.setText(
                TS_txt + tot_surf + " [" + gui_option.unit.get_m2_name() + "]"
            )
            self.out_op_angle.setText(AO_txt + op_angle + " [rad]")
            self.out_slot_height.setText(
                SH_txt + slot_height + " [" + gui_option.unit.get_m_name() + "]"
            )
            self.out_yoke_height.setText(
                YH_txt + yoke_height + " [" + gui_option.unit.get_m_name() + "]"
            )
        else:
            # We can't compute the output => We erase the previous version
            # (that way the user know that something is wrong)
            self.out_wind_surface.setText(WS_txt + "?")
            self.out_tot_surface.setText(TS_txt + "?")
            self.out_op_angle.setText(AO_txt + "?")
            self.out_slot_height.setText(SH_txt + "?")
            self.out_yoke_height.setText(YH_txt + "?")

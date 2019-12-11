from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QGroupBox, QLabel, QVBoxLayout, QWidget

from pyleecan.GUI import gui_option


class WMagnetOut(QGroupBox):
    """Setup of QGroupBox for output for Magnet
    """

    def __init__(self, parent=None):
        """Initialize the widget
        """

        QWidget.__init__(self, parent)
        self.u = gui_option.unit
        # Setup main widget
        self.setTitle(self.tr("Output"))
        self.setMinimumSize(QSize(200, 0))
        self.setObjectName("g_output")
        self.layout = QVBoxLayout(self)
        self.layout.setObjectName("layout")
        # The widget is composed of several QLabel in a vertical layout
        self.out_Smag = QLabel(self)
        self.out_Smag.setObjectName("out_Smag")
        self.layout.addWidget(self.out_Smag)

        self.out_gap = QLabel(self)
        self.out_gap.setObjectName("out_gap")
        self.layout.addWidget(self.out_gap)

        self.out_gap_min = QLabel(self)
        self.out_gap_min.setObjectName("out_gap_min")
        self.layout.addWidget(self.out_gap_min)

        self.out_taum = QLabel(self)
        self.out_taum.setObjectName("out_taum")
        self.layout.addWidget(self.out_taum)

    def comp_output(self):
        """Update the Output text with the computed values

        Parameters
        ----------
        self : WMagnetOut
            A WMagnetOut object
        """
        mach = self.parent().machine
        # Gap is set in SMachineDimension
        gap = format(self.u.get_m(mach.comp_width_airgap_mag()), ".4g")
        self.out_gap.setText(self.tr("gap: ") + gap + " " + self.u.get_m_name())

        mag_txt = self.tr("Magnet surface: ")
        gm_txt = self.tr("gap_min: ")
        taum_txt = self.tr("taum: ")

        if self.parent().check() is None:
            # We compute the output only if the slot is correctly set
            Zs = mach.rotor.slot.Zs
            # Compute all the needed output as string (scientific notation with
            # 2 digits)
            Smag = format(
                self.u.get_m2(mach.rotor.slot.magnet[0].comp_surface()), ".4g"
            )
            gap_min = format(self.u.get_m(mach.comp_width_airgap_mec()), ".4g")

            taum = 100 * mach.rotor.slot.magnet[0].comp_ratio_opening(Zs / 2.0)
            taum = "%.4g" % (taum)

            # Update the GUI to display the Output
            self.out_Smag.setText(mag_txt + Smag + " " + self.u.get_m2_name())
            self.out_gap_min.setText(gm_txt + gap_min + " " + self.u.get_m_name())
            self.out_taum.setText(taum_txt + taum + " %")
        else:
            # We can't compute the output => We erase the previous version
            # (that way the user know that something is wrong without
            # clicking next)
            self.out_Smag.setText(mag_txt + "?")
            self.out_gap_min.setText(gm_txt + "?")
            self.out_taum.setText(taum_txt + " ?")

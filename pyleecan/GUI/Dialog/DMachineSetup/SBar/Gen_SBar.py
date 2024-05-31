# -*- coding: utf-8 -*-
"""File generated according to SBar/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SBar.Ui_SBar import Ui_SBar


class Gen_SBar(Ui_SBar):
    def setupUi(self, SBar):
        """Abstract class to update the widget according to the csv doc"""
        Ui_SBar.setupUi(self, SBar)
        # Setup of in_Hscr
        txt = self.tr("""short circuit ring section radial height [m]""")
        self.in_Hscr.setWhatsThis(txt)
        self.in_Hscr.setToolTip(txt)

        # Setup of lf_Hscr
        self.lf_Hscr.validator().setBottom(0)
        txt = self.tr("""short circuit ring section radial height [m]""")
        self.lf_Hscr.setWhatsThis(txt)
        self.lf_Hscr.setToolTip(txt)

        # Setup of unit_Hscr
        txt = self.tr("""short circuit ring section radial height [m]""")
        self.unit_Hscr.setWhatsThis(txt)
        self.unit_Hscr.setToolTip(txt)

        # Setup of in_Lscr
        txt = self.tr("""short circuit ring section axial length""")
        self.in_Lscr.setWhatsThis(txt)
        self.in_Lscr.setToolTip(txt)

        # Setup of lf_Lscr
        self.lf_Lscr.validator().setBottom(0)
        txt = self.tr("""short circuit ring section axial length""")
        self.lf_Lscr.setWhatsThis(txt)
        self.lf_Lscr.setToolTip(txt)

        # Setup of unit_Lscr
        txt = self.tr("""short circuit ring section axial length""")
        self.unit_Lscr.setWhatsThis(txt)
        self.unit_Lscr.setToolTip(txt)

        # Setup of in_Lewout
        txt = self.tr(
            """straight length of the conductors outside the lamination before the curved part of winding overhang [m] - can be negative to tune the average turn length (only used in voltage driven simulations)"""
        )
        self.in_Lewout.setWhatsThis(txt)
        self.in_Lewout.setToolTip(txt)

        # Setup of lf_Lewout
        self.lf_Lewout.validator().setBottom(0)
        txt = self.tr(
            """straight length of the conductors outside the lamination before the curved part of winding overhang [m] - can be negative to tune the average turn length (only used in voltage driven simulations)"""
        )
        self.lf_Lewout.setWhatsThis(txt)
        self.lf_Lewout.setToolTip(txt)

        # Setup of w_mat_scr
        txt = self.tr("""Material of the Rotor short circuit ring""")
        self.w_mat_scr.setWhatsThis(txt)
        self.w_mat_scr.setToolTip(txt)

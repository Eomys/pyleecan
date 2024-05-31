# -*- coding: utf-8 -*-
"""File generated according to PCondType11/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.PCondType11.Ui_PCondType11 import (
    Ui_PCondType11,
)


class Gen_PCondType11(Ui_PCondType11):
    def setupUi(self, PCondType11):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PCondType11.setupUi(self, PCondType11)
        # Setup of in_Nwpc1_tan
        txt = self.tr(
            """number of form wound strands in parallel per conductor along tangential (horizontal) direction"""
        )
        self.in_Nwpc1_tan.setWhatsThis(txt)
        self.in_Nwpc1_tan.setToolTip(txt)

        # Setup of si_Nwpc1_tan
        self.si_Nwpc1_tan.setMinimum(1)
        self.si_Nwpc1_tan.setMaximum(999999)
        txt = self.tr(
            """number of form wound strands in parallel per conductor along tangential (horizontal) direction"""
        )
        self.si_Nwpc1_tan.setWhatsThis(txt)
        self.si_Nwpc1_tan.setToolTip(txt)

        # Setup of in_Nwpc1_rad
        txt = self.tr(
            """number of form wound strands in parallel per conductor along radial (vertical) direction"""
        )
        self.in_Nwpc1_rad.setWhatsThis(txt)
        self.in_Nwpc1_rad.setToolTip(txt)

        # Setup of si_Nwpc1_rad
        self.si_Nwpc1_rad.setMinimum(1)
        self.si_Nwpc1_rad.setMaximum(999999)
        txt = self.tr(
            """number of form wound strands in parallel per conductor along radial (vertical) direction"""
        )
        self.si_Nwpc1_rad.setWhatsThis(txt)
        self.si_Nwpc1_rad.setToolTip(txt)

        # Setup of in_Hwire
        txt = self.tr("""cf schematics, single strand height without insulation""")
        self.in_Hwire.setWhatsThis(txt)
        self.in_Hwire.setToolTip(txt)

        # Setup of lf_Hwire
        self.lf_Hwire.validator().setBottom(0)
        txt = self.tr("""cf schematics, single strand height without insulation""")
        self.lf_Hwire.setWhatsThis(txt)
        self.lf_Hwire.setToolTip(txt)

        # Setup of in_Wwire
        txt = self.tr("""cf schematics, single strand width without insulation""")
        self.in_Wwire.setWhatsThis(txt)
        self.in_Wwire.setToolTip(txt)

        # Setup of lf_Wwire
        self.lf_Wwire.validator().setBottom(0)
        txt = self.tr("""cf schematics, single strand width without insulation""")
        self.lf_Wwire.setWhatsThis(txt)
        self.lf_Wwire.setToolTip(txt)

        # Setup of in_Wins_wire
        txt = self.tr(
            """(advanced) cf schematics, winding strand insulation thickness"""
        )
        self.in_Wins_wire.setWhatsThis(txt)
        self.in_Wins_wire.setToolTip(txt)

        # Setup of lf_Wins_wire
        self.lf_Wins_wire.validator().setBottom(0)
        txt = self.tr(
            """(advanced) cf schematics, winding strand insulation thickness"""
        )
        self.lf_Wins_wire.setWhatsThis(txt)
        self.lf_Wins_wire.setToolTip(txt)

# -*- coding: utf-8 -*-
"""File generated according to PCondType12/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWindCond.PCondType12.Ui_PCondType12 import (
    Ui_PCondType12,
)


class Gen_PCondType12(Ui_PCondType12):
    def setupUi(self, PCondType12):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PCondType12.setupUi(self, PCondType12)
        # Setup of in_Nwpc1
        txt = self.tr("""number of strands in parallel per conductor""")
        self.in_Nwpc1.setWhatsThis(txt)
        self.in_Nwpc1.setToolTip(txt)

        # Setup of si_Nwpc1
        self.si_Nwpc1.setMinimum(1)
        self.si_Nwpc1.setMaximum(999999)
        txt = self.tr("""number of strands in parallel per conductor""")
        self.si_Nwpc1.setWhatsThis(txt)
        self.si_Nwpc1.setToolTip(txt)

        # Setup of in_Wwire
        txt = self.tr("""cf schematics, single strand diameter without insulation""")
        self.in_Wwire.setWhatsThis(txt)
        self.in_Wwire.setToolTip(txt)

        # Setup of lf_Wwire
        self.lf_Wwire.validator().setBottom(0)
        txt = self.tr("""cf schematics, single strand diameter without insulation""")
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

        # Setup of in_Wins_cond
        txt = self.tr("""(advanced) cf schematics, conductor diameter""")
        self.in_Wins_cond.setWhatsThis(txt)
        self.in_Wins_cond.setToolTip(txt)

        # Setup of lf_Wins_cond
        self.lf_Wins_cond.validator().setBottom(0)
        txt = self.tr("""(advanced) cf schematics, conductor diameter""")
        self.lf_Wins_cond.setWhatsThis(txt)
        self.lf_Wins_cond.setToolTip(txt)

# -*- coding: utf-8 -*-
"""File generated according to BoreSinePole/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.DBore.PBoreSinePole.Ui_BoreSinePole import (
    Ui_BoreSinePole,
)


class Gen_BoreSinePole(Ui_BoreSinePole):
    def setupUi(self, BoreSinePole):
        """Abstract class to update the widget according to the csv doc"""
        Ui_BoreSinePole.setupUi(self, BoreSinePole)
        # Setup of in_W0
        txt = self.tr(u"""Width of the pole""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr(u"""Width of the pole""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_delta_d
        txt = self.tr(u"""d-axis air gap width""")
        self.in_delta_d.setWhatsThis(txt)
        self.in_delta_d.setToolTip(txt)

        # Setup of lf_delta_d
        self.lf_delta_d.validator().setBottom(0)
        txt = self.tr(u"""d-axis air gap width""")
        self.lf_delta_d.setWhatsThis(txt)
        self.lf_delta_d.setToolTip(txt)

        # Setup of in_delta_q
        txt = self.tr(u"""q-axis air gap width""")
        self.in_delta_q.setWhatsThis(txt)
        self.in_delta_q.setToolTip(txt)

        # Setup of lf_delta_q
        self.lf_delta_q.validator().setBottom(0)
        txt = self.tr(u"""q-axis air gap width""")
        self.lf_delta_q.setWhatsThis(txt)
        self.lf_delta_q.setToolTip(txt)

# -*- coding: utf-8 -*-
"""File generated according to PBoreSinePole/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.DBore.PBoreSinePole.Ui_PBoreSinePole import (
    Ui_PBoreSinePole,
)


class Gen_PBoreSinePole(Ui_PBoreSinePole):
    def setupUi(self, PBoreSinePole):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PBoreSinePole.setupUi(self, PBoreSinePole)
        # Setup of in_N
        txt = self.tr(u"""Number of Poles""")
        self.in_N.setWhatsThis(txt)
        self.in_N.setToolTip(txt)

        # Setup of si_N
        self.si_N.setMinimum(0)
        self.si_N.setMaximum(999999)
        txt = self.tr(u"""Number of Poles""")
        self.si_N.setWhatsThis(txt)
        self.si_N.setToolTip(txt)

        # Setup of in_W0
        txt = self.tr(u"""Width of the pole""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr(u"""Width of the pole""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

        # Setup of in_k
        txt = self.tr(u"""pole width modifier""")
        self.in_k.setWhatsThis(txt)
        self.in_k.setToolTip(txt)

        # Setup of lf_k
        self.lf_k.validator().setBottom(0)
        txt = self.tr(u"""pole width modifier""")
        self.lf_k.setWhatsThis(txt)
        self.lf_k.setToolTip(txt)

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

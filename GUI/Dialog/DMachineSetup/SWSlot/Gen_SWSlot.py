# -*- coding: utf-8 -*-
"""Warning : this file has been generated, you shouldn't edit it"""

from pyleecan.GUI.Dialog.DMachineSetup.SWSlot.Ui_SWSlot import Ui_SWSlot


class Gen_SWSlot(Ui_SWSlot):
    def setupUi(self, SWSlot):
        Ui_SWSlot.setupUi(self, SWSlot)
        # Setup of in_Zs
        txt = self.tr(u"""slot number""")
        self.in_Zs.setWhatsThis(txt)
        self.in_Zs.setToolTip(txt)

        # Setup of si_Zs
        self.si_Zs.setMinimum(0)
        self.si_Zs.setMaximum(1000)
        txt = self.tr(u"""slot number""")
        self.si_Zs.setWhatsThis(txt)
        self.si_Zs.setToolTip(txt)

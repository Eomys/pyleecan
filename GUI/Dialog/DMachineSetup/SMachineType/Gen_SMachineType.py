# -*- coding: utf-8 -*-
"""File generated according to SMachineType/gen_list.json
WARNING! All changes made in this file will be lost!
"""

from .....GUI.Dialog.DMachineSetup.SMachineType.Ui_SMachineType import (
    Ui_SMachineType,
)


class Gen_SMachineType(Ui_SMachineType):
    def setupUi(self, SMachineType):
        """Abstract class to update the widget according to the csv doc
        """
        Ui_SMachineType.setupUi(self, SMachineType)
        # Setup of si_p
        self.si_p.setMinimum(1)
        self.si_p.setMaximum(100)
        txt = self.tr(u"""pole pairs number""")
        self.si_p.setWhatsThis(txt)
        self.si_p.setToolTip(txt)

        # Setup of in_p
        txt = self.tr(u"""pole pairs number""")
        self.in_p.setWhatsThis(txt)
        self.in_p.setToolTip(txt)

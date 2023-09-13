# -*- coding: utf-8 -*-
"""File generated according to DBore/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.DBore.Ui_DBore import Ui_DBore


class Gen_DBore(Ui_DBore):
    def setupUi(self, DBore):
        """Abstract class to update the widget according to the csv doc"""
        Ui_DBore.setupUi(self, DBore)
        # Setup of in_alpha
        txt = self.tr("""Angular offset for the bore shape""")
        self.in_alpha.setWhatsThis(txt)
        self.in_alpha.setToolTip(txt)

        # Setup of lf_alpha
        txt = self.tr("""Angular offset for the bore shape""")
        self.lf_alpha.setWhatsThis(txt)
        self.lf_alpha.setToolTip(txt)

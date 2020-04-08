# -*- coding: utf-8 -*-
"""File generated according to PMagnet10/gen_list.json
WARNING! All changes made in this file will be lost!
"""

from ......GUI.Dialog.DMachineSetup.SMagnet.PMagnet10.Ui_PMagnet10 import (
    Ui_PMagnet10,
)


class Gen_PMagnet10(Ui_PMagnet10):
    def setupUi(self, PMagnet10):
        """Abstract class to update the widget according to the csv doc
        """
        Ui_PMagnet10.setupUi(self, PMagnet10)
        # Setup of in_Hmag
        txt = self.tr(u"""magnet radial height [m]""")
        self.in_Hmag.setWhatsThis(txt)
        self.in_Hmag.setToolTip(txt)

        # Setup of lf_Hmag
        self.lf_Hmag.validator().setBottom(0)
        txt = self.tr(u"""magnet radial height [m]""")
        self.lf_Hmag.setWhatsThis(txt)
        self.lf_Hmag.setToolTip(txt)

        # Setup of in_Wmag
        txt = self.tr(u"""magnet bottom width [m]""")
        self.in_Wmag.setWhatsThis(txt)
        self.in_Wmag.setToolTip(txt)

        # Setup of lf_Wmag
        self.lf_Wmag.validator().setBottom(0)
        txt = self.tr(u"""magnet bottom width [m]""")
        self.lf_Wmag.setWhatsThis(txt)
        self.lf_Wmag.setToolTip(txt)

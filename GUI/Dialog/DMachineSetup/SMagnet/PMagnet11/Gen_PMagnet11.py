# -*- coding: utf-8 -*-
"""File generated according to PMagnet11/gen_list.json
WARNING! All changes made in this file will be lost!
"""

from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet11.Ui_PMagnet11 import (
    Ui_PMagnet11,
)


class Gen_PMagnet11(Ui_PMagnet11):
    def setupUi(self, PMagnet11):
        """Abstract class to update the widget according to the csv doc
        """
        Ui_PMagnet11.setupUi(self, PMagnet11)
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
        txt = self.tr(u"""magnet bottom width [rad]""")
        self.in_Wmag.setWhatsThis(txt)
        self.in_Wmag.setToolTip(txt)

        # Setup of lf_Wmag
        self.lf_Wmag.validator().setBottom(0)
        txt = self.tr(u"""magnet bottom width [rad]""")
        self.lf_Wmag.setWhatsThis(txt)
        self.lf_Wmag.setToolTip(txt)

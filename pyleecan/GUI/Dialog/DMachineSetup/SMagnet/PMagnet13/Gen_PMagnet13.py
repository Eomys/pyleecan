# -*- coding: utf-8 -*-
"""File generated according to PMagnet13/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SMagnet.PMagnet13.Ui_PMagnet13 import (
    Ui_PMagnet13,
)


class Gen_PMagnet13(Ui_PMagnet13):
    def setupUi(self, PMagnet13):
        """Abstract class to update the widget according to the csv doc
        """
        Ui_PMagnet13.setupUi(self, PMagnet13)
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

        # Setup of in_Rtopm
        txt = self.tr(u"""radius of the circular top shape [m]""")
        self.in_Rtopm.setWhatsThis(txt)
        self.in_Rtopm.setToolTip(txt)

        # Setup of lf_Rtopm
        self.lf_Rtopm.validator().setBottom(0)
        txt = self.tr(u"""radius of the circular top shape [m]""")
        self.lf_Rtopm.setWhatsThis(txt)
        self.lf_Rtopm.setToolTip(txt)

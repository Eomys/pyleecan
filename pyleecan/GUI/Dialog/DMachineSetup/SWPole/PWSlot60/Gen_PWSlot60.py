# -*- coding: utf-8 -*-
"""File generated according to PWSlot60/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWPole.PWSlot60.Ui_PWSlot60 import Ui_PWSlot60


class Gen_PWSlot60(Ui_PWSlot60):
    def setupUi(self, PWSlot60):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PWSlot60.setupUi(self, PWSlot60)
        # Setup of in_R1
        txt = self.tr("""Pole top radius""")
        self.in_R1.setWhatsThis(txt)
        self.in_R1.setToolTip(txt)

        # Setup of lf_R1
        self.lf_R1.validator().setBottom(0)
        txt = self.tr("""Pole top radius""")
        self.lf_R1.setWhatsThis(txt)
        self.lf_R1.setToolTip(txt)

        # Setup of in_W1
        txt = self.tr("""Pole top width""")
        self.in_W1.setWhatsThis(txt)
        self.in_W1.setToolTip(txt)

        # Setup of lf_W1
        self.lf_W1.validator().setBottom(0)
        txt = self.tr("""Pole top width""")
        self.lf_W1.setWhatsThis(txt)
        self.lf_W1.setToolTip(txt)

        # Setup of in_W2
        txt = self.tr("""Pole bottom width""")
        self.in_W2.setWhatsThis(txt)
        self.in_W2.setToolTip(txt)

        # Setup of lf_W2
        self.lf_W2.validator().setBottom(0)
        txt = self.tr("""Pole bottom width""")
        self.lf_W2.setWhatsThis(txt)
        self.lf_W2.setToolTip(txt)

        # Setup of in_H1
        txt = self.tr("""Pole top height""")
        self.in_H1.setWhatsThis(txt)
        self.in_H1.setToolTip(txt)

        # Setup of lf_H1
        self.lf_H1.validator().setBottom(0)
        txt = self.tr("""Pole top height""")
        self.lf_H1.setWhatsThis(txt)
        self.lf_H1.setToolTip(txt)

        # Setup of in_H2
        txt = self.tr("""Pole bottom height""")
        self.in_H2.setWhatsThis(txt)
        self.in_H2.setToolTip(txt)

        # Setup of lf_H2
        self.lf_H2.validator().setBottom(0)
        txt = self.tr("""Pole bottom height""")
        self.lf_H2.setWhatsThis(txt)
        self.lf_H2.setToolTip(txt)

        # Setup of in_W3
        txt = self.tr("""Edge Distance Ploe-coil """)
        self.in_W3.setWhatsThis(txt)
        self.in_W3.setToolTip(txt)

        # Setup of lf_W3
        self.lf_W3.validator().setBottom(0)
        txt = self.tr("""Edge Distance Ploe-coil """)
        self.lf_W3.setWhatsThis(txt)
        self.lf_W3.setToolTip(txt)

        # Setup of in_H3
        txt = self.tr("""Top Distance Ploe-coil """)
        self.in_H3.setWhatsThis(txt)
        self.in_H3.setToolTip(txt)

        # Setup of lf_H3
        self.lf_H3.validator().setBottom(0)
        txt = self.tr("""Top Distance Ploe-coil """)
        self.lf_H3.setWhatsThis(txt)
        self.lf_H3.setToolTip(txt)

        # Setup of in_H4
        txt = self.tr("""Bottom Distance Ploe-coil """)
        self.in_H4.setWhatsThis(txt)
        self.in_H4.setToolTip(txt)

        # Setup of lf_H4
        self.lf_H4.validator().setBottom(0)
        txt = self.tr("""Bottom Distance Ploe-coil """)
        self.lf_H4.setWhatsThis(txt)
        self.lf_H4.setToolTip(txt)

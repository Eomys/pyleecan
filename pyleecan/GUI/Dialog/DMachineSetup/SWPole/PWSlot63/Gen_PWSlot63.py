# -*- coding: utf-8 -*-
"""File generated according to PWSlot63/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SWPole.PWSlot63.Ui_PWSlot63 import Ui_PWSlot63


class Gen_PWSlot63(Ui_PWSlot63):
    def setupUi(self, PWSlot63):
        """Abstract class to update the widget according to the csv doc"""
        Ui_PWSlot63.setupUi(self, PWSlot63)
        # Setup of in_W0
        txt = self.tr("""Pole bottom width""")
        self.in_W0.setWhatsThis(txt)
        self.in_W0.setToolTip(txt)

        # Setup of lf_W0
        self.lf_W0.validator().setBottom(0)
        txt = self.tr("""Pole bottom width""")
        self.lf_W0.setWhatsThis(txt)
        self.lf_W0.setToolTip(txt)

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
        txt = self.tr("""Width Ploe""")
        self.in_W2.setWhatsThis(txt)
        self.in_W2.setToolTip(txt)

        # Setup of lf_W2
        self.lf_W2.validator().setBottom(0)
        txt = self.tr("""Width Ploe""")
        self.lf_W2.setWhatsThis(txt)
        self.lf_W2.setToolTip(txt)

        # Setup of in_H0
        txt = self.tr("""Pole bottom height""")
        self.in_H0.setWhatsThis(txt)
        self.in_H0.setToolTip(txt)

        # Setup of lf_H0
        self.lf_H0.validator().setBottom(0)
        txt = self.tr("""Pole bottom height""")
        self.lf_H0.setWhatsThis(txt)
        self.lf_H0.setToolTip(txt)

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
        txt = self.tr("""Heigh Ploe""")
        self.in_H2.setWhatsThis(txt)
        self.in_H2.setToolTip(txt)

        # Setup of lf_H2
        self.lf_H2.validator().setBottom(0)
        txt = self.tr("""Heigh Ploe""")
        self.lf_H2.setWhatsThis(txt)
        self.lf_H2.setToolTip(txt)

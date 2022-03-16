# -*- coding: utf-8 -*-
"""File generated according to SLamShape/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMachineSetup.SLamShape.Ui_SLamShape import Ui_SLamShape


class Gen_SLamShape(Ui_SLamShape):
    def setupUi(self, SLamShape):
        """Abstract class to update the widget according to the csv doc"""
        Ui_SLamShape.setupUi(self, SLamShape)
        # Setup of in_L1
        txt = self.tr(
            """Lamination stack active length without radial ventilation airducts but including insulation layers between lamination sheets"""
        )
        self.in_L1.setWhatsThis(txt)
        self.in_L1.setToolTip(txt)

        # Setup of lf_L1
        self.lf_L1.validator().setBottom(0)
        txt = self.tr(
            """Lamination stack active length without radial ventilation airducts but including insulation layers between lamination sheets"""
        )
        self.lf_L1.setWhatsThis(txt)
        self.lf_L1.setToolTip(txt)

        # Setup of in_Kf1
        txt = self.tr("""lamination stacking / packing factor""")
        self.in_Kf1.setWhatsThis(txt)
        self.in_Kf1.setToolTip(txt)

        # Setup of lf_Kf1
        self.lf_Kf1.validator().setBottom(0)
        self.lf_Kf1.validator().setTop(1)
        txt = self.tr("""lamination stacking / packing factor""")
        self.lf_Kf1.setWhatsThis(txt)
        self.lf_Kf1.setToolTip(txt)

        # Setup of w_mat
        txt = self.tr("""Lamination's material""")
        self.w_mat.setWhatsThis(txt)
        self.w_mat.setToolTip(txt)

        # Setup of in_Wrvd
        txt = self.tr("""axial width of ventilation ducts in lamination""")
        self.in_Wrvd.setWhatsThis(txt)
        self.in_Wrvd.setToolTip(txt)

        # Setup of lf_Wrvd
        self.lf_Wrvd.validator().setBottom(0)
        txt = self.tr("""axial width of ventilation ducts in lamination""")
        self.lf_Wrvd.setWhatsThis(txt)
        self.lf_Wrvd.setToolTip(txt)

        # Setup of in_Nrvd
        txt = self.tr("""number of radial air ventilation ducts in lamination""")
        self.in_Nrvd.setWhatsThis(txt)
        self.in_Nrvd.setToolTip(txt)

        # Setup of si_Nrvd
        self.si_Nrvd.setMinimum(0)
        self.si_Nrvd.setMaximum(999999)
        txt = self.tr("""number of radial air ventilation ducts in lamination""")
        self.si_Nrvd.setWhatsThis(txt)
        self.si_Nrvd.setToolTip(txt)

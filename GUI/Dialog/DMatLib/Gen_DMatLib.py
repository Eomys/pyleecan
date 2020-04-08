# -*- coding: utf-8 -*-
"""File generated according to DMatLib/gen_list.json
WARNING! All changes made in this file will be lost!
"""

from ....GUI.Dialog.DMatLib.Ui_DMatLib import Ui_DMatLib


class Gen_DMatLib(Ui_DMatLib):
    def setupUi(self, DMatLib):
        """Abstract class to update the widget according to the csv doc
        """
        Ui_DMatLib.setupUi(self, DMatLib)
        # Setup of out_name
        txt = self.tr(u"""name of the material""")
        self.out_name.setWhatsThis(txt)
        self.out_name.setToolTip(txt)

        # Setup of out_iso
        txt = self.tr(u"""If True, uniformity in all orientations""")
        self.out_iso.setWhatsThis(txt)
        self.out_iso.setToolTip(txt)

        # Setup of out_rho_elec
        txt = self.tr(u"""Resistivity at 20 deg C""")
        self.out_rho_elec.setWhatsThis(txt)
        self.out_rho_elec.setToolTip(txt)

        # Setup of out_epsr
        txt = self.tr(u"""Relative dielectric constant""")
        self.out_epsr.setWhatsThis(txt)
        self.out_epsr.setToolTip(txt)

        # Setup of out_cost_unit
        txt = self.tr(u"""Cost of one kilo of material""")
        self.out_cost_unit.setWhatsThis(txt)
        self.out_cost_unit.setToolTip(txt)

        # Setup of out_Cp
        txt = self.tr(u"""specific heat capacity""")
        self.out_Cp.setWhatsThis(txt)
        self.out_Cp.setToolTip(txt)

        # Setup of out_alpha
        txt = self.tr(u"""thermal expansion coefficient""")
        self.out_alpha.setWhatsThis(txt)
        self.out_alpha.setToolTip(txt)

        # Setup of out_L
        txt = self.tr(
            u"""thermal conductivity (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_L.setWhatsThis(txt)
        self.out_L.setToolTip(txt)

        # Setup of out_LX
        txt = self.tr(
            u"""thermal conductivity (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_LX.setWhatsThis(txt)
        self.out_LX.setToolTip(txt)

        # Setup of out_LY
        txt = self.tr(
            u"""thermal conductivity (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_LY.setWhatsThis(txt)
        self.out_LY.setToolTip(txt)

        # Setup of out_LZ
        txt = self.tr(
            u"""thermal conductivity (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_LZ.setWhatsThis(txt)
        self.out_LZ.setToolTip(txt)

        # Setup of out_rho_meca
        txt = self.tr(u"""mass per unit volume [kg/m3]""")
        self.out_rho_meca.setWhatsThis(txt)
        self.out_rho_meca.setToolTip(txt)

        # Setup of out_E
        txt = self.tr(
            u"""equivalent Young modulus (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_E.setWhatsThis(txt)
        self.out_E.setToolTip(txt)

        # Setup of out_EX
        txt = self.tr(
            u"""equivalent Young modulus (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_EX.setWhatsThis(txt)
        self.out_EX.setToolTip(txt)

        # Setup of out_EY
        txt = self.tr(
            u"""equivalent Young modulus (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_EY.setWhatsThis(txt)
        self.out_EY.setToolTip(txt)

        # Setup of out_EZ
        txt = self.tr(
            u"""equivalent Young modulus (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_EZ.setWhatsThis(txt)
        self.out_EZ.setToolTip(txt)

        # Setup of out_G
        txt = self.tr(
            u"""shear modulus in XZ plane (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_G.setWhatsThis(txt)
        self.out_G.setToolTip(txt)

        # Setup of out_GXY
        txt = self.tr(
            u"""shear modulus in XZ plane (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_GXY.setWhatsThis(txt)
        self.out_GXY.setToolTip(txt)

        # Setup of out_GXZ
        txt = self.tr(
            u"""shear modulus in XY plane (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_GXZ.setWhatsThis(txt)
        self.out_GXZ.setToolTip(txt)

        # Setup of out_GYZ
        txt = self.tr(
            u"""shear modulus in YZ plane (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_GYZ.setWhatsThis(txt)
        self.out_GYZ.setToolTip(txt)

        # Setup of out_nu
        txt = self.tr(
            u"""equivalent Poisson ratio in the XY plane (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_nu.setWhatsThis(txt)
        self.out_nu.setToolTip(txt)

        # Setup of out_nu_XY
        txt = self.tr(
            u"""equivalent Poisson ratio in the XY plane (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_nu_XY.setWhatsThis(txt)
        self.out_nu_XY.setToolTip(txt)

        # Setup of out_nu_XZ
        txt = self.tr(
            u"""equivalent Poisson ratio in the XZ plane (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_nu_XZ.setWhatsThis(txt)
        self.out_nu_XZ.setToolTip(txt)

        # Setup of out_nu_YZ
        txt = self.tr(
            u"""equivalent Poisson ratio in the YZ plane (XY is lamination plane, Z is rotation axis)"""
        )
        self.out_nu_YZ.setWhatsThis(txt)
        self.out_nu_YZ.setToolTip(txt)

        # Setup of out_mur_lin
        txt = self.tr(u"""Relative magnetic permeability""")
        self.out_mur_lin.setWhatsThis(txt)
        self.out_mur_lin.setToolTip(txt)

        # Setup of out_Brm20
        txt = self.tr(u"""magnet remanence induction at 20degC""")
        self.out_Brm20.setWhatsThis(txt)
        self.out_Brm20.setToolTip(txt)

        # Setup of out_alpha_Br
        txt = self.tr(
            u"""temperature coefficient for remanent flux density /degC compared to 20degC"""
        )
        self.out_alpha_Br.setWhatsThis(txt)
        self.out_alpha_Br.setToolTip(txt)

        # Setup of out_wlam
        txt = self.tr(
            u"""lamination sheet width without insulation [m] (0 == not laminated)"""
        )
        self.out_wlam.setWhatsThis(txt)
        self.out_wlam.setToolTip(txt)

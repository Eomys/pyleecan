# -*- coding: utf-8 -*-
"""File generated according to DMatSetup/gen_list.json
WARNING! All changes made in this file will be lost!
"""
from pyleecan.GUI.Dialog.DMatLib.DMatSetup.Ui_DMatSetup import Ui_DMatSetup


class Gen_DMatSetup(Ui_DMatSetup):
    def setupUi(self, DMatSetup):
        """Abstract class to update the widget according to the csv doc"""
        Ui_DMatSetup.setupUi(self, DMatSetup)
        # Setup of in_name
        txt = self.tr("""<qt><nobr>name of the material</nobr></qt>""")
        self.in_name.setWhatsThis(txt)
        self.in_name.setToolTip(txt)

        # Setup of le_name
        txt = self.tr("""<qt><nobr>name of the material</nobr></qt>""")
        self.le_name.setWhatsThis(txt)
        self.le_name.setToolTip(txt)

        # Setup of cb_material_type
        txt = self.tr(
            """<qt><nobr>If Isotropic, uniformity in all orientations</nobr></qt>"""
        )
        self.cb_material_type.setWhatsThis(txt)
        self.cb_material_type.setToolTip(txt)

        # Setup of in_material_type
        txt = self.tr(
            """<qt><nobr>If Isotropic, uniformity in all orientations</nobr></qt>"""
        )
        self.in_material_type.setWhatsThis(txt)
        self.in_material_type.setToolTip(txt)

        # Setup of in_rho_elec
        txt = self.tr("""<qt><nobr>Resistivity at 20 ° C</nobr></qt>""")
        self.in_rho_elec.setWhatsThis(txt)
        self.in_rho_elec.setToolTip(txt)

        # Setup of lf_rho_elec
        self.lf_rho_elec.validator().setBottom(0)
        txt = self.tr("""<qt><nobr>Resistivity at 20 ° C</nobr></qt>""")
        self.lf_rho_elec.setWhatsThis(txt)
        self.lf_rho_elec.setToolTip(txt)

        # Setup of unit_rho_elec
        txt = self.tr("""<qt><nobr>Resistivity at 20 ° C</nobr></qt>""")
        self.unit_rho_elec.setWhatsThis(txt)
        self.unit_rho_elec.setToolTip(txt)

        # Setup of in_alpha_elec
        txt = self.tr("""<qt><nobr>Thermal resistivity coefficient</nobr></qt>""")
        self.in_alpha_elec.setWhatsThis(txt)
        self.in_alpha_elec.setToolTip(txt)

        # Setup of lf_alpha_elec
        self.lf_alpha_elec.validator().setBottom(0)
        txt = self.tr("""<qt><nobr>Thermal resistivity coefficient</nobr></qt>""")
        self.lf_alpha_elec.setWhatsThis(txt)
        self.lf_alpha_elec.setToolTip(txt)

        # Setup of unit_alpha_elec
        txt = self.tr("""<qt><nobr>Thermal resistivity coefficient</nobr></qt>""")
        self.unit_alpha_elec.setWhatsThis(txt)
        self.unit_alpha_elec.setToolTip(txt)

        # Setup of in_cost_unit
        txt = self.tr("""<qt><nobr>Cost of one kilo of material</nobr></qt>""")
        self.in_cost_unit.setWhatsThis(txt)
        self.in_cost_unit.setToolTip(txt)

        # Setup of lf_cost_unit
        self.lf_cost_unit.validator().setBottom(0)
        txt = self.tr("""<qt><nobr>Cost of one kilo of material</nobr></qt>""")
        self.lf_cost_unit.setWhatsThis(txt)
        self.lf_cost_unit.setToolTip(txt)

        # Setup of unit_cost_unit
        txt = self.tr("""<qt><nobr>Cost of one kilo of material</nobr></qt>""")
        self.unit_cost_unit.setWhatsThis(txt)
        self.unit_cost_unit.setToolTip(txt)

        # Setup of in_Cp
        txt = self.tr("""<qt><nobr>specific heat capacity</nobr></qt>""")
        self.in_Cp.setWhatsThis(txt)
        self.in_Cp.setToolTip(txt)

        # Setup of lf_Cp
        self.lf_Cp.validator().setBottom(0)
        txt = self.tr("""<qt><nobr>specific heat capacity</nobr></qt>""")
        self.lf_Cp.setWhatsThis(txt)
        self.lf_Cp.setToolTip(txt)

        # Setup of unit_Cp
        txt = self.tr("""<qt><nobr>specific heat capacity</nobr></qt>""")
        self.unit_Cp.setWhatsThis(txt)
        self.unit_Cp.setToolTip(txt)

        # Setup of in_alpha
        txt = self.tr("""<qt><nobr>thermal expansion coefficient</nobr></qt>""")
        self.in_alpha.setWhatsThis(txt)
        self.in_alpha.setToolTip(txt)

        # Setup of lf_alpha
        self.lf_alpha.validator().setBottom(0)
        txt = self.tr("""<qt><nobr>thermal expansion coefficient</nobr></qt>""")
        self.lf_alpha.setWhatsThis(txt)
        self.lf_alpha.setToolTip(txt)

        # Setup of in_L
        txt = self.tr(
            """<qt><nobr>thermal conductivity (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.in_L.setWhatsThis(txt)
        self.in_L.setToolTip(txt)

        # Setup of unit_L
        txt = self.tr(
            """<qt><nobr>thermal conductivity (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.unit_L.setWhatsThis(txt)
        self.unit_L.setToolTip(txt)

        # Setup of lf_L
        self.lf_L.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>thermal conductivity (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.lf_L.setWhatsThis(txt)
        self.lf_L.setToolTip(txt)

        # Setup of in_Lx
        txt = self.tr(
            """<qt><nobr>thermal conductivity (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.in_Lx.setWhatsThis(txt)
        self.in_Lx.setToolTip(txt)

        # Setup of lf_Lx
        self.lf_Lx.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>thermal conductivity (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.lf_Lx.setWhatsThis(txt)
        self.lf_Lx.setToolTip(txt)

        # Setup of in_Ly
        txt = self.tr(
            """<qt><nobr>thermal conductivity (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.in_Ly.setWhatsThis(txt)
        self.in_Ly.setToolTip(txt)

        # Setup of lf_Ly
        self.lf_Ly.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>thermal conductivity (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.lf_Ly.setWhatsThis(txt)
        self.lf_Ly.setToolTip(txt)

        # Setup of in_Lz
        txt = self.tr(
            """<qt><nobr>thermal conductivity (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.in_Lz.setWhatsThis(txt)
        self.in_Lz.setToolTip(txt)

        # Setup of lf_Lz
        self.lf_Lz.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>thermal conductivity (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.lf_Lz.setWhatsThis(txt)
        self.lf_Lz.setToolTip(txt)

        # Setup of in_rho_meca
        txt = self.tr("""<qt><nobr>mass per unit volume [kg/m3]</nobr></qt>""")
        self.in_rho_meca.setWhatsThis(txt)
        self.in_rho_meca.setToolTip(txt)

        # Setup of lf_rho_meca
        self.lf_rho_meca.validator().setBottom(0)
        txt = self.tr("""<qt><nobr>mass per unit volume [kg/m3]</nobr></qt>""")
        self.lf_rho_meca.setWhatsThis(txt)
        self.lf_rho_meca.setToolTip(txt)

        # Setup of unit_rho_meca
        txt = self.tr("""<qt><nobr>mass per unit volume [kg/m3]</nobr></qt>""")
        self.unit_rho_meca.setWhatsThis(txt)
        self.unit_rho_meca.setToolTip(txt)

        # Setup of in_E
        txt = self.tr(
            """<qt><nobr>equivalent Young modulus (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.in_E.setWhatsThis(txt)
        self.in_E.setToolTip(txt)

        # Setup of lf_E
        self.lf_E.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>equivalent Young modulus (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.lf_E.setWhatsThis(txt)
        self.lf_E.setToolTip(txt)

        # Setup of unit_E
        txt = self.tr(
            """<qt><nobr>equivalent Young modulus (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.unit_E.setWhatsThis(txt)
        self.unit_E.setToolTip(txt)

        # Setup of in_Ex
        txt = self.tr(
            """<qt><nobr>equivalent Young modulus (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.in_Ex.setWhatsThis(txt)
        self.in_Ex.setToolTip(txt)

        # Setup of lf_Ex
        self.lf_Ex.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>equivalent Young modulus (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.lf_Ex.setWhatsThis(txt)
        self.lf_Ex.setToolTip(txt)

        # Setup of in_Ey
        txt = self.tr(
            """<qt><nobr>equivalent Young modulus (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.in_Ey.setWhatsThis(txt)
        self.in_Ey.setToolTip(txt)

        # Setup of lf_Ey
        self.lf_Ey.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>equivalent Young modulus (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.lf_Ey.setWhatsThis(txt)
        self.lf_Ey.setToolTip(txt)

        # Setup of in_Ez
        txt = self.tr(
            """<qt><nobr>equivalent Young modulus (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.in_Ez.setWhatsThis(txt)
        self.in_Ez.setToolTip(txt)

        # Setup of lf_Ez
        self.lf_Ez.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>equivalent Young modulus (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.lf_Ez.setWhatsThis(txt)
        self.lf_Ez.setToolTip(txt)

        # Setup of in_G
        txt = self.tr(
            """<qt><nobr>shear modulus in XZ plane (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.in_G.setWhatsThis(txt)
        self.in_G.setToolTip(txt)

        # Setup of lf_G
        self.lf_G.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>shear modulus in XZ plane (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.lf_G.setWhatsThis(txt)
        self.lf_G.setToolTip(txt)

        # Setup of unit_G
        txt = self.tr(
            """<qt><nobr>shear modulus in XZ plane (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.unit_G.setWhatsThis(txt)
        self.unit_G.setToolTip(txt)

        # Setup of in_Gxy
        txt = self.tr(
            """<qt><nobr>shear modulus in XZ plane (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.in_Gxy.setWhatsThis(txt)
        self.in_Gxy.setToolTip(txt)

        # Setup of lf_Gxy
        self.lf_Gxy.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>shear modulus in XZ plane (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.lf_Gxy.setWhatsThis(txt)
        self.lf_Gxy.setToolTip(txt)

        # Setup of in_Gxz
        txt = self.tr(
            """<qt><nobr>shear modulus in XY plane (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.in_Gxz.setWhatsThis(txt)
        self.in_Gxz.setToolTip(txt)

        # Setup of lf_Gxz
        self.lf_Gxz.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>shear modulus in XY plane (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.lf_Gxz.setWhatsThis(txt)
        self.lf_Gxz.setToolTip(txt)

        # Setup of in_Gyz
        txt = self.tr(
            """<qt><nobr>shear modulus in YZ plane (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.in_Gyz.setWhatsThis(txt)
        self.in_Gyz.setToolTip(txt)

        # Setup of lf_Gyz
        self.lf_Gyz.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>shear modulus in YZ plane (XY is lamination plane, Z is</nobr> rotation axis)</qt>"""
        )
        self.lf_Gyz.setWhatsThis(txt)
        self.lf_Gyz.setToolTip(txt)

        # Setup of in_nu
        txt = self.tr(
            """<qt><nobr>equivalent Poisson ratio in the XY plane (XY is lamination</nobr> plane, Z is rotation axis)</qt>"""
        )
        self.in_nu.setWhatsThis(txt)
        self.in_nu.setToolTip(txt)

        # Setup of lf_nu
        self.lf_nu.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>equivalent Poisson ratio in the XY plane (XY is lamination</nobr> plane, Z is rotation axis)</qt>"""
        )
        self.lf_nu.setWhatsThis(txt)
        self.lf_nu.setToolTip(txt)

        # Setup of in_nu_xy
        txt = self.tr(
            """<qt><nobr>equivalent Poisson ratio in the XY plane (XY is lamination</nobr> plane, Z is rotation axis)</qt>"""
        )
        self.in_nu_xy.setWhatsThis(txt)
        self.in_nu_xy.setToolTip(txt)

        # Setup of lf_nu_xy
        self.lf_nu_xy.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>equivalent Poisson ratio in the XY plane (XY is lamination</nobr> plane, Z is rotation axis)</qt>"""
        )
        self.lf_nu_xy.setWhatsThis(txt)
        self.lf_nu_xy.setToolTip(txt)

        # Setup of in_nu_xz
        txt = self.tr(
            """<qt><nobr>equivalent Poisson ratio in the XZ plane (XY is lamination</nobr> plane, Z is rotation axis)</qt>"""
        )
        self.in_nu_xz.setWhatsThis(txt)
        self.in_nu_xz.setToolTip(txt)

        # Setup of lf_nu_xz
        self.lf_nu_xz.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>equivalent Poisson ratio in the XZ plane (XY is lamination</nobr> plane, Z is rotation axis)</qt>"""
        )
        self.lf_nu_xz.setWhatsThis(txt)
        self.lf_nu_xz.setToolTip(txt)

        # Setup of in_nu_yz
        txt = self.tr(
            """<qt><nobr>equivalent Poisson ratio in the YZ plane (XY is lamination</nobr> plane, Z is rotation axis)</qt>"""
        )
        self.in_nu_yz.setWhatsThis(txt)
        self.in_nu_yz.setToolTip(txt)

        # Setup of lf_nu_yz
        self.lf_nu_yz.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>equivalent Poisson ratio in the YZ plane (XY is lamination</nobr> plane, Z is rotation axis)</qt>"""
        )
        self.lf_nu_yz.setWhatsThis(txt)
        self.lf_nu_yz.setToolTip(txt)

        # Setup of in_mur_lin
        txt = self.tr("""<qt><nobr>Relative magnetic permeability</nobr></qt>""")
        self.in_mur_lin.setWhatsThis(txt)
        self.in_mur_lin.setToolTip(txt)

        # Setup of lf_mur_lin
        self.lf_mur_lin.validator().setBottom(0)
        txt = self.tr("""<qt><nobr>Relative magnetic permeability</nobr></qt>""")
        self.lf_mur_lin.setWhatsThis(txt)
        self.lf_mur_lin.setToolTip(txt)

        # Setup of in_Brm20
        txt = self.tr("""<qt><nobr>magnet remanence induction at 20degC</nobr></qt>""")
        self.in_Brm20.setWhatsThis(txt)
        self.in_Brm20.setToolTip(txt)

        # Setup of lf_Brm20
        txt = self.tr("""<qt><nobr>magnet remanence induction at 20degC</nobr></qt>""")
        self.lf_Brm20.setWhatsThis(txt)
        self.lf_Brm20.setToolTip(txt)

        # Setup of unit_Brm20
        txt = self.tr("""<qt><nobr>magnet remanence induction at 20degC</nobr></qt>""")
        self.unit_Brm20.setWhatsThis(txt)
        self.unit_Brm20.setToolTip(txt)

        # Setup of in_alpha_Br
        txt = self.tr(
            """<qt><nobr>temperature coefficient for remanent flux density</nobr></qt>"""
        )
        self.in_alpha_Br.setWhatsThis(txt)
        self.in_alpha_Br.setToolTip(txt)

        # Setup of lf_alpha_Br
        self.lf_alpha_Br.validator().setTop(0)
        txt = self.tr(
            """<qt><nobr>temperature coefficient for remanent flux density</nobr></qt>"""
        )
        self.lf_alpha_Br.setWhatsThis(txt)
        self.lf_alpha_Br.setToolTip(txt)

        # Setup of in_Wlam
        txt = self.tr(
            """<qt><nobr>lamination sheet width without insulation [m] (0 == not</nobr> laminated)</qt>"""
        )
        self.in_Wlam.setWhatsThis(txt)
        self.in_Wlam.setToolTip(txt)

        # Setup of lf_Wlam
        self.lf_Wlam.validator().setBottom(0)
        txt = self.tr(
            """<qt><nobr>lamination sheet width without insulation [m] (0 == not</nobr> laminated)</qt>"""
        )
        self.lf_Wlam.setWhatsThis(txt)
        self.lf_Wlam.setToolTip(txt)

        # Setup of unit_Wlam
        txt = self.tr(
            """<qt><nobr>lamination sheet width without insulation [m] (0 == not</nobr> laminated)</qt>"""
        )
        self.unit_Wlam.setWhatsThis(txt)
        self.unit_Wlam.setToolTip(txt)

from os import makedirs
from os.path import join
from unittest import TestCase
from shutil import copyfile

import matplotlib.pyplot as plt
from numpy import array, linspace, ones, pi, zeros

from pyleecan.Classes.import_all import *
from pyleecan.Functions.GMSH.gen_3D_mesh import gen_3D_mesh
from pyleecan.Tests import save_plot_path
from pyleecan.Tests.Plot.LamWind import wind_mat
from pyleecan.Tests.Validation.Machine.SCIM_006 import SCIM_006
from pyleecan.Tests.Validation.Machine.SPMSM_015 import SPMSM_015

# Gather results in the same folder
save_path = join(save_plot_path, "ICEM_2020")
makedirs(save_path)


class test_ICEM_2020(TestCase):
    """This test gather all the images/project for the ICEM 2020 publication:
    "Design optimization of innovative electrical machines topologies based
    on Pyleecan open-source object-oriented software"
    """

    def test_FEMM_sym(self):
        """Figure 8: Check that the FEMM can handle symmetry
        From pyleecan/Tests/Validation/Simulation/test_EM_SCIM_NL_006.py
        """
        simu = Simu1(name="ICEM_2020", machine=SCIM_006)
        simu.machine.name = "fig_08_FEMM_sym"

        # Definition of the enforced output of the electrical module
        Nr = ImportMatrixVal(value=ones(1) * 1500)
        Is = ImportMatrixVal(value=array([[20, -10, -10]]))
        Ir = ImportMatrixVal(value=zeros((1, 28)))
        time = ImportGenVectLin(start=0, stop=0, num=1, endpoint=False)
        angle = ImportGenVectLin(start=0, stop=2 * pi, num=4096, endpoint=False)
        simu.input = InCurrent(
            Is=Is,
            Ir=Ir,  # zero current for the rotor
            Nr=Nr,
            angle_rotor=None,  # Will be computed
            time=time,
            angle=angle,
            angle_rotor_initial=0.2244,
        )

        # Definition of the magnetic simulation
        # 2 sym + antiperiodicity = 1/4 Lamination
        simu.mag = MagFEMM(
            is_stator_linear_BH=2,
            is_rotor_linear_BH=2,
            is_symmetry_a=True,
            sym_a=2,
            is_antiper_a=True,
        )
        # Stop after magnetic computation
        simu.struct = None
        # Run simulation
        out = Output(simu=simu)
        simu.run()

        # FEMM files (mesh and results) are available in Results folder
        copyfile(
            join(out.path_res, "Femm", "fig_08_FEMM_sym_model.ans"),
            join(save_path, "fig_08_FEMM_sym_model.ans"),
        )
        copyfile(
            join(out.path_res, "Femm", "fig_08_FEMM_sym_model.fem"),
            join(save_path, "fig_08_FEMM_sym_model.fem"),
        )

    def test_gmsh_mesh_dict(self):
        """Figure 9: Generate a 3D mesh with Gmsh by setting the
        number of element on each lines
        """
        # Stator definition
        stator = LamSlotWind(
            Rint=0.1325,
            Rext=0.2,
            Nrvd=0,
            L1=0.35,
            Kf1=0.95,
            is_internal=False,
            is_stator=True,
        )
        stator.slot = SlotW10(
            Zs=36, H0=1e-3, H1=1.5e-3, H2=30e-3, W0=12e-3, W1=14e-3, W2=12e-3
        )

        # Plot, check and save
        stator.plot(is_lam_only=True)
        fig = plt.gcf()
        fig.savefig(join(save_path, "fig_09_ref_lamination.png"))
        self.assertEqual(len(fig.axes[0].patches), 2)

        # Definition of the number of each element on each line
        mesh_dict = {
            "Tooth_Yoke_Side": 5,
            "Tooth_Yoke_Arc": 5,
            "Tooth_line_3": 2,
            "Tooth_line_4": 8,
            "Tooth_line_5": 1,
            "Tooth_line_6": 1,
            "Tooth_line_7": 1,
            "Tooth_bore_arc_bot": 2,
            "Tooth_bore_arc_top": 2,
            "Tooth_line_10": 1,
            "Tooth_line_11": 1,
            "Tooth_line_12": 1,
            "Tooth_line_13": 8,
            "Tooth_line_14": 2,
        }
        gen_3D_mesh(
            lamination=stator,
            save_path=join(save_path, "fig_09_gmsh_mesh_dict.msh"),
            mesh_size=7e-3,
            user_mesh_dict=mesh_dict,
            is_rect=True,
            Nlayer=18,
        )
        # To see the resulting mesh, gmsh_mesh_dict.msh need to be
        # opened in Gmsh

    def test_SlotMulti_sym(self):
        """Figure 10: Generate a 3D mesh with GMSH for a lamination
        with several slot types and notches
        """

        plt.close("all")
        # Rotor definition
        rotor = LamSlotMulti(
            Rint=0.2,
            Rext=0.7,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )

        # Reference Slot
        Zs = 8
        Slot1 = SlotW10(
            Zs=Zs, W0=50e-3, H0=30e-3, W1=100e-3, H1=30e-3, H2=100e-3, W2=120e-3
        )
        Slot2 = SlotW22(Zs=Zs, W0=pi / 12, H0=50e-3, W2=pi / 6, H2=125e-3)

        # Reference slot are duplicated to get 4 of each in alternance
        slot_list = list()
        for ii in range(Zs // 2):
            slot_list.append(SlotW10(init_dict=Slot1.as_dict()))
            slot_list.append(SlotW22(init_dict=Slot2.as_dict()))
        rotor.slot_list = slot_list
        # Set slot position as linspace
        rotor.alpha = linspace(0, 2 * pi, 8, endpoint=False) + pi / Zs

        # Set evenly distributed notches
        slot3 = SlotW10(Zs=Zs // 2, W0=40e-3, W1=40e-3, W2=40e-3, H0=0, H1=0, H2=25e-3)
        notch = NotchEvenDist(notch_shape=slot3, alpha=2 * pi / Zs)
        rotor.notch = [notch]

        # Plot, check and save
        rotor.plot(sym=4)
        fig = plt.gcf()
        fig.savefig(join(save_path, "fig_10_SlotMulti_sym.png"))
        self.assertEqual(len(fig.axes[0].patches), 1)

        # Generate the gmsh equivalent
        gen_3D_mesh(
            lamination=rotor,
            save_path=join(save_path, "fig_10_gmsh_SlotMulti.msh"),
            sym=4,
            mesh_size=20e-3,
            Nlayer=20,
        )
        # To see the resulting mesh, gmsh_SlotMulti.msh need to be
        # opened in Gmsh

    def test_MachineUD(self):
        """Figure 11: Check that you can plot a machine with 4 laminations
        """
        machine = MachineUD()

        # Main geometry parameter
        Rext = 170e-3  # Exterior radius of outter lamination
        W1 = 30e-3  # Width of first lamination
        A1 = 2.5e-3  # Width of the first airgap
        W2 = 20e-3
        A2 = 10e-3
        W3 = 20e-3
        A3 = 2.5e-3
        W4 = 60e-3

        # Outer stator
        lam1 = LamSlotWind(Rext=Rext, Rint=Rext - W1, is_internal=False, is_stator=True)
        lam1.slot = SlotW22(
            Zs=12, W0=2 * pi / 12 * 0.75, W2=2 * pi / 12 * 0.75, H0=0, H2=W1 * 0.65
        )
        lam1.winding = WindingCW2LT(qs=3, p=3)
        # Outer rotor
        lam2 = LamSlot(
            Rext=lam1.Rint - A1,
            Rint=lam1.Rint - A1 - W2,
            is_internal=True,
            is_stator=False,
        )
        lam2.slot = SlotW10(
            Zs=22, W0=25e-3, W1=25e-3, W2=15e-3, H0=0, H1=0, H2=W2 * 0.75
        )
        # Inner rotor
        lam3 = LamSlot(
            Rext=lam2.Rint - A2,
            Rint=lam2.Rint - A2 - W3,
            is_internal=False,
            is_stator=False,
        )
        lam3.slot = SlotW10(
            Zs=22, W0=17.5e-3, W1=17.5e-3, W2=12.5e-3, H0=0, H1=0, H2=W3 * 0.75
        )
        # Inner stator
        lam4 = LamSlotWind(
            Rext=lam3.Rint - A3,
            Rint=lam3.Rint - A3 - W4,
            is_internal=True,
            is_stator=True,
        )
        lam4.slot = SlotW10(
            Zs=12, W0=25e-3, W1=25e-3, W2=1e-3, H0=0, H1=0, H2=W4 * 0.75
        )
        lam4.winding = WindingCW2LT(qs=3, p=3)
        # Machine definition
        machine.lam_list = [lam1, lam2, lam3, lam4]

        # Plot, check and save
        machine.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "fig_11_MachineUD.png"))
        self.assertEqual(len(fig.axes[0].patches), 56)

    def test_SlotMulti(self):
        """Figure 12: Check that you can plot a LamSlotMulti (two slots kind + notches)
        """
        plt.close("all")
        # Lamination main dimensions definition
        rotor = LamSlotMulti(Rint=0.2, Rext=0.7, is_internal=True, is_stator=False)

        # Reference slot definition
        Slot1 = SlotW10(
            Zs=10, W0=50e-3, H0=30e-3, W1=100e-3, H1=30e-3, H2=100e-3, W2=120e-3
        )
        Slot2 = SlotW22(Zs=12, W0=pi / 12, H0=50e-3, W2=pi / 6, H2=125e-3)

        # Reference slot are duplicated to get 5 of each in alternance
        slot_list = list()
        for ii in range(5):
            slot_list.append(SlotW10(init_dict=Slot1.as_dict()))
            slot_list.append(SlotW22(init_dict=Slot2.as_dict()))

        # Two slots in the list are modified (bigger than the others)
        rotor.slot_list = slot_list
        rotor.slot_list[0].H2 = 300e-3
        rotor.slot_list[7].H2 = 300e-3
        # Set slots position
        rotor.alpha = array([0, 29, 60, 120, 150, 180, 210, 240, 300, 330]) * pi / 180

        # Evenly distributed Notch definition
        slot3 = SlotW10(Zs=12, W0=40e-3, W1=40e-3, W2=40e-3, H0=0, H1=0, H2=25e-3)
        notch = NotchEvenDist(notch_shape=slot3, alpha=15 * pi / 180)
        rotor.notch = [notch]

        # Plot, check and save
        rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "fig_12_LamSlotMulti.png"))
        self.assertEqual(len(fig.axes[0].patches), 2)

    def test_SlotUD(self):
        """Figure 13: User Defined slot "snowflake"
        """

        plt.close("all")
        # Enfore first point on rotor bore
        Rrotor = abs(0.205917893677990 - 0.107339745962156j)
        machine = MachineSRM()
        # Stator definintion
        machine.stator = LamSlotWind(
            Rint=Rrotor + 5e-3, Rext=Rrotor + 120e-3, is_internal=False, is_stator=True
        )
        machine.stator.slot = SlotW21(
            Zs=36, W0=7e-3, H0=10e-3, H1=0, H2=70e-3, W1=30e-3, W2=0.1e-3
        )
        machine.stator.winding = WindingDW2L(qs=3, p=3, coil_pitch=5)

        # Rotor definition
        machine.rotor = LamSlot(
            Rint=0.02, Rext=Rrotor, is_internal=True, is_stator=False
        )
        machine.rotor.axial_vent = [
            VentilationTrap(Zh=6, Alpha0=0, D0=0.025, H0=0.025, W1=0.015, W2=0.04)
        ]
        # Complex coordinates of half the snowflake slot
        point_list = [
            0.205917893677990 - 0.107339745962156j,
            0.187731360198517 - 0.0968397459621556j,
            0.203257639640145 - 0.0919474411167423j,
            0.199329436409870 - 0.0827512886940357j,
            0.174740979141750 - 0.0893397459621556j,
            0.143564064605510 - 0.0713397459621556j,
            0.176848674296337 - 0.0616891108675446j,
            0.172822394854708 - 0.0466628314259158j,
            0.146001886779019 - 0.0531173140978201j,
            0.155501886779019 - 0.0366628314259158j,
            0.145109581933606 - 0.0306628314259158j,
            0.127109581933606 - 0.0618397459621556j,
            0.0916025403784439 - 0.0413397459621556j,
            0.134949327895761 - 0.0282609076372691j,
            0.129324972242779 - 0.0100025773880714j,
            0.0690858798800485 - 0.0283397459621556j,
            0.0569615242270663 - 0.0213397459621556j,
        ]
        machine.rotor.slot = SlotUD(Zs=6, is_sym=True, point_list=point_list)

        # Plot, check and save
        machine.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 83)
        fig.savefig(join(save_path, "fig_13_SlotUD.png"))

    def test_WindingUD(self):
        """Figure 15: User-defined Winding
        From pyleecan/Tests/Plot/LamWind/test_Slot_12_plot.py
        """
        plt.close("all")
        machine = MachineDFIM()
        # Rotor definition
        machine.rotor = LamSlotWind(
            Rint=0.2,
            Rext=0.5,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )
        machine.rotor.axial_vent = [
            VentilationPolar(Zh=6, Alpha0=pi / 6, W1=pi / 6, D0=100e-3, H0=0.3)
        ]
        machine.rotor.slot = SlotW12(Zs=6, R2=35e-3, H0=20e-3, R1=17e-3, H1=130e-3)
        machine.rotor.winding = WindingUD(
            user_wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3
        )
        machine.rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)
        # Stator definion
        machine.stator = LamSlotWind(
            Rint=0.51,
            Rext=0.8,
            is_internal=False,
            is_stator=True,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )
        machine.stator.slot = SlotW12(Zs=18, R2=25e-3, H0=30e-3, R1=0, H1=150e-3)
        machine.stator.winding.Lewout = 60e-3
        machine.stator.winding = WindingDW2L(qs=3, p=3)
        machine.stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

        # Shaft & frame
        machine.shaft = Shaft(Drsh=machine.rotor.Rint * 2, Lshaft=1)
        machine.frame = Frame(Rint=0.8, Rext=0.9, Lfra=1)

        # Plot, check and save
        machine.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "fig_15_WindingUD.png"))
        self.assertEqual(len(fig.axes[0].patches), 73)

    def test_BoreFlower(self):
        """Figure 17: LamHole with uneven bore shape
        From pyleecan/Tests/Plot/LamHole/test_Hole_50_plot.py
        """
        # Rotor definition
        rotor = LamHole(
            is_internal=True, Rint=0.021, Rext=0.075, is_stator=False, L1=0.7
        )
        rotor.hole = list()
        rotor.hole.append(
            HoleM50(
                Zh=8,
                W0=50e-3,
                W1=0,
                W2=1e-3,
                W3=1e-3,
                W4=20.6e-3,
                H0=17.3e-3,
                H1=3e-3,
                H2=0.5e-3,
                H3=6.8e-3,
                H4=0,
            )
        )
        # Rotor axial ventilation ducts
        rotor.axial_vent = list()
        rotor.axial_vent.append(VentilationCirc(Zh=8, Alpha0=0, D0=5e-3, H0=40e-3))
        rotor.axial_vent.append(VentilationCirc(Zh=8, Alpha0=pi / 8, D0=7e-3, H0=40e-3))
        # Remove a magnet
        rotor.hole[0].magnet_1 = None
        # Rotor bore shape
        rotor.bore = BoreFlower(N=8, Rarc=0.05, alpha=pi / 8)

        # Plot, check and save
        rotor.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "fig_17_BoreFlower.png"))
        # 2 for lam + 3*8 for holes + 16 vents
        self.assertEqual(len(fig.axes[0].patches), 42)

    def test_ecc_FEMM(self):
        """Figure 18: transfrom_list in FEMM for eccentricities
        """
        simu = Simu1(name="ICEM_2020", machine=SPMSM_015)
        simu.machine.name = "fig_18_Transform_list"

        # Modify stator Rext to get more convincing translation
        SPMSM_015.stator.Rext = SPMSM_015.stator.Rext * 0.9
        gap = SPMSM_015.comp_width_airgap_mec()

        # Definition of the enforced output of the electrical module
        Nr = ImportMatrixVal(value=ones(1) * 3000)
        Is = ImportMatrixVal(value=array([[0, 0, 0]]))
        time = ImportGenVectLin(start=0, stop=0, num=1, endpoint=True)
        angle = ImportGenVectLin(start=0, stop=2 * 2 * pi / 9, num=2043, endpoint=False)
        simu.input = InCurrent(
            Is=Is,
            Ir=None,  # No winding on the rotor
            Nr=Nr,
            angle_rotor=None,
            time=time,
            angle=angle,
            angle_rotor_initial=0,
        )

        # Definition of the magnetic simulation (is_mmfr=False => no flux from the magnets)
        simu.mag = MagFEMM(
            is_stator_linear_BH=0,
            is_rotor_linear_BH=0,
            is_sliding_band=False,  # Ecc => No sliding band
            is_symmetry_a=False,  # No sym
            is_mmfs=False,
            is_get_mesh=True,
            is_save_FEA=True,
            sym_a=1,
        )
        simu.struct = None

        # Set two transformations
        # First rotate 3rd Magnet
        transform_list = [
            {"type": "rotate", "value": 0.08, "label": "MagnetRotorRadial_S_R0_T0_S3"}
        ]
        # Then Translate the rotor
        transform_list.append(
            {"type": "translate", "value": gap * 0.75, "label": "Rotor"}
        )
        simu.mag.transform_list = transform_list

        # Run the simulation
        out = Output(simu=simu)
        simu.run()

        # FEMM files (mesh and results) are available in Results folder
        copyfile(
            join(out.path_res, "Femm", "fig_18_Transform_list_model.ans"),
            join(save_path, "fig_18_Transform_list_model.ans"),
        )
        copyfile(
            join(out.path_res, "Femm", "fig_18_Transform_list_model.fem"),
            join(save_path, "fig_18_Transform_list_model.fem"),
        )
        # Plot, check, save
        out.plot_mesh_field(
            mesh=out.mag.meshsolution.mesh[0],
            title="Permeability",
            field=out.mag.meshsolution.solution[0].face["mu"],
        )
        fig = plt.gcf()
        fig.savefig(join(save_path, "fig_18_transform_list.png"))

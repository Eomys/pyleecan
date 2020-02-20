from numpy import ones, pi, array, zeros, linspace
from unittest import TestCase
from os import makedirs
from os.path import join
import matplotlib.pyplot as plt
from pyleecan.Tests import save_plot_path
from pyleecan.Tests.Plot.LamWind import wind_mat
from pyleecan.Classes.import_all import *
from pyleecan.Tests.Validation.Machine.SPMSM_015 import SPMSM_015
from pyleecan.Functions.GMSH.gen_3D_mesh import gen_3D_mesh

save_path = join(save_plot_path, "ICEM_2020")
makedirs(save_path)


class test_ICEM_2020(TestCase):
    """This test gather all the images for the publication in ICEM 2020
    """

    def test_SlotMulti(self):
        """Test that you can plot a LamSlotMulti (two slots kind + notches)
        """
        plt.close("all")
        test_obj = LamSlotMulti(
            Rint=0.2,
            Rext=0.7,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )

        Slot1 = SlotW10(
            Zs=10, W0=50e-3, H0=30e-3, W1=100e-3, H1=30e-3, H2=100e-3, W2=120e-3
        )
        Slot2 = SlotW22(Zs=12, W0=pi / 12, H0=50e-3, W2=pi / 6, H2=125e-3)

        slot_list = list()
        for ii in range(5):
            slot_list.append(SlotW10(init_dict=Slot1.as_dict()))
            slot_list.append(SlotW22(init_dict=Slot2.as_dict()))

        test_obj.slot_list = slot_list
        test_obj.slot_list[0].H2 = 300e-3
        test_obj.slot_list[7].H2 = 300e-3

        slot3 = SlotW10(Zs=12, W0=40e-3, W1=40e-3, W2=40e-3, H0=0, H1=0, H2=25e-3)
        notch = NotchEvenDist(notch_shape=slot3, alpha=15 * pi / 180)
        test_obj.notch = [notch]

        test_obj.alpha = (
            array([0, 29, 60, 120, 150, 180, 210, 240, 300, 330]) * pi / 180
        )

        # Plot, check and save
        test_obj.plot()
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_SlotMulti.png"))
        self.assertEqual(len(fig.axes[0].patches), 2)

    def test_SlotMulti_sym(self):
        """Test that you can plot a LamSlotMulti with sym
        """

        plt.close("all")
        test_obj = LamSlotMulti(
            Rint=0.2,
            Rext=0.7,
            is_internal=True,
            is_stator=False,
            L1=0.9,
            Nrvd=2,
            Wrvd=0.05,
        )

        Zs = 8
        Slot1 = SlotW10(
            Zs=Zs, W0=50e-3, H0=30e-3, W1=100e-3, H1=30e-3, H2=100e-3, W2=120e-3
        )
        Slot2 = SlotW22(Zs=Zs, W0=pi / 12, H0=50e-3, W2=pi / 6, H2=125e-3)

        slot_list = list()
        for ii in range(Zs // 2):
            slot_list.append(SlotW10(init_dict=Slot1.as_dict()))
            slot_list.append(SlotW22(init_dict=Slot2.as_dict()))

        test_obj.slot_list = slot_list

        slot3 = SlotW10(Zs=Zs // 2, W0=40e-3, W1=40e-3, W2=40e-3, H0=0, H1=0, H2=25e-3)
        notch = NotchEvenDist(notch_shape=slot3, alpha=2 * pi / Zs)
        test_obj.notch = [notch]

        test_obj.alpha = linspace(0, 2 * pi, 8, endpoint=False) + pi / Zs

        # Plot, check and save
        test_obj.plot(sym=2)
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_SlotMulti_sym.png"))
        self.assertEqual(len(fig.axes[0].patches), 1)

        # Generate the gmsh equivalent
        gen_3D_mesh(
            lamination=test_obj,
            save_path=join(save_path, "Lamination.msh"),
            sym=4,
            mesh_size=20e-3,
            Nlayer=20,
        )

    def test_ecc_FEMM(self):
        """Test of the transfrom_list in FEMM for eccentricities
        """
        simu = Simu1(name="EM_SPMSM_NL_001", machine=SPMSM_015)
        # Modify stator Rext to get move convinsing translation
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
            is_sliding_band=False,
            is_symmetry_a=False,
            is_mmfs=False,
            is_get_mesh=True,
            is_save_FEA=True,
            sym_a=1,
        )
        simu.struct = None
        transform_list = [
            {"type": "rotate", "value": 0.08, "label": "MagnetRotorRadial_S_R0_T0_S3"}
        ]
        transform_list.append(
            {"type": "translate", "value": gap * 0.75, "label": "Rotor"}
        )
        simu.mag.transform_list = transform_list

        out = Output(simu=simu)
        simu.run()

        out.plot_mesh_field(
            mesh=out.mag.meshsolution.mesh[0],
            title="Permeability",
            field=out.mag.meshsolution.solution[0].face["mu"],
        )
        fig = plt.gcf()
        fig.savefig(join(save_path, "test_ecc_FEMM.png"))

    def test_SlotUD(self):
        """Test User Defined slot "snowflake"
        """

        plt.close("all")
        Rrotor = abs(0.205917893677990 - 0.107339745962156j)
        test_obj = MachineSRM()
        # Stator definintion
        test_obj.stator = LamSlotWind(
            Rint=Rrotor + 5e-3, Rext=Rrotor + 120e-3, is_internal=False, is_stator=True
        )
        test_obj.stator.slot = SlotW21(
            Zs=36, W0=7e-3, H0=10e-3, H1=0, H2=70e-3, W1=30e-3, W2=0.1e-3
        )
        test_obj.stator.winding = WindingDW2L(qs=3, p=3, coil_pitch=5)

        # Rotor definition
        test_obj.rotor = LamSlot(
            Rint=0.02, Rext=Rrotor, is_internal=True, is_stator=False
        )
        test_obj.rotor.axial_vent = [
            VentilationTrap(Zh=6, Alpha0=0, D0=0.025, H0=0.025, W1=0.015, W2=0.04)
        ]
        # Complex coordinates of the snowflake slot
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
        test_obj.rotor.slot = SlotUD(Zs=6, is_sym=True, point_list=point_list)

        # Plot, check and save
        test_obj.plot()
        fig = plt.gcf()
        self.assertEqual(len(fig.axes[0].patches), 83)
        fig.savefig(join(save_path, "test_Christmas.png"))

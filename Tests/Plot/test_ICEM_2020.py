from os import makedirs
from os.path import join, isdir
import pytest
from shutil import copyfile

import matplotlib.pyplot as plt
from numpy import array, linspace, ones, pi, zeros

from pyleecan.Classes.import_all import *

try:
    from pyleecan.Functions.GMSH.gen_3D_mesh import gen_3D_mesh
except ImportError as error:
    gen_3D_mesh = error
from Tests import save_plot_path
from Tests.Plot.LamWind import wind_mat
from pyleecan.Functions.load import load
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Output import Output
from pyleecan.Classes.SlotUD2 import SlotUD2
from pyleecan.Classes.OptiDesignVar import OptiDesignVar
from pyleecan.Classes.OptiObjective import OptiObjective
from pyleecan.Classes.OptiProblem import OptiProblem
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.OptiGenAlgNsga2Deap import OptiGenAlgNsga2Deap

import numpy as np
import random
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

# Gather results in the same folder
save_path = join(save_plot_path, "ICEM_2020")
if not isdir(save_path):
    makedirs(save_path)


"""This test gather all the images/project for the ICEM 2020 publication:
"Design optimization of innovative electrical machines topologies based
on Pyleecan open-source object-oriented software"
"""


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.SCIM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_sym():
    """Figure 9: Check that the FEMM can handle symmetry
    From pyleecan/Tests/Validation/Simulation/test_EM_SCIM_NL_006.py
    """
    SCIM_006 = load(join(DATA_DIR, "Machine", "SCIM_006.json"))
    simu = Simu1(name="test_ICEM_2020", machine=SCIM_006)
    simu.machine.name = "fig_09_FEMM_sym"

    # Definition of the enforced output of the electrical module
    N0 = 1500
    Is = ImportMatrixVal(value=array([[20, -10, -10]]))
    Ir = ImportMatrixVal(value=zeros((1, 28)))
    Nt_tot = 1
    Na_tot = 4096
    simu.input = InputCurrent(
        Is=Is,
        Ir=Ir,  # zero current for the rotor
        OP=OPdq(N0=N0),
        Nt_tot=Nt_tot,
        Na_tot=Na_tot,
        angle_rotor_initial=0.2244,
    )

    # Definition of the magnetic simulation
    # 2 sym + antiperiodicity = 1/4 Lamination
    simu.mag = MagFEMM(
        type_BH_stator=2, type_BH_rotor=2, is_periodicity_a=True, is_fast_draw=False
    )
    # Stop after magnetic computation
    simu.force = None
    simu.struct = None
    # Run simulation
    out = Output(simu=simu)
    simu.run()

    # FEMM files (mesh and results) are available in Results folder
    copyfile(
        join(out.path_result, "Femm", "fig_09_FEMM_sym_model.ans"),
        join(save_path, "fig_09_FEMM_sym_model.ans"),
    )
    copyfile(
        join(out.path_result, "Femm", "fig_09_FEMM_sym_model.fem"),
        join(save_path, "fig_09_FEMM_sym_model.fem"),
    )


@pytest.mark.GMSH
def test_gmsh_mesh_dict():
    """Figure 10: Generate a 3D mesh with Gmsh by setting the
    number of element on each lines
    """
    if isinstance(gen_3D_mesh, ImportError):
        raise ImportError("Fail to import gen_3D_mesh (gmsh package missing)")

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
    stator.plot(is_lam_only=True, is_show_fig=False)
    fig = plt.gcf()
    fig.savefig(join(save_path, "fig_10_ref_lamination.png"))
    fig.savefig(join(save_path, "fig_10_ref_lamination.svg"), format="svg")
    assert len(fig.axes[0].patches) == 2

    # Definition of the number of each element on each line
    mesh_dict = {
        "0": 5,  # Yoke_Side_Right
        "1": 5,  # Yoke_Side_Left
        "2": 5,  # Yoke_Arc
        "3": 2,
        "4": 8,
        "5": 1,
        "6": 1,
        "7": 1,
        "8": 2,  # bore_arc_bot
        "9": 2,  # bore_arc_top
        "10": 1,
        "11": 1,
        "12": 1,
        "13": 8,
        "14": 2,
    }
    gen_3D_mesh(
        lamination=stator,
        save_path=join(save_path, "fig_10_gmsh_mesh_dict.msh"),
        mesh_size=7e-3,
        user_mesh_dict=mesh_dict,
        is_rect=True,
        Nlayer=18,
        display=False,
    )
    # To see the resulting mesh, gmsh_mesh_dict.msh need to be
    # opened in Gmsh


@pytest.mark.skip
@pytest.mark.GMSH
def test_SlotMulti_sym():
    """Figure 11: Genera
    te a 3D mesh with GMSH for a lamination
    with several slot types and notches
    """

    if isinstance(gen_3D_mesh, ImportError):
        raise ImportError("Fail to import gen_3D_mesh (gmsh package missing)")

    plt.close("all")
    # Rotor definition
    rotor = LamSlotMulti(
        Rint=0.2, Rext=0.7, is_internal=True, is_stator=False, L1=0.9, Nrvd=2, Wrvd=0.05
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
    rotor.plot(sym=4, is_show_fig=False)
    fig = plt.gcf()
    fig.savefig(join(save_path, "fig_11_SlotMulti_sym.png"))
    fig.savefig(join(save_path, "fig_11_SlotMulti_sym.svg"), format="svg")
    assert len(fig.axes[0].patches) == 1

    # Generate the gmsh equivalent
    gen_3D_mesh(
        lamination=rotor,
        save_path=join(save_path, "fig_11_gmsh_SlotMulti.msh"),
        sym=4,
        mesh_size=20e-3,
        Nlayer=20,
        display=False,
    )
    # To see the resulting mesh, gmsh_SlotMulti.msh need to be
    # opened in Gmsh


@pytest.mark.MachineUD
def test_MachineUD():
    """Figure 12: Check that you can plot a machine with 4 laminations"""
    machine = MachineUD()
    machine.name = "Machine with 4 laminations"

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
    lam1.winding = WindingUD(qs=3, p=3)
    lam1.winding.init_as_CW2LT()
    # External Rotor
    lam2 = LamSlot(
        Rext=lam1.Rint - A1, Rint=lam1.Rint - A1 - W2, is_internal=True, is_stator=False
    )
    lam2.slot = SlotW10(Zs=22, W0=25e-3, W1=25e-3, W2=15e-3, H0=0, H1=0, H2=W2 * 0.75)
    # Internal Rotor
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
        Rext=lam3.Rint - A3, Rint=lam3.Rint - A3 - W4, is_internal=True, is_stator=True
    )
    lam4.slot = SlotW10(Zs=12, W0=25e-3, W1=25e-3, W2=1e-3, H0=0, H1=0, H2=W4 * 0.75)
    lam4.winding = WindingUD(qs=3, p=3)
    lam4.winding.init_as_CW2LT()
    # Machine definition
    machine.lam_list = [lam1, lam2, lam3, lam4]
    machine.shaft = Shaft(Drsh=lam4.Rint * 2)

    # Plot, check and save
    machine.plot(is_show_fig=False, is_clean_plot=True)
    fig = plt.gcf()
    fig.savefig(join(save_path, "fig_12_MachineUD.png"))
    fig.savefig(join(save_path, "fig_12_MachineUD.svg"), format="svg")
    assert len(fig.axes[0].patches) == 57

    machine.frame = None
    machine.name = None

    machine.plot(is_show_fig=False, is_clean_plot=True)
    fig = plt.gcf()
    fig.savefig(join(save_path, "fig_12_MachineUD_no_frame_no_name.png"))
    fig.savefig(join(save_path, "fig_12_MachineUD_no_frame_no_name.svg"), format="svg")
    assert len(fig.axes[0].patches) == 57


def test_SlotMulti_rotor():
    """Figure 13: Check that you can plot a LamSlotMulti rotor (two slots kind + notches)"""
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
    rotor.plot(is_show_fig=False, is_clean_plot=True, edgecolor="k")
    fig = plt.gcf()
    fig.savefig(join(save_path, "fig_13_LamSlotMulti_rotor.png"))
    fig.savefig(join(save_path, "fig_13_LamSlotMulti_rotor.svg"), format="svg")
    assert len(fig.axes[0].patches) == 2


def test_SlotMulti_stator():
    """Figure 13: Check that you can plot a LamSlotMulti stator (two slots kind + notches)"""
    plt.close("all")
    # Lamination main dimensions definition
    stator = LamSlotMulti(Rint=0.2, Rext=0.7, is_internal=False, is_stator=True)

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
    stator.slot_list = slot_list
    stator.slot_list[0].H2 = 300e-3
    stator.slot_list[7].H2 = 300e-3
    # Set slots position
    stator.alpha = array([0, 29, 60, 120, 150, 180, 210, 240, 300, 330]) * pi / 180

    # Evenly distributed Notch definition
    slot3 = SlotW10(Zs=12, W0=40e-3, W1=40e-3, W2=40e-3, H0=0, H1=0, H2=25e-3)
    notch = NotchEvenDist(notch_shape=slot3, alpha=15 * pi / 180)
    stator.notch = [notch]

    # Plot, check and save
    stator.plot(is_show_fig=False, is_clean_plot=True)
    fig = plt.gcf()
    fig.savefig(join(save_path, "fig_13_LamSlotMulti_stator.png"))
    fig.savefig(join(save_path, "fig_13_LamSlotMulti_stator.svg"), format="svg")
    assert len(fig.axes[0].patches) == 2


@pytest.mark.SlotUD
def test_SlotUD():
    """Figure 14: User Defined slot "snowflake" """

    plt.close("all")
    # Enfore first point on rotor bore
    Rrotor = abs(0.205917893677990 - 0.107339745962156j)
    machine = MachineSRM()
    machine.name = "User-Defined Slot"
    # Stator definintion
    machine.stator = LamSlotWind(
        Rint=Rrotor + 5e-3, Rext=Rrotor + 120e-3, is_internal=False, is_stator=True
    )
    machine.stator.slot = SlotW21(
        Zs=36, W0=7e-3, H0=10e-3, H1=0, H2=70e-3, W1=30e-3, W2=0.1e-3
    )
    machine.stator.winding = WindingUD(qs=3, p=3, coil_pitch=5)
    machine.stator.winding.init_as_DWL(nlay=2)

    # Rotor definition
    machine.rotor = LamSlot(Rint=0.02, Rext=Rrotor, is_internal=True, is_stator=False)
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
    machine.rotor.slot = SlotUD(Zs=6)
    machine.rotor.slot.set_from_point_list(is_sym=True, point_list=point_list)

    # Plot, check and save
    machine.plot(is_show_fig=False, is_clean_plot=True)
    fig = plt.gcf()
    assert len(fig.axes[0].patches) == 83
    fig.savefig(join(save_path, "fig_14_SlotUD.png"))
    fig.savefig(join(save_path, "fig_14_SlotUD.svg"), format="svg")


def test_WindingUD():
    """Figure 16: User-defined Winding
    From pyleecan/Tests/Plot/LamWind/test_Slot_12_plot.py
    """
    plt.close("all")
    machine = MachineDFIM()
    machine.name = "User Defined Winding"
    # Rotor definition
    machine.rotor = LamSlotWind(
        Rint=0.2, Rext=0.5, is_internal=True, is_stator=False, L1=0.9, Nrvd=2, Wrvd=0.05
    )
    machine.rotor.axial_vent = [
        VentilationPolar(Zh=6, Alpha0=0, W1=pi / 6, D0=100e-3, H0=0.3)
    ]
    machine.rotor.slot = SlotW12(Zs=6, R2=35e-3, H0=20e-3, R1=17e-3, H1=130e-3)
    machine.rotor.winding = WindingUD(wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3)
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
    machine.stator.winding = WindingUD(qs=3, p=3, coil_pitch=1)
    machine.stator.winding.init_as_DWL(nlay=2)
    machine.stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

    # Shaft & frame
    machine.shaft = Shaft(Drsh=machine.rotor.Rint * 2, Lshaft=1)
    machine.frame = Frame(Rint=0.8, Rext=0.9, Lfra=1)

    # Plot, check and save
    machine.plot(is_show_fig=False)
    fig = plt.gcf()
    fig.savefig(join(save_path, "fig_16_WindingUD.png"))
    fig.savefig(join(save_path, "fig_16_WindingUD.svg"), format="svg")
    assert len(fig.axes[0].patches) == 73


def test_WindingUD_layer():
    """Figure 17: User-defined Winding with uneven winding layer"""
    plt.close("all")
    # Rotor definition
    rotor = LamSlotWind(
        Rint=0.2, Rext=0.5, is_internal=True, is_stator=False, L1=0.9, Nrvd=2, Wrvd=0.05
    )
    rotor.axial_vent = [VentilationCirc(Zh=6, Alpha0=0, D0=100e-3, H0=0.3)]
    rotor.slot = SlotW11(
        Zs=6, H0=15e-3, W0=60e-3, W1=100e-3, W2=100e-3, H1=20e-3, H2=200e-3
    )
    rotor.slot = rotor.slot.convert_to_SlotUD2()
    assert isinstance(rotor.slot, SlotUD2)
    key = "Nrad=2, Ntan=2"
    Top, Bottom = rotor.slot.active_surf.split_line(0, 100, is_join=True)
    Bottom_Left, Bottom_Right = Bottom.split_line(
        0.320 - 100j, 0.320 + 100j, is_join=True
    )
    Top_Left, Top_Right = Top.split_line(0.410 - 100j, 0.410 + 100j, is_join=True)
    rotor.slot.split_active_surf_dict = {
        key: [Bottom_Right, Bottom_Left, Top_Right, Top_Left]
    }
    rotor.winding = WindingUD(wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3)
    rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)

    # For testing the _set_split_active_surf_dict method
    rotor.save(join(save_path, "Fig17_rotor_wind_layer.json"))
    rotor = load(join(save_path, "Fig17_rotor_wind_layer.json"))

    # Plot, check and save
    rotor.plot(is_show_fig=False, is_clean_plot=True,edgecolor="k")
    fig = plt.gcf()
    fig.savefig(join(save_path, "fig_17_WindingUD_layer.png"))
    fig.savefig(join(save_path, "fig_17_WindingUD_layer.svg"), format="svg")
    assert len(fig.axes[0].patches) == 32


def test_BoreFlower(is_show_fig=False):
    """Figure 18: LamHole with uneven bore shape
    From pyleecan/Tests/Plot/LamHole/test_Hole_50_plot.py
    """
    # Rotor definition
    rotor = LamHole(is_internal=True, Rint=0.021, Rext=0.075, is_stator=False, L1=0.7)
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
    rotor.yoke = BoreFlower(N=8, Rarc=0.05 / 4, alpha=pi / 8)

    # Plot, check and save
    fig, _ = rotor.plot(is_show_fig=is_show_fig)
    fig.savefig(join(save_path, "fig_18_BoreFlower.png"))
    fig.savefig(join(save_path, "fig_18_BoreFlower.svg"), format="svg")
    # 2 for lam + 3*8 for holes + 16 vents
    assert len(fig.axes[0].patches) == 42
    fig, _ = rotor.plot(is_show_fig=is_show_fig, sym=8)
    fig.savefig(join(save_path, "fig_18_BoreFlower_sym.png"))
    fig.savefig(join(save_path, "fig_18_BoreFlower_sym.svg"), format="svg")
    # 1 for lam + 3*1 for holes + 3 vents
    assert len(fig.axes[0].patches) == 7


@pytest.mark.SPMSM
@pytest.mark.MagFEMM
@pytest.mark.long_5s
@pytest.mark.SingleOP
@pytest.mark.periodicity
def test_ecc_FEMM():
    """Figure 19: transfrom_list in FEMM for eccentricities"""
    SPMSM_015 = load(join(DATA_DIR, "Machine", "SPMSM_015.json"))
    simu = Simu1(name="test_ICEM_2020_ecc", machine=SPMSM_015)
    simu.machine.name = "fig_19_Transform_list"

    # Modify stator Rext to get more convincing translation
    SPMSM_015.stator.Rext = SPMSM_015.stator.Rext * 0.9
    gap = SPMSM_015.comp_width_airgap_mec()

    # Definition of the enforced output of the electrical module
    N0 = 3000
    Is = ImportMatrixVal(value=array([[0, 0, 0]]))
    time = ImportGenVectLin(start=0, stop=0, num=1, endpoint=True)
    angle = ImportGenVectLin(start=0, stop=2 * 2 * pi / 9, num=2043, endpoint=False)
    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        OP=OPdq(N0=N0),
        time=time,
        angle=angle,
        angle_rotor_initial=0,
    )

    # Definition of the magnetic simulation (is_mmfr=False => no flux from the magnets)
    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_sliding_band=False,  # Ecc => No sliding band
        is_periodicity_a=False,
        is_mmfs=False,
        is_get_meshsolution=True,
        is_fast_draw=False,
    )
    simu.force = None
    simu.struct = None

    # Set two transformations
    # First rotate 3rd Magnet
    transform_list = [
        {"type": "rotate", "value": 0.08, "label": "MagnetRotorRadial_S_R0_T0_S3"}
    ]
    # Then Translate the rotor
    transform_list.append({"type": "translate", "value": gap * 0.75, "label": "Rotor"})
    simu.mag.transform_list = transform_list

    # Run the simulation
    out = Output(simu=simu)
    simu.run()

    # FEMM files (mesh and results) are available in Results folder
    copyfile(
        join(out.path_result, "Femm", "fig_19_Transform_list_model.ans"),
        join(save_path, "fig_19_Transform_list_model.ans"),
    )
    copyfile(
        join(out.path_result, "Femm", "fig_19_Transform_list_model.fem"),
        join(save_path, "fig_19_Transform_list_model.fem"),
    )
    # Plot, check, save
    out.mag.meshsolution.plot_mesh(
        save_path=join(save_path, "fig_19_transform_list.png"), is_show_fig=False
    )


@pytest.mark.skip
@pytest.mark.long_5s
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_Optimization_problem():
    """
    Figure19: Machine topology before optimization
    Figure20: Individuals in the fitness space
    Figure21: Pareto Front in the fitness space
    Figure22: Topology to maximize first torque harmonic
    Figure22: Topology to minimize second torque harmonic

    WARNING: The computation takes 6 hours on a single 3GHz CPU core.
    The algorithm uses randomization at different steps so
    the results won't be exactly the same as the one in the publication
    """
    # ------------------ #
    # DEFAULT SIMULATION #
    # ------------------ #

    # First, we need to define a default simulation.
    # This simulation will the base of every simulation during the optimization process

    # Load the machine
    SPMSM_001 = load(join(DATA_DIR, "Machine", "SPMSM_001.json"))

    # Definition of the enforced output of the electrical module
    Na_tot = 1024  # Angular steps
    Nt_tot = 32  # Time step
    Is = ImportMatrixVal(
        value=np.array(
            [
                [1.73191211247099e-15, 24.4948974278318, -24.4948974278318],
                [-0.925435413499285, 24.9445002597334, -24.0190648462341],
                [-1.84987984757817, 25.3673918959653, -23.5175120483872],
                [-2.77234338398183, 25.7631194935712, -22.9907761095894],
                [-3.69183822565029, 26.1312592975275, -22.4394210718773],
                [-4.60737975447626, 26.4714170945114, -21.8640373400352],
                [-5.51798758565886, 26.7832286350338, -21.2652410493749],
                [-6.42268661752422, 27.0663600234871, -20.6436734059628],
                [-7.32050807568877, 27.3205080756888, -20.0000000000000],
                [-8.21049055044714, 27.5454006435389, -19.3349100930918],
                [-9.09168102627374, 27.7407969064430, -18.6491158801692],
                [-9.96313590233562, 27.9064876291883, -17.9433517268527],
                [-10.8239220029239, 28.0422953859991, -17.2183733830752],
                [-11.6731175767218, 28.1480747505277, -16.4749571738058],
                [-12.5098132838389, 28.2237124515809, -15.7138991677421],
                [-13.3331131695549, 28.2691274944141, -14.9360143248592],
                [-14.1421356237309, 28.2842712474619, -14.1421356237310],
                [-14.9360143248592, 28.2691274944141, -13.3331131695549],
                [-15.7138991677420, 28.2237124515809, -12.5098132838389],
                [-16.4749571738058, 28.1480747505277, -11.6731175767219],
                [-17.2183733830752, 28.0422953859991, -10.8239220029240],
                [-17.9433517268527, 27.9064876291883, -9.96313590233564],
                [-18.6491158801692, 27.7407969064430, -9.09168102627375],
                [-19.3349100930918, 27.5454006435389, -8.21049055044716],
                [-20, 27.3205080756888, -7.32050807568879],
                [-20.6436734059628, 27.0663600234871, -6.42268661752424],
                [-21.2652410493749, 26.7832286350338, -5.51798758565888],
                [-21.8640373400352, 26.4714170945114, -4.60737975447627],
                [-22.4394210718772, 26.1312592975275, -3.69183822565031],
                [-22.9907761095894, 25.7631194935712, -2.77234338398184],
                [-23.5175120483872, 25.3673918959653, -1.84987984757819],
                [-24.0190648462341, 24.9445002597334, -0.925435413499304],
            ]
        )
    )
    N0 = 400
    Ir = ImportMatrixVal(value=np.zeros((Nt_tot, 28)))

    SPMSM_001.name = (
        "Default SPMSM machine"  # Rename the machine to have the good plot title
    )

    # Definition of the simulation
    simu = Simu1(name="test_Optimization_problem", machine=SPMSM_001)

    simu.input = InputCurrent(
        Is=Is,
        Ir=Ir,  # zero current for the rotor
        OP=OPdq(N0=N0),
        Nt_tot=Nt_tot,
        Na_tot=Na_tot,
        angle_rotor_initial=0.39,
    )

    # Definition of the magnetic simulation
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_periodicity_a=True,
    )

    simu.struct = None

    # Default Output
    output = Output(simu=simu)

    # Modify magnet width and the slot opening height
    output.simu.machine.stator.slot.H0 = 0.001
    output.simu.machine.rotor.slot.magnet[0].Wmag *= 0.98

    # FIG21 Display default machine
    output.simu.machine.plot(is_show_fig=False)
    fig = plt.gcf()
    fig.savefig(join(save_path, "fig_21_Machine_topology_before_optimization.png"))
    fig.savefig(
        join(save_path, "fig_21_Machine_topology_before_optimization.svg"), format="svg"
    )
    plt.close("all")
    # -------------------- #
    # OPTIMIZATION PROBLEM #
    # -------------------- #

    # Objective functions
    """Return the average torque opposite (opposite to be maximized)"""
    tem_av = "lambda output: -abs(output.mag.Tem_av)"

    """Return the torque ripple """
    Tem_rip_pp = "lambda output: abs(output.mag.Tem_rip_pp)"

    my_objs = [
        OptiObjective(
            name="Maximization of the average torque",
            symbol="Tem_av",
            unit="N.m",
            keeper=tem_av,
        ),
        OptiObjective(
            name="Minimization of the torque ripple",
            symbol="Tem_rip_pp",
            unit="N.m",
            keeper=Tem_rip_pp,
        ),
    ]

    # Design variables
    my_vars = [
        OptiDesignVar(
            name="Stator slot opening",
            symbol="W0",
            unit="m",
            type_var="interval",
            space=[
                0.2 * output.simu.machine.stator.slot.W2,
                output.simu.machine.stator.slot.W2,
            ],
            get_value="lambda space: random.uniform(*space)",
            setter="simu.machine.stator.slot.W0",
        ),
        OptiDesignVar(
            name="Rotor magnet width",
            symbol="Wmag",
            unit="m",
            type_var="interval",
            space=[
                0.5 * output.simu.machine.rotor.slot.W0,
                0.99 * output.simu.machine.rotor.slot.W0,
            ],  # May generate error in FEMM
            get_value="lambda space: random.uniform(*space)",
            setter="simu.machine.rotor.slot.magnet[0].Wmag",
        ),
    ]

    # Problem creation
    my_prob = OptiProblem(output=output, design_var=my_vars, obj_func=my_objs)

    # Solve problem with NSGA-II
    solver = OptiGenAlgNsga2Deap(problem=my_prob, size_pop=12, nb_gen=40, p_mutate=0.5)
    res = solver.solve()

    # ------------- #
    # PLOTS RESULTS #
    # ------------- #

    res.plot_generation(x_symbol="Tem_av", y_symbol="Tem_rip_pp")
    fig = plt.gcf()
    fig.savefig(join(save_path, "fig_20_Individuals_in_fitness_space.png"))
    fig.savefig(
        join(save_path, "fig_20_Individuals_in_fitness_space.svg"), format="svg"
    )

    res.plot_pareto(x_symbol="Tem_av", y_symbol="Tem_rip_pp")
    fig = plt.gcf()
    fig.savefig(join(save_path, "Pareto_front_in_fitness_space.png"))
    fig.savefig(join(save_path, "Pareto_front_in_fitness_space.svg"), format="svg")

    # Extraction of best topologies for every objective
    pareto_index = (
        res.get_pareto_index()
    )  # Extract individual index in the pareto front

    idx_1 = pareto_index[0]  # First objective
    idx_2 = pareto_index[0]  # Second objective

    Tem_av = res["Tem_av"].result
    Tem_rip_pp = res["Tem_rip_pp"].result

    for i in pareto_index:
        # First objective
        if Tem_av[i] < Tem_av[idx_1]:
            idx_1 = i
        # Second objective
        if Tem_rip_pp[i] < Tem_rip_pp[idx_2]:
            idx_2 = i

    # Get corresponding simulations
    simu1 = res.get_simu(idx_1)
    simu2 = res.get_simu(idx_2)

    # Rename machine to modify the title
    name1 = "Machine that maximizes the average torque ({:.3f} Nm)".format(
        abs(Tem_av[idx_1])
    )
    simu1.machine.name = name1
    name2 = "Machine that minimizes the torque ripple ({:.4f}Nm)".format(
        abs(Tem_rip_pp[idx_2])
    )
    simu2.machine.name = name2

    # plot the machine
    simu1.machine.plot(is_show_fig=False)
    fig = plt.gcf()
    fig.savefig(
        join(save_path, "fig_21_Topology_to_maximize_average_torque.png"), format="png"
    )
    fig.savefig(
        join(save_path, "fig_21_Topology_to_maximize_average_torque.svg"), format="svg"
    )

    simu2.machine.plot(is_show_fig=False)
    fig = plt.gcf()
    fig.savefig(
        join(save_path, "fig_21_Topology_to_minimize_torque_ripple.png"), format="png"
    )
    fig.savefig(
        join(save_path, "fig_21_Topology_to_minimize_torque_ripple.svg"), format="svg"
    )


if __name__ == "__main__":
    test_WindingUD_layer()
    # test_FEMM_sym()
    # test_WindingUD()
    # test_ecc_FEMM()
    # test_WindingUD_layer()
    print("Done")

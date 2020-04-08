# -*- coding: utf-8 -*-

from os.path import join
import matplotlib.pyplot as plt
from numpy import array, pi, zeros

from ....Classes.Frame import Frame
from ....Classes.LamSlotWind import LamSlotWind
from ....Classes.LamSquirrelCage import LamSquirrelCage
from ....Classes.MachineDFIM import MachineDFIM
from ....Classes.Shaft import Shaft
from ....Classes.VentilationCirc import VentilationCirc
from ....Classes.VentilationPolar import VentilationPolar
from ....Classes.VentilationTrap import VentilationTrap
from ....Classes.Winding import Winding
from ....Classes.WindingUD import WindingUD
from ....Classes.WindingCW2LT import WindingCW2LT
from ....Classes.WindingDW2L import WindingDW2L
from ....Classes.MatMagnetics import MatMagnetics
from ....Classes.SlotW22 import SlotW22

from ....Tests import save_plot_path as save_path
from ....Tests.Plot.LamWind import wind_mat


"""unittest for Lamination with winding plot"""


def test_Lam_Wind_22_wind_22():
    """Test machine plot with Slot 22 and winding rad=2, tan=2
    """
    print("\nTest plot Slot 22")
    plt.close("all")
    test_obj = MachineDFIM()
    test_obj.rotor = LamSlotWind(
        Rint=0, Rext=0.5, is_internal=True, is_stator=False, L1=0.8, Nrvd=4, Wrvd=0.05,
    )
    test_obj.rotor.slot = SlotW22(Zs=6, W0=pi / 20, W2=pi / 10, H0=20e-3, H2=150e-3)
    test_obj.rotor.winding = WindingUD(user_wind_mat=wind_mat, qs=4, p=4, Lewout=60e-3)
    test_obj.rotor.mat_type.mag = MatMagnetics(Wlam=0.5e-3)
    test_obj.shaft = Shaft(Drsh=test_obj.rotor.Rint * 2, Lshaft=1)

    test_obj.stator = LamSlotWind(
        Rint=0.51,
        Rext=0.8,
        is_internal=False,
        is_stator=True,
        L1=0.8,
        Nrvd=4,
        Wrvd=0.05,
    )
    test_obj.stator.slot = SlotW22(Zs=18, W0=pi / 20, W2=pi / 10, H0=20e-3, H2=150e-3)
    test_obj.stator.winding = WindingDW2L(qs=3, p=3)
    test_obj.stator.mat_type.mag = MatMagnetics(Wlam=0.5e-3)
    test_obj.stator.winding.Lewout = 60e-3
    test_obj.frame = Frame(Rint=0.8, Rext=0.8, Lfra=1)

    test_obj.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Wind_s22_1-Machine.png"))
    # Rotor + Stator + 0 for frame + 0 for shaft
    assert len(fig.axes[0].patches) == 63

    test_obj.rotor.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Wind_s22_2-Rotor.png"))
    # 1 for lam + 4*Zs for wind
    assert len(fig.axes[0].patches) == 25

    test_obj.stator.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Wind_s22_3-Stator.png"))
    # 2 for lam + Zs*2 for wind
    assert len(fig.axes[0].patches) == 38

    tooth = test_obj.rotor.slot.get_surface_tooth()
    tooth.plot(color="r")
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Wind_s22_Tooth_in.png"))

    tooth = test_obj.stator.slot.get_surface_tooth()
    tooth.plot(color="r")
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Wind_s22_Tooth_out.png"))

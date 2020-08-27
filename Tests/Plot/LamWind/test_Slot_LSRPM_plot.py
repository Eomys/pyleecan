# -*- coding: utf-8 -*-
from os.path import join
import pytest

import matplotlib.pyplot as plt
from numpy import array, pi, zeros

from pyleecan.Classes.Frame import Frame
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.MachineDFIM import MachineDFIM
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.WindingCW2LT import WindingCW2LT
from pyleecan.Classes.WindingDW2L import WindingDW2L
from pyleecan.Classes.SlotWLSRPM import SlotWLSRPM

from Tests import save_plot_path as save_path
from Tests.Plot.LamWind import wind_mat, wind_mat2


"""unittest for Lamination with winding plot"""


@pytest.fixture
def machine():
    """Run at the begining of every test to setup the machine"""
    plt.close("all")
    test_obj = LamSlotWind(
        Rint=50.7e-3,
        Rext=72.5e-3,
        is_internal=False,
        is_stator=True,
        L1=0.95,
        Nrvd=0,
        Wrvd=0,
    )
    test_obj.slot = SlotWLSRPM(
        Zs=12, W1=8e-3,W3=11.6e-3, H2=14.8e-3, R1=0.75e-3
    )

    return test_obj





def test_Lam_Wind_LSRPM_wind_tan(machine):
    """Test machine plot with Slot LSRPM and winding rad=1, tan=2
    """
    machine.winding = WindingCW2LT(qs=3, p=4, Lewout=0)
    machine.plot()
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_Lam_Wind_sLSRPM_2-tan-wind.png"))
    # 2 for lam + Zs*2 for wind
    assert len(fig.axes[0].patches) == 26


 
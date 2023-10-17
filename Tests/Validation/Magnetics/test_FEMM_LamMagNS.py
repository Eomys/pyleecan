from os.path import join, isdir
from os import makedirs
from multiprocessing import cpu_count
import matplotlib.pyplot as plt
import pytest
from Tests import save_validation_path as save_path

from numpy import exp, sqrt, pi, max as np_max
from numpy.testing import assert_array_almost_equal

from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.LamSlotMagNS import LamSlotMagNS
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D

from pyleecan.definitions import DATA_DIR


# python -m pytest ./Tests/Validation/Magnetics/test_FEMM_LamSlotMagNS.py
@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_LamSlotMagNS():
    """Validation of LamSlotMagNS in FEMM"""
    res_path = join(save_path, "LamSlotMagNS")
    if not isdir(res_path):
        makedirs(res_path)
    B = load(join(DATA_DIR, "Machine", "Benchmark.json"))
    B.name = "Toyota_Benchmark_MagNS_FEMM"
    BNS = B.copy()
    # Change rotor type to have different North/South Pole
    BNS.rotor = LamSlotMagNS(init_dict=B.rotor.as_dict())
    # North pole is unchange
    BNS.rotor.magnet_north = B.rotor.magnet.copy()
    BNS.rotor.magnet_south = B.rotor.magnet.copy()
    # Change magnet dimensions on south pole
    BNS.rotor.slot_south = B.rotor.slot.copy()
    BNS.rotor.slot_south.H1 /= 2
    BNS.rotor.slot_south.W1 /= 2
    # South magnet have different material
    BNS.rotor.magnet_south.mat_type.name += "_2"
    BNS.rotor.magnet_south.mat_type.mag.mur_lin = 2

    # Check plot machine
    fig, ax = BNS.plot(
        is_clean_plot=True,
        is_show_fig=True,
    )
    fig.savefig(join(res_path, "machine.png"))
    fig.savefig(join(res_path, "machine.svg"), format="svg")

    fig, ax = BNS.rotor.plot(is_add_arrow=True, is_clean_plot=True, is_show_fig=False)
    fig.savefig(join(res_path, "rotor_sym.png"))
    fig.savefig(join(res_path, "rotor_sym.svg"), format="svg")

    # Check periodicity
    assert B.comp_periodicity_spatial() == (1, True)
    assert BNS.comp_periodicity_spatial() == (1, False)  # N/S no longer sym

    # Check machine in FEMM
    simu = Simu1(name="test_FEMM_LamSlotMagNS", machine=BNS)
    simu.path_result = join(save_path, simu.name)
    simu.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
        Na_tot=2048,
        Nt_tot=1,
    )

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(
        type_BH_stator=1,
        type_BH_rotor=1,
        is_periodicity_a=True,  # No sym in fact
        is_periodicity_t=False,
        is_fast_draw=True,  # Will draw 1/5 of rotor then copy rotate
        nb_worker=cpu_count(),
        # Kmesh_fineness=2,
    )
    simu.path_result = join(res_path, simu.name)

    # Run simulations
    out = simu.run()

    out.mag.B.plot_2D_Data(
        "angle{°}",
        "time[0]",
        save_path=join(save_path, simu.name + "_B_space.png"),
        is_show_fig=False,
        **dict_2D
    )

    return out


# To run it without pytest
if __name__ == "__main__":
    out = test_FEMM_LamSlotMagNS()
    print("Done")

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
from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.MagFEMM import MagFEMM

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D

from pyleecan.definitions import DATA_DIR


# python -m pytest ./Tests/Validation/Magnetics/test_FEMM_NotchKey.py
@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_NotchKey_Airgap():
    """Validation of NotchKey in FEMM"""
    res_path = join(save_path, "NotchKey_Airgap")
    if not isdir(res_path):
        makedirs(res_path)
    B = load(join(DATA_DIR, "Machine", "Benchmark.json"))
    Steel = load(join(DATA_DIR, "Material", "Steel1.json"))
    Steel2 = Steel.copy()
    Steel2.name = "Steel2"
    Steel2.mag.mur_lin /= 2
    B.name = "Benchmark_NotchKey_Airgap_FEMM"
    # Reduce magnet width
    B.rotor.slot.W1 /= 2
    B.rotor.slot.W0 /= 2
    # Add notches with keys
    B.rotor.notch = [
        NotchEvenDist(
            alpha=0,
            key_mat=Steel,
            notch_shape=SlotM11(
                H1=B.rotor.slot.H1 * 1.2,
                H0=0,
                W1=B.rotor.slot.W1,
                W0=B.rotor.slot.W0,
                Zs=B.rotor.slot.Zs,
                is_bore=True,
            ),
        )
    ]
    B.stator.notch = [
        NotchEvenDist(
            alpha=0,
            key_mat=Steel2,
            notch_shape=SlotM10(
                H1=4e-3,
                H0=3e-3,
                W1=5e-3,
                W0=5e-3,
                Zs=B.stator.slot.Zs,
                is_bore=True,
            ),
        )
    ]
    # Check plot machine
    fig, ax = B.plot(
        is_max_sym=True,
        is_clean_plot=True,
        is_show_fig=False,
    )
    fig.savefig(join(res_path, "machine_sym.png"))
    fig.savefig(join(res_path, "machine_sym.svg"), format="svg")

    fig, ax = B.plot(
        save_path=join(res_path, "machine_full.png"),
        is_clean_plot=True,
        is_show_fig=False,
    )
    fig.savefig(join(res_path, "machine_full.png"))
    fig.savefig(join(res_path, "machine_full.svg"), format="svg")

    fig, ax = B.rotor.plot(is_add_arrow=True, is_show_fig=False)
    fig.savefig(join(res_path, "rotor.png"))
    fig.savefig(join(res_path, "rotor.svg"), format="svg")

    # plt.show()
    # Check periodicity
    assert B.comp_periodicity_spatial() == (1, True)

    # Check machine in FEMM with sym
    simu = Simu1(name="test_FEMM_Mag_Key", machine=B)
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
        is_periodicity_a=True,
        is_periodicity_t=False,
        nb_worker=cpu_count(),
        # Kmesh_fineness=2,
    )
    simu.path_result = join(res_path, simu.name)

    # Same simu without symetry
    simu2 = simu.copy()
    simu2.name = simu.name + "_Full"
    simu2.path_result = join(res_path, simu2.name)
    simu2.mag.is_periodicity_a = False

    # Run simulations
    out = simu.run()
    out2 = simu2.run()

    out.mag.B.plot_2D_Data(
        "angle{°}",
        "time[0]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_space.png"),
        is_show_fig=False,
        **dict_2D
    )

    # Compare both simu
    Bflux = out.mag.B
    arg_list = ["angle"]
    result = Bflux.get_rphiz_along(*arg_list)
    Brad = result["radial"]
    angle = result["angle"]

    Bflux2 = out2.mag.B
    arg_list = ["angle"]
    result2 = Bflux2.get_rphiz_along(*arg_list)
    Brad2 = result2["radial"]

    assert_array_almost_equal(Brad, Brad2, decimal=1)
    plt.close()
    return out


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_NotchKey_inner():
    """Validation of NotchKey in FEMM"""
    res_path = join(save_path, "NotchKey_inner")
    if not isdir(res_path):
        makedirs(res_path)
    B = load(join(DATA_DIR, "Machine", "Benchmark.json"))
    Steel = load(join(DATA_DIR, "Material", "Steel1.json"))
    B.name = "Benchmark_NotchKey_inner_FEMM"
    # Reduce magnet width
    B.rotor.slot.W1 /= 2
    B.rotor.slot.W0 /= 2
    # Add notches with keys
    B.rotor.notch = [
        NotchEvenDist(
            alpha=0,
            key_mat=Steel,
            notch_shape=SlotM11(
                H1=B.rotor.slot.H1 * 0.8,
                H0=B.rotor.slot.H1,
                W1=B.rotor.slot.W1,
                W0=B.rotor.slot.W0,
                Zs=B.rotor.slot.Zs,
                is_bore=True,
            ),
        )
    ]
    B.stator.notch = [
        NotchEvenDist(
            alpha=0,
            key_mat=Steel,
            notch_shape=SlotM10(
                H1=2e-3,
                H0=3e-3,
                W1=5e-3,
                W0=5e-3,
                Zs=B.stator.slot.Zs,
                is_bore=True,
            ),
        )
    ]
    # Check plot machine
    fig, ax = B.plot(
        is_max_sym=True,
        is_clean_plot=True,
        is_show_fig=False,
    )
    fig.savefig(join(res_path, "machine_sym.png"))
    fig.savefig(join(res_path, "machine_sym.svg"), format="svg")

    fig, ax = B.plot(
        save_path=join(res_path, "machine_full.png"),
        is_clean_plot=True,
        is_show_fig=False,
    )
    fig.savefig(join(res_path, "machine_full.png"))
    fig.savefig(join(res_path, "machine_full.svg"), format="svg")

    fig, ax = B.rotor.plot(is_add_arrow=True, is_show_fig=False)
    fig.savefig(join(res_path, "rotor.png"))
    fig.savefig(join(res_path, "rotor.svg"), format="svg")

    # plt.show()
    # Check periodicity
    assert B.comp_periodicity_spatial() == (1, True)

    # Check machine in FEMM with sym
    simu = Simu1(name="test_FEMM_Mag_Key", machine=B)
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
        is_periodicity_a=True,
        is_periodicity_t=False,
        nb_worker=cpu_count(),
        # Kmesh_fineness=2,
    )
    simu.path_result = join(res_path, simu.name)

    # Same simu without symetry
    simu2 = simu.copy()
    simu2.name = simu.name + "_Full"
    simu2.path_result = join(res_path, simu2.name)
    simu2.mag.is_periodicity_a = False

    # Run simulations
    out = simu.run()
    out2 = simu2.run()

    out.mag.B.plot_2D_Data(
        "angle{°}",
        "time[0]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_space.png"),
        is_show_fig=False,
        **dict_2D
    )

    # Compare both simu
    Bflux = out.mag.B
    arg_list = ["angle"]
    result = Bflux.get_rphiz_along(*arg_list)
    Brad = result["radial"]
    angle = result["angle"]

    Bflux2 = out2.mag.B
    arg_list = ["angle"]
    result2 = Bflux2.get_rphiz_along(*arg_list)
    Brad2 = result2["radial"]

    assert_array_almost_equal(Brad, Brad2, decimal=1)
    plt.close()
    return out


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_NotchKey_2():
    """Validation of NotchKey in FEMM, 2 key with B(H) curves"""
    res_path = join(save_path, "NotchKey_2")
    if not isdir(res_path):
        makedirs(res_path)
    B = load(join(DATA_DIR, "Machine", "Benchmark.json"))
    M400 = load(join(DATA_DIR, "Material", "M400-50A.json"))
    M270 = load(join(DATA_DIR, "Material", "M270-35A.json"))
    B.name = "Benchmark_NotchKey_FEMM_2"
    # Reduce magnet width
    B.rotor.slot.W1 /= 2
    B.rotor.slot.W0 /= 2
    # Add notches with keys
    B.rotor.notch = [
        NotchEvenDist(
            alpha=0,
            key_mat=M270,
            notch_shape=SlotM11(
                H1=B.rotor.slot.H1 * 0.8,
                H0=0,
                W1=B.rotor.slot.W1,
                W0=B.rotor.slot.W0,
                Zs=B.rotor.slot.Zs // 2,
                is_bore=True,
            ),
        ),
        NotchEvenDist(
            alpha=2 * pi / B.rotor.slot.Zs,
            key_mat=M400,
            notch_shape=SlotM11(
                H1=B.rotor.slot.H1 * 1.2,
                H0=0,
                W1=B.rotor.slot.W1,
                W0=B.rotor.slot.W0,
                Zs=B.rotor.slot.Zs // 2,
                is_bore=True,
            ),
        ),
    ]

    # Check plot machine
    fig, ax = B.plot(
        save_path=join(res_path, "machine_full.png"),
        is_clean_plot=True,
        is_show_fig=False,
    )
    fig.savefig(join(res_path, "machine_full.png"))
    fig.savefig(join(res_path, "machine_full.svg"), format="svg")

    fig, ax = B.rotor.plot(is_add_arrow=True, is_show_fig=False)
    fig.savefig(join(res_path, "rotor.png"))
    fig.savefig(join(res_path, "rotor.svg"), format="svg")

    # plt.show()
    # Check periodicity
    assert B.comp_periodicity_spatial() == (1, False)

    # Check machine in FEMM with sym
    simu = Simu1(name="test_FEMM_Mag_Key_2", machine=B)
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
        is_periodicity_a=True,
        is_periodicity_t=False,
        nb_worker=cpu_count(),
        # Kmesh_fineness=2,
    )
    simu.path_result = join(res_path, simu.name)

    # Run simulations
    out = simu.run()
    plt.close()
    return out


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_NotchKey_NoCut():
    """Validation of NotchKey in FEMM, No key on Ox axis"""
    res_path = join(save_path, "NotchKey_NoCut")
    if not isdir(res_path):
        makedirs(res_path)
    B = load(join(DATA_DIR, "Machine", "Benchmark.json"))
    M400 = load(join(DATA_DIR, "Material", "M400-50A.json"))
    M270 = load(join(DATA_DIR, "Material", "M270-35A.json"))
    B.name = "Benchmark_NotchKey_FEMM_NoCut"
    # Reduce magnet width
    B.rotor.slot.W1 /= 2
    B.rotor.slot.W0 /= 2
    # Add notches with keys
    B.rotor.notch = [
        NotchEvenDist(
            alpha=0,
            key_mat=None,  # No key on Ox, but a notch
            notch_shape=SlotM11(
                H1=0,
                H0=B.rotor.slot.H1 * 0.5,
                W1=0,
                W0=B.rotor.slot.W0,
                Zs=2,
                is_bore=True,
            ),
        ),
        NotchEvenDist(
            alpha=2 * pi / B.rotor.slot.Zs,
            key_mat=M400,
            notch_shape=SlotM11(
                H1=B.rotor.slot.H1 * 1.2,
                H0=0,
                W1=B.rotor.slot.W1,
                W0=B.rotor.slot.W0,
                Zs=2,
                is_bore=True,
            ),
        ),
    ]
    # Lamination on Ox for the Stator
    B.stator.notch = [
        NotchEvenDist(
            alpha=2 * pi / B.stator.slot.Zs,
            key_mat=M400,
            notch_shape=SlotM10(
                H1=4e-3,
                H0=3e-3,
                W1=5e-3,
                W0=5e-3,
                Zs=B.stator.slot.Zs // 2,
                is_bore=True,
            ),
        )
    ]
    # Check plot machine
    fig, ax = B.plot(
        save_path=join(res_path, "machine_full.png"),
        is_clean_plot=True,
        is_show_fig=False,
    )
    fig.savefig(join(res_path, "machine_full.png"))
    fig.savefig(join(res_path, "machine_full.svg"), format="svg")

    fig, ax = B.rotor.plot(is_add_arrow=True, is_show_fig=False)
    fig.savefig(join(res_path, "rotor.png"))
    fig.savefig(join(res_path, "rotor.svg"), format="svg")

    # Check periodicity
    assert B.comp_periodicity_spatial() == (1, True)

    # Check machine in FEMM with sym
    simu = Simu1(name="test_FEMM_Mag_Key_NoCut", machine=B)
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
        is_periodicity_a=True,
        is_periodicity_t=False,
        nb_worker=cpu_count(),
        # Kmesh_fineness=2,
    )
    simu.path_result = join(res_path, simu.name)

    # Same simu without symetry
    simu2 = simu.copy()
    simu2.name = simu.name + "_Full"
    simu2.path_result = join(res_path, simu2.name)
    simu2.mag.is_periodicity_a = False

    # Run simulations
    out = simu.run()
    out2 = simu2.run()

    out.mag.B.plot_2D_Data(
        "angle{°}",
        "time[0]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_space.png"),
        is_show_fig=False,
        **dict_2D
    )

    # Compare both simu
    Bflux = out.mag.B
    arg_list = ["angle"]
    result = Bflux.get_rphiz_along(*arg_list)
    Brad = result["radial"]
    angle = result["angle"]

    Bflux2 = out2.mag.B
    arg_list = ["angle"]
    result2 = Bflux2.get_rphiz_along(*arg_list)
    Brad2 = result2["radial"]

    assert_array_almost_equal(Brad, Brad2, decimal=1)
    plt.close()
    return out


# To run it without pytest
if __name__ == "__main__":
    out = test_FEMM_NotchKey_NoCut()
    out = test_FEMM_NotchKey_Airgap()
    out = test_FEMM_NotchKey_inner()
    out = test_FEMM_NotchKey_2()
    print("Done")

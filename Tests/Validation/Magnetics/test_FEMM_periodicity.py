from os import makedirs
from os.path import join, isdir
from multiprocessing import cpu_count

import pytest
from Tests import save_validation_path as save_path
import matplotlib.pyplot as plt
from numpy import exp, sqrt, pi, max as np_max
from numpy.testing import assert_array_almost_equal

from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.BoreUD import BoreUD
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.SlotCirc import SlotCirc
from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.Classes.SlotM18 import SlotM18
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.BoreFlower import BoreFlower
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D

from pyleecan.definitions import DATA_DIR


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
@pytest.mark.ForceMT
def test_FEMM_periodicity_time_no_periodicity_a():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    SPMSM_015 = load(join(DATA_DIR, "Machine", "SPMSM_015.json"))

    assert SPMSM_015.comp_periodicity_spatial() == (9, False)

    name = "test_FEMM_periodicity_time_no_periodicity_a"

    simu = Simu1(name=name + "_1", machine=SPMSM_015)

    # Definition of the enforced output of the electrical module
    I0_rms = 250 / sqrt(2)
    Phi0 = 140 * pi / 180  # Maximum Torque Per Amp

    Id_ref = (I0_rms * exp(1j * Phi0)).real
    Iq_ref = (I0_rms * exp(1j * Phi0)).imag

    simu.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=Id_ref, Iq_ref=Iq_ref),
        Na_tot=252 * 9,
        Nt_tot=4 * 9,
    )

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(
        type_BH_stator=1,
        type_BH_rotor=1,
        is_periodicity_a=False,
        is_periodicity_t=True,
        nb_worker=cpu_count(),
        # Kmesh_fineness=2,
    )
    simu.force = ForceMT()

    # Definition of the magnetic simulation: no periodicity
    simu2 = simu.copy()
    simu2.name = name + "_2"
    simu2.mag.is_periodicity_t = False

    # Run simulations
    out = simu.run()

    out2 = simu2.run()

    # Plot the result
    out.mag.B.plot_2D_Data(
        "time",
        "angle[0]{°}",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_time.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.mag.B.plot_2D_Data(
        "angle{°}",
        "time[1]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_space.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.force.AGSF.plot_2D_Data(
        "wavenumber=[0,100]",
        "time[0]",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_space_fft.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.force.AGSF.plot_2D_Data(
        "freqs",
        "angle[0]",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_fft2.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.mag.Tem.plot_2D_Data(
        "time",
        data_list=[out2.mag.Tem],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_Tem_time.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.mag.Phi_wind_stator.plot_2D_Data(
        "time",
        "phase[]",
        data_list=[out2.mag.Phi_wind_stator],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_Phi_wind_stator_time.png"),
        is_show_fig=False,
        **dict_2D
    )

    Bflux = out.mag.B
    arg_list = ["time"]
    result = Bflux.get_rphiz_along(*arg_list)
    Brad = result["radial"]
    time = result["time"]

    Bflux2 = out2.mag.B
    arg_list = ["time"]
    result2 = Bflux2.get_rphiz_along(*arg_list)
    Brad2 = result2["radial"]
    time2 = result2["time"]

    # Compare both simu
    assert_array_almost_equal((Brad - Brad2) / Brad2, 0, decimal=2)
    assert_array_almost_equal(time, time2, decimal=6)

    AGSF = out.force.AGSF
    arg_list = ["time"]
    result_AGSF = AGSF.get_rphiz_along(*arg_list)
    Prad = result_AGSF["radial"]
    time3 = result_AGSF["time"]

    AGSF2 = out2.force.AGSF
    arg_list = ["time"]
    result_AGSF2 = AGSF2.get_rphiz_along(*arg_list)
    Prad2 = result_AGSF2["radial"]
    time4 = result_AGSF2["time"]

    # Compare both simu
    assert_array_almost_equal((Prad - Prad2) / Prad2, 0, decimal=2)
    assert_array_almost_equal(time3, time4, decimal=6)

    return out, out2


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
@pytest.mark.ForceMT
def test_FEMM_periodicity_time():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    SPMSM_015 = load(join(DATA_DIR, "Machine", "SPMSM_015.json"))

    assert SPMSM_015.comp_periodicity_spatial() == (9, False)

    name = "test_FEMM_periodicity_time"

    simu = Simu1(name=name + "_1", machine=SPMSM_015)

    # Definition of the enforced output of the electrical module
    I0_rms = 250 / sqrt(2)
    Phi0 = 140 * pi / 180  # Maximum Torque Per Amp

    Id_ref = (I0_rms * exp(1j * Phi0)).real
    Iq_ref = (I0_rms * exp(1j * Phi0)).imag

    simu.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=Id_ref, Iq_ref=Iq_ref),
        Na_tot=252 * 9,
        Nt_tot=4 * 9,
    )

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(
        type_BH_stator=1,
        type_BH_rotor=1,
        is_periodicity_a=True,
        is_periodicity_t=True,
        nb_worker=cpu_count(),
        # Kmesh_fineness=2,
    )
    simu.force = ForceMT()

    # Definition of the magnetic simulation: no periodicity
    simu2 = simu.copy()
    simu2.name = name + "_2"
    simu2.mag.is_periodicity_t = False

    # Run simulations
    out = simu.run()

    out2 = simu2.run()

    # Plot the result
    out.mag.B.plot_2D_Data(
        "time",
        "angle[0]{°}",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_time.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.mag.B.plot_2D_Data(
        "angle{°}",
        "time[1]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_space.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.force.AGSF.plot_2D_Data(
        "wavenumber=[0,100]",
        "time[0]",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_space_fft.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.force.AGSF.plot_2D_Data(
        "freqs",
        "angle[0]",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_freqs.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.force.AGSF.plot_2D_Data(
        "time",
        "angle[0]",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_time.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.force.AGSF.plot_2D_Data(
        "angle",
        "time[0]",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_angle.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.mag.Tem.plot_2D_Data(
        "time",
        data_list=[out2.mag.Tem],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_Tem_time.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.mag.Phi_wind_stator.plot_2D_Data(
        "time",
        "phase[]",
        data_list=[out2.mag.Phi_wind_stator],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_Phi_wind_stator_time.png"),
        is_show_fig=False,
        **dict_2D
    )

    # Compare both simu with B
    Bflux = out.mag.B
    arg_list = ["time"]
    result = Bflux.get_rphiz_along(*arg_list)
    Brad = result["radial"]
    time = result["time"]

    # Check Flux spatio-temporal reconstruction full
    Bflux2 = out2.mag.B
    arg_list = ["time"]
    result2 = Bflux2.get_rphiz_along(*arg_list)
    Brad2 = result2["radial"]
    time = result2["time"]

    assert_array_almost_equal(Brad, Brad2, decimal=2)

    # Compare both simu with AGSF
    AGSF = out.force.AGSF
    arg_list = ["time"]
    result_AGSF = AGSF.get_rphiz_along(*arg_list)
    Prad = result_AGSF["radial"]
    time = result_AGSF["time"]

    AGSF2 = out2.force.AGSF
    arg_list = ["time"]
    result_AGSF2 = AGSF2.get_rphiz_along(*arg_list)
    Prad2 = result_AGSF2["radial"]
    time = result_AGSF2["time"]

    assert_array_almost_equal(Prad / 100000, Prad2 / 100000, decimal=2)

    return out, out2


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
@pytest.mark.ForceMT
def test_FEMM_periodicity_angle():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    SPMSM_015 = load(join(DATA_DIR, "Machine", "SPMSM_015.json"))
    # Add ventilation ducts on symmetry lines
    Hy = SPMSM_015.stator.comp_height_yoke()
    H1 = SPMSM_015.stator.comp_radius_mid_yoke() - Hy / 4
    H2 = SPMSM_015.stator.comp_radius_mid_yoke() + Hy / 4
    D0 = SPMSM_015.stator.comp_height_yoke() / 4
    Zh = SPMSM_015.stator.slot.Zs * 2
    SPMSM_015.stator.axial_vent = [
        VentilationCirc(
            Zh=Zh,
            Alpha0=0,
            D0=D0,
            H0=H1,
        ),
        VentilationCirc(Zh=Zh, D0=D0, H0=H2, Alpha0=2 * pi / Zh * 0.9),
    ]
    # Same on rotor
    Hy = SPMSM_015.rotor.comp_height_yoke()
    H1 = SPMSM_015.rotor.comp_radius_mid_yoke() - Hy / 4
    H2 = SPMSM_015.rotor.comp_radius_mid_yoke() + Hy / 4
    D0 = SPMSM_015.rotor.comp_height_yoke() / 6
    Zh = SPMSM_015.rotor.slot.Zs * 2
    SPMSM_015.rotor.axial_vent = [
        VentilationPolar(Zh=Zh, Alpha0=0, D0=D0, H0=H1, W1=pi / Zh * 0.5),
        VentilationPolar(
            Zh=Zh, D0=D0, H0=H2, Alpha0=2 * pi / Zh * 0.9, W1=pi / Zh * 0.5
        ),
    ]
    # Add notches on yoke and bore symetry lines
    Zs = SPMSM_015.stator.slot.Zs
    W0 = SPMSM_015.stator.slot.W0 * 0.7
    H0 = SPMSM_015.stator.slot.H0 * 0.8
    NBS = SlotCirc(Zs=Zs, W0=W0, H0=H0)
    SPMSM_015.stator.notch = [NotchEvenDist(alpha=0, notch_shape=NBS)]
    NYS = SlotM10(Zs=Zs, W0=W0, H0=H0,is_bore=False)
    # SPMSM_015.stator.notch.append(NotchEvenDist(alpha=0, notch_shape=NYS))

    Zr = SPMSM_015.rotor.slot.Zs
    W0 = SPMSM_015.stator.slot.W0 * 0.1
    H0 = SPMSM_015.rotor.comp_height_yoke() * 0.05
    NBR = SlotCirc(Zs=Zr, W0=W0, H0=H0)
    SPMSM_015.rotor.notch = [NotchEvenDist(alpha=0.001, notch_shape=NBR)]
    NYR = SlotM10(Zs=Zr, W0=W0, H0=H0,is_bore=False)
    # SPMSM_015.rotor.notch.append(NotchEvenDist(alpha=0, notch_shape=NYR))

    # fig, ax = SPMSM_015.plot(sym=3, is_clean_plot=True)
    # fig.savefig(join(save_path, "SPMSM_015_2.png"))
    # fig.savefig(join(save_path, "SPMSM_015_2.svg"), format="svg")
    # plt.show()

    assert SPMSM_015.comp_periodicity_spatial() == (9, False)

    simu = Simu1(name="test_FEMM_periodicity_angle", machine=SPMSM_015)

    # Definition of the enforced output of the electrical module
    I0_rms = 250 / sqrt(2)
    Phi0 = 140 * pi / 180  # Maximum Torque Per Amp

    Id_ref = (I0_rms * exp(1j * Phi0)).real
    Iq_ref = (I0_rms * exp(1j * Phi0)).imag

    simu.input = InputCurrent(
        OP=OPdq(N0=1000, Id_ref=Id_ref, Iq_ref=Iq_ref),
        Na_tot=252 * 9,
        Nt_tot=4 * 9,
    )

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(
        type_BH_stator=1,
        type_BH_rotor=1,
        is_periodicity_a=True,
        is_periodicity_t=True,
        nb_worker=cpu_count(),
        # Kmesh_fineness=2,
    )
    simu.force = ForceMT()

    # Definition of the magnetic simulation: no periodicity
    # Definition of the magnetic simulation: no periodicity
    simu2 = simu.copy()
    simu2.name = simu.name + "_Full"
    simu2.mag.is_periodicity_a = False

    simu2.force = ForceMT()

    # Run simulations
    out = simu.run()
    assert np_max(out.mag.B.components["radial"].values) == pytest.approx(4.82, rel=0.1)

    out2 = simu2.run()
    assert np_max(out2.mag.B.components["radial"].values) == pytest.approx(
        4.82, rel=0.1
    )

    # Plot the result
    out.mag.B.plot_2D_Data(
        "time",
        "angle[0]{°}",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_time.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.mag.B.plot_2D_Data(
        "angle{°}",
        "time[1]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_space.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.force.AGSF.plot_2D_Data(
        "wavenumber=[0,100]",
        "time[0]",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_space_fft.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.force.AGSF.plot_2D_Data(
        "freqs",
        "angle[0]",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_fft2.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.mag.Tem.plot_2D_Data(
        "time",
        data_list=[out2.mag.Tem],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_Tem_time.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.mag.Phi_wind_stator.plot_2D_Data(
        "time",
        "phase[]",
        data_list=[out2.mag.Phi_wind_stator],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_Phi_wind_stator_time.png"),
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

    return out, out2


def test_Bore_sym():
    """Check that angular periodicity can be applied on Bore shape"""
    res_path = join(save_path, "test_Bore_sym")
    if not isdir(res_path):
        makedirs(res_path)
    TP = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    # Add Bore shape with intersect method
    TP.rotor.bore = BoreFlower(
        N=8, Rarc=TP.rotor.Rext * 0.55, alpha=pi / 8, type_merge_slot=1
    )
    TP.stator.slot.H0 *= 4
    TP.stator.Rint *= 1.1
    TP.stator.Rext *= 1.05
    TP.rotor.hole[0].H1 *= 3
    # Generate "hexagonal Bore Radius"
    line_list = list()
    Rbo = TP.stator.Rint
    Zs = TP.stator.slot.Zs
    N = 6
    for ii in range(Zs // N):
        Z1 = Rbo * exp(1j * ii * 2 * pi / (Zs / N))
        Z2 = Rbo * exp(1j * (ii * 2 * pi / (Zs / N) + pi / (Zs / N)))
        Z3 = Rbo * exp(1j * (ii + 1) * 2 * pi / (Zs / N))
        line_list.append(Segment(begin=Z1, end=Z2))
        line_list.append(Segment(begin=Z2, end=Z3))
    # Use connect method for merge
    TP.stator.bore = BoreUD(line_list=line_list, sym=8, type_merge_slot=0)
    # fig, ax = TP.stator.plot(is_clean_plot=True, is_show_fig=False)
    # fig.savefig(join(save_path, "Hexa_Bore.png"))
    # fig.savefig(join(save_path, "Hexa_Bore.svg"), format="svg")
    # fig, ax = TP.stator.plot(sym=8, is_clean_plot=True, is_show_fig=False)
    # fig.savefig(join(save_path, "Hexa_Bore_sym.png"))
    # fig.savefig(join(save_path, "Hexa_Bore_sym.svg"), format="svg")
    # Add Notch to merge with the Bore shape (middle of pole)
    Zr = TP.rotor.hole[0].Zh
    W0 = TP.stator.slot.W0
    H0 = TP.stator.slot.H0 / 4
    NC = SlotCirc(Zs=Zr, W0=W0 * 5, H0=H0 * 5)
    NR = SlotM10(Zs=Zr, W0=W0 * 5, H0=H0 * 7.5)
    TP.rotor.notch = [
        NotchEvenDist(alpha=pi / 8, notch_shape=NC),
    ]

    fig, ax = TP.plot(sym=8, is_clean_plot=True, is_show_fig=False, save_path=join(res_path, "1_notch_sym.png"))
    # fig.savefig(join(save_path, "1_notch_sym.png"))
    # fig.savefig(join(save_path, "1_notch_sym.svg"), format="svg")
    fig, ax = TP.plot(is_show_fig=False, is_clean_plot=True)
    # fig.savefig(join(save_path, "1_notch_full.png"))
    # fig.savefig(join(save_path, "1_notch_full.svg"), format="svg")
    assert TP.comp_periodicity_spatial() == (4, True)

    # Add notch on sym line
    TP2 = TP.copy()
    TP2.rotor.notch.append(NotchEvenDist(alpha=0, notch_shape=NR))
    fig, ax = TP2.plot(sym=8, is_show_fig=False, is_clean_plot=True)
    # fig.savefig(join(save_path, "2_notch_sym.png"))
    # fig.savefig(join(save_path, "2_notch_sym.svg"), format="svg")
    fig, ax = TP2.plot(is_show_fig=False, is_clean_plot=True)
    # fig.savefig(join(save_path, "2_notch_full.png"))
    # fig.savefig(join(save_path, "2_notch_full.svg"), format="svg")
    fig, ax = TP2.rotor.plot(sym=4, is_show_fig=False, is_clean_plot=True, edgecolor="k")
    # fig.savefig(join(save_path, "2_notch_full_rotor.png"))
    # fig.savefig(join(save_path, "2_notch_full_rotor.svg"), format="svg")
    assert TP2.comp_periodicity_spatial() == (4, True)

    # Create all simulations
    simu = Simu1(name="test_FEMM_periodicity_angle_Bore", machine=TP)
    simu.path_result = join(res_path, simu.name)
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

    # Definition of the magnetic simulation: no periodicity
    simu2 = simu.copy()
    simu2.name = simu.name + "_Full"
    simu2.path_result = join(res_path, simu2.name)
    simu2.mag.is_periodicity_a = False

    simu3 = simu.copy()
    simu3.machine = TP2
    simu3.name = simu.name + "_2_notch"
    simu3.path_result = join(res_path, simu3.name)

    simu4 = simu.copy()
    simu4.machine = TP2
    simu4.name = simu.name + "_2_notch_Full"
    simu4.path_result = join(res_path, simu4.name)
    simu4.mag.is_periodicity_a = False

    # Run simulations
    out = simu.run()
    out2 = simu2.run()
    out3 = simu3.run()
    out4 = simu4.run()

    # Plot the result
    out.mag.B.plot_2D_Data(
        "angle{°}",
        "time[0]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(res_path, simu.name + "_B_space.png"),
        is_show_fig=False,
        **dict_2D
    )
    out3.mag.B.plot_2D_Data(
        "angle{°}",
        "time[0]",
        data_list=[out4.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(res_path, simu3.name + "_B_space.png"),
        is_show_fig=False,
        **dict_2D
    )

    # Compare simu
    Bflux = out.mag.B
    arg_list = ["angle"]
    result = Bflux.get_rphiz_along(*arg_list)
    Brad = result["radial"]

    Bflux2 = out2.mag.B
    arg_list = ["angle"]
    result2 = Bflux2.get_rphiz_along(*arg_list)
    Brad2 = result2["radial"]

    assert_array_almost_equal(Brad, Brad2, decimal=1)

    Bflux = out3.mag.B
    arg_list = ["angle"]
    result = Bflux.get_rphiz_along(*arg_list)
    Brad = result["radial"]

    Bflux2 = out4.mag.B
    arg_list = ["angle"]
    result2 = Bflux2.get_rphiz_along(*arg_list)
    Brad2 = result2["radial"]

    assert_array_almost_equal(Brad, Brad2, decimal=1)


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
@pytest.mark.ForceMT
def test_Ring_Magnet():
    """Check that a machine with Ring magnet can be simulated with sym"""
    machine = load(join(DATA_DIR, "Machine", "SPMSM_001.json"))
    machine.rotor.slot = SlotM18(init_dict=machine.rotor.slot.as_dict())
    simu = Simu1(name="test_FEMM_periodicity_RingMag", machine=machine)

    # Definition of the enforced output of the electrical module
    I0_rms = 250 / sqrt(2)
    Phi0 = 140 * pi / 180  # Maximum Torque Per Amp

    Id_ref = (I0_rms * exp(1j * Phi0)).real
    Iq_ref = (I0_rms * exp(1j * Phi0)).imag

    simu.input = InputCurrent(
        OP=OPdq(Id_ref=Id_ref, Iq_ref=Iq_ref, N0=1000),
        Na_tot=252 * 9,
        Nt_tot=8 * 3,
    )

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(
        type_BH_stator=1,
        type_BH_rotor=1,
        is_periodicity_a=False,
        is_periodicity_t=True,
        nb_worker=1,  # cpu_count(),
        # Kmesh_fineness=2,
    )
    simu.force = ForceMT()

    # Definition of the magnetic simulation: no periodicity
    simu2 = simu.copy()
    simu.name = simu.name + "_no_sym"
    simu2.name = simu2.name + "_sym"
    simu2.mag.is_periodicity_a = True

    # Run simulations
    out = simu.run()

    out2 = simu2.run()

    # Plot the result
    out.mag.B.plot_2D_Data(
        "time",
        "angle[0]{°}",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_time.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.mag.B.plot_2D_Data(
        "angle{°}",
        "time[1]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_space.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.mag.Tem.plot_2D_Data(
        "time",
        data_list=[out2.mag.Tem],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_Tem_time.png"),
        is_show_fig=False,
        **dict_2D
    )

    Bflux = out.mag.B
    arg_list = ["time"]
    result = Bflux.get_rphiz_along(*arg_list)
    Brad = result["radial"]
    time = result["time"]

    Bflux2 = out2.mag.B
    arg_list = ["time"]
    result2 = Bflux2.get_rphiz_along(*arg_list)
    Brad2 = result2["radial"]
    time2 = result2["time"]

    # Compare both simu
    assert_array_almost_equal((Brad - Brad2) / Brad2, 0, decimal=2)
    assert_array_almost_equal(time, time2, decimal=6)

    return out, out2


# To run it without pytest
if __name__ == "__main__":
    test_Bore_sym()
    out, out2 = test_FEMM_periodicity_angle()
    # out3, out4 = test_FEMM_periodicity_time()
    # out5, out6 = test_FEMM_periodicity_time_no_periodicity_a()
    # test_Ring_Magnet()
    print("Done")

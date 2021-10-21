from os.path import join
from multiprocessing import cpu_count

import pytest
from Tests import save_validation_path as save_path

from numpy import exp, sqrt, pi, max as np_max
from numpy.testing import assert_array_almost_equal

from pyleecan.Classes.Simu1 import Simu1
import matplotlib.pyplot as plt
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.SlotCirc import SlotCirc
from pyleecan.Classes.SlotM10 import SlotM10
from pyleecan.Classes.NotchEvenDist import NotchEvenDist
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Output import Output

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

    simu = Simu1(name="test_FEMM_periodicity_time_no_periodicity_a", machine=SPMSM_015)

    # Definition of the enforced output of the electrical module
    I0_rms = 250 / sqrt(2)
    Phi0 = 140 * pi / 180  # Maximum Torque Per Amp

    Id_ref = (I0_rms * exp(1j * Phi0)).real
    Iq_ref = (I0_rms * exp(1j * Phi0)).imag

    simu.input = InputCurrent(
        Id_ref=Id_ref,
        Iq_ref=Iq_ref,
        Na_tot=252 * 9,
        Nt_tot=4 * 9,
        N0=1000,
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
    simu2.mag.is_periodicity_t = False

    # Run simulations
    out = Output(simu=simu)
    simu.run()

    out2 = Output(simu=simu2)
    simu2.run()

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
        "phase",
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

    simu = Simu1(name="test_FEMM_periodicity_time", machine=SPMSM_015)

    # Definition of the enforced output of the electrical module
    I0_rms = 250 / sqrt(2)
    Phi0 = 140 * pi / 180  # Maximum Torque Per Amp

    Id_ref = (I0_rms * exp(1j * Phi0)).real
    Iq_ref = (I0_rms * exp(1j * Phi0)).imag

    simu.input = InputCurrent(
        Id_ref=Id_ref,
        Iq_ref=Iq_ref,
        Na_tot=252 * 9,
        Nt_tot=4 * 9,
        N0=1000,
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
    simu2.mag.is_periodicity_t = False

    # Run simulations
    out = Output(simu=simu)
    simu.run()

    out2 = Output(simu=simu2)
    simu2.run()

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
        "phase",
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

    assert_array_almost_equal(Prad / 1000, Prad2 / 1000, decimal=0)

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
    NYS = SlotM10(Zs=Zs, W0=W0, H0=H0)
    # SPMSM_015.stator.yoke_notch = [NotchEvenDist(alpha=0, notch_shape=NYS)]

    Zr = SPMSM_015.rotor.slot.Zs
    W0 = SPMSM_015.stator.slot.W0 * 0.1
    H0 = SPMSM_015.rotor.comp_height_yoke() * 0.05
    NBR = SlotCirc(Zs=Zr, W0=W0, H0=H0)
    SPMSM_015.rotor.notch = [NotchEvenDist(alpha=0.001, notch_shape=NBR)]
    NYR = SlotM10(Zs=Zr, W0=W0, H0=H0)
    # SPMSM_015.rotor.yoke_notch = [NotchEvenDist(alpha=0, notch_shape=NYR)]

    # SPMSM_015.plot(sym=3)
    # plt.show()

    simu = Simu1(name="test_FEMM_periodicity_angle", machine=SPMSM_015)

    # Definition of the enforced output of the electrical module
    I0_rms = 250 / sqrt(2)
    Phi0 = 140 * pi / 180  # Maximum Torque Per Amp

    Id_ref = (I0_rms * exp(1j * Phi0)).real
    Iq_ref = (I0_rms * exp(1j * Phi0)).imag

    simu.input = InputCurrent(
        Id_ref=Id_ref,
        Iq_ref=Iq_ref,
        Na_tot=252 * 9,
        Nt_tot=4 * 9,
        N0=1000,
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
    out = Output(simu=simu)
    simu.run()
    assert np_max(out.mag.B.components["radial"].values) == pytest.approx(3.95, rel=0.1)

    out2 = Output(simu=simu2)
    simu2.run()
    assert np_max(out2.mag.B.components["radial"].values) == pytest.approx(3.95, rel=0.1)

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
        "phase",
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


# To run it without pytest
if __name__ == "__main__":

    out, out2 = test_FEMM_periodicity_angle()
    # out3, out4 = test_FEMM_periodicity_time()
    # out5, out6 = test_FEMM_periodicity_time_no_periodicity_a()

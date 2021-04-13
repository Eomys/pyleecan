from os.path import join
from multiprocessing import cpu_count

import pytest
from Tests import save_validation_path as save_path

from numpy import exp, sqrt, pi, meshgrid, zeros, real
from numpy.testing import assert_array_almost_equal

from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.InputCurrent import InputCurrent

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Output import Output

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.definitions import DATA_DIR


@pytest.mark.long
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_periodicity_time_no_periodicity_a():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    SPMSM_015 = load(join(DATA_DIR, "Machine", "SPMSM_015.json"))

    assert SPMSM_015.comp_periodicity() == (9, False, 9, True)

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
        Kmesh_fineness=2,
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


@pytest.mark.long
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_periodicity_time():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    SPMSM_015 = load(join(DATA_DIR, "Machine", "SPMSM_015.json"))

    assert SPMSM_015.comp_periodicity() == (9, False, 9, True)

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
        Kmesh_fineness=2,
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


@pytest.mark.long
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_periodicity_angle():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    SPMSM_015 = load(join(DATA_DIR, "Machine", "SPMSM_015.json"))

    assert SPMSM_015.comp_periodicity() == (9, False, 9, True)

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
        is_periodicity_t=False,
        nb_worker=cpu_count(),
        Kmesh_fineness=2,
    )
    simu.force = ForceMT()

    # Definition of the magnetic simulation: no periodicity
    # Definition of the magnetic simulation: no periodicity
    simu2 = simu.copy()
    simu2.mag.is_periodicity_a = False

    simu2.force = ForceMT()

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
    out3, out4 = test_FEMM_periodicity_time()
    out5, out6 = test_FEMM_periodicity_time_no_periodicity_a()

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
from pyleecan.definitions import DATA_DIR


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
@pytest.mark.failed  # reason:  Arrays are not almost equal to 2 decimals 'test1_AGSF'
def test_FEMM_periodicity():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))

    assert IPMSM_A.comp_periodicity() == (4, True, 4, True)

    simu = Simu1(name="FEMM_periodicity", machine=IPMSM_A)

    # Definition of the enforced output of the electrical module
    I0_rms = 250 / sqrt(2)
    Phi0 = 140 * pi / 180  # Maximum Torque Per Amp

    Id_ref = (I0_rms * exp(1j * Phi0)).real
    Iq_ref = (I0_rms * exp(1j * Phi0)).imag

    simu.input = InputCurrent(
        Id_ref=Id_ref,
        Iq_ref=Iq_ref,
        Na_tot=252 * 8,
        Nt_tot=2 * 8,
        N0=1000,
    )

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(
        type_BH_stator=1,
        type_BH_rotor=1,
        is_periodicity_a=True,
        is_periodicity_t=True,
        nb_worker=cpu_count(),
    )
    simu.force = ForceMT(is_periodicity_a=True, is_periodicity_t=True)

    # Definition of the magnetic simulation: no periodicity
    simu2 = simu.copy()
    simu2.mag = MagFEMM(
        type_BH_stator=1,
        type_BH_rotor=1,
        is_periodicity_a=False,
        is_periodicity_t=False,
        nb_worker=cpu_count(),
    )
    simu2.force = ForceMT(is_periodicity_a=False, is_periodicity_t=False)

    # Run simulations
    out = Output(simu=simu)
    simu.run()

    out2 = Output(simu=simu2)
    simu2.run()

    # Plot the result
    out.plot_2D_Data(
        "mag.B",
        "time",
        "angle[0]{°}",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_time.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "mag.B",
        "angle",
        "time[0]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_space.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "mag.B",
        "wavenumber=[0,100]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_space_fft.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "force.AGSF",
        "time",
        "angle[0]{°}",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_time.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "force.AGSF",
        "angle",
        "time[0]",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_space.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "force.AGSF",
        "wavenumber=[0,100]",
        "time[0]",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_space_fft.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "mag.Tem",
        "time",
        data_list=[out2.mag.Tem],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_Tem_time.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "mag.Phi_wind_stator",
        "time",
        "phase",
        data_list=[out2.mag.Phi_wind_stator],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_Phi_wind_stator_time.png"),
        is_show_fig=False,
    )

    # Check Flux spatio-temporal reconstruction sym
    Bflux = out.mag.B
    arg_list = ["time", "angle"]
    result = Bflux.get_rphiz_along(*arg_list)
    Brad = result["radial"]
    time = result["time"]
    angle = result["angle"]
    Xangle, Xtime = meshgrid(angle, time)

    arg_list = ["freqs", "wavenumber"]
    result_freq = Bflux.get_rphiz_along(*arg_list)
    Brad_wr = result_freq["radial"]
    freqs = result_freq["freqs"]
    wavenumber = result_freq["wavenumber"]
    Nf = len(freqs)
    Nr = len(wavenumber)

    XB_rad = zeros(Brad.shape)

    for ir in range(Nr):
        r = wavenumber[ir]
        for ifrq in range(Nf):
            frq = freqs[ifrq]
            XB_rad = XB_rad + real(
                Brad_wr[ifrq, ir] * exp(1j * 2 * pi * frq * Xtime + 1j * r * Xangle)
            )

    test1 = abs(Brad - XB_rad) / abs(Brad).max()
    assert_array_almost_equal(test1, 0, decimal=2)
    assert_array_almost_equal(Brad, XB_rad, decimal=6)

    # Check Flux spatio-temporal reconstruction full
    Bflux2 = out2.mag.B
    arg_list = ["time", "angle"]
    result2 = Bflux2.get_rphiz_along(*arg_list)
    Brad2 = result2["radial"]
    time = result2["time"]
    angle = result2["angle"]
    Xangle, Xtime = meshgrid(angle, time)

    arg_list = ["freqs", "wavenumber"]
    result_freq2 = Bflux2.get_rphiz_along(*arg_list)
    Brad_wr2 = result_freq2["radial"]
    freqs = result_freq2["freqs"]
    wavenumber = result_freq2["wavenumber"]
    Nf = len(freqs)
    Nr = len(wavenumber)

    XB_rad2 = zeros(Brad2.shape)

    for ir in range(Nr):
        r = wavenumber[ir]
        for ifrq in range(Nf):
            frq = freqs[ifrq]
            XB_rad2 = XB_rad2 + real(
                Brad_wr2[ifrq, ir] * exp(1j * 2 * pi * frq * Xtime + 1j * r * Xangle)
            )

    test2 = abs(Brad2 - XB_rad2) / abs(Brad2).max()
    assert_array_almost_equal(test2, 0, decimal=2)
    assert_array_almost_equal(Brad2, XB_rad2, decimal=2)

    # Compare both simu
    test11 = abs(Brad - Brad2) / abs(Brad).max()
    assert_array_almost_equal(test11, 0, decimal=1)

    test22 = abs(XB_rad - XB_rad2) / abs(Brad).max()
    assert_array_almost_equal(test22, 0, decimal=1)

    # Check AGSF spatio-temporal reconstruction sym
    AGSF = out.force.AGSF
    arg_list = ["time", "angle"]
    result_AGSF = AGSF.get_rphiz_along(*arg_list)
    Prad = result_AGSF["radial"]
    time = result_AGSF["time"]
    angle = result_AGSF["angle"]
    Xangle, Xtime = meshgrid(angle, time)

    arg_list = ["freqs", "wavenumber"]
    result_freq_agsf = AGSF.get_rphiz_along(*arg_list)
    Prad_wr = result_freq_agsf["radial"]
    freqs = result_freq_agsf["freqs"]
    wavenumber = result_freq_agsf["wavenumber"]
    Nf = len(freqs)
    Nr = len(wavenumber)

    XP_rad = zeros(Prad.shape)

    for ir in range(Nr):
        r = wavenumber[ir]
        for ifrq in range(Nf):
            frq = freqs[ifrq]
            XP_rad = XP_rad + real(
                Prad_wr[ifrq, ir] * exp(1j * 2 * pi * frq * Xtime + 1j * r * Xangle)
            )

    test1_AGSF = abs(Prad - XP_rad) / abs(Prad).max()
    assert_array_almost_equal(test1_AGSF, 0, decimal=2)

    # Check AGSF spatio-temporal reconstruction full
    AGSF2 = out2.force.AGSF
    arg_list = ["time", "angle"]
    result_AGSF2 = AGSF2.get_rphiz_along(*arg_list)
    Prad2 = result_AGSF2["radial"]
    time = result_AGSF2["time"]
    angle = result_AGSF2["angle"]
    Xangle, Xtime = meshgrid(angle, time)

    arg_list = ["freqs", "wavenumber"]
    result_freq_agsf2 = AGSF2.get_rphiz_along(*arg_list)
    Prad_wr2 = result_freq_agsf2["radial"]
    freqs = result_freq_agsf2["freqs"]
    wavenumber = result_freq_agsf2["wavenumber"]
    Nf = len(freqs)
    Nr = len(wavenumber)

    XP_rad2 = zeros(Prad2.shape)

    for ir in range(Nr):
        r = wavenumber[ir]
        for ifrq in range(Nf):
            frq = freqs[ifrq]
            XP_rad2 = XP_rad2 + real(
                Prad_wr2[ifrq, ir] * exp(1j * 2 * pi * frq * Xtime + 1j * r * Xangle)
            )

    test2_AGSF = abs(Prad2 - XP_rad2) / abs(Prad2).mean()
    assert_array_almost_equal(test2_AGSF, 0, decimal=2)

    # Reconstrcution results should be the same
    test3_AGSF = abs(XP_rad - XP_rad2) / abs(XP_rad2).mean()
    assert_array_almost_equal(test3_AGSF, 0, decimal=1)

    return out, out2


# To run it without pytest
if __name__ == "__main__":

    out, out2 = test_FEMM_periodicity()

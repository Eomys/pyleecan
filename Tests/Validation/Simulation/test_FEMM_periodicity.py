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
def test_FEMM_periodicity_time_no_periodicity_a():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))

    assert IPMSM_A.comp_periodicity() == (4, True, 4, True)

    simu = Simu1(name="FEMM_periodicity_time", machine=IPMSM_A)

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
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=False,
        is_periodicity_t=True,
        nb_worker=cpu_count(),
        Kmesh_fineness=2,
    )
    simu.force = ForceMT()

    # Definition of the magnetic simulation: no periodicity
    simu2 = simu.copy()
    simu2.mag.is_periodicity_t=False

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
        "force.AGSF",
        "time",
        "angle[0]{°}",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_time.png"),
        is_show_fig=False,
    )
    
    out.plot_2D_Data(
        "mag.B",
        "freqs",
        "angle[0]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_fft2.png"),
        is_show_fig=False,
    )
    
    out.plot_2D_Data(
        "force.AGSF",
        "freqs",
        "angle[0]",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_fft2.png"),
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
    assert_array_almost_equal(Brad, Brad2, decimal=6)
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
    assert_array_almost_equal(Prad, Prad2, decimal=4)
    assert_array_almost_equal(time3, time4, decimal=6)
    
    return out, out2


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_FEMM_periodicity_time():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))

    assert IPMSM_A.comp_periodicity() == (4, True, 4, True)

    simu = Simu1(name="FEMM_periodicity_time", machine=IPMSM_A)

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
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=True,
        is_periodicity_t=True,
        nb_worker=cpu_count(),
        Kmesh_fineness=2,
    )
    simu.force = ForceMT()

    # Definition of the magnetic simulation: no periodicity
    simu2 = simu.copy()
    simu2.mag.is_periodicity_t=False

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
        "force.AGSF",
        "time",
        "angle[0]{°}",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_time.png"),
        is_show_fig=False,
    )
    
    out.plot_2D_Data(
        "mag.B",
        "freqs",
        "angle[0]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_fft2.png"),
        is_show_fig=False,
    )
    
    out.plot_2D_Data(
        "force.AGSF",
        "freqs",
        "angle[0]",
        data_list=[out2.force.AGSF],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_fft2.png"),
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

    # The second part of the test is to check that the SciDataTool objects work correctly.
    # Check Flux spatio-temporal reconstruction sym
    Bflux = out.mag.B
    arg_list = ["time"]
    result = Bflux.get_rphiz_along(*arg_list)
    Brad = result["radial"]
    time = result["time"]

    arg_list = ["freqs"]
    result_freq = Bflux.get_rphiz_along(*arg_list)
    Brad_wr = result_freq["radial"]
    freqs = result_freq["freqs"]
    Nf = len(freqs)

    XB_rad = zeros(Brad.shape)

    for ifrq in range(Nf):
        frq = freqs[ifrq]
        XB_rad = XB_rad + real(
            Brad_wr[ifrq] * exp(1j * 2 * pi * frq * time)
        )

    assert_array_almost_equal(Brad, XB_rad, decimal=6)

    # Check Flux spatio-temporal reconstruction full
    Bflux2 = out2.mag.B
    arg_list = ["time"]
    result2 = Bflux2.get_rphiz_along(*arg_list)
    Brad2 = result2["radial"]
    time = result2["time"]

    arg_list = ["freqs"]
    result_freq2 = Bflux2.get_rphiz_along(*arg_list)
    Brad_wr2 = result_freq2["radial"]
    freqs = result_freq2["freqs"]
    Nf = len(freqs)

    XB_rad2 = zeros(Brad2.shape)

    for ifrq in range(Nf):
        frq = freqs[ifrq]
        XB_rad2 = XB_rad2 + real(
            Brad_wr2[ifrq] * exp(1j * 2 * pi * frq * time)
        )

    assert_array_almost_equal(Brad2, XB_rad2, decimal=6)

    # Compare both simu
    assert_array_almost_equal(Brad, Brad2, decimal=6)

    # Check AGSF spatio-temporal reconstruction sym
    AGSF = out.force.AGSF
    arg_list = ["time"]
    result_AGSF = AGSF.get_rphiz_along(*arg_list)
    Prad = result_AGSF["radial"]
    time = result_AGSF["time"]

    arg_list = ["freqs"]
    result_freq_agsf = AGSF.get_rphiz_along(*arg_list)
    Prad_wr = result_freq_agsf["radial"]
    freqs = result_freq_agsf["freqs"]

    Nf = len(freqs)

    XP_rad = zeros(Prad.shape)

    for ifrq in range(Nf):
        frq = freqs[ifrq]
        XP_rad = XP_rad + real(
            Prad_wr[ifrq] * exp(1j * 2 * pi * frq * time)
        )

    assert_array_almost_equal(Prad, XP_rad, decimal=4)

    # Check AGSF spatio-temporal reconstruction full
    AGSF2 = out2.force.AGSF
    arg_list = ["time"]
    result_AGSF2 = AGSF2.get_rphiz_along(*arg_list)
    Prad2 = result_AGSF2["radial"]
    time = result_AGSF2["time"]

    arg_list = ["freqs"]
    result_freq_agsf2 = AGSF2.get_rphiz_along(*arg_list)
    Prad_wr2 = result_freq_agsf2["radial"]
    freqs = result_freq_agsf2["freqs"]
    Nf = len(freqs)

    XP_rad2 = zeros(Prad2.shape)

    for ifrq in range(Nf):
        frq = freqs[ifrq]
        XP_rad2 = XP_rad2 + real(
            Prad_wr2[ifrq] * exp(1j * 2 * pi * frq * time)
        )

    assert_array_almost_equal(Prad2, XP_rad2, decimal=4)
    
    # Compare both simu
    assert_array_almost_equal(Prad, Prad2, decimal=4)

    return out, out2

@pytest.mark.validation
@pytest.mark.FEMM
def test_FEMM_periodicity_angle():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))

    assert IPMSM_A.comp_periodicity() == (4, True, 4, True)

    simu = Simu1(name="FEMM_periodicity_angle", machine=IPMSM_A)

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
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=True,
        is_periodicity_t=False,
        nb_worker=cpu_count(),
        Kmesh_fineness=2,
    )
    simu.force = ForceMT()

    # Definition of the magnetic simulation: no periodicity
    simu2 = simu.copy()
    simu2.mag = MagFEMM(
        type_BH_stator=1,
        type_BH_rotor=1,
        is_periodicity_a=False,
        is_periodicity_t=False,
        nb_worker=cpu_count(),
    )
    simu2.force = ForceMT()

    # Run simulations
    out = Output(simu=simu)
    simu.run()

    out2 = Output(simu=simu2)
    simu2.run()

    # Plot the result
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

    # Check Flux spatio-temporal reconstruction sym
    Bflux = out.mag.B
    arg_list = ["angle"]
    result = Bflux.get_rphiz_along(*arg_list)
    Brad = result["radial"]
    angle = result["angle"]

    arg_list = ["wavenumber"]
    result_freq = Bflux.get_rphiz_along(*arg_list)
    Brad_wr = result_freq["radial"]
    wavenumber = result_freq["wavenumber"]
    Nr = len(wavenumber)

    XB_rad = zeros(Brad.shape)

    for ir in range(Nr):
        r = wavenumber[ir]
        XB_rad = XB_rad + real(
            Brad_wr[ir] * exp(1j * r * angle)
        )

    assert_array_almost_equal(Brad, XB_rad, decimal=6)

    return out, out2

# To run it without pytest
if __name__ == "__main__":
    
    out, out2 = test_FEMM_periodicity_angle()
    
    out3, out4 = test_FEMM_periodicity_time()
    
    #out5, out6 = test_FEMM_periodicity_time_no_periodicity_a()
    
    
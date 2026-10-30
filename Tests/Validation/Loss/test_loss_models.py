import numpy as np
import pytest
from SciDataTool.Classes.Data1D import Data1D
from SciDataTool.Classes.DataLinspace import DataLinspace
from SciDataTool.Classes.DataTime import DataTime
from SciDataTool.Classes.VectorField import VectorField

from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.LossModelBertotti import LossModelBertotti
from pyleecan.Classes.LossModelSteinmetz import LossModelSteinmetz
from pyleecan.Classes.Material import Material
from pyleecan.Classes.MatMagnetics import MatMagnetics

BERTOTTI_PARAMETERS = {
    "k_hy": 0.25,
    "k_ed": 0.08,
    "k_ex": 0.12,
    "alpha_B": 1.7,
}

PARAMETERS = {
    "k_hy": 0.25,
    "k_ed": 0.08,
    "alpha_f": 1.3,
    "alpha_B": 1.7,
}


def make_bertotti_material(parameters=BERTOTTI_PARAMETERS):
    freq, flux_density = np.meshgrid(
        np.linspace(1.0, 8.0, 8),
        np.linspace(0.15, 0.95, 9),
    )
    loss_density = (
        parameters["k_hy"] * freq * flux_density ** parameters["alpha_B"]
        + parameters["k_ed"] * (freq * flux_density) ** 2
        + parameters["k_ex"] * (freq * flux_density) ** 1.5
    )
    loss_data = np.vstack((freq.ravel(), flux_density.ravel(), loss_density.ravel()))

    return Material(mag=MatMagnetics(LossData=ImportMatrixVal(value=loss_data)))


def make_material(parameters=PARAMETERS):
    freq, flux_density = np.meshgrid(
        np.linspace(1.0, 8.0, 8),
        np.linspace(0.15, 0.95, 9),
    )
    loss_density = (
        parameters["k_hy"]
        * freq ** parameters["alpha_f"]
        * flux_density ** parameters["alpha_B"]
        + parameters["k_ed"] * (freq * flux_density) ** 2
    )
    loss_data = np.vstack((freq.ravel(), flux_density.ravel(), loss_density.ravel()))

    return Material(mag=MatMagnetics(LossData=ImportMatrixVal(value=loss_data)))


def test_comp_coeff_fits_all_parameters():
    model = LossModelSteinmetz()

    material = make_material()

    model.comp_coeff(material)

    model.plot_fitting(material, is_show_fig=False)

    for parameter, expected in PARAMETERS.items():
        assert getattr(model, parameter) == pytest.approx(expected, rel=1e-4)


@pytest.mark.parametrize("fixed_parameter", PARAMETERS)
def test_comp_coeff_preserves_enforced_parameter(fixed_parameter):
    fixed_value = PARAMETERS[fixed_parameter] * 1.3
    parameters = {**PARAMETERS, fixed_parameter: fixed_value}
    model = LossModelSteinmetz(**{fixed_parameter: fixed_value})

    material = make_material(parameters)

    model.comp_coeff(material)

    model.plot_fitting(material, is_show_fig=False)

    assert getattr(model, fixed_parameter) == fixed_value


def test_bertotti_comp_coeff_fits_all_parameters():
    model = LossModelBertotti()

    material = make_bertotti_material()

    model.comp_coeff(material)

    model.plot_fitting(material, is_show_fig=False)

    for parameter, expected in BERTOTTI_PARAMETERS.items():
        assert getattr(model, parameter) == pytest.approx(expected, rel=1e-4)


@pytest.mark.parametrize("fixed_parameter", BERTOTTI_PARAMETERS)
def test_bertotti_comp_coeff_preserves_enforced_parameter(fixed_parameter):
    fixed_value = BERTOTTI_PARAMETERS[fixed_parameter] * 1.3
    parameters = {**BERTOTTI_PARAMETERS, fixed_parameter: fixed_value}
    model = LossModelBertotti(**{fixed_parameter: fixed_value})

    material = make_bertotti_material(parameters)

    model.comp_coeff(material)

    model.plot_fitting(material, is_show_fig=False)

    assert getattr(model, fixed_parameter) == fixed_value


def test_comp_core_loss_freq_time():

    Nt = 1000
    Nelem = 1
    freqs_0 = np.array([1, 5, 7, 11])
    B_amp = np.zeros(freqs_0.shape, dtype=float)
    B_amp = 1 / (freqs_0) ** 2
    B_phase = np.zeros(freqs_0.shape, dtype=float)
    # B_phase = 1 / freqs_0

    field = np.zeros((Nt, Nelem, 2), dtype=float)
    Time = DataLinspace(
        name="time",
        unit="s",
        initial=0,
        final=1,
        number=Nt,
        include_endpoint=False,
    )
    Indice = Data1D(values=np.arange(Nelem), name="indice", is_components=True)

    time = Time.get_values()

    for f, B, phase in zip(freqs_0, B_amp, B_phase):
        if f == 0:
            coeff = 1
        else:
            coeff = np.sqrt(2)

        # B_x component
        field[:, :, 0] += B / coeff * np.cos(2 * np.pi * f * time)[:, None]
        # B_y component
        field[:, :, 1] += B / coeff * np.sin(2 * np.pi * f * time)[:, None]

    symbol = "B"
    unit = "T"
    name = "Magnetic flux density"
    axis_list = [Time, Indice]

    components = {}

    x_data = DataTime(
        name=name,
        unit=unit,
        symbol=symbol + "x",
        axes=axis_list,
        values=field[:, :, 0],
        is_real=True,
    )
    components["comp_x"] = x_data

    y_data = DataTime(
        name=name,
        unit=unit,
        symbol=symbol + "y",
        axes=axis_list,
        values=field[:, :, 1],
        is_real=True,
    )
    components["comp_y"] = y_data

    Bvect = VectorField(name=name, symbol=symbol, components=components)
    dB_dt_v = Bvect.get_vectorfield_along("time=derivate", "indice")

    Bval = Bvect.get_xyz_along("time", "indice", is_squeeze=False)
    Bfft = Bvect.get_xyz_along("freqs", "indice", is_squeeze=False)
    freqs = Bfft["freqs"]

    # Check input harmonics
    for f, B, phase in zip(freqs_0, B_amp, B_phase):
        Bx_fft_ii = Bfft["comp_x"][freqs == f, 0]
        # B_fft_ii = Bfft["comp_x"][freqs == f, 0]

        if f == 0:
            coeff = 1
        else:
            coeff = np.sqrt(2)

        assert pytest.approx(Bx_fft_ii - B / coeff * np.exp(1j * phase), rel=1e-2) == 0

    Bfft_square = np.abs(Bfft["comp_x"]) ** 2 + np.abs(Bfft["comp_y"]) ** 2

    dB_dt = dB_dt_v.get_xyz_along("time", "indice", is_squeeze=False)

    dB_dt_square = dB_dt["comp_x"] ** 2 + dB_dt["comp_y"] ** 2

    # np.testing.assert_array_almost_equal(B_amp, Bfft["comp_x"][1:, 0])

    P_ec = freqs[:, None] ** 2 * Bfft_square

    P_ec1 = freqs_0**2 * B_amp**2

    P_ec2 = 1 / (2 * np.pi**2) * dB_dt_square

    P_ec.sum(), P_ec1.sum(), P_ec2.mean()

    assert pytest.approx(np.abs(P_ec.sum() - P_ec1.sum()), rel=1e-2) == 0
    assert pytest.approx(np.abs(P_ec.sum() - P_ec2.mean()), abs=1e-1) == 0

    P_ex = freqs[:, None] ** 1.5 * Bfft_square**0.75

    P_ex1 = freqs_0**1.5 * B_amp ** (2 * 0.75)

    P_ex2 = 1 / 8.763363 * dB_dt_square**0.75

    P_ex.sum(), P_ex1.sum(), P_ex2.mean()

    assert pytest.approx(np.abs(P_ex.sum() - P_ex1.sum()), rel=1e-2) == 0
    # assert pytest.approx(np.abs(P_ex.sum() - P_ex2.mean()), rel=1e-2) == 0

    alpha_B = 2.5

    P_hys = freqs[:, None] * Bfft_square ** (alpha_B / 2)

    P_hys1 = freqs_0 * B_amp**alpha_B

    P_hys2 = (
        np.abs(Bval["comp_x"] * dB_dt["comp_x"])
        + np.abs(Bval["comp_y"] * dB_dt["comp_y"])
    ) / np.pi

    P_hys.sum(), P_hys1.sum(), P_hys2.mean()

    assert pytest.approx(np.abs(P_hys.sum() - P_hys1.sum()), rel=1e-2) == 0
    # assert pytest.approx(np.abs(P_hys.sum() - P_hys2.mean()), rel=1e-2) == 0


def test_comp_magnet_loss_freq_time():

    Nt = 1000
    Nelem = 11
    freqs_0 = np.array([0, 6, 12])  # np.arange(0, Nt / 2 + 1)
    Az_amp = np.ones(freqs_0.shape, dtype=float)
    Az_amp[1:] = 1 / freqs_0[1:]
    Az_phase = np.zeros(freqs_0.shape, dtype=float)
    Se_mag = 1e-6 * np.ones(Nelem, dtype=float)
    sigma_m = 5e5
    kseg = 1

    potential = np.zeros((Nt, Nelem), dtype=float)
    Time = DataLinspace(
        name="time",
        unit="s",
        initial=0,
        final=1,
        number=Nt,
        include_endpoint=False,
    )
    Indice = Data1D(values=np.arange(Nelem), name="indice", is_components=True)

    time = Time.get_values()

    for f, Az, phase in zip(freqs_0, Az_amp, Az_phase):
        if f == 0:
            coeff = 1
        else:
            coeff = np.sqrt(2)
        # A_z component
        potential += Az / coeff * np.cos(2 * np.pi * f * time + phase)[:, None]

    # Take opposite potential on half on the elements
    potential[:, int(np.round(Nelem / 2)) :] *= -1

    symbol = "Az_{elem}"
    unit = "Wb/m"
    name = "Magnetic vector potential"
    axis_list = [Time, Indice]

    Az_dt = DataTime(
        name=name,
        unit=unit,
        symbol=symbol,
        axes=axis_list,
        values=potential,
        is_real=True,
    )

    # Compute magnetic vector potential fft
    Az_df = Az_dt.get_along("freqs", "indice", is_squeeze=False)
    Az_fft = Az_df[symbol]
    freqs = Az_df["freqs"]

    # Compute magnetic vector potential derivative over time
    dAz_dt = Az_dt.get_data_along("time=derivate", "indice")
    dAz_dt_val = dAz_dt.get_along("time[smallestperiod]", "indice")[dAz_dt.symbol]

    # Check input harmonics
    for f, Az, phase in zip(freqs_0, Az_amp, Az_phase):
        Az_fft_ii = Az_fft[freqs == f, 0]

        if f == 0:
            coeff = 1
        else:
            coeff = np.sqrt(2)

        assert pytest.approx(Az_fft_ii - Az / coeff * np.exp(1j * phase), rel=1e-6) == 0

    w = 2 * np.pi * freqs[:, None]
    Az_mean = np.matmul(Az_fft, Se_mag)[:, None] / np.sum(Se_mag)
    Jm_fft = -1j * sigma_m * w * (Az_fft - Az_mean)
    Pdensity = 0.5 * kseg * np.abs(Jm_fft) ** 2 / sigma_m
    Pmag = np.matmul(Pdensity.sum(axis=0), Se_mag)

    # Calculate eddy-current current density in this magnet
    Jm1 = -sigma_m * dAz_dt_val
    # Ensure average current flowing through the surface is 0
    Jc1 = np.matmul(Jm1, Se_mag)[:, None] / Se_mag.sum()
    Jm1 -= Jc1
    # Calculate Joule loss density due to eddy-current
    Pdensity1 = kseg * Jm1**2 / sigma_m
    Pmag1 = np.matmul(Pdensity1.mean(axis=0), Se_mag)

    assert pytest.approx(Pmag - Pmag1, abs=0.5) == 0


# To run it without pytest
if __name__ == "__main__":
    test_comp_core_loss_freq_time()

    test_comp_magnet_loss_freq_time()

    print("Done")

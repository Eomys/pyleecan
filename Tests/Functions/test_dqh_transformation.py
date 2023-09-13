import pytest

from numpy import pi, array, linspace, zeros, cos, mean, sqrt, sin
from numpy.testing import assert_array_almost_equal

from SciDataTool import DataTime, Data1D, Norm_ref

from pyleecan.Functions.Electrical.dqh_transformation import (
    n2dqh,
    dqh2n,
    n2dqh_DataTime,
    dqh2n_DataTime,
    get_phase_dir,
    get_phase_dir_DataTime,
)
from pyleecan.Functions.Winding.gen_phase_list import gen_name

param_list = [
    {"qs": 3, "current_dir": -1, "phase_dir": -1},  # pyleecan convention, 3 phases
    {"qs": 3, "current_dir": 1, "phase_dir": 1},  # other convention, 3 phases
    {"qs": 3, "current_dir": 1, "phase_dir": -1},  # other convention, 3 phases
    {"qs": 6, "current_dir": -1, "phase_dir": -1},  # pyleecan convention, 6 phases
    {"qs": 11, "current_dir": -1, "phase_dir": -1},  # pyleecan convention, 11 phases
]

is_show_fig = False


@pytest.mark.parametrize("param_dict", param_list)
def test_dqh_transformation(param_dict):
    """Check that the dqh transformations can return a correct output"""

    Nt = 100
    f_elec = 1  # assume unit frequency

    # Get parameters for current test case
    qs = param_dict["qs"]
    current_dir = param_dict["current_dir"]  # current direction
    phase_dir = param_dict["phase_dir"]  # phase direction

    # Define time and electrical angle arrays
    time = linspace(0, 1 / f_elec, Nt, endpoint=False)
    angle_elec = current_dir * 2 * pi * f_elec * time

    # Time axis for plots including angle_elec normalization used for DQH (cf Input.comp_axis_time())
    norm_time = {"angle_elec": Norm_ref(ref=current_dir / (2 * pi * f_elec))}
    Time = Data1D(name="time", unit="s", values=time, normalizations=norm_time)

    # Check that values stored in Time data object agrees with initial values
    angle_elec_bis = Time.get_values(is_smallestperiod=True, normalization="angle_elec")
    assert_array_almost_equal(angle_elec, angle_elec_bis)

    # Phase axis for plots
    Phase = Data1D(
        name="phase",
        unit="",
        values=gen_name(qs),
        is_components=True,
    )

    # Calculate dqh transform for several current angles
    angle_curr_list = array([0, 45, 90, 180, 270]) * pi / 180
    for angle_curr in angle_curr_list:
        In = zeros((Nt, qs))
        for ii in range(qs):
            # current dir is included in angle_elec while phase_dir is related
            # to the one enforced in Clarke transform
            In[:, ii] = cos(angle_elec + angle_curr + phase_dir * 2 * ii * pi / qs)

        # check Idqh calculated with RMS convention (pyleecan convention)
        Idqh_rms = n2dqh(In, angle_elec, is_dqh_rms=True, phase_dir=phase_dir)
        assert_array_almost_equal(
            mean(Idqh_rms, axis=0),
            array([cos(angle_curr) / sqrt(2), sin(angle_curr) / sqrt(2), 0]),
        )

        # check Idqh calculated with peak convention (other convention)
        Idqh_peak = n2dqh(In, angle_elec, is_dqh_rms=False, phase_dir=phase_dir)
        assert_array_almost_equal(Idqh_rms * sqrt(2), Idqh_peak)

        # check In calculated from Idqh with rms convention (pyleecan convention)
        In_rms = dqh2n(Idqh_rms, angle_elec, n=qs, is_n_rms=False, phase_dir=phase_dir)
        assert_array_almost_equal(In, In_rms)

        # check In calculated from Idqh with peak convention (other convention)
        In_peak = dqh2n(Idqh_peak, angle_elec, n=qs, is_n_rms=True, phase_dir=phase_dir)
        assert_array_almost_equal(In, In_peak)

        # Test calculation dqh transform directly applied to DataND objects
        In_data = DataTime(
            name="Stator current",
            unit="A",
            symbol="I_s",
            axes=[Time, Phase],
            values=In,
        )
        I_dqh_data = n2dqh_DataTime(In_data, phase_dir=phase_dir)
        assert_array_almost_equal(I_dqh_data.values, Idqh_rms)
        In_data1 = dqh2n_DataTime(I_dqh_data, n=qs, phase_dir=phase_dir)
        assert_array_almost_equal(In_data1.values, In_rms)

        # Check phase_dir calculation
        phase_dir_calc1 = get_phase_dir(In, current_dir)
        phase_dir_calc2 = get_phase_dir_DataTime(In_data)
        assert phase_dir_calc1 == phase_dir
        assert phase_dir_calc2 == phase_dir

        if is_show_fig:
            In_data.plot_2D_Data("time", "phase[]")
            I_dqh_data.plot_2D_Data("time", "phase[]")

    pass


if __name__ == "__main__":
    for param_dict in param_list:
        test_dqh_transformation(param_dict)

    # test_dqh_transformation(param_list[1])

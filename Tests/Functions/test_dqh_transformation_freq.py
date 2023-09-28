import pytest

from numpy import pi, array, linspace, zeros, cos, exp, abs as np_abs, angle
from numpy.testing import assert_array_almost_equal

from SciDataTool import DataTime, Data1D, Norm_ref

from pyleecan.Functions.Electrical.dqh_transformation import n2dqh_DataTime
from pyleecan.Functions.Electrical.dqh_transformation_freq import (
    n2dqh_DataFreq,
    dqh2n_DataFreq,
    get_phase_dir,
    get_phase_dir_DataFreq,
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
def test_dqh_transformation_freq(param_dict):
    """Check that the dqh transformations can return a correct output"""

    Nt = 500
    felec = 1  # assume unit frequency
    angle_curr = 0  # pi / 2

    # Get parameters for current test case
    qs = param_dict["qs"]
    current_dir = param_dict["current_dir"]  # current direction
    phase_dir = param_dict["phase_dir"]  # phase direction

    # Define time and electrical angle arrays
    time = linspace(0, 1 / felec, Nt, endpoint=False)
    angle_elec = current_dir * 2 * pi * felec * time

    # Time axis for plots including angle_elec normalization used for DQH (cf Input.comp_axis_time())
    norm_time = {"angle_elec": Norm_ref(ref=current_dir / (2 * pi * felec))}
    Time = Data1D(name="time", unit="s", values=time, normalizations=norm_time)

    # Phase axis for plots
    Phase = Data1D(name="phase", unit="", values=gen_name(qs), is_components=True)

    A_harm = array(
        [
            1 * exp(1j * angle_curr),
            0.1 * exp(1j * pi / 3),
            0.2 * exp(1j * pi / 8),
            1j * 0.05,
            0.15,
        ],
        dtype=complex,
    )
    order_harm = array([1, -5, 7, -11, 13])

    In = zeros((Nt, qs))
    for ii in range(qs):
        # current dir is included in angle_elec while phase_dir is related
        # to the one enforced in Clarke transform
        for A, order in zip(A_harm, order_harm):
            In[:, ii] += abs(A) * cos(
                order * angle_elec + phase_dir * 2 * ii * pi / qs + angle(A)
            )

    # Test calculation dqh transform directly applied to DataND objects
    In_dt = DataTime(
        name="Stator current",
        unit="A",
        symbol="I_s",
        axes=[Time, Phase],
        values=In,
    )

    Idqh_dt = n2dqh_DataTime(In_dt, phase_dir=phase_dir)

    Idqh_df = n2dqh_DataFreq(
        In_dt, felec=felec, phase_dir=phase_dir, current_dir=current_dir
    )

    result_dqh_dt = Idqh_dt.get_along("freqs", "phase[]")
    Idqh_val_dt = result_dqh_dt[Idqh_dt.symbol][[0, 6, 12], :]

    result_dqh_df = Idqh_df.get_along("freqs", "phase[]")
    Idqh_val_df = result_dqh_df[Idqh_df.symbol]

    assert_array_almost_equal(np_abs(Idqh_val_dt - Idqh_val_df), 0)

    In_df = dqh2n_DataFreq(
        Idqh_df, felec=felec, n=qs, phase_dir=phase_dir, current_dir=current_dir
    )

    In_dt_val = In_dt.get_along("freqs", "phase[]")[In_dt.symbol]
    In_df_val = In_df.get_along("freqs", "phase[]")[In_df.symbol]

    assert_array_almost_equal(np_abs(In_dt_val[[1, 5, 7, 11, 13], :] - In_df_val), 0)

    # Check phase_dir calculation
    phase_dir_calc1 = get_phase_dir(In_dt_val, current_dir)
    phase_dir_calc2 = get_phase_dir_DataFreq(In_dt)
    assert phase_dir_calc1 == phase_dir
    assert phase_dir_calc2 == phase_dir

    if is_show_fig:
        Idqh_dt.plot_2D_Data("time", "phase[]")
        Idqh_dt.plot_2D_Data("freqs", "phase[]")

        Idqh_df.plot_2D_Data("time", "phase[]")
        Idqh_df.plot_2D_Data("freqs", "phase[]")

        In_dt.plot_2D_Data("time", "phase[]")
        In_dt.plot_2D_Data("freqs", "phase[]")

        In_df.plot_2D_Data("time", "phase[]")
        In_df.plot_2D_Data("freqs", "phase[]")

    pass


if __name__ == "__main__":
    for param_dict in param_list:
        test_dqh_transformation_freq(param_dict)

    # test_dqh_transformation_freq(param_list[1])

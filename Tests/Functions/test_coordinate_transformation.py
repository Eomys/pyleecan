import pytest

from numpy import pi, array, linspace, zeros, cos, mean, sqrt, sin
from numpy.testing import assert_array_almost_equal

from SciDataTool import DataTime, Data1D, Norm_ref, Norm_affine

from pyleecan.Functions.Electrical.coordinate_transformation import (
    n2dqh,
    dqh2n,
    n2dqh_DataTime,
    dqh2n_DataTime,
)
from pyleecan.Functions.Winding.gen_phase_list import gen_name

param_list = [
    {"qs": 3, "rot_dir": -1},
    {"qs": 3, "rot_dir": 1},
    {"qs": 6, "rot_dir": -1},
    {"qs": 11, "rot_dir": -1},
]

is_show_fig = False


@pytest.mark.parametrize("param_dict", param_list)
def test_coordinate_transformation(param_dict):
    """Check that the coordinate transformations can return a correct output"""

    Nt = 100
    f_elec = 1
    p = 1
    N0 = f_elec / p

    qs = param_dict["qs"]
    rot_dir = param_dict["rot_dir"]
    current_dir = -rot_dir

    time = linspace(0, 1 / f_elec, Nt, endpoint=False)
    angle_elec = current_dir * 2 * pi * f_elec * time

    # Time axis for plots
    norm_time = {
        "elec_order": Norm_ref(ref=f_elec),
        "mech_order": Norm_ref(ref=N0 / 60),
        "angle_elec": Norm_ref(ref=current_dir / (2 * pi * f_elec)),
        "angle_rotor": Norm_affine(slope=rot_dir * N0 * 360 / 60, offset=0),
    }
    Time = Data1D(name="time", unit="s", values=time, normalizations=norm_time)

    angle_elec_bis = Time.get_values(is_smallestperiod=True, normalization="angle_elec")
    assert_array_almost_equal(angle_elec, angle_elec_bis)

    # Phase axis for plots
    Phase = Data1D(
        name="phase",
        unit="",
        values=gen_name(qs),
        is_components=True,
    )

    phase_list = array([0, 45, 90, 180, 270]) * pi / 180
    for phase in phase_list:
        In = zeros((Nt, qs))
        for ii in range(qs):
            In[:, ii] = cos(angle_elec + phase + rot_dir * 2 * ii * pi / qs)

        Idqh_rms = n2dqh(In, angle_elec, is_dqh_rms=True, is_clockwise=rot_dir < 0)
        Idqh_amp = n2dqh(In, angle_elec, is_dqh_rms=False, is_clockwise=rot_dir < 0)
        In_check_rms = dqh2n(
            Idqh_rms, angle_elec, n=qs, is_n_rms=False, is_clockwise=rot_dir < 0
        )
        In_check_amp = dqh2n(
            Idqh_amp, angle_elec, n=qs, is_n_rms=True, is_clockwise=rot_dir < 0
        )

        assert_array_almost_equal(
            mean(Idqh_rms, axis=0),
            array([cos(phase) / sqrt(2), sin(phase) / sqrt(2), 0]),
        )

        assert_array_almost_equal(Idqh_rms * sqrt(2), Idqh_amp)

        assert_array_almost_equal(In, In_check_rms)
        assert_array_almost_equal(In, In_check_amp)

        In_data = DataTime(
            name="Stator current",
            unit="A",
            symbol="I_s",
            axes=[Time, Phase],
            values=In,
        )

        I_dqh_data = n2dqh_DataTime(In_data)
        In_data_check = dqh2n_DataTime(I_dqh_data, n=qs)

        if is_show_fig:
            In_data.plot_2D_Data("time", "phase[]")
            I_dqh_data.plot_2D_Data("time", "phase[]")

    pass


if __name__ == "__main__":

    for param_dict in param_list:
        test_coordinate_transformation(param_dict)

    # test_coordinate_transformation(param_list[2])

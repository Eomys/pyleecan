from os.path import join

import pytest
from numpy import array, nan
from numpy.testing import assert_array_almost_equal

from Tests import save_validation_path as save_path

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Skew import Skew
from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D

from pyleecan.definitions import DATA_DIR

is_show_fig = False


@pytest.mark.SIPMSM
@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.SliceModel
@pytest.mark.MagFEMM
def test_FEMM_skew():
    """Validate skew effect on cogging torque based on SPMSM 12s/4p from W. Fei and Z. Q. Zhu,
    'Comparison of Cogging Torque Reduction in Permanent Magnet Brushless Machines by Conventional
    and Herringbone Skewing Techniques,' in IEEE Transactions on Energy Conversion, vol. 28, no. 3,
    pp. 664-674, Sept. 2013, doi: 10.1109/TEC.2013.2270871."""

    SPMSM_skew = load(join(DATA_DIR, "Machine", "SPMSM_skew.json"))

    SPMSM_no_skew = SPMSM_skew.copy()
    SPMSM_no_skew.rotor.skew = None
    name = "test_FEMM_skew"

    simu_no_skew = Simu1(name=name + "_none", machine=SPMSM_no_skew)

    simu_no_skew.input = InputCurrent(
        N0=1200,
        Id_ref=0,
        Iq_ref=0,
        Tem_av_ref=0,
        Na_tot=400 * 4,
        Nt_tot=40 * 4,
    )

    # Definition of the magnetic simulation (direct calculation with permeance mmf)
    simu_no_skew.mag = MagFEMM(
        is_periodicity_a=True, is_periodicity_t=True, nb_worker=4
    )

    # Run simulation
    out_no_skew = simu_no_skew.run()

    # Set 2 segment skew
    SPMSM_skew.rotor.skew = Skew(
        type_skew="linear",
        is_step=True,
        rate=1,
        Nstep=2,
    )
    simu_skew_2seg = simu_no_skew.copy()
    simu_skew_2seg.machine = SPMSM_skew
    simu_skew_2seg.name = name + "_2seg"
    simu_skew_2seg.mag.Slice_enforced = None

    # Run simulation
    out_skew_2seg = simu_skew_2seg.run()

    # Set 3 segments skew
    SPMSM_skew_3seg = SPMSM_skew.copy()
    SPMSM_skew_3seg.rotor.skew = Skew(
        type_skew="linear",
        is_step=True,
        rate=1,
        Nstep=3,
    )
    simu_skew_3seg = simu_no_skew.copy()
    simu_skew_3seg.machine = SPMSM_skew_3seg
    simu_skew_3seg.name = name + "_3seg"
    simu_skew_3seg.mag.Slice_enforced = None

    # Run simulation
    out_skew_3seg = simu_skew_3seg.run()

    # # Plot the result
    SPMSM_skew.rotor.skew.plot(
        # save_path=join(save_path, "test_skew_IPMSM_plot_rotor_skew")
    )
    SPMSM_skew_3seg.rotor.skew.plot(
        # save_path=join(save_path, "test_skew_IPMSM_plot_rotor_skew")
    )

    data_list = [out_skew_2seg.mag.Tem, out_skew_3seg.mag.Tem]
    legend_list = ["no skew", "skew 2 seg", "skew 3 seg"]
    linestyles = ["solid", "dashed", "dotted"]

    if is_show_fig:

        out_no_skew.mag.Tem.plot_2D_Data(
            "time->angle_rotor",
            data_list=data_list,
            legend_list=legend_list,
            linestyles=linestyles,
            # save_path=join(save_path, "test_skew_IPMSM_B_slice.png"),
            # is_show_fig=False,
            x_min=0,
            x_max=30,
            **dict_2D
        )

    return out_no_skew, out_skew_2seg, out_skew_3seg


# To run it without pytest
if __name__ == "__main__":
    out_no_skew = test_FEMM_skew()

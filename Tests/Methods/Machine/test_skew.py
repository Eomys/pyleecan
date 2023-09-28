from os.path import join

import pytest

from numpy import pi
from numpy.testing import assert_array_almost_equal, assert_almost_equal

from pyleecan.Classes.Skew import Skew

from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR

from Tests import save_path

is_show_fig = False


@pytest.mark.IPMSM
@pytest.mark.SCIM
@pytest.mark.SliceModel
def test_skew_pattern():
    """Validation of the structural module for IPMSM machine"""

    # Load machines
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    Audi_eTron = load(join(DATA_DIR, "Machine", "Audi_eTron.json"))

    Z1 = Toyota_Prius.stator.get_Zs()
    ssp1 = 2 * pi / Z1

    Z2 = Audi_eTron.rotor.get_Zs()
    ssp2 = 2 * pi / Z2

    # %% 2-Stepped linear skew, half stator slot pitch
    Toyota_Prius.rotor.skew = Skew(type_skew="linear", is_step=True, Nstep=2, rate=0.5)

    angle_step_linear, z_step_linear = Toyota_Prius.rotor.skew.comp_pattern()

    assert_array_almost_equal(
        angle_step_linear,
        [
            -0.032724923474893676,
            -0.032724923474893676,
            0.032724923474893676,
            0.032724923474893676,
        ],
    )

    assert_array_almost_equal(
        z_step_linear,
        [-0.04191, 0.0, 0.0, 0.04191],
    )

    assert max(angle_step_linear) - min(angle_step_linear) == 0.5 * ssp1
    Toyota_Prius.rotor.skew.plot(
        save_path=join(save_path, "test_IPMSM_plot_rotor_skew1"),
        is_show_fig=is_show_fig,
    )

    # %% 3-Stepped linear skew, one stator slot pitch
    Toyota_Prius.rotor.skew = Skew(type_skew="linear", is_step=True, Nstep=3, rate=1)

    angle_step_linear, z_step_linear = Toyota_Prius.rotor.skew.comp_pattern()

    assert_array_almost_equal(
        angle_step_linear,
        [
            -0.06544984694978735,
            -0.06544984694978735,
            0.0,
            0.0,
            0.06544984694978735,
            0.06544984694978735,
        ],
    )

    assert_array_almost_equal(
        z_step_linear,
        [
            -0.04191,
            -0.01397,
            -0.01397,
            0.013970000000000003,
            0.013970000000000003,
            0.04191,
        ],
    )

    assert max(angle_step_linear) - min(angle_step_linear) == ssp1
    Toyota_Prius.rotor.skew.plot(
        save_path=join(save_path, "test_IPMSM_plot_rotor_skew2"),
        is_show_fig=is_show_fig,
    )

    # %% 4-Stepped V-shape skew, one stator slot pitch
    Toyota_Prius.rotor.skew = Skew(type_skew="vshape", is_step=True, Nstep=4, rate=1)

    angle_step_vshape, z_step_vshape = Toyota_Prius.rotor.skew.comp_pattern()

    assert_array_almost_equal(
        angle_step_vshape,
        [
            -0.06544984694978735,
            -0.06544984694978735,
            0.06544984694978735,
            0.06544984694978735,
            0.06544984694978735,
            0.06544984694978735,
            -0.06544984694978735,
            -0.06544984694978735,
        ],
    )

    assert_array_almost_equal(
        z_step_vshape,
        [-0.04191, -0.020955, -0.020955, 0.0, 0.0, 0.020955, 0.020955, 0.04191],
    )

    assert max(angle_step_vshape) - min(angle_step_vshape) == ssp1
    Toyota_Prius.rotor.skew.plot(
        save_path=join(save_path, "test_IPMSM_plot_rotor_skew3"),
        is_show_fig=is_show_fig,
    )

    # %% 3-Stepped V-shape skew, one stator slot pitch
    Toyota_Prius.rotor.skew = Skew(type_skew="vshape", is_step=True, Nstep=3, rate=1)

    angle_step_vshape, z_step_vshape = Toyota_Prius.rotor.skew.comp_pattern()

    assert_array_almost_equal(
        angle_step_vshape,
        [
            -0.04363323129985823,
            -0.04363323129985823,
            0.08726646259971647,
            0.08726646259971647,
            -0.04363323129985823,
            -0.04363323129985823,
        ],
    )

    assert_array_almost_equal(
        z_step_vshape,
        [
            -0.04191,
            -0.01397,
            -0.01397,
            0.013970000000000003,
            0.013970000000000003,
            0.04191,
        ],
    )

    assert max(angle_step_vshape) - min(angle_step_vshape) == ssp1
    Toyota_Prius.rotor.skew.plot(
        save_path=join(save_path, "test_IPMSM_plot_rotor_skew4"),
        is_show_fig=is_show_fig,
    )

    # %% 5-Stepped alternate skew, one stator slot pitch
    Toyota_Prius.rotor.skew = Skew(type_skew="zig-zag", is_step=True, Nstep=5, rate=0.8)

    angle_step_alternate, z_step_alternate = Toyota_Prius.rotor.skew.comp_pattern()

    assert_array_almost_equal(
        angle_step_alternate,
        [
            0.041887902047863905,
            0.041887902047863905,
            -0.06283185307179585,
            -0.06283185307179585,
            0.041887902047863905,
            0.041887902047863905,
            -0.06283185307179585,
            -0.06283185307179585,
            0.041887902047863905,
            0.041887902047863905,
        ],
    )

    assert_array_almost_equal(
        z_step_alternate,
        [
            -0.04191,
            -0.025146,
            -0.025146,
            -0.008381999999999999,
            -0.008381999999999999,
            0.008382000000000008,
            0.008382000000000008,
            0.025146000000000005,
            0.025146000000000005,
            0.04191,
        ],
    )

    assert_almost_equal(
        max(angle_step_alternate) - min(angle_step_alternate), 0.8 * ssp1, decimal=12
    )
    Toyota_Prius.rotor.skew.plot(
        save_path=join(save_path, "test_IPMSM_plot_rotor_skew5"),
        is_show_fig=is_show_fig,
    )

    # %% 2-Stepped UD skew
    angle_list = [0.5, -0.2]
    Toyota_Prius.rotor.skew = Skew(
        type_skew="user-defined", is_step=True, angle_list=angle_list
    )

    angle_step_ud, z_step_ud = Toyota_Prius.rotor.skew.comp_pattern()

    assert_array_almost_equal(
        angle_step_ud,
        [0.5, 0.5, -0.2, -0.2],
    )

    assert_array_almost_equal(
        z_step_ud,
        [-0.04191, 0.0, 0.0, 0.04191],
    )

    assert max(angle_step_ud) - min(angle_step_ud) == max(angle_list) - min(angle_list)
    Toyota_Prius.rotor.skew.plot(
        save_path=join(save_path, "test_IPMSM_plot_rotor_skew6"),
        is_show_fig=is_show_fig,
    )

    # %% Continuous linear skew, one rotor slot pitch
    Audi_eTron.rotor.skew = Skew(type_skew="linear", is_step=False, rate=1)

    angle_cont_lin, z_cont_lin = Audi_eTron.rotor.skew.comp_pattern()

    assert_array_almost_equal(
        angle_cont_lin,
        [-0.054165390579134366, 0.054165390579134366],
    )

    assert_array_almost_equal(
        z_cont_lin,
        [-0.06, 0.06],
    )

    assert max(angle_cont_lin) - min(angle_cont_lin) == ssp2
    Audi_eTron.rotor.skew.plot(
        save_path=join(save_path, "test_SCIM_plot_rotor_skew1"),
        is_show_fig=is_show_fig,
    )

    return Toyota_Prius, Audi_eTron


if __name__ == "__main__":
    Toyota_Prius, Audi_eTron = test_skew_pattern()
    print("Done")
    # Toyota_Prius.rotor.skew.plot(is_show_fig=True)
    # Audi_eTron.rotor.skew.plot(is_show_fig=True)

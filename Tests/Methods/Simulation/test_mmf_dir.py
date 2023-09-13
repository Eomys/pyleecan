import pytest

from numpy import pi
from numpy.testing import assert_almost_equal

from os.path import join

from multiprocessing import cpu_count

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent

from pyleecan.Functions.load import load
from pyleecan.Methods.Simulation.Input import CURRENT_DIR_REF

from pyleecan.definitions import DATA_DIR


param_list = [
    {
        "name": "Toyota_Prius",
        "resistance": 0.035951,
        "stator_d_axis": 1.3089,
        "rotor_d_axis": pi / 8,
        "mmf_dir": 1,
        "Tem_av": 367.01,
    },
    {
        "name": "Protean_InWheel",
        "resistance": 0.000733,
        "stator_d_axis": 0.09817,
        "rotor_d_axis": pi / 64,
        "mmf_dir": -1,
        "Tem_av": 811.65,
    },
]

is_show_fig = False


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.parametrize("param_dict", param_list)
def test_mmf_dir(param_dict, nb_worker=int(cpu_count() / 2)):
    """test calculation of stator mmf rotating direction according to winding pattern and rotor direction"""

    machine = load(join(DATA_DIR, "Machine", param_dict["name"] + ".json"))

    p = machine.get_pole_pair_number()

    current_dir_ref = CURRENT_DIR_REF

    # Check that resistance computation is correct
    resistance = machine.stator.comp_resistance_wind()
    assert_almost_equal(resistance, param_dict["resistance"], decimal=5)

    # Check that the DQ axis are correct for the stator
    d_axis = machine.stator.comp_angle_d_axis()
    assert_almost_equal(d_axis, param_dict["stator_d_axis"], decimal=4)
    q_axis = machine.stator.comp_angle_q_axis()
    assert_almost_equal(q_axis, param_dict["stator_d_axis"] + pi / 2 / p, decimal=4)

    # Check that the DQ axis are correct for the rotor
    d_axis = machine.rotor.comp_angle_d_axis()
    assert_almost_equal(d_axis, param_dict["rotor_d_axis"], decimal=4)
    q_axis = machine.rotor.comp_angle_q_axis()
    assert_almost_equal(q_axis, param_dict["rotor_d_axis"] + pi / 2 / p, decimal=4)

    # Check mmf rotating direction with current rotating in default
    mmf_dir = machine.stator.comp_mmf_dir(is_plot=False, current_dir=current_dir_ref)
    assert mmf_dir == param_dict["mmf_dir"]

    # Check mmf rotating direction by reversing current rotating direction
    mmf_dir_inv = machine.stator.comp_mmf_dir(
        is_plot=False, current_dir=-current_dir_ref
    )
    assert (
        mmf_dir_inv == -mmf_dir
    ), "mmf_dir_inv should be opposite when reversing current rotating direction"

    # Check mmf rotating direction by reversing current rotating direction
    machine_B = machine.copy()
    machine_B.stator.winding.is_reverse_wind = (
        not machine_B.stator.winding.is_reverse_wind
    )
    mmf_dir_rev_wind = machine_B.stator.comp_mmf_dir(
        is_plot=False, current_dir=current_dir_ref
    )
    assert (
        mmf_dir_rev_wind == -mmf_dir
    ), "mmf_dir_inv should be opposite when reversing machine winding pattern"

    # Check torque sign with MagFEMM calculation
    if param_dict["Tem_av"] is not None:
        simu = Simu1(name="test_mmf_dir_" + machine.name, machine=machine)

        # Compute time and space (anti-)periodicities from the machine
        per_a, is_aper_a = machine.comp_periodicity_spatial()
        per_t, is_aper_t, _, _ = machine.comp_periodicity_time()

        per_a = int(2 * per_a) if is_aper_a else per_a
        per_t = int(2 * per_t) if is_aper_t else per_t

        simu.input = InputCurrent(
            OP=OPdq(Id_ref=-100, Iq_ref=200, N0=1000),  # arbitrary current
            Nt_tot=4 * per_t,
            Na_tot=200 * per_a,
        )

        # Definition of the MagFEMM simulation
        simu.mag = MagFEMM(
            is_periodicity_a=True,
            is_periodicity_t=True,
            nb_worker=nb_worker,
            Kmesh_fineness=0.5,  # reduce mesh size to speed up calculation
            T_mag=60,
        )

        # Run simulation
        out = simu.run()

        # Check torque value
        assert_almost_equal(out.mag.Tem_av, param_dict["Tem_av"], decimal=2)

        if is_show_fig:
            out.mag.Tem.plot_2D_Data("time")

            out.mag.B.components["radial"].plot_3D_Data("time", "angle")

            out.mag.B.components["radial"].plot_3D_Data("freqs", "wavenumber")

            out.elec.get_Is().plot_2D_Data("time", "phase[]")

    return out


if __name__ == "__main__":
    for param_dict in param_list:
        out = test_mmf_dir(param_dict)

    # out = test_mmf_dir(param_list[1])

import pytest
from numpy import pi
from os.path import join
from multiprocessing import cpu_count

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


param_list = [
    {
        "name": "Toyota_Prius",
        "resistance": 0.035951,
        "stator_d_axis": 1.3076,
        "rotor_d_axis": pi / 8,
        "rot_dir": 1,
    },
    {
        "name": "PR0178_machine_new",
        "resistance": 0.035951,
        "stator_d_axis": 1.3076,
        "rotor_d_axis": pi / 8,
        "rot_dir": 1,
    },
]


@pytest.mark.parametrize("param_dict", param_list)
def test_rot_dir_dq_axis(param_dict, nb_worker=int(cpu_count() / 2)):

    machine = load(join(DATA_DIR, "Machine", param_dict["name"] + ".json"))

    p = machine.get_pole_pair_number()

    # # Check that resistance computation is correct
    # result = machine.stator.comp_resistance_wind()
    # assert result == pytest.approx(param_dict["resistance"], abs=0.00001)

    # # Check that the DQ axis are correct for the stator
    # d_axis = machine.stator.comp_angle_d_axis()
    # assert d_axis == pytest.approx(param_dict["stator_d_axis"], abs=0.001)

    # q_axis = machine.stator.comp_angle_q_axis()
    # assert q_axis == pytest.approx(param_dict["stator_d_axis"] + pi / 2 / p, abs=0.001)

    # # Check that the DQ axis are correct for the rotor
    # d_axis = machine.rotor.comp_angle_d_axis()
    # assert d_axis == pytest.approx(param_dict["rotor_d_axis"], abs=0.0001)
    # q_axis = machine.rotor.comp_angle_q_axis()
    # assert q_axis == pytest.approx(param_dict["rotor_d_axis"] + pi / 2 / p, abs=0.0001)

    rot_dir = machine.stator.comp_mmf_dir(is_plot=True)
    # assert rot_dir == param_dict["rot_dir"], (
    #     "rot_dir=" + str(rot_dir) + " instead of " + str(param_dict["rot_dir"])
    # )

    machine_B = machine.copy()
    machine_B.stator.winding.is_reverse_wind = (
        not machine_B.stator.winding.is_reverse_wind
    )
    rot_dir_inv = machine_B.stator.comp_mmf_dir()
    assert rot_dir_inv == -rot_dir

    simu = Simu1(name="test_rot_dir_dq_axis_" + machine.name, machine=machine)

    # Compute time and space (anti-)periodicities from the machine
    per_a, is_aper_a = machine.comp_periodicity_spatial()
    per_t, is_aper_t, _, _ = machine.comp_periodicity_time()

    per_a = int(2 * per_a) if is_aper_a else per_a
    per_t = int(2 * per_t) if is_aper_t else per_t

    simu.input = InputCurrent(
        OP=OPdq(Id_ref=-50, Iq_ref=150, N0=1000),
        # OP=OPdq(Id_ref=0, Iq_ref=0, N0=1000),
        Nt_tot=10 * nb_worker * per_t,
        Na_tot=200 * per_a,
    )

    # Definition of the magnetic simulation (only one OP in MLUT => direct calculation)
    simu.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=True,
        nb_worker=nb_worker,
    )

    out = simu.run()

    out.elec.get_Is().plot_2D_Data("time", "phase[]")

    out.mag.Tem.plot_2D_Data("time")

    out.mag.B.components["radial"].plot_3D_Data("time", "angle")

    out.mag.B.components["radial"].plot_3D_Data("freqs", "wavenumber")

    return out


if __name__ == "__main__":
    out = test_rot_dir_dq_axis(param_list[1])

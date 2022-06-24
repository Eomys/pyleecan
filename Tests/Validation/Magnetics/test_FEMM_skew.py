from os.path import join

import pytest

from numpy import lcm, pi

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Skew import Skew
from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D

from pyleecan.definitions import DATA_DIR

from Tests import save_validation_path as save_path

is_show_fig = False


@pytest.mark.SIPMSM
@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.SliceModel
@pytest.mark.MagFEMM
def test_FEMM_skew():
    """Validate skew effect on cogging torque inspired from SPMSM 12s/4p from W. Fei and Z. Q. Zhu,
    'Comparison of Cogging Torque Reduction in Permanent Magnet Brushless Machines by Conventional
    and Herringbone Skewing Techniques,' in IEEE Transactions on Energy Conversion, vol. 28, no. 3,
    pp. 664-674, Sept. 2013, doi: 10.1109/TEC.2013.2270871."""

    def comp_skew_angle(Zs, p, Nstep):
        """Inspired from equation number 5 (page 3) to determine skew angle function of number of steps"""
        return 2 * pi * (Nstep - 1) / (Nstep * lcm(Zs, 2 * p))

    SPMSM_skew = load(join(DATA_DIR, "Machine", "SPMSM_skew.json"))
    Zs = SPMSM_skew.stator.get_Zs()  # Stator slot number
    p = SPMSM_skew.get_pole_pair_number()  # Pole pair number
    ssp = 2 * pi / Zs  # Stator slot pitch

    SPMSM_no_skew = SPMSM_skew.copy()
    SPMSM_no_skew.rotor.skew = None
    name = "test_FEMM_skew"

    simu_no_skew = Simu1(name=name + "_none", machine=SPMSM_no_skew)

    simu_no_skew.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0, Tem_av_ref=0),
        Na_tot=400 * 4,
        Nt_tot=40 * 4,
    )

    # Definition of the magnetic simulation (direct calculation with permeance mmf)
    simu_no_skew.mag = MagFEMM(
        is_periodicity_a=True, is_periodicity_t=True, nb_worker=4, Kmesh_fineness=0.5,
    )

    # Run reference simulation
    out_no_skew = simu_no_skew.run()

    # Run skewed simulation
    out_list = list()
    for k in range(2, 6):
        # Set k^th segment skew
        rate_kseg = comp_skew_angle(Zs, p, Nstep=k) / ssp
        SPMSM_skew_kseg = SPMSM_skew.copy()
        SPMSM_skew_kseg.rotor.skew = Skew(
            type_skew="linear", is_step=True, rate=rate_kseg, Nstep=k,
        )
        simu_skew_kseg = simu_no_skew.copy()
        simu_skew_kseg.machine = SPMSM_skew_kseg
        simu_skew_kseg.name = name + "_" + str(k) + "seg"
        simu_skew_kseg.mag.Slice_enforced = None

        out_skew_kseg = simu_skew_kseg.run()

        out_list.append(out_skew_kseg)

    data_list = [out.mag.Tem for out in out_list]
    legend_list = ["no skew"] + ["skew " + str(k) + " seg" for k in range(2, 6)]
    linestyles = ["solid", "solid", "dashed", "dashdot", "dotted"]

    for out_skew in out_list:

        Nstep = out_skew.simu.machine.rotor.skew.Nstep

        # Plot skew pattern result
        out_skew.simu.machine.rotor.skew.plot(
            save_path=join(save_path, "test_FEMM_skew_pattern_Nstep" + str(Nstep))
        )

        out_skew.mag.Tem_slice.plot_2D_Data(
            "time->angle_rotor",
            "z[smallestpattern]",
            x_min=0,
            x_max=30,
            **dict_2D,
            save_path=join(
                save_path, "test_FEMM_skew_Tem_slice_Nstep" + str(Nstep) + ".png",
            ),
            is_show_fig=is_show_fig,
        )

    out_no_skew.mag.Tem.plot_2D_Data(
        "time->angle_rotor",
        data_list=data_list,
        legend_list=legend_list,
        linestyles=linestyles,
        save_path=join(save_path, "test_FEMM_skew_Tem_compare.png"),
        is_show_fig=is_show_fig,
        x_min=0,
        x_max=30,
        **dict_2D,
    )

    return out_no_skew, out_list


# To run it without pytest
if __name__ == "__main__":
    out_no_skew = test_FEMM_skew()

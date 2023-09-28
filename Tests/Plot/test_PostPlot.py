from os.path import join

import pytest

from numpy import exp, sqrt, pi

import matplotlib.pyplot as plt
from pyleecan.Classes.OPdq import OPdq

from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.InputCurrent import InputCurrent

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT

from pyleecan.Classes.PostPlot import PostPlot

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.definitions import DATA_DIR


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
@pytest.mark.ForceMT
def test_PostPlot():
    """Validation of the PostPlot class to plot airgap flux automatically as postprocessing at the end of the simulation"""

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    simu = Simu1(name="test_PostPlot", machine=Toyota_Prius)

    # Definition of the enforced output of the electrical module
    I0_rms = 250 / sqrt(2)
    Phi0 = 140 * pi / 180  # Maximum Torque Per Amp

    Id_ref = (I0_rms * exp(1j * Phi0)).real
    Iq_ref = (I0_rms * exp(1j * Phi0)).imag

    simu.input = InputCurrent(
        Na_tot=252 * 8,
        Nt_tot=20 * 8,
        OP=OPdq(N0=1000, Id_ref=Id_ref, Iq_ref=Iq_ref),
    )

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(is_periodicity_a=True, is_periodicity_t=True, nb_worker=4)
    simu.force = ForceMT(is_periodicity_a=True, is_periodicity_t=True)

    # Plot radial and tangential flux densities over angle as an automated PostProc
    # and save the picture
    fig1, axes1 = plt.subplots(2, 1)
    fig2, axes2 = plt.subplots(1, 2)

    plot_B_rad_tan_space1 = PostPlot(
        method="plot_2D_Data",
        quantity="mag.B",
        param_list=["angle"],
        param_dict=dict(
            {
                "component_list": ["radial"],
                "is_show_fig": False,
                "save_path": None,
                "fig": fig1,
                "ax": axes1[0],
            },
            **dict_2D
        ),
    )

    plot_B_rad_tan_space2 = PostPlot(
        method="plot_2D_Data",
        quantity="mag.B",
        param_list=["angle"],
        param_dict=dict(
            {
                "component_list": ["tangential"],
                "is_show_fig": False,
                "fig": fig1,
                "ax": axes1[1],
            },
            **dict_2D
        ),
        name="plot_B_rad_tan_space",
        save_format="png",
    )

    plot_machine_Tem_time1 = PostPlot(
        method="plot",
        quantity="simu.machine",
        param_dict={
            "is_show_fig": False,
            "save_path": None,
            "fig": fig2,
            "ax": axes2[0],
        },
    )

    plot_machine_Tem_time2 = PostPlot(
        method="plot_2D_Data",
        quantity="mag.Tem",
        param_list=["time"],
        param_dict=dict(
            {
                "is_show_fig": False,
                "fig": fig2,
                "ax": axes2[1],
            },
            **dict_2D
        ),
        name="plot_machine_Tem_time",
        save_format="png",
    )

    plot_P_radial_space_svg = PostPlot(
        method="plot_2D_Data",
        quantity="force.AGSF",
        param_list=["angle"],
        param_dict=dict(
            {
                "component_list": ["radial"],
                "is_show_fig": False,
            },
            **dict_2D
        ),
        name="plot_P_radial_space",
        save_format="svg",
    )

    plot_Is = PostPlot(
        method="plot_2D_Data",
        quantity="elec.get_Is",
        param_list=["time", "phase[]"],
        param_dict=dict(
            {
                "is_show_fig": False,
            },
            **dict_2D
        ),
        name="plot_Is",
        save_format="png",
    )

    simu.postproc_list = [
        plot_B_rad_tan_space1,
        plot_B_rad_tan_space2,
        plot_machine_Tem_time1,
        plot_machine_Tem_time2,
        plot_P_radial_space_svg,
        plot_Is,
    ]

    # Run simulations
    out = simu.run()

    return out


# To run it without pytest
if __name__ == "__main__":
    out = test_PostPlot()

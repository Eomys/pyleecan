from os.path import join

import pytest

from numpy import exp, sqrt, pi

from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.InputCurrent import InputCurrent

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT

from pyleecan.Classes.PostPlot import PostPlot

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_PostPlot():
    """Validation of the PostPlot class to plot airgap flux automatically as postprocessing at the end of the simulation"""

    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))

    simu = Simu1(name="PostPlot", machine=IPMSM_A)

    # Definition of the enforced output of the electrical module
    I0_rms = 250 / sqrt(2)
    Phi0 = 140 * pi / 180  # Maximum Torque Per Amp

    Id_ref = (I0_rms * exp(1j * Phi0)).real
    Iq_ref = (I0_rms * exp(1j * Phi0)).imag

    simu.input = InputCurrent(
        Id_ref=Id_ref,
        Iq_ref=Iq_ref,
        Na_tot=252 * 8,
        Nt_tot=2 * 8,
        N0=1000,
    )

    # Definition of the magnetic simulation: with periodicity
    simu.mag = MagFEMM(is_periodicity_a=True, is_periodicity_t=True)
    simu.force = ForceMT(is_periodicity_a=True, is_periodicity_t=True)

    plot_B_radial_space = PostPlot(
        method="plot_2D_Data",
        param_list=["mag.B", "angle"],
        param_dict={
            "component_list": ["radial"],
        },
        name="plot_B_radial_space",
        is_show_fig=True,
        save_format="png",
    )

    plot_B_tangential_space = PostPlot(
        method="plot_2D_Data",
        param_list=["mag.B", "angle"],
        param_dict={
            "component_list": ["tangential"],
        },
        name="plot_B_tangential_space",
        is_show_fig=False,
        save_format="svg",
    )

    simu.postproc_list = [plot_B_radial_space, plot_B_tangential_space]

    # Run simulations
    out = simu.run()

    return out


# To run it without pytest
if __name__ == "__main__":

    out = test_PostPlot()

from os.path import join

import pytest
from Tests import save_validation_path as save_path

from numpy import exp, sqrt, pi

from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.InputCurrent import InputCurrent

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Output import Output

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_FEMM_periodicity():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""

    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))

    assert IPMSM_A.comp_periodicity() == (4, True, 4, True)

    simu = Simu1(name="FEMM_periodicity", machine=IPMSM_A)

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
    simu.mag = MagFEMM(is_periodicity_a=True, is_periodicity_t=True, nb_worker=2)
    simu.force = ForceMT(is_periodicity_a=True, is_periodicity_t=True)

    # Definition of the magnetic simulation: no periodicity
    simu2 = simu.copy()
    simu2.mag = MagFEMM(is_periodicity_a=False, is_periodicity_t=False, nb_worker=2)
    simu2.force = ForceMT(is_periodicity_a=False, is_periodicity_t=False)

    # Run simulations
    out = Output(simu=simu)
    simu.run()

    out2 = Output(simu=simu2)
    simu2.run()

    # Plot the result
    out.plot_2D_Data(
        "mag.B",
        "time",
        "angle[0]{°}",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_time.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "mag.B",
        "angle",
        "time[0]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_space.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "mag.B",
        "wavenumber=[0,100]",
        data_list=[out2.mag.B],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_B_space_fft.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "force.P",
        "time",
        "angle[0]{°}",
        data_list=[out2.force.P],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_time.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "force.P",
        "angle",
        "time[0]",
        data_list=[out2.force.P],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_space.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "force.P",
        "wavenumber=[0,100]",
        "time[0]",
        data_list=[out2.force.P],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_P_space_fft.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "mag.Tem",
        "time",
        data_list=[out2.mag.Tem],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_Tem_time.png"),
        is_show_fig=False,
    )

    out.plot_2D_Data(
        "mag.Phi_wind_stator",
        "time",
        "phase",
        data_list=[out2.mag.Phi_wind_stator],
        legend_list=["Periodic", "Full"],
        save_path=join(save_path, simu.name + "_Phi_wind_stator_time.png"),
        is_show_fig=False,
    )

    return out, out2


# To run it without pytest
if __name__ == "__main__":

    out, out2 = test_FEMM_periodicity()

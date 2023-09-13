from pyleecan.Classes.OPdq import OPdq
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Functions.Plot import dict_2D

from Tests import save_plot_path
from os.path import join

import pytest


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.ForceMT
@pytest.mark.periodicity
@pytest.mark.IPMSM
@pytest.mark.SingleOP
def test_AGSF_slotless():
    """Validation of AGSF calculation on slotless machine.

    Electrical machine is an academic slotless machine inspired
    from [R. Pile et al., Application Limits of the Airgap Maxwell
    Tensor, CEFC, 2018] but with interior magnet such as Toyota
    Prius machine.

    """
    Slotless_CEFC = load(join(DATA_DIR, "Machine", "Slotless_CEFC.json"))
    simu = Simu1(name="test_AGSF_slotless", machine=Slotless_CEFC)

    simu.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0), Ir=None, Na_tot=2 ** 6, Nt_tot=2
    )

    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_get_meshsolution=True,
        is_periodicity_a=True,
        is_periodicity_t=False,
    )

    simu.force = ForceMT()

    out = simu.run()

    # Plot the AGSF as a function of space with the spatial fft
    out.force.AGSF.plot_2D_Data(
        "angle{rad}",
        component_list=["radial"],
        save_path=join(save_plot_path, "test_AGSF_slotless_plot_force_space.png"),
        is_show_fig=False,
        **dict_2D
    )

    out.force.AGSF.plot_2D_Data(
        "wavenumber=[0,78]",
        component_list=["radial"],
        save_path=join(save_plot_path, "test_AGSF_slotless_plot_force_space_fft.png"),
        is_show_fig=False,
        **dict_2D
    )

    return out


# To run it without pytest
if __name__ == "__main__":
    out = test_AGSF_slotless()

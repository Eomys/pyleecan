import pytest
from os.path import join
from pyleecan.Classes.OPdq import OPdq

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
import matplotlib.pyplot as plt
from Tests import save_validation_path as save_path
from numpy.testing import assert_array_almost_equal


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.IPMSM
@pytest.mark.SingleOP
def test_FEMM_airgap_winding():
    """Test to compute the Flux in FEMM with winding in the airgap and make sure that the simulation is running."""

    # Loading the Toyota Prius then closing its slots
    M18 = load(join(DATA_DIR, "Machine", "slotless_M18.json"))
    simu = Simu1(name="test_FEMM_airgap_winding", machine=M18)

    simu.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=-80, Iq_ref=-80),
        Na_tot=2**6,
        Nt_tot=8,
    )

    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_get_meshsolution=True,
        is_periodicity_a=False,
        is_periodicity_t=True,
        nb_worker=4,
    )

    out = simu.run()

    simu_sym = simu.copy()
    simu_sym.mag.is_periodicity_a = True

    out_sym = simu_sym.run()

    out.mag.B.plot_2D_Data(
        "time",
        "angle[0]{°}",
        data_list=[out_sym.mag.B],
        legend_list=["Full", "Periodic"],
        save_path=join(save_path, simu.name + "_B_time.png"),
        is_show_fig=False,
        # **dict_2D
    )

    Bflux = out.mag.B
    arg_list = ["time"]
    result = Bflux.get_rphiz_along(*arg_list)
    Brad = result["radial"]
    time = result["time"]

    Bflux2 = out_sym.mag.B
    arg_list = ["time"]
    result2 = Bflux2.get_rphiz_along(*arg_list)
    Brad2 = result2["radial"]
    time2 = result2["time"]

    # Compare both simu
    assert_array_almost_equal((Brad - Brad2) / Brad2, 0, decimal=2)
    assert_array_almost_equal(time, time2, decimal=6)

    plt.show()
    return out, out_sym


# To run it without pytest
if __name__ == "__main__":
    out = test_FEMM_airgap_winding()
    print("Done")

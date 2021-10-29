from os.path import join
from numpy.testing import assert_almost_equal

from Tests import save_validation_path as save_path
from numpy import sqrt, pi
from multiprocessing import cpu_count

import pytest

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputElec import InputElec
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_PMSM import EEC_PMSM
from pyleecan.Classes.FluxLinkFEMM import FluxLinkFEMM
from pyleecan.Classes.IndMagFEMM import IndMagFEMM
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.definitions import DATA_DIR


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.EEC_PMSM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_EEC_PMSM():
    """Validation of the PMSM Electrical Equivalent Circuit with the Prius machine
    Compute Torque from EEC results and compare with Yang et al, 2013
    """

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    simu = Simu1(name="test_EEC_PMSM", machine=Toyota_Prius)

    # Definition of the input
    simu.input = InputElec(N0=2000, Nt_tot=10, Na_tot=2048)
    simu.input.set_Id_Iq(I0=250 / sqrt(2), Phi0=60 * pi / 180)

    # Define second simu for FEMM comparison
    simu2 = simu.copy()
    simu2.name = "test_EEC_PMSM_FEMM"

    # Definition of the electrical simulation (FEMM)
    simu.elec = Electrical()
    simu.elec.eec = EEC_PMSM(
        indmag=IndMagFEMM(is_periodicity_a=True, Nt_tot=10),
        fluxlink=FluxLinkFEMM(is_periodicity_a=True, Nt_tot=10),
    )

    simu.mag = None
    simu.force = None
    simu.struct = None

    out = Output(simu=simu)
    simu.run()

    # Definition of the magnetic simulation (FEMM)
    simu2.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=True,
        nb_worker=cpu_count(),
    )

    out2 = Output(simu=simu2)
    simu2.run()

    # Plot 3-phase current function of time
    out.elec.get_Is().plot_2D_Data(
        "time",
        "phase[]",
        save_path=join(save_path, "EEC_FEMM_IPMSM_currents.png"),
        is_show_fig=False,
        **dict_2D
    )

    # from Yang et al, 2013
    assert out.elec.Tem_av_ref == pytest.approx(81.69, rel=0.1)
    assert out2.mag.Tem_av == pytest.approx(81.91, rel=0.1)

    return out, out2


# To run it without pytest
if __name__ == "__main__":
    out, out2 = test_EEC_PMSM()
    print("Done")

from os.path import join
from numpy.testing import assert_almost_equal

from Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1


from pyleecan.Classes.InputElec import InputElec
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_PMSM import EEC_PMSM
from pyleecan.Classes.FluxLinkFEMM import FluxLinkFEMM
from pyleecan.Classes.IndMagFEMM import IndMagFEMM
from pyleecan.Classes.Output import Output
import pytest
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_E_IPMSM_FL_002():
    """Validation of the PMSM Electrical Equivalent Circuit with the Prius machine"""

    simu = Simu1(name="E_IPMSM_FL_002", machine=IPMSM_A)

    # Definition of the input
    simu.input = InputElec(
        N0=2000,
        Id_ref=-100,
        Iq_ref=200,
        Nt_tot=10,
        Na_tot=2048,
        rot_dir=1,
    )

    # Definition of the electrical simulation (FEMM)
    simu.elec = Electrical()
    simu.elec.eec = EEC_PMSM(
        indmag=IndMagFEMM(is_symmetry_a=True, sym_a=4, is_antiper_a=True, Nt_tot=10),
        fluxlink=FluxLinkFEMM(
            is_symmetry_a=True, sym_a=4, is_antiper_a=True, Nt_tot=10
        ),
    )

    simu.mag = None
    simu.force = None
    simu.struct = None

    out = Output(simu=simu)
    simu.run()

    assert_almost_equal(out.elec.Tem_av_ref, -7, decimal=1)

    out.plot_A_time(
        "elec.Is",
        index_list=[0, 1, 2],
        save_path=join(save_path, "test_E_IPMSM_FL_002_currents.png"),
    )

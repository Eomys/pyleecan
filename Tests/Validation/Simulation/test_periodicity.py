from numpy import zeros, ones, pi, array, sqrt
from os.path import join
import matplotlib.pyplot as plt

# from Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Output import Output
import pytest
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_periodicity():
    """Validation of the implementaiton of periodic angle axis in Magnetic (MagFEMM) and Force (ForceMT) modules"""
    simu = Simu1(name="EM_IPMSM_FL_003", machine=IPMSM_A)

    # Definition of the enforced output of the electrical module
    simu.input = InputCurrent(
        Id_ref=200,
        Iq_ref=-100,
        Ir=None,
        Na_tot=252 * 8,
        Nt_tot=1,
        N0=1000,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(is_periodicity_a=True)
    simu.force = ForceMT(is_periodicity_a=True)
    simu.struct = None

    out = simu.run()

    return out


# To run it without pytest
if __name__ == "__main__":
    out = test_periodicity()

    out.plot_A_space(
        "mag.B",
        t_index=0,
        is_fft=True,
        # data_list=[out2.mag.B],
        # legend_list=["Periodic", "Full"],
        # save_path=join(save_path, "test_EM_IPMSM_PMMF_B1.png"),
    )

    out.plot_A_space(
        "force.P",
        t_index=0,
        is_fft=True,
        # legend_list=["Periodic"],
    )

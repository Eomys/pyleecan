from numpy import zeros, ones, pi, array
from os.path import join
import matplotlib.pyplot as plt
from Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal

from pyleecan.Classes.ModelBH_Langevin import ModelBH_Langevin
from pyleecan.Classes.ModelBH_linear_sat import ModelBH_linear_sat
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Output import Output
import pytest
from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.definitions import DATA_DIR

import matplotlib.pyplot as plt


@pytest.mark.long_5s
@pytest.mark.IPMSM
@pytest.mark.FEMM
@pytest.mark.MagFEMM
@pytest.mark.SingleOP
def test_EM_BH_Model_001_Toyota_Prius():
    """Validation of the TOYOTA Prius 2004 interior magnet (V shape) with distributed winding
    50 kW peak, 400 Nm peak at 1500 rpm from publication

    from publication
    Z. Yang, M. Krishnamurthy and I. P. Brown,
    "Electromagnetic and vibrational characteristic of IPM over full torque-speed range,"
    Electric Machines & Drives Conference (IEMDC), 2013 IEEE International, Chicago, IL, 2013, pp. 295-302.
    Test compute the Flux in FEMM, with and without symmetry
    """
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    simu = Simu1(name="test_EM_BH_Model_001_Toyota_Prius", machine=Toyota_Prius)

    # Definition of the enforced output of the electrical module
    N0 = 2504
    Is_mat = zeros((1, 3))
    Is_mat[0, :] = array([0, 12.2474, -12.2474])
    Is = ImportMatrixVal(value=Is_mat)
    Nt_tot = 1
    Na_tot = 2048

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        N0=N0,
        angle_rotor=None,  # Will be computed
        Nt_tot=Nt_tot,
        Na_tot=Na_tot,
        angle_rotor_initial=0.86,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=0, type_BH_rotor=0, is_periodicity_a=True, Kgeo_fineness=0.75,
    )
    simu.force = None
    simu.struct = None

    simu.machine.stator.mat_type.mag.BH_curve = None  # Replace imported BH curve
    simu.machine.stator.mat_type.mag.ModelBH = ModelBH_Langevin(
        Bs=1.46, a=1000, Hmax=8000, Bmax=None,
    )

    fig = simu.machine.stator.mat_type.mag.plot_BH(color="b")

    simu2 = simu.copy()
    simu2.machine.stator.mat_type.mag.ModelBH = ModelBH_Langevin(
        Bs=1.46, a=25, Hmax=8000, Bmax=None,
    )

    simu2.machine.stator.mat_type.mag.plot_BH(fig=fig, color="r")
    plt.legend(["a=1000", "a=25"])
    plt.savefig(join(save_path, simu.name + "_sat_curve.png"))

    out = simu.run()
    out2 = simu2.run()

    # Plot the result by comparing the two simulation
    plt.close("all")

    out.mag.B.plot_2D_Data(
        "angle[smallestperiod]",
        data_list=[out2.mag.B],
        legend_list=["a=1000", "a=25"],
        save_path=join(save_path, simu.name + "_B.png"),
        is_show_fig=False,
        **dict_2D
    )


# To run it without pytest
if __name__ == "__main__":

    out = test_EM_BH_Model_001_Toyota_Prius()

from numpy import ones, pi, array, linspace
from os.path import join
import matplotlib.pyplot as plt
from Tests import save_validation_path as save_path
from numpy.testing import assert_array_almost_equal
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
import pytest

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.definitions import DATA_DIR

IPMSM_xxx = load(join(DATA_DIR, "Machine", "IPMSM_xxx.json"))


@pytest.mark.MagFEMM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_import_model():
    """Test to compute a simulation with/without reusing femm file"""
    # First simulation creating femm file
    simu = Simu1(name="test_FEMM_import_model", machine=IPMSM_xxx)

    # Initialization of the simulation starting point
    simu.input = InputCurrent()

    # Set time and space discretization
    simu.input.Nt_tot = 2
    simu.input.Na_tot = 1024

    # Definition of the enforced output of the electrical module
    simu.input.Is = ImportMatrixVal(
        value=array(  # Stator currents as a function of time
            [
                [6.97244193e-06, 2.25353053e02, -2.25353060e02],
                [-2.60215295e02, 1.30107654e02, 1.30107642e02],
            ]
        )
    )
    simu.input.Ir = None  # SPMSM machine => no rotor currents to define
    simu.input.OP = OPdq(N0=3000)  # Rotor speed [rpm]

    # Definition of the magnetic simulation
    simu.mag = MagFEMM(type_BH_stator=2, type_BH_rotor=2, is_periodicity_a=True,)
    out = simu.run()

    # Second simulation, importing femm file and FEMM_dict
    simu2 = Simu1(input=simu.input.copy(), machine=simu.machine.copy())
    simu2.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_periodicity_a=True,
        is_periodicity_t=False,
        import_file=out.simu.mag.get_path_save_fem(out),
        FEMM_dict_enforced=out.mag.internal.FEMM_dict,
    )

    out2 = simu2.run()

    # Plot the result by comparing the two simulation
    plt.close("all")
    out.mag.B.plot_2D_Data(
        "angle{°}",
        data_list=[out2.mag.B],
        legend_list=["Creating .fem", "Importing .fem"],
        save_path=join(save_path, "test_FEMM_import_model_B.png"),
        is_show_fig=False,
        **dict_2D
    )

    assert_array_almost_equal(
        out.mag.B.components["tangential"].values,
        out2.mag.B.components["tangential"].values,
        decimal=3,
    )
    assert_array_almost_equal(
        out.mag.B.components["radial"].values,
        out2.mag.B.components["radial"].values,
        decimal=3,
    )
    assert_array_almost_equal(out.mag.Tem.values, out2.mag.Tem.values, decimal=3)

    return out, out2


if __name__ == "__main__":
    out, out2 = test_FEMM_import_model()

from numpy import pi, array, linspace, zeros
from os.path import join
import matplotlib.pyplot as plt
from multiprocessing import cpu_count
import pytest
from numpy.testing import assert_array_almost_equal
from Tests import save_validation_path as save_path
from pyleecan.Classes.OPdqf import OPdqf
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.InputFlux import InputFlux
from pyleecan.Classes.ImportMatlab import ImportMatlab
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.definitions import DATA_DIR
from Tests import TEST_DATA_DIR


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.WRSM
def test_FEMM_compare_Zoe():
    """Test compute the Flux in FEMM of machine Zoe, with and without symmetry"""
    Zoe = load(join(DATA_DIR, "Machine", "Renault_Zoe.json"))
    simu = Simu1(name="test_FEMM_compare_Zoe", machine=Zoe, path_result=save_path)

    # Initialization of the simulation starting point
    simu.input = InputCurrent()
    # Set time and space discretization
    simu.input.Na_tot = 2048
    simu.input.Nt_tot = 1
    simu.input.OP = OPdqf(N0=3000, Id_ref=0, Iq_ref=70, If_ref=10)  # Rotor speed [rpm]

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        is_periodicity_a=False, is_periodicity_t=False, nb_worker=cpu_count()
    )
    simu.force = None
    simu.struct = None

    assert Zoe.comp_periodicity_spatial() == (2, True)
    # Copy the simu and activate the symmetry
    simu_sym = simu.copy()
    simu_sym.mag.is_periodicity_a = True

    out = simu.run()
    out.export_to_mat(join(save_path, "test_FEMM_WRSM.mat"))

    out2 = simu_sym.run()

    # Plot the result by comparing the two simulation
    plt.close("all")
    out.mag.B.plot_2D_Data(
        "angle{°}",
        data_list=[out2.mag.B],
        legend_list=["No symmetry", "1/4 symmetry"],
        save_path=join(save_path, "test_FEMM_compare_Zoe.png"),
        is_show_fig=False,
        **dict_2D
    )
    # Check Output
    B_rad = out.mag.B.components["radial"].get_along("time", "angle")["B_{rad}"]
    B_tan = out.mag.B.components["tangential"].get_along("time", "angle")["B_{circ}"]
    B_rad_sym = out2.mag.B.components["radial"].get_along("time", "angle")["B_{rad}"]
    B_tan_sym = out2.mag.B.components["tangential"].get_along("time", "angle")[
        "B_{circ}"
    ]

    assert_array_almost_equal(B_rad, B_rad_sym, decimal=1)
    assert_array_almost_equal(B_tan, B_tan_sym, decimal=1)
    assert max(B_rad) == pytest.approx(1.268, rel=0.1)
    assert max(B_tan) == pytest.approx(0.445, rel=0.1)
    assert out.mag.Tem_av == pytest.approx(51.987, rel=0.1)


if __name__ == "__main__":
    test_FEMM_compare_Zoe()
    print("Done")

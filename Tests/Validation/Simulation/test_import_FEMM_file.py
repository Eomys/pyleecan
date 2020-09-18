from numpy import ones, pi, array, linspace
from os.path import join
import matplotlib.pyplot as plt
from Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
import pytest

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

IPMSM_xxx = load(join(DATA_DIR, "Machine", "IPMSM_xxx.json"))


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_import_FEMM_file():
    """Test to compute a simulation with/without reusing femm file"""
    # First simulation creating femm file
    simu = Simu1(name="EM_IPMSM_FL_001", machine=IPMSM_xxx)

    # Initialization of the simulation starting point
    simu.input = InputCurrent()

    # Set time and space discretization
    simu.input.time = ImportMatrixVal(
        value=linspace(start=0, stop=0.015, num=2, endpoint=True)
    )
    simu.input.angle = ImportMatrixVal(
        value=linspace(start=0, stop=2 * pi, num=1024, endpoint=False)
    )

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
    simu.input.N0 = 3000  # Rotor speed [rpm]
    simu.input.angle_rotor_initial = 0.5216 + pi  # Rotor position at t=0 [rad]

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_symmetry_a=True,
        sym_a=4,
        is_antiper_a=True,
    )
    out = simu.run()

    # Second simulation, importing femm file and FEMM_dict
    simu2 = Simu1(input=simu.input.copy(), machine=simu.machine.copy(),)

    simu2.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_symmetry_a=True,
        sym_a=4,
        is_antiper_a=True,
        import_file=out.simu.mag.get_path_save_fem(out),
        FEMM_dict=out.mag.FEMM_dict,
    )

    out2 = simu2.run()

    # Plot the result by comparing the two simulation
    plt.close("all")
    out.plot_A_space(
        "mag.B",
        data_list=[out2.mag.B],
        legend_list=["Creating .fem", "Importing .fem"],
        color_list=["b", "r"],
        linestyle_list=["-", "dotted"],
    )

    fig = plt.gcf()
    fig.savefig(join(save_path, "test_import_FEMM_file.png"))

    assert (
        out.mag.B.components["tangential"].values
        - out2.mag.B.components["tangential"].values
        < 1e-8
    ).all()
    assert (
        out.mag.B.components["radial"].values - out2.mag.B.components["radial"].values
        < 1e-8
    ).all()
    assert (out.mag.Tem.values - out2.mag.Tem.values < 1e-8).all()

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


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_EM_IPMSM_FL_001():
    """Test compute the Flux in FEMM of machine IPMSM_xxx, with and without symmetry"""
    IPMSM_xxx = load(join(DATA_DIR, "Machine", "IPMSM_xxx.json"))
    simu = Simu1(name="EM_IPMSM_FL_001", machine=IPMSM_xxx)

    # Initialization of the simulation starting point
    simu.input = InputCurrent()
    # Set time and space discretization
    simu.input.time = ImportMatrixVal(
        value=linspace(start=0, stop=0.015, num=4, endpoint=True)
    )
    simu.input.Na_tot = 1024

    # Definition of the enforced output of the electrical module
    simu.input.Is = ImportMatrixVal(
        value=array(  # Stator currents as a function of time
            [
                [6.97244193e-06, 2.25353053e02, -2.25353060e02],
                [-2.60215295e02, 1.30107654e02, 1.30107642e02],
                [-6.97244208e-06, -2.25353053e02, 2.25353060e02],
                [2.60215295e02, -1.30107654e02, -1.30107642e02],
            ]
        )
    )
    simu.input.Ir = None  # SPMSM machine => no rotor currents to define
    simu.input.N0 = 3000  # Rotor speed [rpm]
    simu.input.angle_rotor_initial = 0.5216 + pi  # Rotor position at t=0 [rad]

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(type_BH_stator=2, type_BH_rotor=2, is_periodicity_a=False)
    simu.force = None
    simu.struct = None

    assert IPMSM_xxx.comp_periodicity() == (4, True, 4, True)
    # Copy the simu and activate the symmetry
    simu_sym = Simu1(init_dict=simu.as_dict())
    simu_sym.mag.is_periodicity_a = True

    out = Output(simu=simu)
    simu.run()

    out2 = Output(simu=simu_sym)
    simu_sym.run()

    # Plot the result by comparing the two simulation
    plt.close("all")
    out.plot_2D_Data(
        "mag.B",
        "angle",
        data_list=[out2.mag.B],
        legend_list=["No symmetry", "1/4 symmetry"],
        save_path=join(save_path, "test_EM_IPMSM_FL_001_sym.png"),
        is_show_fig=False
    )

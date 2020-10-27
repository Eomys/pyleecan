from numpy import ones, pi, array
from os.path import join
import matplotlib.pyplot as plt
from Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.InputFlux import InputFlux
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportMatlab import ImportMatlab
from pyleecan.Classes.ImportData import ImportData
from pyleecan.Classes.ImportVectorField import ImportVectorField

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
from Tests import TEST_DATA_DIR
import pytest

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_Magnetic_FEMM_sym():
    """Validation of a polar SIPMSM with surface magnet
    Linear lamination material

    From publication
    Lubin, S. Mezani, and A. Rezzoug,
    “2-D Exact Analytical Model for Surface-Mounted Permanent-Magnet Motors with Semi-Closed Slots,”
    IEEE Trans. Magn., vol. 47, no. 2, pp. 479–492, 2011.
    Test compute the Flux in FEMM, with and without symmetry
    and with MANATEE semi-analytical subdomain model
    """
    SPMSM_003 = load(join(DATA_DIR, "Machine", "SPMSM_003.json"))
    simu = Simu1(name="EM_SPMSM_FL_001", machine=SPMSM_003)

    # Definition of the enforced output of the electrical module
    N0 = 3000
    Is = ImportMatrixVal(
        value=array(
            [
                [6.97244193e-06, 2.25353053e02, -2.25353060e02],
                [-2.60215295e02, 1.30107654e02, 1.30107642e02],
                [-6.97244208e-06, -2.25353053e02, 2.25353060e02],
                [2.60215295e02, -1.30107654e02, -1.30107642e02],
            ]
        )
    )
    time = ImportGenVectLin(start=0, stop=0.015, num=4, endpoint=True)
    Na_tot = 1024

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        N0=N0,
        angle_rotor=None,  # Will be computed
        time=time,
        Na_tot=Na_tot,
        angle_rotor_initial=0.5216 + pi,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(type_BH_stator=2, type_BH_rotor=2, is_periodicity_a=False)
    simu.force = None
    simu.struct = None
    # Copy the simu and activate the symmetry
    assert SPMSM_003.comp_periodicity() == (1, True, 1, True)
    simu_sym = Simu1(init_dict=simu.as_dict())
    simu_sym.mag.is_periodicity_a = True

    # Just load the Output and ends (we could also have directly filled the Output object)
    simu_load = Simu1(init_dict=simu.as_dict())
    simu_load.mag = None
    mat_file = join(TEST_DATA_DIR, "EM_SPMSM_FL_001_MANATEE_SDM.mat")
    Br = ImportMatlab(file_path=mat_file, var_name="XBr")
    Bt = ImportMatlab(file_path=mat_file, var_name="XBt")
    Time = ImportData(field=time, unit="s", name="time")
    Angle = ImportData(
        field=ImportGenVectLin(start=0, stop=2 * pi, num=1024, endpoint=False),
        unit="rad",
        name="angle",
    )
    Br_data = ImportData(
        axes=[Time, Angle],
        field=Br,
        unit="T",
        name="Radial airgap flux density",
        symbol="B_r",
    )
    Bt_data = ImportData(
        axes=[Time, Angle],
        field=Bt,
        unit="T",
        name="Tangential airgap flux density",
        symbol="B_t",
    )
    B = ImportVectorField(components={"radial": Br_data, "tangential": Bt_data})
    simu_load.input = InputFlux(time=time, Na_tot=Na_tot, B=B, OP=simu.input.copy())
    out = Output(simu=simu)
    simu.run()

    out2 = Output(simu=simu_sym)
    simu_sym.run()

    out3 = Output(simu=simu_load)
    simu_load.run()

    # Plot the result by comparing the two simulation (sym / no sym)
    plt.close("all")

    out.plot_2D_Data(
        "mag.B",
        "angle",
        data_list=[out2.mag.B],
        legend_list=["No symmetry", "1/2 symmetry"],
        save_path=join(save_path, "test_EM_SPMSM_FL_001_sym.png"),
    )

    # Plot the result by comparing the two simulation (sym / MANATEE)
    plt.close("all")

    out.plot_2D_Data(
        "mag.B",
        "angle",
        data_list=[out3.mag.B],
        legend_list=["No symmetry", "MANATEE SDM"],
        save_path=join(save_path, "test_EM_SPMSM_FL_001_SDM.png"),
    )


if __name__ == "__main__":
    test_Magnetic_FEMM_sym()
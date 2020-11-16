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
    """Validation of a polar SIPMSM with inset magnet
    Armature load (magnet field canceled by is_mmfr=False)

    from publication
    A. Rahideh and T. Korakianitis,
    “Analytical Magnetic Field Calculation of Slotted Brushless Permanent-Magnet Machines With Surface Inset Magnets,”
    vol. 48, no. 10, pp. 2633–2649, 2012.
    Test compute the Flux in FEMM, with and without symmetry
    and with MANATEE semi-analytical subdomain model
    """
    SIPMSM_001 = load(join(DATA_DIR, "Machine", "SIPMSM_001.json"))
    simu = Simu1(name="EM_SIPMSM_AL_001", machine=SIPMSM_001)

    # Definition of the enforced output of the electrical module
    N0 = 150
    Is = ImportMatrixVal(
        value=array([[14.1421, -7.0711, -7.0711], [-14.1421, 7.0711, 7.0711]])
    )
    time = ImportGenVectLin(start=0, stop=0.1, num=2, endpoint=True)
    Na_tot = 1024

    Ar = ImportMatrixVal(value=array([2.5219, 0.9511]) + pi / 6)
    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        N0=N0,
        angle_rotor=Ar,  # Will be computed
        time=time,
        Na_tot=Na_tot,
        angle_rotor_initial=0,
    )

    # Definition of the magnetic simulation (is_mmfr=False => no flux from the magnets)
    assert SIPMSM_001.comp_periodicity() == (1, False, 2, True)
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_periodicity_a=False,
        is_periodicity_t=False,
        is_mmfr=False,
        angle_stator_shift=-pi / 6,
    )
    simu.force = None
    simu.struct = None
    # Just load the Output and ends (we could also have directly filled the Output object)
    simu_load = Simu1(init_dict=simu.as_dict())
    simu_load.mag = None
    mat_file = join(TEST_DATA_DIR, "EM_SIPMSM_AL_001_MANATEE_SDM.mat")
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

    out3 = Output(simu=simu_load)
    simu_load.run()

    # Plot the result by comparing the two simulation (no sym / MANATEE SDM)
    plt.close("all")

    out.plot_2D_Data(
        "mag.B",
        "angle",
        data_list=[out3.mag.B],
        legend_list=["No symmetry", "MANATEE SDM"],
        save_path=join(save_path, "test_EM_SIPMSM_AL_001_SDM.png"),
        is_show_fig=False,
    )

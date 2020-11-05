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
    """Validation of outer rotor SPMSM
    Open circuit (Null Stator currents)

    Machine B from Vu Xuan Hung thesis
    "Modeling of exterior rotor permanent magnet machines with concentrated windings"
    Hanoi university of science and technology 2012
    Test compute the Flux in FEMM, with and without symmetry
    and with MANATEE semi-analytical subdomain model
    """

    SPMSM_015 = load(join(DATA_DIR, "Machine", "SPMSM_015.json"))
    simu = Simu1(name="EM_SPMSM_NL_001", machine=SPMSM_015)

    # Definition of the enforced output of the electrical module
    N0 = 3000
    Is = ImportMatrixVal(value=array([[0, 0, 0]]))
    time = ImportGenVectLin(start=0, stop=0, num=1, endpoint=True)
    angle = ImportGenVectLin(start=0, stop=2 * 2 * pi / 9, num=2043, endpoint=False)

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        N0=N0,
        angle_rotor=None,
        time=time,
        angle=angle,
        angle_rotor_initial=0,
    )

    # Definition of the magnetic simulation (is_mmfr=False => no flux from the magnets)
    assert SPMSM_015.comp_periodicity() == (9, False, 9, True)
    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_t=False,
        is_periodicity_a=True,
        is_mmfs=False,
    )
    simu.force = None
    simu.struct = None
    # Just load the Output and ends (we could also have directly filled the Output object)
    simu_load = Simu1(init_dict=simu.as_dict())
    simu_load.mag = None
    mat_file = join(TEST_DATA_DIR, "EM_SPMSM_NL_001_MANATEE_SDM.mat")
    Br = ImportMatlab(file_path=mat_file, var_name="Br")
    Bt = ImportMatlab(file_path=mat_file, var_name="Bt")
    angle2 = ImportGenVectLin(start=0, stop=2 * pi / 9, num=2048 / 9, endpoint=False)
    Time = ImportData(field=time, unit="s", name="time")
    Angle = ImportData(
        field=angle2, unit="rad", name="angle", symmetries={"angle": {"period": 2}}
    )
    Br_data = ImportData(
        axes=[Time, Angle],
        field=Br,
        unit="T",
        name="Radial airgap flux density",
        symbol="B_r",
        symmetries={"angle": {"period": 2}},
    )
    Bt_data = ImportData(
        axes=[Time, Angle],
        field=Bt,
        unit="T",
        name="Tangential airgap flux density",
        symbol="B_t",
        symmetries={"angle": {"period": 2}},
    )
    B = ImportVectorField(components={"radial": Br_data, "tangential": Bt_data})
    simu_load.input = InputFlux(time=time, angle=angle2, B=B, OP=simu.input.copy())

    out = Output(simu=simu)
    simu.run()

    out3 = Output(simu=simu_load)
    simu_load.run()

    plt.close("all")

    out.plot_2D_Data(
        "mag.B",
        "angle",
        data_list=[out3.mag.B],
        legend_list=["Symmetry", "MANATEE SDM"],
        save_path=join(save_path, "test_EM_SPMSM_NL_001_SDM.png"),
        is_show_fig=False
    )

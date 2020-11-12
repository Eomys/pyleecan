from os import chdir

chdir("../../..")

from numpy import ones, pi, array, zeros
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
    """Validation of the FEMM model of a polar SCIM machine
    Only one time step

    From publication:
    K. Boughrara
    Analytical Analysis of Cage Rotor Induction Motors in Healthy, Defective and Broken Bars Conditions
    IEEE Trans on Mag, 2014
    Test compute the Flux in FEMM, with and without symmetry
    and with MANATEE MMF analytical model
    """

    SCIM_006 = load(join(DATA_DIR, "Machine", "SCIM_006.json"))
    simu = Simu1(name="EM_SCIM_NL_006", machine=SCIM_006)

    # Definition of the enforced output of the electrical module
    N0 = 1500
    Is = ImportMatrixVal(value=array([[20, -10, -10]]))
    Ir = ImportMatrixVal(value=zeros((1, 28)))
    time = ImportGenVectLin(start=0, stop=0, num=1, endpoint=False)
    Na_tot = 4096

    simu.input = InputCurrent(
        Is=Is,
        Ir=Ir,  # zero current for the rotor
        N0=N0,
        angle_rotor=None,  # Will be computed
        time=time,
        Na_tot=Na_tot,
        angle_rotor_initial=0.2244,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_periodicity_a=False,
        is_periodicity_t=False,
    )
    simu.force = None
    simu.struct = None
    # Copy the simu and activate the symmetry
    assert SCIM_006.comp_periodicity() == (2, True, 28, False)
    simu_sym = Simu1(init_dict=simu.as_dict())
    simu_sym.mag.is_periodicity_a = True

    # Just load the Output and ends (we could also have directly filled the Output object)
    simu_load = Simu1(init_dict=simu.as_dict())
    simu_load.mag = None
    mat_file = join(TEST_DATA_DIR, "EM_SCIM_NL_006_MANATEE_MMF.mat")
    Br = ImportMatlab(file_path=mat_file, var_name="XBr")
    angle2 = ImportGenVectLin(start=0, stop=pi, num=4096 / 2, endpoint=False)
    Time = ImportData(field=time, unit="s", name="time")
    Angle = ImportData(field=angle2, unit="rad", name="angle")
    Br_data = ImportData(
        axes=[Time, Angle],
        field=Br,
        unit="T",
        name="Radial airgap flux density",
        symbol="B_r",
    )
    B = ImportVectorField(components={"radial": Br_data})
    simu_load.input = InputFlux(time=time, angle=angle2, B=B, OP=simu.input.copy())

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
        save_path=join(save_path, "test_EM_SCIM_NL_006_sym.png"),
        is_show_fig=False,
    )

    # Plot the result by comparing the two simulation (no sym / MANATEE)
    plt.close("all")

    out.plot_2D_Data(
        "mag.B",
        "angle",
        data_list=[out3.mag.B],
        legend_list=["No symmetry", "MANATEE MMF"],
        component_list=["radial"],
        save_path=join(save_path, "test_EM_SCIM_NL_006_MMF.png"),
        is_show_fig=False,
    )

    return out, out2, out3


# To run it without pytest
if __name__ == "__main__":
    out, out2, out3 = test_Magnetic_FEMM_sym()

from numpy import zeros, ones, pi, array
from os.path import join
import matplotlib.pyplot as plt
from Tests import save_validation_path as save_path

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


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_EM_IPMSM_FL_002():
    """Validation of the TOYOTA Prius 2004 interior magnet (V shape) with distributed winding
    50 kW peak, 400 Nm peak at 1500 rpm from publication

    from publication
    Z. Yang, M. Krishnamurthy and I. P. Brown,
    "Electromagnetic and vibrational characteristic of IPM over full torque-speed range,"
    Electric Machines & Drives Conference (IEMDC), 2013 IEEE International, Chicago, IL, 2013, pp. 295-302.
    Test compute the Flux in FEMM, with and without symmetry
    """
    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))
    simu = Simu1(name="EM_IPMSM_FL_002", machine=IPMSM_A)

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
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=False,
        Kgeo_fineness=0.75,
    )
    simu.force = None
    simu.struct = None
    # simu.struct.force = ForceMT()
    # Copy the simu and activate the symmetry
    assert IPMSM_A.comp_periodicity() == (4, True, 4, True)
    simu_sym = Simu1(init_dict=simu.as_dict())
    simu_sym.mag.is_periodicity_a = True

    out = Output(simu=simu)
    simu.run()

    out2 = Output(simu=simu_sym)
    simu_sym.run()

    # Plot the result by comparing the two simulation
    plt.close("all")

    out.plot_2D_Data("mag.B", "angle", 
                     data_list=[out2.mag.B], 
                     legend_list=["No symmetry", "1/2 symmetry"],
                     save_path=join(save_path, "test_EM_IPMSM_FL_002_sym.png"))

    # # Plot the surface magnetic forces
    # plt.close("all")
    # out.plot_force_space(j_t0=0, is_deg=False, out_list=[])

    # fig = plt.gcf()
    # fig.savefig(join(save_path, "test_EM_IPMSM_FL_002_force.png"))

from numpy import zeros, ones, pi, array
from os.path import join
import matplotlib.pyplot as plt
from Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1
from Tests.Validation.Machine.IPMSM_A import IPMSM_A

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal

from pyleecan.Classes.FluxLinkFEMM import FluxLinkFEMM
from pyleecan.Classes.IndMagFEMM import IndMagFEMM
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Output import Output
import pytest


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
    simu = Simu1(name="EM_IPMSM_FL_002", machine=IPMSM_A)

    # Definition of the enforced output of the electrical module
    Nr = ImportMatrixVal(value=ones(1) * 2504)
    Is_mat = zeros((1, 3))
    Is_mat[0, :] = array([0, 12.2474, -12.2474])
    Is = ImportMatrixVal(value=Is_mat)
    time = ImportGenVectLin(start=0, stop=0, num=1, endpoint=False)
    angle = ImportGenVectLin(start=0, stop=2 * pi, num=2048, endpoint=False)

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        Nr=Nr,
        angle_rotor=None,  # Will be computed
        time=time,
        angle=angle,
        angle_rotor_initial=0.86,
    )

    # Definition of the electrical simulation (FEMM)
    simu.elec.fluxlink = FluxLinkFEMM(is_symmetry_a=True, sym_a=4, is_antiper_a=True)
    simu.elec.indmag = IndMagFEMM(is_symmetry_a=True, sym_a=4, is_antiper_a=True)

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_symmetry_a=False,
        is_antiper_a=True,
        Kgeo_fineness=0.75,
    )
    simu.struct = None
    # simu.struct.force = ForceMT()
    # Copy the simu and activate the symmetry
    simu_sym = Simu1(init_dict=simu.as_dict())
    simu_sym.mag.is_symmetry_a = True
    simu_sym.mag.sym_a = 4
    simu_sym.mag.is_antiper_a = True
    simu_sym.struct = None

    out = Output(simu=simu)
    out.post.legend_name = "No symmetry"
    simu.run()

    out2 = Output(simu=simu_sym)
    out2.post.legend_name = "1/2 symmetry"
    out2.post.line_color = "r--"
    simu_sym.run()

    # Plot the result by comparing the two simulation
    plt.close("all")
    out.plot_B_space(out_list=[out2])

    fig = plt.gcf()
    fig.savefig(join(save_path, "test_EM_IPMSM_FL_002_sym.png"))

    # # Plot the surface magnetic forces
    # plt.close("all")
    # out.plot_force_space(j_t0=0, is_deg=False, out_list=[])

    # fig = plt.gcf()
    # fig.savefig(join(save_path, "test_EM_IPMSM_FL_002_force.png"))

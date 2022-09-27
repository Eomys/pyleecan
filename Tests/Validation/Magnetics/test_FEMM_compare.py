from numpy import pi, array, linspace, zeros
from os.path import join
import matplotlib.pyplot as plt
from multiprocessing import cpu_count
import pytest

from Tests import save_validation_path as save_path
from pyleecan.Classes.OPdq import OPdq
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
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_compare_IPMSM_xxx():
    """Test compute the Flux in FEMM of machine IPMSM_xxx, with and without symmetry"""
    IPMSM_xxx = load(join(DATA_DIR, "Machine", "IPMSM_xxx.json"))
    simu = Simu1(name="test_FEMM_compare_IPMSM_xxx", machine=IPMSM_xxx)

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
    simu.input.OP = OPdq(N0=3000)  # Rotor speed [rpm]
    simu.input.angle_rotor_initial = 0.5216 + pi  # Rotor position at t=0 [rad]

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=2, type_BH_rotor=2, is_periodicity_a=False, nb_worker=cpu_count()
    )
    simu.force = None
    simu.struct = None

    assert IPMSM_xxx.comp_periodicity_spatial() == (4, True)
    # Copy the simu and activate the symmetry
    simu_sym = Simu1(init_dict=simu.as_dict())
    simu_sym.mag.is_periodicity_a = True

    out = simu.run()
    out.export_to_mat(join(save_path, "test_FEMM_compare_IPMSM_xxx.mat"))

    out2 = simu_sym.run()

    # Plot the result by comparing the two simulation
    plt.close("all")
    out.mag.B.plot_2D_Data(
        "angle{°}",
        data_list=[out2.mag.B],
        legend_list=["No symmetry", "1/4 symmetry"],
        save_path=join(save_path, "test_FEMM_compare_IPMSM_xxx.png"),
        is_show_fig=False,
        **dict_2D
    )


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_compare_IPMSM_xxx_lam_sym():
    """Test compute the Flux in FEMM of machine IPMSM_xxx, with is_fast_draw at True (with lamination symetry) or False (without)"""
    IPMSM_xxx = load(join(DATA_DIR, "Machine", "IPMSM_xxx.json"))
    simu = Simu1(name="test_FEMM_compare_IPMSM_xxx_lam_sym", machine=IPMSM_xxx)

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
    simu.input.OP = OPdq(N0=3000)  # Rotor speed [rpm]
    simu.input.angle_rotor_initial = 0.5216 + pi  # Rotor position at t=0 [rad]

    # Definition of the magnetic simulation (no lam symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_periodicity_a=True,
        nb_worker=cpu_count(),
        is_fast_draw=False,
    )
    simu.force = None
    simu.struct = None

    assert IPMSM_xxx.comp_periodicity_spatial() == (4, True)
    assert IPMSM_xxx.stator.comp_periodicity_geo() == (48, False)
    assert IPMSM_xxx.rotor.comp_periodicity_geo() == (8, False)

    # Copy the simu and activate the symmetry
    simu_sym = Simu1(init_dict=simu.as_dict())
    simu_sym.mag.is_fast_draw = True

    out = simu.run()

    out2 = simu_sym.run()

    # Plot the result by comparing the two simulation
    plt.close("all")
    out.mag.B.plot_2D_Data(
        "angle{°}",
        data_list=[out2.mag.B],
        legend_list=["WIthout lam symmetry", "With lam symmetry"],
        save_path=join(save_path, "test_FEMM_compare_IPMSM_xxx.png"),
        is_show_fig=False,
        **dict_2D
    )


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_compare_Prius():
    """Validation of the TOYOTA Prius 2004 interior magnet (V shape) with distributed winding
    50 kW peak, 400 Nm peak at 1500 rpm from publication

    from publication
    Z. Yang, M. Krishnamurthy and I. P. Brown,
    "Electromagnetic and vibrational characteristic of IPM over full torque-speed range,"
    Electric Machines & Drives Conference (IEMDC), 2013 IEEE International, Chicago, IL, 2013, pp. 295-302.
    Test compute the Flux in FEMM, with and without symmetry
    """
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    simu = Simu1(name="test_FEMM_compare_Toyota_Prius", machine=Toyota_Prius)

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
        OP=OPdq(N0=N0),
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
    assert Toyota_Prius.comp_periodicity_spatial() == (4, True)
    simu_sym = Simu1(init_dict=simu.as_dict())
    simu_sym.mag.is_periodicity_a = True

    out = simu.run()

    out2 = simu_sym.run()

    # Plot the result by comparing the two simulation
    plt.close("all")

    out.mag.B.plot_2D_Data(
        "angle{°}",
        data_list=[out2.mag.B],
        legend_list=["No symmetry", "1/2 symmetry"],
        save_path=join(save_path, "test_FEMM_compare_Toyota_Prius.png"),
        is_show_fig=False,
        **dict_2D
    )


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.SCIM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_compare_SCIM():
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
    simu = Simu1(name="test_FEMM_compare_SCIM", machine=SCIM_006)

    # Definition of the enforced output of the electrical module
    N0 = 1500
    Is = ImportMatrixVal(value=array([[20, -10, -10]]))
    Ir = ImportMatrixVal(value=zeros((1, 28)))
    time = ImportGenVectLin(start=0, stop=0, num=1, endpoint=False)
    Na_tot = 4096

    simu.input = InputCurrent(
        Is=Is,
        Ir=Ir,  # zero current for the rotor
        OP=OPdq(N0=N0),
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
    assert SCIM_006.comp_periodicity_spatial() == (2, True)
    simu_sym = Simu1(init_dict=simu.as_dict())
    simu_sym.mag.is_periodicity_a = True

    # Just load the Output and ends (we could also have directly filled the Output object)
    simu_load = Simu1(init_dict=simu.as_dict())
    simu_load.mag = None
    mat_file = join(TEST_DATA_DIR, "EM_SCIM_NL_006_MANATEE_MMF.mat")
    Br = ImportMatlab(file_path=mat_file, var_name="XBr")
    angle2 = ImportGenVectLin(start=0, stop=pi, num=4096 / 2, endpoint=False)
    simu_load.input = InputFlux(
        time=time,
        angle=angle2,
        B_dict={"B_{rad}": Br},
        Is=Is,
        Ir=Ir,
        OP=OPdq(N0=simu.input.OP.N0),
    )

    out2 = simu_sym.run()

    out = simu.run()

    out3 = simu_load.run()

    # Plot the result by comparing the two simulation (sym / no sym)
    plt.close("all")

    out.mag.B.plot_2D_Data(
        "angle{°}",
        data_list=[out2.mag.B],
        legend_list=["No symmetry", "1/2 symmetry"],
        save_path=join(save_path, "test_FEMM_compare_SCIM_sym.png"),
        is_show_fig=False,
        **dict_2D
    )

    # Plot the result by comparing the two simulation (no sym / MANATEE)
    plt.close("all")

    out.mag.B.plot_2D_Data(
        "angle{°}",
        data_list=[out3.mag.B],
        legend_list=["No symmetry", "MANATEE MMF"],
        component_list=["radial"],
        save_path=join(save_path, "test_FEMM_compare_SCIM_PMMF.png"),
        is_show_fig=False,
        **dict_2D
    )


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.SIPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_FEMM_compare_SIPMSM():
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
    simu = Simu1(name="test_FEMM_compare_SIPMSM", machine=SIPMSM_001)

    # Definition of the enforced output of the electrical module
    N0 = 150
    Is = ImportMatrixVal(
        value=array([[14.1421, -7.0711, -7.0711], [-14.1421, 7.0711, 7.0711]])
    )
    Nt_tot = 2
    time = ImportGenVectLin(start=0, stop=0.1, num=Nt_tot, endpoint=True)
    Na_tot = 1024

    Ar = ImportMatrixVal(value=array([2.5219, 0.9511]) + pi / 6)
    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        OP=OPdq(N0=N0),
        # angle_rotor=Ar,  # Will be computed
        time=time,
        Nt_tot=Nt_tot,
        Na_tot=Na_tot,
        angle_rotor_initial=0,
    )

    # Definition of the magnetic simulation (is_mmfr=False => no flux from the magnets)
    assert SIPMSM_001.comp_periodicity_spatial() == (1, False)
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_periodicity_a=False,
        is_periodicity_t=False,
        is_mmfr=False,
        angle_stator_shift=-pi / 6,
        nb_worker=2,
    )
    simu.force = None
    simu.struct = None
    # Just load the Output and ends (we could also have directly filled the Output object)
    simu_load = Simu1(init_dict=simu.as_dict())
    simu_load.mag = None
    mat_file = join(TEST_DATA_DIR, "EM_SIPMSM_AL_001_MANATEE_SDM.mat")
    Br = ImportMatlab(file_path=mat_file, var_name="XBr")
    Bt = ImportMatlab(file_path=mat_file, var_name="XBt")
    simu_load.input = InputFlux(
        time=time,
        Na_tot=Na_tot,
        Nt_tot=Nt_tot,
        B_dict={"B_{rad}": Br, "B_{circ}": Bt},
        Is=Is,
        Ir=None,  # No winding on the rotor
        OP=OPdq(N0=simu.input.OP.N0),
    )

    out = simu.run()

    out3 = simu_load.run()

    # Plot the result by comparing the two simulation (no sym / MANATEE SDM)
    plt.close("all")

    out.mag.B.plot_2D_Data(
        "angle{°}",
        data_list=[out3.mag.B],
        legend_list=["No symmetry", "MANATEE SDM"],
        save_path=join(save_path, "test_FEMM_compare_SIPMSM.png"),
        is_show_fig=False,
        **dict_2D
    )


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_SPMSM_load():
    """Validation of a polar SPMSM with surface magnet
    Linear lamination material

    From publication
    Lubin, S. Mezani, and A. Rezzoug,
    “2-D Exact Analytical Model for Surface-Mounted Permanent-Magnet Motors with Semi-Closed Slots,”
    IEEE Trans. Magn., vol. 47, no. 2, pp. 479–492, 2011.
    Test compute the Flux in FEMM, with and without symmetry
    and with MANATEE semi-analytical subdomain model
    """
    SPMSM_003 = load(join(DATA_DIR, "Machine", "SPMSM_003.json"))
    simu = Simu1(name="test_FEMM_compare_SPMSM_load", machine=SPMSM_003)

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
        OP=OPdq(N0=N0),
        time=time,
        Na_tot=Na_tot,
        angle_rotor_initial=0.5216 + pi,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=2, type_BH_rotor=2, is_periodicity_a=False, nb_worker=cpu_count()
    )
    simu.force = None
    simu.struct = None
    # Copy the simu and activate the symmetry
    assert SPMSM_003.comp_periodicity_spatial() == (1, True)
    simu_sym = Simu1(init_dict=simu.as_dict())
    simu_sym.mag.is_periodicity_a = True

    # Just load the Output and ends (we could also have directly filled the Output object)
    simu_load = Simu1(init_dict=simu.as_dict())
    simu_load.mag = None
    mat_file = join(TEST_DATA_DIR, "EM_SPMSM_FL_001_MANATEE_SDM.mat")
    Br = ImportMatlab(file_path=mat_file, var_name="XBr")
    Bt = ImportMatlab(file_path=mat_file, var_name="XBt")
    simu_load.input = InputFlux(
        time=time,
        Na_tot=Na_tot,
        B_dict={"B_{rad}": Br, "B_{circ}": Bt},
        Is=Is,
        Ir=None,  # No winding on the rotor
        OP=OPdq(N0=simu.input.OP.N0),
    )
    out = simu.run()

    out2 = simu_sym.run()

    out3 = simu_load.run()

    # Plot the result by comparing the two simulation (sym / no sym)
    plt.close("all")

    out.mag.B.plot_2D_Data(
        "angle{°}",
        data_list=[out2.mag.B],
        legend_list=["No symmetry", "1/2 symmetry"],
        save_path=join(save_path, "test_FEMM_compare_SPMSM_load_sym.png"),
        is_show_fig=False,
        **dict_2D
    )

    # Plot the result by comparing the two simulation (sym / MANATEE)
    plt.close("all")

    out.mag.B.plot_2D_Data(
        "angle{°}",
        data_list=[out3.mag.B],
        legend_list=["No symmetry", "MANATEE SDM"],
        save_path=join(save_path, "test_FEMM_compare_SPMSM_load_SDM.png"),
        is_show_fig=False,
        **dict_2D
    )


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_SPMSM_noload():
    """Validation of External Rotor SPMSM
    Open circuit (Null Stator currents)

    Machine B from Vu Xuan Hung thesis
    "Modeling of exterior rotor permanent magnet machines with concentrated windings"
    Hanoi university of science and technology 2012
    Test compute the Flux in FEMM, with and without symmetry
    and with MANATEE semi-analytical subdomain model
    """

    SPMSM_015 = load(join(DATA_DIR, "Machine", "SPMSM_015.json"))
    simu = Simu1(name="test_FEMM_compare_SPMSM_noload", machine=SPMSM_015)

    # Definition of the enforced output of the electrical module
    N0 = 3000
    Is = ImportMatrixVal(value=array([[0, 0, 0]]))
    time = ImportGenVectLin(start=0, stop=0, num=1, endpoint=True)
    angle = ImportGenVectLin(start=0, stop=2 * 2 * pi / 9, num=2043, endpoint=False)

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        OP=OPdq(N0=N0),
        time=time,
        angle=angle,
        angle_rotor_initial=0,
    )

    # Definition of the magnetic simulation (is_mmfr=False => no flux from the magnets)
    assert SPMSM_015.comp_periodicity_spatial() == (9, False)
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
    simu_load.input = InputFlux(
        time=time,
        angle=angle2,
        B_dict={"B_{rad}": Br, "B_{circ}": Bt},
        Is=Is,
        Ir=None,  # No winding on the rotor
        OP=OPdq(N0=simu.input.OP.N0),
    )

    out = simu.run()

    out3 = simu_load.run()

    plt.close("all")

    out.mag.B.plot_2D_Data(
        "angle{°}",
        data_list=[out3.mag.B],
        legend_list=["Symmetry", "MANATEE SDM"],
        save_path=join(save_path, "test_FEMM_compare_SPMSM_noload.png"),
        is_show_fig=False,
        **dict_2D
    )


if __name__ == "__main__":
    test_FEMM_compare_IPMSM_xxx()
    test_FEMM_compare_IPMSM_xxx_lam_sym()
    # test_FEMM_compare_Prius()
    # test_FEMM_compare_SCIM()
    # test_FEMM_compare_SIPMSM()
    # test_SPMSM_load()
    # test_SPMSM_noload()

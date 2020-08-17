from numpy import ones, pi, array, zeros, linspace, cos
from os.path import join
import matplotlib.pyplot as plt
from Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.InputFlux import InputFlux
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportMatlab import ImportMatlab

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
from Tests import TEST_DATA_DIR
import pytest

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

SynRM_001 = load(join(DATA_DIR, "Machine", "SynRM_001.json"))


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_Magnetic_Phi0():
    """Validation of a SynRM machine from Syr-e r29 open source software
    https://sourceforge.net/projects/syr-e/
    Test compute the Torque in FEMM as a function of Phi0
    and compare the results with Syr-e r29
    """
    # The aim of this validation test is to compute the torque as a function of Phi0
    # As (for now) there is no electrical model, we will compute the current for each Phi0 here
    freq0 = 50  # supply frequency [Hz]
    qs = 3  # Number of phases
    p = 2  # Number of pole pairs
    Nt_tot = 3  # Number of time step for each current angle Phi0
    Imax = 28.6878  # Nominal stator current magnitude [A]
    # to have one torque ripple period since torque ripple appears at multiple of 6*freq0
    Nrev = 1 / 6
    time = linspace(0, Nrev * p / freq0 * (1 - 1 / Nt_tot), Nt_tot)

    Phi0 = (
        array(
            [
                0.0,
                15.0,
                30.0,
                45.0,
                60.0,
                67.5,
                75.0,
                85.0,
                90.0,
                95.0,
                105.0,
                120.0,
                135.0,
                150.0,
                165.0,
                180.0,
            ]
        )
        * pi
        / 180
    )
    Is_list = list()
    for Phi in Phi0:
        Is = zeros((Nt_tot, qs))
        for q in range(qs):
            Is[:, q] = Imax * cos(2 * pi * freq0 * time - q * 2 * pi / qs + Phi)
        Is_list.append(Is)

    # Definition of the main simulation
    simu = Simu1(name="EM_SynRM_FL_001", machine=SynRM_001)
    time_obj = ImportMatrixVal(value=time)
    angle = ImportGenVectLin(start=0, stop=2 * pi, num=2016, endpoint=False)
    alpha_rotor = ImportMatrixVal(value=array([0, pi / 9, 2 * pi / 9]) + 2.6180)

    simu.input = InputCurrent(
        Is=None,
        Ir=None,  # No winding on the rotor
        N0=None,
        angle_rotor=alpha_rotor,
        time=time_obj,
        angle=angle,
        angle_rotor_initial=0,
    )

    # Definition of the magnetic simulation (1/2 symmetry)
    assert SynRM_001.comp_sym() == (2, True)
    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_symmetry_a=True,
        is_antiper_a=True,
        sym_a=2,
    )
    simu.force = None
    simu.struct = None
    # Expected results
    Tem = [
        0.08,
        7.09,
        13.95,
        19.75,
        23.75,
        23.63,
        21.62,
        8.7655,
        -0.21,
        -8.8544,
        -21.316,
        -23.73,
        -20.20,
        -13.99,
        -7.5445,
        0.08,
    ]
    Tem_FEMM = zeros(Phi0.shape)
    for ii, I in enumerate(Is_list):
        simu.input.Is = ImportMatrixVal(value=I)
        out = Output(simu=simu)
        simu.run()
        print("test_EM_SynRM_FL_001: " + str(ii + 1) + "/16")
        Tem_FEMM[ii] = out.mag.Tem_av

    fig, ax = plt.subplots()
    ax.set_title("Torque as a function of Phi0")
    ax.set_xlabel("Phi0 [rad]")
    ax.set_ylabel("Torque [N.m]")
    ax.plot(Phi0, Tem_FEMM, "r", label="FEMM")
    ax.plot(Phi0, Tem, "b--", label="Syr-e")

    fig.savefig(join(save_path, "test_EM_SynRM_FL_001.png"))

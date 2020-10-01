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
from pyleecan.Classes.ForceMT import ForceMT

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
from Tests import TEST_DATA_DIR
import pytest
import json

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_Magnetic_AGSF():
    """Validation of a SynRM machine from Syr-e r29 open source software
    https://sourceforge.net/projects/syr-e/
    Test compute air-gap surface force with Maxwell Tensor and load the results
    """
    # The aim of this validation test is to compute the torque as a function of Phi0
    # As (for now) there is no electrical model, we will compute the current for each Phi0 here
    SynRM_001 = load(join(DATA_DIR, "Machine", "SynRM_001.json"))
    freq0 = 50  # supply frequency [Hz]
    qs = 3  # Number of phases
    p = 2  # Number of pole pairs
    Nt_tot = 2 ** 6  # Number of time step for each current angle Phi0
    Imax = 28.6878  # Nominal stator current magnitude [A]
    # to have one torque ripple period since torque ripple appears at multiple of 6*freq0
    Nrev = 1
    time = linspace(0, Nrev * p / freq0 * (1 - 1 / Nt_tot), Nt_tot)

    Is = zeros((Nt_tot, qs))
    for q in range(qs):
        Is[:, q] = Imax * cos(2 * pi * freq0 * time - q * 2 * pi / qs)

    # Definition of the main simulation
    simu = Simu1(name="FM_SynRM_FL_001", machine=SynRM_001)
    time_obj = ImportMatrixVal(value=time)
    angle = ImportGenVectLin(start=0, stop=2 * pi, num=2016, endpoint=False)
    alpha_rotor = ImportGenVectLin(start=0, stop=2 * pi, num=Nt_tot, endpoint=False)

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
    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_symmetry_a=True,
        is_antiper_a=True,
        sym_a=2,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.force = ForceMT()

    simu.struct = None

    simu.input.Is = ImportMatrixVal(value=Is)
    out = Output(simu=simu)
    simu.run()

    # Test save with MeshSolution object in out
    out.save(save_path=save_path + "\Output.json")

    # Plot the AGSF as a function of space with the spatial fft
    r_max = 78
    out.plot_A_space("force.P", is_fft=True, r_max=r_max)
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_FM_SynRM_FL_001_plot_force_space"))

    # Plot the AGSF as a function of time with the time fft
    freq_max = 1000
    out.plot_A_time("force.P", alpha=0, is_fft=True, freq_max=freq_max)
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_FM_SynRM_FL_001_plot_force_time"))

    # # Plot the AGSF as a function of space with the spatial fft
    # out.plot_A_space("force.Ptan", is_fft=True, r_max=r_max)

    # # Plot the AGSF as a function of time with the time fft
    # out.plot_A_time("force.Ptan", alpha=0, is_fft=True, freq_max=freq_max)

    # ------------------------------------------------------

    load_path = join(save_path, "Output.json")

    # Test to load the Meshsolution object (inside the output):
    with open(load_path) as json_file:
        json_tmp = json.load(json_file)
        out = Output(init_dict=json_tmp)

    # Plot the AGSF as a function of space with the spatial fft
    r_max = 78
    out.plot_A_space(
        "force.P",
        is_fft=True,
        r_max=r_max,
        fund_harm=0,
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_space"),
    )

    # Plot the AGSF as a function of time with the time fft
    freq_max = 1000
    out.plot_A_time(
        "force.P",
        alpha=0,
        is_fft=True,
        freq_max=freq_max,
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_time"),
    )

    out.plot_A_fft2(
        "force.P",
        component_list=["radial"],
        freq_max=freq_max,
        r_max=r_max,
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_fft2"),
    )

    out.plot_A_cfft2(
        "force.P",
        component_list=["radial"],
        freq_max=freq_max,
        r_max=r_max,
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_cfft2"),
    )

    out.plot_A_time_space(
        "force.P",
        component_list=["radial"],
        freq_max=freq_max,
        r_max=r_max,
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_force_time_space"),
    )
    out.plot_A_time_space(
        "mag.B",
        component_list=["radial"],
        freq_max=freq_max,
        r_max=r_max,
        save_path=join(save_path, "test_FM_SynRM_FL_001_plot_flux_time_space"),
    )
    # ------------------------------------------------------

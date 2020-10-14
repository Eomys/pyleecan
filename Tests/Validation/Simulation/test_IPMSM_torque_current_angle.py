# Load the machine
import sys
from os.path import dirname, abspath, normpath, join
import matplotlib.pyplot as plt

sys.path.insert(0, normpath(abspath(join(dirname(__file__), "..", "..", ".."))))
sys.path.insert(0, normpath(abspath(dirname(__file__))))

from pyleecan.Functions.Plot.plot_A_2D import plot_A_2D
from pyleecan.definitions import config_dict
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from os.path import join
from pyleecan.Classes.import_all import *
from numpy import ones, zeros, linspace, pi, array, sqrt
from Tests import save_validation_path as save_path
import pytest


@pytest.mark.FEMM
@pytest.mark.long
def test_OP():
    IPMSM_A = load(join(DATA_DIR, "Machine", "IPMSM_A.json"))

    # Initialization of the Simulation
    simu = Simu1(name="tuto_Id_Iq", machine=IPMSM_A)

    # Definition of the magnetic simulation (FEMM with symmetry and sliding band)
    simu.mag = MagFEMM(
        is_periodicity_a=True,
        Kgeo_fineness=1,
    )
    # Run only Magnetic module
    simu.elec = None
    simu.force = None
    simu.struct = None

    # Definition of a sinusoidal current
    simu.input = InputCurrent()
    simu.input.Id_ref = -100  # [A]
    simu.input.Iq_ref = 200  # [A]

    simu.input.Nt_tot = 3  # Number of time step
    simu.input.Na_tot = 2048  # Spatial discretization
    simu.input.N0 = 2000  # Rotor speed [rpm]

    varload = VarLoadCurrent(is_torque=True)
    varload.type_OP_matrix = 0  # Matrix N0, I0, Phi0, Tem_ref

    N_simu = 13
    # creating the Operating point matrix
    OP_matrix = zeros((N_simu, 4))
    # Set N0 = 2000 [rpm] for all simulation
    OP_matrix[:, 0] = 2000 * ones((N_simu))
    # Set I0 = 250 [A] for all simulation
    OP_matrix[:, 1] = 250 * ones((N_simu)) / sqrt(2)
    # Set Phi0 from 60° to 180° (i.e from -30° to 90° degree with respect to q-axis as specified in original publication)
    OP_matrix[:, 2] = linspace(60 * pi / 180, 180 * pi / 180, N_simu)
    # Set reference torque from Yang et al, 2013
    OP_matrix[:, 3] = array(
        [79, 125, 160, 192, 237, 281, 319, 343, 353, 332, 266, 164, 22]
    )
    varload.OP_matrix = OP_matrix
    print(OP_matrix)

    simu.var_simu = varload
    Xout = simu.run()

    print("Values available in XOutput:")
    print(Xout.xoutput_dict.keys())

    print("\nI0 for each simulation:")
    print(Xout["I0"].result)
    print("\nPhi0 for each simulation:")
    print(Xout["Phi0"].result)

    fig = Xout.plot_multi("Phi0", "Tem_av")
    fig.savefig(join(save_path, "test_IPMSM_A_Tem.png"))

    fig = Xout.plot_multi("Id", "Iq")
    fig.savefig(join(save_path, "test_IPMSM_A_Id_Iq.png"))

    curve_colors = config_dict["PLOT"]["COLOR_DICT"]["CURVE_COLORS"]

    plot_A_2D(
        array([x * 180 / pi for x in Xout.xoutput_dict["Phi0"].result]),
        [Xout.xoutput_dict["Tem_av"].result, Xout.xoutput_dict["Tem_av_ref"].result],
        color_list=curve_colors,
        legend_list=["Pyleecan", "Yang et al, 2013"],
        xlabel="Current angle [°]",
        ylabel="Electrical torque [N.m]",
        title="Electrical torque vs current angle",
    )
    fig = plt.gcf()
    fig.savefig(join(save_path, "test_IPMSM_torque_validation.png"))

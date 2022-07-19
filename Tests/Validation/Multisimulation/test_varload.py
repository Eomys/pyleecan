# Load the machine
import sys
from os.path import dirname, abspath, normpath, join

from pyleecan.Classes.OPdq import OPdq
import pytest

from numpy import ones, zeros, linspace, pi, array, sqrt, arange, exp
from multiprocessing import cpu_count

from SciDataTool.Functions.Plot.plot_2D import plot_2D
from pyleecan.definitions import config_dict
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from os.path import join
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Classes.DataKeeper import DataKeeper
from Tests import save_validation_path as save_path


@pytest.mark.MagFEMM
@pytest.mark.ForceMT
@pytest.mark.long_5s
@pytest.mark.IPMSM
@pytest.mark.VarLoadCurrent
@pytest.mark.periodicity
def test_varload():

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    # Initialization of the Simulation
    simu = Simu1(name="test_varload", machine=Toyota_Prius)

    # Definition of the magnetic simulation (FEMM with symmetry and sliding band)
    simu.mag = MagFEMM(
        is_periodicity_a=True, is_periodicity_t=True, nb_worker=cpu_count(),
    )
    # Run only Magnetic module
    simu.elec = None
    simu.force = None
    simu.struct = None

    # Definition of a sinusoidal current
    simu.input = InputCurrent()
    I0_rms = 250 / sqrt(2)
    Phi0 = 140 * pi / 180  # Maximum Torque Per Amp
    Id_ref = (I0_rms * exp(1j * Phi0)).real
    Iq_ref = (I0_rms * exp(1j * Phi0)).imag
    Tem_av_ref = array(
        [79, 125, 160, 192, 237, 281, 319, 343, 353, 332, 266, 164, 22]
    )  # Yang et al, 2013
    Phi0_ref = linspace(60 * pi / 180, 180 * pi / 180, Tem_av_ref.size)

    # Choose which operating points to run
    step = 2  # step=1 to do all OP
    # step=2 to do 1 OP out of 2 (fastest)
    I_simu = arange(0, Tem_av_ref.size, step)
    N_simu = I_simu.size

    I0_rms = 250 / sqrt(2)

    simu.input.Nt_tot = 8 * 5  # Number of time step
    simu.input.Na_tot = 2048  # Spatial discretization
    simu.input.OP = OPdq(N0=2000)

    simu.var_simu = VarLoadCurrent()
    # Matrix N0, I0, Phi0, Tem_ref
    # creating the Operating point matrix
    OP_matrix = zeros((N_simu, 4))
    # Set N0 = 2000 [rpm] for all simulation
    OP_matrix[:, 0] = 2000 * ones((N_simu))
    # Set I0 = 250/sqrt(2) [Arms] for all simulation
    OP_matrix[:, 1] = I0_rms * ones((N_simu))
    # Set Phi0 from 60° to 180°
    OP_matrix[:, 2] = Phi0_ref[I_simu]
    # Set reference torque from Yang et al, 2013
    OP_matrix[:, 3] = Tem_av_ref[I_simu]
    simu.var_simu.set_OP_array(
        OP_matrix, "N0", "I0", "Phi0", "Tem",
    )

    # Datakeepers
    I0_dk = DataKeeper(
        name="Stator current rms amplitude",
        symbol="I0",
        unit="Arms",
        keeper="lambda output: output.elec.OP.get_I0_Phi0()['I0']",
    )
    Phi0_dk = DataKeeper(
        name="Stator current phase",
        symbol="Phi0",
        unit="rad",
        keeper="lambda output: output.elec.OP.get_I0_Phi0()['Phi0']",
    )
    # Airgap flux density Datakeeper
    B_dk = DataKeeper(
        name="Airgap Flux Density", symbol="B", unit="T", keeper="lambda out: out.mag.B"
    )

    # Stator Winding Flux Datakeeper
    Phi_wind_stator_dk = DataKeeper(
        name="Stator Winding Flux",
        symbol="Phi_{wind}",
        unit="Wb",
        keeper="lambda out: out.mag.Phi_wind_stator",
    )

    # Instanteneous torque Datakeeper
    Tem_dk = DataKeeper(
        name="Electromagnetic torque",
        symbol="T_{em}",
        unit="N.m",
        keeper="lambda out: out.mag.Tem",
    )
    # Store Datakeepers
    simu.var_simu.datakeeper_list = [I0_dk, Phi0_dk, B_dk, Phi_wind_stator_dk, Tem_dk]

    Xout = simu.run()

    print("Values available in XOutput:")
    print(Xout.xoutput_dict.keys())

    print("\nI0 for each simulation:")
    print(Xout["I0"].result)
    print("\nPhi0 for each simulation:")
    print(Xout["Phi0"].result)

    Xout.plot_multi(
        "Phi0",
        "Tem_av",
        is_show_fig=False,
        save_path=join(save_path, "EM_FEMM_IPMSM_varload_Tem.png"),
    )
    # fig.savefig(join(save_path, "EM_FEMM_IPMSM_varload_Tem.png"))

    Xout.plot_multi(
        "Id",
        "Iq",
        is_show_fig=False,
        save_path=join(save_path, "EM_FEMM_IPMSM_varload_Id_Iq.png"),
    )
    # fig.savefig(join(save_path, "EM_FEMM_IPMSM_varload_Id_Iq.png"))

    curve_colors = config_dict["PLOT"]["COLOR_DICT"]["COLOR_LIST"]

    plot_2D(
        array([x * 180 / pi for x in Xout.xoutput_dict["Phi0"].result]),
        [Xout.xoutput_dict["Tem_av"].result, Xout.xoutput_dict["Tem_av_ref"].result],
        color_list=curve_colors,
        legend_list=["Pyleecan", "Yang et al, 2013"],
        xlabel="Current angle [°]",
        ylabel="Electrical torque [N.m]",
        title="Electrical torque vs current angle",
        save_path=join(save_path, "EM_FEMM_IPMSM_varload_torque_validation.png"),
        is_show_fig=False,
    )

    Xout.print_memory(detail_level=4)
    return Xout


if __name__ == "__main__":
    Xout = test_varload()

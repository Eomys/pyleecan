from os.path import join
from multiprocessing import cpu_count
import pytest
from numpy import array, ones, pi, zeros, sqrt
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Classes.DataKeeper import DataKeeper
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load
from SciDataTool.Functions.Plot.plot_2D import plot_2D
from Tests import save_validation_path as save_path
from pyleecan.definitions import config_dict


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.SynRM
@pytest.mark.VarLoadCurrent
@pytest.mark.periodicity
def test_FEMM_torque():
    """Validation of a SynRM machine from Syr-e r29 open source software
    https://sourceforge.net/projects/syr-e/
    Test compute the Torque in FEMM as a function of Phi0
    and compare the results with Syr-e r29
    """
    # The aim of this validation test is to compute the torque as a function of Phi0
    # As (for now) there is no electrical model, we will compute the current for each Phi0 here
    SynRM_001 = load(join(DATA_DIR, "Machine", "SynRM_001.json"))
    felec = 50  # supply frequency [Hz]
    Nt_tot = 3  # Number of time step for each current angle Phi0
    Imax = 28.6878 / sqrt(2)  # RMS stator current magnitude [A]
    # to have one torque ripple period since torque ripple appears at multiple of 6*felec
    p = SynRM_001.stator.get_pole_pair_number()
    N0 = 60 * felec / p

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

    # Definition of the main simulation
    simu = Simu1(name="test_FEMM_torque", machine=SynRM_001)
    Na_tot = 2016
    simu.input = InputCurrent(
        Is=None,
        Ir=None,  # No winding on the rotor
        OP=OPdq(N0=N0, felec=felec),
        Nt_tot=Nt_tot,
        Nrev=1 / 6,
        Na_tot=Na_tot,
    )
    simu.var_simu = VarLoadCurrent(is_reuse_femm_file=True)

    # Matrix N0, I0, Phi0, Tem_ref
    N_simu = Phi0.size
    OP_matrix = zeros((N_simu, 4))
    OP_matrix[:, 0] = ones(N_simu) * N0
    OP_matrix[:, 1] = ones(N_simu) * Imax
    OP_matrix[:, 2] = Phi0
    OP_matrix[:, 3] = Tem
    simu.var_simu.set_OP_array(
        OP_matrix, "N0", "I0", "Phi0", "Tem", input_index=0, is_update_input=True
    )

    # Definition of the magnetic simulation (1/2 symmetry)
    assert SynRM_001.comp_periodicity_spatial() == (2, True)
    simu.mag = MagFEMM(
        type_BH_stator=0,
        type_BH_rotor=0,
        is_periodicity_a=True,
        is_periodicity_t=False,
        nb_worker=cpu_count(),
    )
    simu.force = None
    simu.struct = None
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
    simu.var_simu.datakeeper_list = [I0_dk, Phi0_dk]
    Xout = simu.run()

    curve_colors = config_dict["PLOT"]["COLOR_DICT"]["CURVE_COLORS"]
    plot_2D(
        array([x * 180 / pi for x in Xout.xoutput_dict["Phi0"].result]),
        [Xout.xoutput_dict["Tem_av"].result, Xout.xoutput_dict["Tem_av_ref"].result],
        color_list=curve_colors,
        legend_list=["Pyleecan", "Syr-e r29"],
        xlabel="Current angle [°]",
        ylabel="Electrical torque [N.m]",
        title="Electrical torque vs current angle",
        save_path=join(save_path, "test_FEMM_torque.png"),
        is_show_fig=False,
    )

    return Xout


if __name__ == "__main__":
    Xout = test_FEMM_torque()

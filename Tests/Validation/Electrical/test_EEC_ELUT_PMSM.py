from os.path import join

from Tests import save_validation_path as save_path, TEST_DATA_DIR
from numpy import sqrt, pi
from multiprocessing import cpu_count

import pytest
from pyleecan.Classes.ImportGenPWM import ImportGenPWM
from pyleecan.Classes.InputVoltage import InputVoltage
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.PostLUT import PostLUT
from pyleecan.Classes.DataKeeper import DataKeeper
from pyleecan.Classes.ImportMatrixXls import ImportMatrixXls
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_ANL import EEC_ANL

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.definitions import DATA_DIR

is_show_fig = False


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.EEC_PMSM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.skip(reason="Work in progress")
def test_EEC_ELUT_PMSM():
    """Validation of the PMSM Electrical Equivalent Circuit with the Prius machine"""

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    # Generate ELUT
    simu = Simu1(name="test_LUT_PMSM", machine=Toyota_Prius)

    # Definition of the input
    simu.input = InputCurrent(
        Nt_tot=8 * 10,
        Na_tot=8 * 200,
        OP=OPdq(N0=1000, Id_ref=0, Iq_ref=0),
    )

    # Load OP_matrix
    OP_matrix = (
        ImportMatrixXls(
            file_path=join(TEST_DATA_DIR, "OP_ELUT_PMSM.xlsx"), sheet="Feuil1"
        )
        .get_data()
        .astype(float)
    )

    # Set varspeed simulation
    simu.var_simu = VarLoadCurrent(
        type_OP_matrix=1,
        OP_matrix=OP_matrix,
        is_keep_all_output=True,
        stop_if_error=True,
    )

    # Define second simu for FEMM comparison
    simu.mag = MagFEMM(is_periodicity_a=True, is_periodicity_t=True, nb_worker=4)

    # Stator Winding Flux along dq Datakeeper
    Phi_wind_dk = DataKeeper(
        name="Stator Winding Flux",
        symbol="Phi_{wind}",
        unit="Wb",
        keeper="lambda out: out.mag.Phi_wind_stator",
    )

    # Store Datakeepers
    simu.var_simu.datakeeper_list = [Phi_wind_dk]

    # Postprocessing
    simu.var_simu.postproc_list = [PostLUT()]

    out = simu.run()

    ELUT = out.simu.var_simu.postproc_list[0].LUT

    # Simu with EEC using ELUT
    fmax = 20000
    fswi = 7000
    Vdc1 = 1000  # Bus voltage
    U0 = 800  # Phase voltage
    simu_EEC = Simu1(name="test_LUT_PMSM", machine=Toyota_Prius)

    # Definition of the input
    simu_EEC.input = InputVoltage(
        Na_tot=1024,
        Nt_tot=1024,
        PWM=ImportGenPWM(fmax=fmax, fswi=fswi, Vdc1=Vdc1, U0=U0),
        OP=OPdq(N0=1000, Id_ref=50, Iq_ref=100, Ud_ref=200, Uq_ref=300),
    )

    simu_EEC.elec = Electrical(eec=EEC_ANL(), ELUT_enforced=ELUT)

    out_EEC = simu_EEC.run()

    # Plot 3-phase current function of time
    out.mag.Phi_wind_stator.plot_2D_Data(
        "time",
        "phase[]",
        save_path=join(save_path, "EEC_FEMM_IPMSM_currents.png"),
        is_show_fig=is_show_fig,
        **dict_2D
    )

    out_EEC.elec.Is_harm.plot_2D_Data(
        "freqs",
        save_path=join(save_path, "EEC_FEMM_IPMSM_Is_harm.png"),
        is_show_fig=is_show_fig,
        **dict_2D
    )

    return out, out_EEC


# To run it without pytest
if __name__ == "__main__":
    out, out_EEC = test_EEC_ELUT_PMSM()

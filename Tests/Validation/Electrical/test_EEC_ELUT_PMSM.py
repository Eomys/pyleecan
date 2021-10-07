from os.path import join

from Tests import save_validation_path as save_path, TEST_DATA_DIR
from numpy import sqrt, pi
from multiprocessing import cpu_count

import pytest

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.PostELUT import PostELUT
from pyleecan.Classes.DataKeeper import DataKeeper
from pyleecan.Classes.ImportMatrixXls import ImportMatrixXls

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.definitions import DATA_DIR


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.EEC_PMSM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.skip(reason="Work in progress")
def test_ELUT_PMSM():
    """Validation of the PMSM Electrical Equivalent Circuit with the Prius machine
    Compute Torque from EEC results and compare with Yang et al, 2013
    """

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    simu = Simu1(name="test_ELUT_PMSM", machine=Toyota_Prius)

    # Definition of the input
    simu.input = InputCurrent(
        N0=1000, Nt_tot=8 * 80, Na_tot=8 * 200, Id_ref=0, Iq_ref=0
    )

    # Load OP_matrix
    OP_matrix = ImportMatrixXls(
        file_path=join(TEST_DATA_DIR, "OP_ELUT_PMSM.xlsx"), sheet="Feuil1"
    ).get_data()

    # Set varspeed simulation
    simu.var_simu = VarLoadCurrent(
        type_OP_matrix=1, OP_matrix=OP_matrix, is_keep_all_output=True
    )

    # Define second simu for FEMM comparison
    simu.mag = MagFEMM(is_periodicity_a=True, is_periodicity_t=True, nb_worker=4)

    # Stator Winding Flux along dq Datakeeper
    Phi_wind_dq_dk = DataKeeper(
        name="Stator Winding Flux along dq axes",
        symbol="Phi_{dq}",
        unit="Wb",
        keeper="lambda out: out.mag.comp_Phi_dq()",
    )

    # Store Datakeepers
    simu.var_simu.datakeeper_list = [Phi_wind_dq_dk]

    # Postprocessing
    simu.var_simu.postproc_list = [PostELUT()]

    out = simu.run()

    # Plot 3-phase current function of time
    out.mag.Phi_wind_stator.plot_2D_Data(
        "time",
        "phase[]",
        # save_path=join(save_path, "EEC_FEMM_IPMSM_currents.png"),
        # is_show_fig=False,
        **dict_2D
    )

    return out


# To run it without pytest
if __name__ == "__main__":
    out = test_ELUT_PMSM()

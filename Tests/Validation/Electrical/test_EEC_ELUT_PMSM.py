from os.path import join

from Tests import save_validation_path as save_path
from numpy import sqrt, pi
from multiprocessing import cpu_count

import pytest

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.PostELUT import PostELUT
from pyleecan.Classes.DataKeeper import DataKeeper

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.definitions import DATA_DIR


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.EEC_PMSM
@pytest.mark.IPMSM
@pytest.mark.periodicity
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

    # Set varspeed simulation
    simu.var_simu = VarLoadCurrent(type_OP_matrix=1, OP_matrix=OP_matrix)

    # Define second simu for FEMM comparison
    simu.mag = MagFEMM(is_periodicity_a=True, is_periodicity_t=True, nb_worker=4)

    # Datakeepers
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
    simu.var_simu.datakeeper_list = [Phi_wind_stator_dk, Tem_dk]

    # Postprocessing
    simu.var_simu.postproc_list = [PostELUT()]

    out = simu.run()

    # Definition of the magnetic simulation (FEMM)

    # out2 = Output(simu=simu2)
    # simu2.run()

    # # Plot 3-phase current function of time
    # out.elec.get_Is().plot_2D_Data(
    #     "time",
    #     "phase[]",
    #     save_path=join(save_path, "EEC_FEMM_IPMSM_currents.png"),
    #     is_show_fig=False,
    #     **dict_2D
    # )

    # # from Yang et al, 2013
    # assert out.elec.Tem_av_ref == pytest.approx(81.81, rel=0.1)
    # assert out2.mag.Tem_av == pytest.approx(81.70, rel=0.1)

    return out, out2


# To run it without pytest
if __name__ == "__main__":
    out, out2 = test_ELUT_PMSM()

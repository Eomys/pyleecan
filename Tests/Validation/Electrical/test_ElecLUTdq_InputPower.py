from os.path import join

from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputPower import InputPower
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Classes.PostLUT import PostLUT
from pyleecan.Classes.ElecLUTdq import ElecLUTdq
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.LossFEMM import LossFEMM

from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR


def test_ElecLUTdq_InputPower():
    """Test to calculate Id/Iq in Toyota_Prius using InputPower
    to get requested power while minimizing losses"""

    machine = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    LUT_enforced = load("LUT.h5")

    # First simulation creating femm file
    simu = Simu1(name="test_ElecLUTdq_InputPower", machine=machine)

    # Initialization of the simulation starting point
    simu.input = InputPower(
        OP=OPdq(N0=1000, Pem_av_ref=3.5e4),
        Nt_tot=20 * 8,
        Na_tot=200 * 8,
        is_periodicity_a=True,
        is_periodicity_t=True,
        U_max=500,
        J_max=6e6,
    )

    simu.elec = ElecLUTdq(
        n_interp=100,
        n_Id=2,
        n_Iq=2,
        Id_max=0,
        Iq_min=0,
        LUT_enforced=LUT_enforced,
        LUT_simu=Simu1(
            input=InputCurrent(
                OP=OPdq(),
                Nt_tot=20 * 8,
                Na_tot=200 * 8,
                is_periodicity_a=True,
                is_periodicity_t=True,
            ),
            var_simu=VarLoadCurrent(
                type_OP_matrix=1,
                postproc_list=[PostLUT(is_save_LUT=True)],
                is_keep_all_output=True,
            ),
            mag=MagFEMM(
                is_periodicity_a=True,
                is_periodicity_t=True,
                nb_worker=4,
                is_get_meshsolution=True,
            ),
            loss=LossFEMM(
                Ce=0.53,  # eddy current loss coefficients [W/(m^3*T^2*Hz^2)]
                Cp=1,  # proximity loss coefficient
                Ch=143,  # hysteresis loss coefficient [W/(m^3*T^2*Hz)]
                # is_get_meshsolution=True,
                Tsta=100,
            ),
        ),
    )

    out = simu.run()

    return out


# To run it without pytest
if __name__ == "__main__":
    out = test_ElecLUTdq_InputPower()

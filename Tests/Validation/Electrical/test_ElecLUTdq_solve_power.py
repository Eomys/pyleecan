from os.path import join

import numpy as np

import pytest

from SciDataTool.Functions.Plot.plot_3D import plot_3D
from pyleecan.Classes.LossModelSteinmetz import LossModelSteinmetz

from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputVoltage import InputVoltage
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent
from pyleecan.Classes.PostLUT import PostLUT
from pyleecan.Classes.ElecLUTdq import ElecLUTdq
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.LossFEMM import LossFEMM

from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR


@pytest.mark.skip(reason="Work in progress")
def test_ElecLUTdq_solve_power():
    """Test to calculate Id/Iq in Toyota_Prius using solve_power
    to get requested power while minimizing losses"""

    machine = load(join(DATA_DIR, "Machine", "Toyota_Prius_loss.json"))

    # LUT_enforced = load("C:/pyleecan/pyleecan_B/pyleecan/pyleecan/Results/LUT.h5")
    LUT_enforced = None

    # First simulation creating femm file
    simu = Simu1(name="test_ElecLUTdq_solve_power", machine=machine)

    # Initialization of the simulation starting point
    simu.input = InputVoltage(
        OP=OPdq(N0=1200, Pem_av_ref=5e4),
        Nt_tot=4 * 8,
        Na_tot=200 * 8,
        is_periodicity_a=True,
        is_periodicity_t=True,
    )

    k_hy = 0.011381
    k_ed = 4.67e-5
    alpha_f = 1.1499
    alpha_B = 1.7622
    Cprox = 1  # Neglecting proximity effect

    loss_model = LossModelSteinmetz(
        k_hy=k_hy, k_ed=k_ed, alpha_f=alpha_f, alpha_B=alpha_B
    )

    simu.elec = ElecLUTdq(
        Urms_max=800,
        Jrms_max=30e6,
        n_interp=100,
        n_Id=2,
        n_Iq=2,
        Id_max=0,
        Iq_min=0,
        LUT_enforced=LUT_enforced,
        is_grid_dq=True,
        LUT_simu=Simu1(
            input=InputCurrent(
                OP=OPdq(),
                Nt_tot=4 * 4 * 8,
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
                Cp=Cprox,
                is_get_meshsolution=True,
                Tsta=100,
                type_skin_effect=0,
                model_dict={"stator core": loss_model, "rotor core": loss_model},
            ),
        ),
    )

    out = simu.run()

    LUT_grid = out.simu.elec.LUT_enforced

    # Get Id_min, Id_max, Iq_min, Iq_max from OP_matrix
    OP_matrix = LUT_grid.get_OP_array("N0", "Id", "Iq")
    Id_min = OP_matrix[:, 1].min()
    Id_max = OP_matrix[:, 1].max()
    Iq_min = OP_matrix[:, 2].min()
    Iq_max = OP_matrix[:, 2].max()

    nd, nq = 100, 100
    Id_vect = np.linspace(Id_min, Id_max, nd)
    Iq_vect = np.linspace(Iq_min, Iq_max, nq)
    Id, Iq = np.meshgrid(Id_vect, Iq_vect)
    Id, Iq = Id.ravel(), Iq.ravel()

    # Interpolate Phid/Phiq on the refined mesh
    Phi_dqh_grid = LUT_grid.interp_Phi_dqh(Id, Iq)

    dict_map = {
        "Xdata": Id.reshape((nd, nq))[0, :],
        "Ydata": Iq.reshape((nd, nq))[:, 0],
        "xlabel": "d-axis current [Arms]",
        "ylabel": "q-axis current [Arms]",
        "type_plot": "pcolor",
        "is_contour": True,
    }

    # Plot Phi_d map
    plot_3D(
        Zdata=Phi_dqh_grid[0, :].reshape((nd, nq)).T,
        zlabel="$\Phi_d$ [Wb]",
        title="Flux linkage map in dq plane (d-axis)",
        **dict_map,
    )

    # Plot Phi_q map
    plot_3D(
        Zdata=Phi_dqh_grid[1, :].reshape((nd, nq)).T,
        zlabel="$\Phi_q$ [Wb]",
        title="Flux linkage map in dq plane (q-axis)",
        **dict_map,
    )

    return out


# To run it without pytest
if __name__ == "__main__":
    out = test_ElecLUTdq_solve_power()

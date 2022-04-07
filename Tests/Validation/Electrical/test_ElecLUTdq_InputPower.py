from os.path import join

import numpy as np


from SciDataTool.Functions.Plot.plot_3D import plot_3D


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

    LUT_enforced = load("C:/pyleecan/pyleecan_B/pyleecan/pyleecan/Results/LUT.h5")
    # LUT_enforced = None

    # First simulation creating femm file
    simu = Simu1(name="test_ElecLUTdq_InputPower", machine=machine)

    # Initialization of the simulation starting point
    simu.input = InputPower(
        OP=OPdq(N0=1200, Pem_av_ref=50e4),
        Nt_tot=20 * 8,
        Na_tot=200 * 8,
        is_periodicity_a=True,
        is_periodicity_t=True,
        U_max=500,
        J_max=30e6,
    )

    simu.elec = ElecLUTdq(
        n_interp=100,
        n_Id=3,
        n_Iq=3,
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
                Ce=0.53,  # eddy current loss coefficients [W/(m^3*T^2*Hz^2)]
                Cp=1,  # proximity loss coefficient
                Ch=143,  # hysteresis loss coefficient [W/(m^3*T^2*Hz)]
                # is_get_meshsolution=True,
                Tsta=100,
            ),
        ),
    )

    out = simu.run()

    LUT_grid = out.simu.elec.LUT_enforced

    # Get Id_min, Id_max, Iq_min, Iq_max from OP_matrix
    OP_matrix = LUT_grid.get_OP_matrix()
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

    simu.elec.is_grid_dq = False
    LUT_line = simu.elec.comp_LUTdq()

    # Interpolate Phid/Phiq on the refined mesh
    Phi_dqh_line = LUT_line.interp_Phi_dqh(Id, Iq)

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

    # Plot Phi_d map
    plot_3D(
        Zdata=Phi_dqh_line[0, :].reshape((nd, nq)).T,
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

    # Plot Phi_q map
    plot_3D(
        Zdata=Phi_dqh_line[1, :].reshape((nd, nq)).T,
        zlabel="$\Phi_q$ [Wb]",
        title="Flux linkage map in dq plane (q-axis)",
        **dict_map,
    )

    return out


# To run it without pytest
if __name__ == "__main__":
    out = test_ElecLUTdq_InputPower()

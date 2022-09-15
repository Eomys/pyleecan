from os.path import join

from numpy import sqrt, pi, linspace, array, zeros
from numpy.testing import assert_almost_equal

from multiprocessing import cpu_count

import pytest

from SciDataTool.Functions.Plot.plot_2D import plot_2D

from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_PMSM import EEC_PMSM
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D

from pyleecan.definitions import DATA_DIR

from Tests import save_validation_path as save_path

is_show_fig = False


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.EEC_PMSM
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_EEC_PMSM(nb_worker=int(0.5 * cpu_count())):
    """Validation of the PMSM Electrical Equivalent Circuit by comparing torque with MagFEMM"""

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    simu = Simu1(name="test_EEC_PMSM", machine=Toyota_Prius)

    # Definition of the input
    simu.input = InputCurrent(OP=OPdq(N0=2000), Nt_tot=8 * 16, Na_tot=2048)
    simu.input.set_Id_Iq(I0=250 / sqrt(2), Phi0=60 * pi / 180)

    # Definition of the magnetic simulation
    simu_mag = simu.copy()
    simu_mag.mag = MagFEMM(
        is_periodicity_a=True, is_periodicity_t=True, nb_worker=nb_worker, T_mag=60
    )

    # Definition of the electrical simulation
    simu.elec = Electrical()
    simu.elec.eec = EEC_PMSM(
        fluxlink=MagFEMM(
            is_periodicity_t=True, is_periodicity_a=True, nb_worker=nb_worker, T_mag=60,
        ),
    )

    out = simu.run()
    out_mag = simu_mag.run()

    # from Yang et al, 2013
    assert out.elec.Tem_av == pytest.approx(82.1, rel=0.1)
    assert out_mag.mag.Tem_av == pytest.approx(82, rel=0.1)

    # Plot 3-phase current function of time
    if is_show_fig:
        out.elec.get_Is().plot_2D_Data(
            "time",
            "phase[]",
            # save_path=join(save_path, "EEC_FEMM_IPMSM_currents.png"),
            # is_show_fig=False,
            **dict_2D
        )

    return out


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.EEC_PMSM
@pytest.mark.IPMSM
@pytest.mark.periodicity
def test_EEC_PMSM_sync_rel(nb_worker=int(0.5 * cpu_count())):
    """Validation of the PMSM Electrical Equivalent Circuit with the Prius machine
    Compute Torque from EEC results and compare with Yang et al, 2013
    """

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    simu = Simu1(name="test_EEC_PMSM_sync_rel", machine=Toyota_Prius)

    # Definition of the input
    simu.input = InputCurrent(
        OP=OPdq(N0=2000, Tem_av_ref=79), Nt_tot=8 * 16, Na_tot=2048
    )
    simu.input.set_Id_Iq(I0=250 / sqrt(2), Phi0=60 * pi / 180)

    # Definition of the simulation (FEMM)
    simu.elec = Electrical()
    simu.elec.eec = EEC_PMSM(
        fluxlink=MagFEMM(
            is_periodicity_t=True, is_periodicity_a=True, nb_worker=nb_worker, T_mag=60,
        ),
        type_skin_effect=0,
    )

    # Creating the Operating point matrix
    Tem_av_ref = array([79, 125, 160, 192, 237, 281, 319, 343, 353, 332, 266, 164, 22])
    N_simu = Tem_av_ref.size
    Phi0_ref = linspace(60 * pi / 180, 180 * pi / 180, N_simu)
    OP_matrix = zeros((N_simu, 4))
    # Set N0 = 2000 [rpm] for all simulation
    OP_matrix[:, 0] = 2000
    # Set I0 = 250/sqrt(2) [A] (RMS) for all simulations
    OP_matrix[:, 1] = 250 / sqrt(2)
    # Set Phi0 from 60 to 180
    OP_matrix[:, 2] = Phi0_ref
    # Set reference torque from Yang et al, 2013
    OP_matrix[:, 3] = Tem_av_ref

    simu.var_simu = VarLoadCurrent(is_keep_all_output=True)
    simu.var_simu.set_OP_array(
        OP_matrix, "N0", "I0", "Phi0", "Tem", input_index=0, is_update_input=True
    )

    out = simu.run()

    Tem_eec = [out_ii.elec.Tem_av for out_ii in out.output_list]

    Tem_sync = zeros(N_simu)
    Tem_rel = zeros(N_simu)
    for ii, out_ii in enumerate(out.output_list):
        Tem_sync[ii], Tem_rel[ii] = out_ii.elec.eec.comp_torque_sync_rel()

    Tem2 = Tem_sync + Tem_rel
    assert_almost_equal(Tem_eec - Tem2, 0, decimal=12)

    if is_show_fig:

        plot_2D(
            array([x * 180 / pi for x in out.xoutput_dict["Phi0"].result]),
            [Tem_eec, Tem_av_ref],
            legend_list=["Pyleecan", "Yang et al, 2013"],
            xlabel="Current angle [deg]",
            ylabel="Electrical torque [N.m]",
            title="Electrical torque vs current angle",
            **dict_2D
        )

        plot_2D(
            array([x * 180 / pi for x in out.xoutput_dict["Phi0"].result]),
            [Tem_eec, Tem_sync, Tem_rel],
            legend_list=["Overall", "Synchronous", "Reluctant"],
            xlabel="Current angle [deg]",
            ylabel="Electrical torque [N.m]",
            title="Electrical torque vs current angle",
            **dict_2D
        )

    return out


# To run it without pytest
if __name__ == "__main__":
    out = test_EEC_PMSM()
    out = test_EEC_PMSM_sync_rel()
    print("Done")

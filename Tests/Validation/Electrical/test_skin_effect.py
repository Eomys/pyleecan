from os.path import join

from numpy import sqrt, pi

import pytest

from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.Electrical import Electrical
from pyleecan.Classes.EEC_PMSM import EEC_PMSM
from pyleecan.Classes.FluxLinkFEMM import FluxLinkFEMM
from pyleecan.Classes.IndMagFEMM import IndMagFEMM
from pyleecan.Classes.Output import Output
from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR


# @pytest.mark.long_5s
# @pytest.mark.MagFEMM
# @pytest.mark.EEC_PMSM
# @pytest.mark.IPMSM
# @pytest.mark.periodicity
# @pytest.mark.SingleOP
@pytest.mark.skip(reason="Work in progress")
def test_skin_effect():
    """Validation of the PMSM Electrical Equivalent Circuit with the Prius machine
    Compute Torque from EEC results and compare with Yang et al, 2013
    """

    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    simu = Simu1(name="test_skin_effect", machine=Toyota_Prius)

    # Definition of the input
    simu.input = InputCurrent(N0=2000, Nt_tot=10, Na_tot=2048)
    simu.input.set_Id_Iq(I0=250 / sqrt(2), Phi0=60 * pi / 180)

    # # Define second simu for FEMM comparison
    # simu2 = simu.copy()
    # simu2.name = "test_EEC_PMSM_FEMM"

    # Definition of the electrical simulation (FEMM)
    simu.elec = Electrical(type_skin_effect=1)
    simu.elec.eec = EEC_PMSM(
        indmag=IndMagFEMM(is_periodicity_a=True, Nt_tot=10),
        fluxlink=FluxLinkFEMM(is_periodicity_a=True, Nt_tot=10),
    )

    simu.mag = None
    simu.force = None
    simu.struct = None

    out = Output(simu=simu)
    #%%
    simu.run()

    # # Definition of the magnetic simulation (FEMM)
    # simu2.mag = MagFEMM(
    #     type_BH_stator=0,
    #     type_BH_rotor=0,
    #     is_periodicity_a=True,
    #     nb_worker=cpu_count(),
    # )

    # out2 = Output(simu=simu2)
    # simu2.run()

    # Plot 3-phase current function of time
    # out.elec.get_Is().plot_2D_Data(
    #     "time",
    #     "phase",
    #     save_path=join(save_path, "EEC_FEMM_IPMSM_currents.png"),
    #     is_show_fig=False,
    #     **dict_2D
    # )

    # from Yang et al, 2013
    # assert_almost_equal(out.elec.Tem_av_ref, 81.81, decimal=1)
    # assert_almost_equal(out2.mag.Tem_av, 81.70, decimal=1)


if __name__ == "__main__":
    test_skin_effect()

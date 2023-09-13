# -*- coding: utf-8 -*-
import pytest

from os.path import join

from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.InputCurrent import InputCurrent

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.definitions import DATA_DIR
from Tests import save_validation_path as save_path


@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.MagFEMM
@pytest.mark.ForceMT
@pytest.mark.SIPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_compare_Kmesh():
    """Validation of the AGSF transfer algorithm for SPMSM benchmark machine: sensitivity to the maximum considered wavenumbers"""

    # Load machine
    Benchmark = load(join(DATA_DIR, "Machine", "Benchmark.json"))

    # Prepare simulation
    simu = Simu1(name="test_compare_Kmesh_direct", machine=Benchmark)

    simu.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0),
        Ir=None,
        Na_tot=5 * 2**8,
        Nt_tot=2,
    )

    # Configure simulation
    simu.elec = None

    simu.force = ForceMT()

    simu.mag = MagFEMM(
        is_periodicity_a=False,
        is_periodicity_t=False,
        is_sliding_band=False,
        Kmesh_fineness=1,
    )

    Rsbo = 0.0480
    Rrbo = 0.0450
    Rs = (Rsbo - Rrbo) * 99 / 100 + Rrbo

    simu2 = simu.copy()
    simu2.name = "test_compare_Kmesh_transfer"
    simu2.force.is_agsf_transfer = True
    simu2.force.Rsbo_enforced_transfer = Rs
    simu2.force.max_wavenumber_transfer = 100

    # Enforced Rag for ref
    simu.mag.Rag_enforced = Rs

    # Simu with low finesness
    simu3 = simu.copy()
    simu3.name = "test_compare_Kmesh_direct_fine"
    simu3.mag.Kmesh_fineness = 2  # 4
    out = simu.run()
    out2 = simu2.run()
    out3 = simu3.run()

    AGSF_list = list()
    AGSF_list.append(out2.force.AGSF)
    AGSF_list.append(out3.force.AGSF)
    legend_list = ["Direct", "Transfer", "Direct Fine Mesh"]

    # out.force.AGSF.plot_2D_Data(
    #     "angle=[0,3.14]",
    #     "time=0",
    #     data_list=AGSF_list,
    #     legend_list=legend_list,
    #     save_path=join(save_path, "test_compare_Kmesh.png"),
    #     is_show_fig=False,
    #     **dict_2D
    # )

    out.force.AGSF.plot_2D_Data(
        "wavenumber",
        "freqs=0",
        x_min=-1,
        x_max=37,
        data_list=AGSF_list,
        legend_list=legend_list,
        save_path=join(save_path, "test_compare_Kmesh_fft.png"),
        is_show_fig=False,
        barwidth=800,
        **dict_2D
    )

    return out, out2, out3


if __name__ == "__main__":
    out, out2, out3 = test_compare_Kmesh()

# -*- coding: utf-8 -*-
import pytest

from os.path import join

from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.InputCurrent import InputCurrent

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from Tests import save_validation_path as save_path


def test_AC_IPMSM_AGSF_transfer_Kmesh():
    """Validation of the AGSF transfer algorithm for SPMSM benchmark machine: sensitivity to the maximum considered wavenumbers"""

    # Load machine
    Benchmark = load(join(DATA_DIR, "Machine", "Benchmark.json"))

    # Prepare simulation
    simu = Simu1(name="AC_IPMSM_plot", machine=Benchmark)

    simu.input = InputCurrent(
        Id_ref=0, Iq_ref=0, Ir=None, Na_tot=5 * 2 ** 8, Nt_tot=2, N0=1200
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
    simu2.force.is_agsf_transfer = True
    simu2.force.Rsbo_enforced_transfer = Rs
    simu2.force.max_wavenumber_transfer = 100

    out2 = simu2.run()

    # Enforced Rag for ref
    simu.mag.Rag_enforced = Rs
    out = simu.run()

    # Simu with low finesness
    simu3 = simu.copy()
    simu3.mag.Kmesh_fineness = 4
    out3 = simu3.run()

    AGSF_list = list()
    AGSF_list.append(out2.force.AGSF)
    AGSF_list.append(out3.force.AGSF)
    legend_list = ["Direct", "Transfert", "Direct Maillage Fin"]

    # out.plot_2D_Data(
    #     "force.AGSF",
    #     "angle=[0,3.14]",
    #     "time=0",
    #     data_list=AGSF_list,
    #     legend_list=legend_list,
    #     save_path=join(save_path, "test_Benchmark_AGSF_var_Kmesh_compare.png"),
    #     is_show_fig=False,
    # )

    out.plot_2D_Data(
        "force.AGSF",
        "wavenumber",
        "freqs=0",
        x_min=-1,
        x_max=37,
        data_list=AGSF_list,
        legend_list=legend_list,
        save_path=join(save_path, "test_Benchmark_AGSF_var_Kmesh_compare_fft.png"),
        is_show_fig=False,
        barwidth=800,
    )

    return out, out2, out3


if __name__ == "__main__":

    # test_AC_IPMSM_AGSF_transfer_compare_Rag_variation()

    out, out2, out3 = test_AC_IPMSM_AGSF_transfer_Kmesh()

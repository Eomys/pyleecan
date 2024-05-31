# -*- coding: utf-8 -*-
import pytest

from os.path import join
from multiprocessing import cpu_count

from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.InputCurrent import InputCurrent

from pyleecan.Functions.load import load
from pyleecan.Functions.Plot import dict_2D
from pyleecan.definitions import DATA_DIR
from Tests import save_validation_path as save_path

DELTA = 1e-6


@pytest.mark.SIPMSM
@pytest.mark.ForceMT
@pytest.mark.MagFEMM
@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.periodicity
@pytest.mark.SingleOP
@pytest.mark.skip(reason="Research only")
def test_Benchmark_AGSF_Rag():
    """Comparison of AGSF at different radius for the 12s10p benchmark
    machine from publication:

    DEVILLERS, Emile, HECQUET, Michel, CIMETIERE,
    Xavier, et al. Experimental benchmark for magnetic noise and vibrations
    analysis in electrical machines. In : 2018 XIII International Conference
    on Electrical Machines (ICEM). IEEE, 2018. p. 745-751.

    """

    # Load machine
    Benchmark = load(join(DATA_DIR, "Machine", "Benchmark.json"))

    # Prepare simulation
    simu = Simu1(name="AC_IPMSM_plot", machine=Benchmark)

    simu.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0),
        Ir=None,
        Na_tot=5 * 2**8,
        Nt_tot=2,
    )

    # Configure simulation
    simu.elec = None

    simu.force = ForceMT(
        is_periodicity_a=False,
        is_periodicity_t=False,
    )

    simu.mag = MagFEMM(
        is_periodicity_a=False,
        is_periodicity_t=False,
        is_sliding_band=False,
        Kmesh_fineness=2,  # 4
        nb_worker=cpu_count(),
    )

    Rsbo = 0.0480
    Rrbo = 0.0450

    # Test 1 : at 10% of the air-gap
    K = [90, 50, 10]
    Nk = len(K)

    simu_list = list()
    out_list = list()
    AGSF_list = list()
    legend_list = list()
    for ik in range(Nk):
        k = K[ik]
        Rag = (Rsbo - Rrbo) * k / 100 + Rrbo

        simu_list.append(simu.copy())
        simu_list[ik].mag.Rag_enforced = Rag
        out = simu_list[ik].run()
        out_list.append(out)
        legend_list.append(str(k) + "%")

        if ik > 0:
            AGSF_list.append(out_list[ik].force.AGSF)

    out_list[0].force.AGSF.plot_2D_Data(
        "angle=[0,3.14]",
        "time=0",
        data_list=AGSF_list,
        legend_list=legend_list,
        save_path=join(save_path, "test_Benchmark_AGSF_var_Rag_compare.png"),
        is_show_fig=False,
        **dict_2D
    )

    out_list[0].force.AGSF.plot_2D_Data(
        "wavenumber",
        "freqs=0",
        x_min=0,
        x_max=24,
        data_list=AGSF_list,
        legend_list=legend_list,
        save_path=join(save_path, "test_Benchmark_AGSF_var_Rag_compare_fft.png"),
        is_show_fig=False,
        barwidth=800,
        **dict_2D
    )

    return out


if __name__ == "__main__":
    out = test_Benchmark_AGSF_Rag()

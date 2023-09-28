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


@pytest.mark.MagFEMM
@pytest.mark.ForceMT
@pytest.mark.SIPMSM
@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.periodicity
@pytest.mark.SingleOP
@pytest.mark.skip(reason="Research only")
def test_compare_Rag_variation():
    """Validation of the AGSF transfer algorithm for SIPMSM benchmark machine"""

    # Load machine
    Benchmark = load(join(DATA_DIR, "Machine", "Benchmark.json"))

    # Prepare simulation
    simu = Simu1(name="test_compare_Rag_variation_direct", machine=Benchmark)

    simu.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0),
        Ir=None,
        Na_tot=5 * 2 ** 8,
        Nt_tot=2,
    )

    # Configure simulation
    simu.elec = None

    simu.force = ForceMT()

    simu.mag = MagFEMM(
        is_periodicity_a=False,
        is_periodicity_t=False,
        is_sliding_band=False,
        Kmesh_fineness=2,  # 4
        nb_worker=cpu_count(),
    )

    simu2 = simu.copy()
    simu2.name = "test_compare_Rag_variation_transfer"
    simu2.force.is_agsf_transfer = True
    simu2.force.max_wavenumber_transfer = 70

    Rsbo = 0.0480
    Rrbo = 0.0450

    # Test 1 : at 10% of the air-gap
    K = [10, 90]
    Nk = len(K)

    simu_list = list()
    simu_list2 = list()

    out_list = list()
    out_list2 = list()

    AGSF_list = list()
    AGSF_list2 = list()

    legend_list = list()
    legend_list2 = list()

    for ik in range(Nk):
        k = K[ik]
        Rag = (Rsbo - Rrbo) * k / 100 + Rrbo

        simu_ik = simu.copy()
        simu_ik.name += "_" + str(k)
        simu_ik.mag.Rag_enforced = Rag
        simu_list.append(simu_ik)
        out_list.append(simu_list[ik].run())
        legend_list.append(str(k) + "%")
        AGSF_list.append(out_list[ik].force.AGSF)

        simu2_ik = simu2.copy()
        simu2_ik.name += "_" + str(k)
        simu2_ik.force.Rsbo_enforced_transfer = Rag
        simu_list2.append(simu2_ik)
        out_list2.append(simu_list2[ik].run())
        legend_list2.append(str(k) + "%")
        AGSF_list2.append(out_list2[ik].force.AGSF)

        out_list[ik].force.AGSF.plot_2D_Data(
            "angle",
            "time=0",
            data_list=[AGSF_list2[ik]],
            legend_list=["Direct", "Transfer"],
            save_path=join(
                save_path, "test_Benchmark_AGSF_var_Rag_compare_" + str(k) + ".png"
            ),
            is_show_fig=False,
            **dict_2D
        )

        out_list[ik].force.AGSF.plot_2D_Data(
            "wavenumber",
            "freqs=0",
            x_min=0,
            x_max=24,
            data_list=[AGSF_list2[ik]],
            legend_list=["Direct", "Transfer"],
            save_path=join(
                save_path, "test_Benchmark_AGSF_var_Rag_compare_fft_" + str(k) + ".png"
            ),
            is_show_fig=False,
            **dict_2D
        )


@pytest.mark.MagFEMM
@pytest.mark.ForceMT
@pytest.mark.SIPMSM
@pytest.mark.long_5s
@pytest.mark.long_1m
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_compare_Rag_variation_Nmax_sensitivity():
    """Validation of the AGSF transfer algorithm for SPMSM benchmark machine: sensitivity to the maximum considered wavenumbers"""

    # Load machine
    Benchmark = load(join(DATA_DIR, "Machine", "Benchmark.json"))

    # Prepare simulation
    simu = Simu1(
        name="test_compare_Rag_variation_Nmax_sensitivity_direct", machine=Benchmark
    )

    simu.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0),
        Ir=None,
        Na_tot=5 * 2 ** 8,
        Nt_tot=2,
    )

    # Configure simulation
    simu.elec = None

    simu.force = ForceMT()

    simu.mag = MagFEMM(
        is_periodicity_a=False,
        is_periodicity_t=False,
        is_sliding_band=False,
        Kmesh_fineness=2,  # 4
        # nb_worker=cpu_count(),
    )

    simu2 = simu.copy()
    simu2.name = "test_compare_Rag_variation_Nmax_sensitivity_transfer"
    simu2.force.is_agsf_transfer = True

    Rsbo = 0.0480
    Rrbo = 0.0450

    # Test 1 : at 10% of the air-gap
    K = [70, 200]
    # K = [70]
    Nk = len(K)

    out_list = list()
    AGSF_list = list()
    legend_list = list()

    Rs = (Rsbo - Rrbo) * 90 / 100 + Rrbo
    simu.mag.Rag_enforced = Rs
    simu2.force.Rsbo_enforced_transfer = Rs

    out = simu.run()
    legend_list.append("Direct")

    for ik in range(Nk):
        k = K[ik]

        sim = simu2.copy()
        sim.name += "_" + str(k)
        sim.force.max_wavenumber_transfer = k
        out_tmp = sim.run()
        legend_list.append("Transfer (Nmax=" + str(k) + ")")
        AGSF_list.append(out_tmp.force.AGSF)

    out.force.AGSF.plot_2D_Data(
        "angle",
        "time=0",
        data_list=AGSF_list,
        legend_list=legend_list,
        save_path=join(
            save_path, "test_compare_Rag_variation_Nmax_sensitivity_" + str(k) + ".png"
        ),
        is_show_fig=False,
        **dict_2D
    )


if __name__ == "__main__":
    # test_AC_IPMSM_AGSF_transfer_compare_Rag_variation()

    # test_compare_Rag_variation()

    test_compare_Rag_variation_Nmax_sensitivity()

# -*- coding: utf-8 -*-
import pytest

from os.path import join
from multiprocessing import cpu_count

from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.InputCurrent import InputCurrent

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
from Tests import save_validation_path as save_path

DELTA = 1e-6


@pytest.mark.validation
@pytest.mark.Force
@pytest.mark.long
def test_Benchmark_AGSF_transfer():
    """Validation test using AGSF transfer for the 12s10p benchmark
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
        Id_ref=0, Iq_ref=0, Ir=None, Na_tot=5 * 2 ** 9, Nt_tot=2, N0=1200
    )

    # Configure simulation
    simu.elec = None
    simu.mag = MagFEMM(
        is_periodicity_a=False,
        is_periodicity_t=False,
        is_sliding_band=False,
        nb_worker=cpu_count(),
    )
    simu.force = ForceMT(
        is_periodicity_a=False,
        is_periodicity_t=False,
    )

    # Run simulation with Rag in the middle of the air-gap
    out = simu.run()

    # Test 2 : with transfer
    simu2 = simu.copy()
    simu2.force.is_agsf_transfer = True
    simu2.force.max_wavenumber_transfer = 100

    out2 = simu2.run()

    # simu 3 directly at Rsbo
    Rsbo = 0.0480
    Rrbo = 0.0450

    k = 99.8
    Rag = (Rsbo - Rrbo) * k / 100 + Rrbo
    simu3 = simu.copy()
    simu3.mag.Rag_enforced = Rag
    out3 = simu3.run()

    out2.plot_2D_Data(
        "force.AGSF",
        "angle=[0,3.14]",
        "time=0",
        data_list=[out.force.AGSF, out3.force.AGSF],
        legend_list=["Rag + Transfer", "Rag", "Rsbo"],
        save_path=join(save_path, "test_Benchmark_AGSF_TR_compare.png"),
        is_show_fig=False,
    )

    out2.plot_2D_Data(
        "force.AGSF",
        "wavenumber",
        "tangential",
        "time=0",
        x_min=0,
        x_max=24,
        data_list=[out.force.AGSF, out3.force.AGSF],
        legend_list=["Rag + Transfer", "Rag", "Rsbo"],
        save_path=join(save_path, "test_Benchmark_AGSF_TR_compare_fft2.png"),
        is_show_fig=False,
        barwidth=2000,
    )


if __name__ == "__main__":

    test_Benchmark_AGSF_transfer()

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


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.ForceMT
@pytest.mark.IPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_IPMSM():
    """Validation of the AGSF transfer calculation for IPMSM machine"""

    # Load machine
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    # Prepare simulation
    simu = Simu1(name="test_compare_transfer_IPMSM_no_transfer", machine=Toyota_Prius)

    simu.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0),
        Ir=None,
        Na_tot=2**11,
        Nt_tot=2**6,
    )

    # Configure simulation
    simu.elec = None
    simu.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=True,
    )
    simu.force = ForceMT(
        is_periodicity_a=True,
        is_periodicity_t=True,
    )

    # Run simulation
    out = simu.run()

    # Test 2 : with transfer
    simu2 = simu.copy()
    simu2.name = "test_compare_transfer_IPMSM_with_transfer"

    simu2.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0),
        Ir=None,
        Na_tot=2**11,
        Nt_tot=2**6,
    )

    simu2.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=True,
    )
    simu2.force = ForceMT(
        is_agsf_transfer=True,
        is_periodicity_a=True,
        is_periodicity_t=True,
    )

    out2 = simu2.run()

    out2.force.AGSF.plot_2D_Data(
        "angle[oneperiod]",
        "time=0",
        data_list=[out.force.AGSF],
        legend_list=["With Transfer", "No Transfer"],
        save_path=join(save_path, "test_compare_transfer_IPMSM.png"),
        is_show_fig=False,
        **dict_2D
    )

    max_r = 42
    out2.force.AGSF.plot_2D_Data(
        "wavenumber",
        "time=0",
        x_min=-max_r,
        x_max=+max_r,
        data_list=[out.force.AGSF],
        legend_list=["With Transfer", "No Transfer"],
        save_path=join(save_path, "test_compare_transfer_IPMSM_fft2.png"),
        is_show_fig=False,
        barwidth=600,
        **dict_2D
    )

    return out, out2


@pytest.mark.long_5s
@pytest.mark.MagFEMM
@pytest.mark.ForceMT
@pytest.mark.SIPMSM
@pytest.mark.parallel
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_Benchmark():
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
    simu = Simu1(name="test_compare_transfer_Benchmark_Rag", machine=Benchmark)

    simu.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0),
        Ir=None,
        Na_tot=5 * 2**9,
        Nt_tot=2,
    )

    # Configure simulation
    simu.elec = None
    simu.mag = MagFEMM(
        is_periodicity_a=False,
        is_periodicity_t=False,
        is_sliding_band=False,
    )
    simu.force = ForceMT(
        is_periodicity_a=False,
        is_periodicity_t=False,
    )

    # Test 2 : with transfer
    simu2 = simu.copy()
    simu2.name = "test_compare_transfer_Benchmark_Rag_Transfer"
    simu2.force.is_agsf_transfer = True
    simu2.force.max_wavenumber_transfer = 100

    # simu 3 directly at Rsbo
    Rsbo = 0.0480
    Rrbo = 0.0450

    k = 99.8
    Rag = (Rsbo - Rrbo) * k / 100 + Rrbo
    simu3 = simu.copy()
    simu2.name = "test_compare_transfer_Benchmark_Rsbo"
    simu3.mag.Rag_enforced = Rag
    # Run simulation with Rag in the middle of the air-gap
    out = simu.run()
    out2 = simu2.run()
    out3 = simu3.run()

    out2.force.AGSF.plot_2D_Data(
        "angle=[0,3.14]",
        "time=0",
        data_list=[out.force.AGSF, out3.force.AGSF],
        legend_list=["Rag + Transfer", "Rag", "Rsbo"],
        save_path=join(save_path, "test_compare_transfer_Benchmark.png"),
        is_show_fig=False,
        **dict_2D
    )

    out2.force.AGSF.plot_2D_Data(
        "wavenumber",
        "tangential",
        "time=0",
        x_min=0,
        x_max=24,
        data_list=[out.force.AGSF, out3.force.AGSF],
        legend_list=["Rag + Transfer", "Rag", "Rsbo"],
        save_path=join(save_path, "test_compare_transfer_Benchmark_fft2.png"),
        is_show_fig=False,
        barwidth=2000,
        **dict_2D
    )
    return out, out2, out3


if __name__ == "__main__":
    # out, out2 = test_IPMSM()
    out3, out4, out5 = test_Benchmark()

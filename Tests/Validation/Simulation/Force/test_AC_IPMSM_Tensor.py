# -*- coding: utf-8 -*-
import pytest

from os.path import join
from numpy import zeros, exp, pi, real, meshgrid, mean
from multiprocessing import cpu_count
from numpy.testing import assert_array_almost_equal


from pyleecan.Classes.ForceMT import ForceMT
from pyleecan.Classes.ForceTensor import ForceTensor
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
def test_Benchmark_Tensor():
    """Validation of the AGSF spectrum calculation for IPMSM machine"""

    # Load machine
    Benchmark = load(join(DATA_DIR, "Machine", "Benchmark.json"))
    # Prepare simulation
    simu = Simu1(name="Benchmark_Tensor", machine=Benchmark)

    simu.input = InputCurrent(
        Id_ref=0, Iq_ref=0, Ir=None, Na_tot=2 ** 6, Nt_tot=1, N0=1200
    )

    simu.elec = None

    simu.mag = MagFEMM(
        type_BH_stator=1,  # 0 for saturated
        type_BH_rotor=1,
        is_periodicity_a=False,
        is_periodicity_t=False,
        is_get_meshsolution=True,
        is_sliding_band=False,
        # nb_worker=cpu_count(),
        Kmesh_fineness=1,
    )
    simu.force = ForceTensor(
        is_periodicity_a=False,
        is_periodicity_t=False,
    )

    # Run simulation
    out = simu.run()

    out.force.meshsolution.plot_glyph(
        label="F",
        is_point_arrow=True,
        # is_show_fig=True,
        # save_path=join(save_path,"magneto_plot_glyph.png"),
    )

    return out


if __name__ == "__main__":

    out = test_Benchmark_Tensor()

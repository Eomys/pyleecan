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


@pytest.mark.SIPMSM
@pytest.mark.periodicity
@pytest.mark.ForceMT
@pytest.mark.long
@pytest.mark.ForceTensor
@pytest.mark.MeshSol
@pytest.mark.SingleOP
def test_Benchmark_Tensor():
    """Validation of the AGSF spectrum calculation for IPMSM machine"""

    # Load machine
    Benchmark = load(join(DATA_DIR, "Machine", "Benchmark.json"))
    # Prepare simulation
    simu = Simu1(name="Benchmark_Tensor", machine=Benchmark)

    simu.input = InputCurrent(
        Id_ref=0, Iq_ref=0, Ir=None, Na_tot=2 ** 6, Nt_tot=3, N0=1200
    )

    simu.elec = None

    simu.mag = MagFEMM(
        type_BH_stator=1,
        type_BH_rotor=1,
        is_periodicity_a=True,
        is_periodicity_t=False,
        is_get_meshsolution=True,
        # nb_worker=cpu_count(),
        Kmesh_fineness=2,
    )
    simu.force = ForceTensor(
        is_periodicity_a=True,
        is_periodicity_t=False,
    )

    # Run simulation
    out = simu.run()

    out.force.meshsolution.plot_glyph(
        label="F",
        is_point_arrow=True,
        is_show_fig=False,
        save_path=join(save_path, "magneto_plot_glyph.png"),
    )

    return out


if __name__ == "__main__":

    out = test_Benchmark_Tensor()

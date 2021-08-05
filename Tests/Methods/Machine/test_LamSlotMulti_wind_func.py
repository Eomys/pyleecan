from os.path import join

import matplotlib.pyplot as plt
import pytest
from numpy import linspace, pi
from pyleecan.Classes.LamSlotMultiWind import LamSlotMultiWind
from numpy.testing import assert_array_almost_equal
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load
from Tests import save_plot_path as save_path


@pytest.mark.LamSlotMulti
def test_wind_func():
    """Test to compute the winding function for a LamSlotMultiWind."""
    # Load machine
    SPMSM_001 = load(join(DATA_DIR, "Machine", "SPMSM_001.json"))
    SPMSM_001_multi = SPMSM_001.copy()

    # New lamination main dimensions definition
    stator = LamSlotMultiWind(init_dict=SPMSM_001.stator.as_dict())

    # New slots definition
    Slot1 = SPMSM_001.stator.slot.copy()

    # Slots are duplicated to get 6 of each in alternance
    slot_list = list()
    for ii in range(12):
        slot_list.append(Slot1.copy())

    # Assign slots to stator and set positions
    stator.slot_list = slot_list
    stator.alpha = linspace(0, 360, 12, endpoint=False) * pi / 180 + pi / 12

    # Assign stator to machine
    SPMSM_001_multi.stator = stator

    wf = SPMSM_001.stator.comp_wind_function(angle=None, Na=2048, alpha_mmf0=0, per_a=1)
    wf_multi = SPMSM_001_multi.stator.comp_wind_function(
        angle=None, Na=2048, alpha_mmf0=0, per_a=1
    )

    assert_array_almost_equal(wf, wf_multi)


if __name__ == "__main__":
    test_wind_func()

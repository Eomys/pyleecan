from os.path import join

from pyleecan.Classes.LamSlotWind import LamSlotWind

import pytest

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


"""pytest for comp_periodicity"""


@pytest.mark.periodicity
def test_comp_periodicity_spatial():
    rotor = LamSlotWind(
        Rint=0.2,
        Rext=0.5,
        is_internal=True,
        is_stator=False,
        L1=0.95,
        Nrvd=1,
        Wrvd=0.05,
    )
    rotor.winding = None
    assert rotor.comp_periodicity_spatial() == (1, False)


@pytest.mark.periodicity
def test_comp_periodicity():

    machine = load(join(DATA_DIR, "Machine", "Benchmark.json"))

    # Spatial periodicities
    (
        per_a,
        is_antiper_a,
    ) = machine.comp_periodicity_spatial()

    assert per_a, is_antiper_a == (1, True)

    # Time periodicities in both static and rotating referentials
    (
        per_t_S,
        is_antiper_t_S,
        per_t_R,
        is_antiper_t_R,
    ) = machine.comp_periodicity_time(slip=0)

    assert (per_t_S, is_antiper_t_S, per_t_R, is_antiper_t_R) == (
        5,
        True,
        1,
        False,
    )

    machine = load(join(DATA_DIR, "Machine", "SPMSM_015.json"))

    # Spatial periodicities
    (
        per_a,
        is_antiper_a,
    ) = machine.comp_periodicity_spatial()

    assert per_a, is_antiper_a == (9, False)

    # Time periodicities in both static and rotating referentials
    (
        per_t_S,
        is_antiper_t_S,
        per_t_R,
        is_antiper_t_R,
    ) = machine.comp_periodicity_time(slip=0)

    assert (per_t_S, is_antiper_t_S, per_t_R, is_antiper_t_R) == (
        9,
        True,
        9,
        False,
    )

    machine = load(join(DATA_DIR, "Machine", "Audi_eTron.json"))

    # Spatial periodicities
    (
        per_a,
        is_antiper_a,
    ) = machine.comp_periodicity_spatial()

    assert per_a, is_antiper_a == (2, False)

    # Time periodicities in both static and rotating referentials
    (
        per_t_S,
        is_antiper_t_S,
        per_t_R,
        is_antiper_t_R,
    ) = machine.comp_periodicity_time(slip=0)

    assert (per_t_S, is_antiper_t_S, per_t_R, is_antiper_t_R) == (
        2,
        False,
        2,
        False,
    )


if __name__ == "__main__":
    test_comp_periodicity()

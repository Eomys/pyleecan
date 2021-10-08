import pytest
from os.path import join

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

machine_list = [
    ["Toyota_Prius", (4, True, 4, True)],
    ["BMW_i3", (6, True, 6, True)],
    ["Protean_InWheel", (8, False, 32, True)],
    ["Tesla_S", (2, False, 2, False)],
    ["Audi_eTron", (2, False, 2, False)],
    ["Benchmark", (1, True, 5, True)],
    ["SCIM_001", (1, True, 1, True)],
    ["SCIM_006", (2, True, 2, True)],
    ["SPMSM_001", (4, False, 4, True)],
    ["SPMSM_003", (1, True, 1, True)],
    ["SPMSM_015", (9, False, 9, True)],
    ["SIPMSM_001", (1, False, 2, True)],
    ["SynRM_001", (2, True, 2, True)],
    ["LSRPM_001", (4, False, 4, True)],
]


@pytest.mark.periodicity
@pytest.mark.parametrize("machine", machine_list)
def test_comp_periodicity(machine):

    machine_obj = load(join(DATA_DIR, "Machine", machine[0] + ".json"))

    per_a, aper_a = machine_obj.comp_periodicity_spatial()

    per_t, aper_t, _, _ = machine_obj.comp_periodicity_time()

    msg = (
        "Wrong periodicity calculation for "
        + machine_obj.name
        + ": "
        + str((per_a, aper_a, per_t, aper_t))
    )
    assert (per_a, aper_a, per_t, aper_t) == machine[1], msg

    return (per_a, aper_a, per_t, aper_t)


# To run it without pytest
if __name__ == "__main__":

    per_tuple = test_comp_periodicity(machine_list[-1])

    for machine in machine_list:
        per_tuple = test_comp_periodicity(machine)

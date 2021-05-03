# -*- coding: utf-8 -*-


from os.path import isfile, join

import pytest
from pyleecan.Functions.load import (
    load,
)
from Tests import TEST_DATA_DIR
from pyleecan.definitions import DATA_DIR


# 1: LamSlotMag convertion (magnet from slot to lamination)
file_list = list()
file_list.append(
    {
        "ref": join(DATA_DIR, "Machine", "SPMSM_001.json"),
        "old": join(TEST_DATA_DIR, "Retrocompatibility", "Magnet", "SPMSM_001.json"),
    }
)

# 2: Winding convertion (star of slot)
wind_list = list()
wind_list.append(  # WindingSC + WindingDW2L
    {
        "ref": join(DATA_DIR, "Machine", "SCIM_001.json"),
        "old": join(TEST_DATA_DIR, "Retrocompatibility", "Winding", "SCIM_001.json"),
    }
)
wind_list.append(  # WindingCW1L
    {
        "ref": join(DATA_DIR, "Machine", "SPMSM_002.json"),
        "old": join(TEST_DATA_DIR, "Retrocompatibility", "Winding", "SPMSM_002.json"),
    }
)
wind_list.append(  # WindingCW2LT
    {
        "ref": join(DATA_DIR, "Machine", "SPMSM_015.json"),
        "old": join(TEST_DATA_DIR, "Retrocompatibility", "Winding", "SPMSM_015.json"),
    }
)
wind_list.append(  # WindingUD
    {
        "ref": join(DATA_DIR, "Machine", "SPMSM_020.json"),
        "old": join(TEST_DATA_DIR, "Retrocompatibility", "Winding", "SPMSM_020.json"),
    }
)
wind_list.append(  # WindingSC + WindingDW2L
    {
        "ref": join(DATA_DIR, "Machine", "TESLA_S.json"),
        "old": join(TEST_DATA_DIR, "Retrocompatibility", "Winding", "TESLA_S.json"),
    }
)
wind_list.append(  # WindingDW1L
    {
        "ref": join(DATA_DIR, "Machine", "Toyota_Prius.json"),
        "old": join(
            TEST_DATA_DIR, "Retrocompatibility", "Winding", "Toyota_Prius.json"
        ),
    }
)


@pytest.mark.parametrize("file_dict", file_list)
def test_save_load_retro(file_dict):
    """Check that the convertion works"""
    ref = load(file_dict["ref"])
    old = load(file_dict["old"])

    assert ref == old


@pytest.mark.parametrize("file_dict", wind_list)
def test_save_load_wind_retro(file_dict):
    """Check that the winding convertion works"""
    ref = load(file_dict["ref"])
    old = load(file_dict["old"])

    if hasattr(ref.rotor, "winding"):
        msg = (
            "Error for "
            + ref.name
            + ": "
            + str(ref.rotor.winding.compare(old.rotor.winding, "rotor.winding"))
        )
        assert ref.rotor.winding == old.rotor.winding, msg


if __name__ == "__main__":
    test_save_load_retro(file_list[0])

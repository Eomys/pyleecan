# -*- coding: utf-8 -*-


from os.path import isfile, join

import pytest
from pyleecan.Functions.load import (
    load,
)
from Tests import TEST_DATA_DIR
from pyleecan.definitions import DATA_DIR


file_list = list()
# 1: LamSlotMag convertion (magnet from slot to lamination)
file_list.append(
    {
        "ref": join(DATA_DIR, "Machine", "SPMSM_001.json"),
        "old": join(TEST_DATA_DIR, "Retrocompatibility", "SPMSM_001.json"),
    }
)
# 2: Winding convertion (star of slot)
file_list.append(
    {
        "ref": join(DATA_DIR, "Machine", "SCIM_006.json"),
        "old": join(TEST_DATA_DIR, "Retrocompatibility", "SCIM_006.json"),
    }
)


@pytest.mark.parametrize("file_dict", file_list)
def test_save_load_retro(file_dict):
    """Check that the convertion works"""
    ref = load(file_dict["ref"])
    old = load(file_dict["old"])

    assert ref == old

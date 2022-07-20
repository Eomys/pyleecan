# -*- coding: utf-8 -*-


from os.path import isfile, join

import pytest
from numpy import array_equal
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load
from pyleecan.Functions.Load.retrocompatibility import is_before_version
from Tests import TEST_DATA_DIR

# 4: OP_matrix convertion (ndarray to object)
OPM_list = list()
OPM_list.append(  # VarParam of VarLoadCurrent (OP Id/Iq)
    {
        "ref": join(
            TEST_DATA_DIR,
            "Retrocompatibility",
            "OP_matrix",
            "new",
            "test_multi_multi.json",
        ),
        "old": join(
            TEST_DATA_DIR,
            "Retrocompatibility",
            "OP_matrix",
            "old",
            "test_multi_multi.json",
        ),
    }
)
OPM_list.append(  # VarLoadCurrent (I0/Phi0/Tem)
    {
        "ref": join(
            TEST_DATA_DIR, "Retrocompatibility", "OP_matrix", "new", "test_varload.json"
        ),
        "old": join(
            TEST_DATA_DIR, "Retrocompatibility", "OP_matrix", "old", "test_varload.json"
        ),
    }
)

# 3: HoleUD convertion (label update)
hole_list = list()
hole_list.append(  # WindingCW1L
    {
        "ref": join(DATA_DIR, "Machine", "BMW_i3.json"),
        "old": join(TEST_DATA_DIR, "Retrocompatibility", "Label", "BMW_i3.json"),
    }
)

# 2: Winding convertion (star of slot)
wind_list = list()
# wind_list.append(  # WindingSC + WindingDW2L
#     {
#         "ref": join(DATA_DIR, "Machine", "SCIM_001.json"),
#         "old": join(TEST_DATA_DIR, "Retrocompatibility", "Winding", "SCIM_001.json"),
#     }
# )
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
# wind_list.append(  # WindingSC + WindingDW2L
#     {
#         "ref": join(DATA_DIR, "Machine", "Tesla_S.json"),
#         "old": join(TEST_DATA_DIR, "Retrocompatibility", "Winding", "Tesla_S.json"),
#     }
# )
wind_list.append(  # WindingDW1L
    {
        "ref": join(DATA_DIR, "Machine", "Toyota_Prius.json"),
        "old": join(
            TEST_DATA_DIR, "Retrocompatibility", "Winding", "Toyota_Prius.json"
        ),
    }
)


def test_save_OPM_None_retro():
    """Check that the OP_matrix convertion works with None"""
    simu = load(
        join(TEST_DATA_DIR, "Retrocompatibility", "OP_matrix", "test_OPM_None.json",),
    )
    assert simu.var_simu.OP_matrix is None


@pytest.mark.parametrize("file_dict", OPM_list)
def test_save_OPM_retro(file_dict):
    """Check that the OP_matrix convertion works"""
    ref = load(file_dict["ref"])
    old = load(file_dict["old"])

    ref_var = ref.get_var_load()
    old_var = old.get_var_load()
    # Datakeeper were added between the 2 versions
    ref_var.datakeeper_list = None
    old_var.datakeeper_list = None

    # Check old file is converted to current version
    msg = (
        "Error for "
        + ref.name
        + ": "
        + str(ref_var.compare(old_var, "var_load", is_add_value=True))
    )
    assert ref_var == old_var, msg


@pytest.mark.parametrize("file_dict", hole_list)
def test_save_load_hole_retro(file_dict):
    """Check that the HoleUD convertion works"""
    ref = load(file_dict["ref"])
    old = load(file_dict["old"])

    hole_ref = ref.rotor.hole[0]
    hole_old = old.rotor.hole[0]

    # Check old file is converted to current version
    msg = "Error for " + ref.name + ": " + str(hole_ref.compare(hole_old, "hole"))
    assert hole_ref == hole_old, msg


@pytest.mark.parametrize("file_dict", wind_list)
def test_save_load_wind_retro(file_dict):
    """Check that the winding convertion works (convert to WindingUD instead of Winding)"""
    ref = load(file_dict["ref"])
    old = load(file_dict["old"])

    # Check old file is converted to current version
    if hasattr(ref.rotor, "winding"):
        msg = (
            "Error for "
            + ref.name
            + ": "
            + str(ref.rotor.winding.compare(old.rotor.winding, "rotor.winding"))
        )
        assert ref.rotor.winding == old.rotor.winding, msg

    msg = "Error for " + ref.name
    assert ref.stator.winding.p == old.stator.winding.p, msg
    assert ref.stator.winding.qs == old.stator.winding.qs, msg
    assert ref.stator.winding.Ntcoil == old.stator.winding.Ntcoil, msg
    assert array_equal(
        ref.stator.winding.get_connection_mat(),
        -1 * old.stator.winding.get_connection_mat(),
    ) or array_equal(
        ref.stator.winding.get_connection_mat(),
        old.stator.winding.get_connection_mat(),
    ), msg


def test_before_version():
    """Check that we can detect previous version"""
    assert is_before_version("1.2.3", "1.2.1")
    assert is_before_version("1.2.3", "1.1.3")
    assert is_before_version("1.2.3", "0.2.3")
    assert not is_before_version("1.2.3", "2.2.3")
    assert not is_before_version("1.2.3", "1.3.0")
    assert not is_before_version("1.2.3", "1.2.4")
    assert not is_before_version("1.2.3", "1.2.3")
    assert not is_before_version("1.2.3", "1.2.3.2")
    assert is_before_version("1.2.3.2", "1.2.3")


if __name__ == "__main__":
    test_save_OPM_None_retro()
    for file_dict in OPM_list:
        test_save_OPM_retro(file_dict)

    # for file_dict in hole_list:
    #     test_save_load_hole_retro(file_dict)

    # for file_dict in wind_list:
    #     test_save_load_wind_retro(file_dict)
    print("Done")

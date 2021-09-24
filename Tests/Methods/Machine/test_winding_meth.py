# -*- coding: utf-8 -*-

import pytest
from os.path import join, isdir
from os import makedirs

from numpy import array_equal

from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.WindingUD import WindingUD
from pyleecan.Classes.Slot import Slot

from Tests import save_load_path as save_path, TEST_DATA_DIR
from Tests.Plot.LamWind import wind_mat

# Init result folder
save_path = join(save_path, "Winding")
if not isdir(save_path):
    makedirs(save_path)

exp_imp_list = list()
# Nrad = Ntan = 1
test_obj = LamSlotWind()
test_obj.slot.Zs = 36
test_obj.winding = Winding(qs=3, p=3, Nlayer=1, coil_pitch=0, Ntcoil=8)
exp_shape = (1, 1, 36, 3)
exp_imp_list.append({"test_obj": test_obj, "exp_shape": exp_shape})

# Nrad = 2; Ntan = 1
test_obj = LamSlotWind()
test_obj.slot.Zs = 36
test_obj.winding = Winding(qs=3, p=3, Nlayer=2, coil_pitch=5, Ntcoil=9)
exp_shape = (2, 1, 36, 3)
exp_imp_list.append({"test_obj": test_obj, "exp_shape": exp_shape})
wind_per = test_obj.winding.get_connection_mat()  # For periodicity import test

# Ntan = 1 ; Ntan = 2
test_obj = LamSlotWind()
test_obj.slot.Zs = 12
test_obj.winding = Winding(qs=3, p=5, Nlayer=2, coil_pitch=1, Ntcoil=10)
exp_shape = (1, 2, 12, 3)
exp_imp_list.append({"test_obj": test_obj, "exp_shape": exp_shape})

# Nrad = 2 ; Ntan = 2 ; qs = 4
test_obj = LamSlotWind()
test_obj.slot.Zs = 6
test_obj.winding = WindingUD(
    qs=4, p=4, wind_mat=wind_mat, Nlayer=4, coil_pitch=None, Ntcoil=1
)
exp_shape = (2, 2, 6, 4)
exp_imp_list.append({"test_obj": test_obj, "exp_shape": exp_shape})


@pytest.mark.parametrize("test_dict", exp_imp_list)
def test_export_import_Head_Full(test_dict):
    """Check that export/import works"""

    exp_shape = test_dict["exp_shape"]
    wind_name = "Wind_" + str(exp_shape[0]) + "_" + str(exp_shape[1])

    # Header=True, Skip=False
    save_path_1 = join(save_path, wind_name + "_" + "Head_Full.csv")
    test_dict["test_obj"].winding.export_to_csv(
        file_path=save_path_1, is_add_header=True, is_skip_empty=False
    )
    result = WindingUD()
    result.import_from_csv(save_path_1)
    assert result.get_connection_mat().shape == exp_shape
    assert array_equal(
        test_dict["test_obj"].winding.get_connection_mat(), result.get_connection_mat()
    )
    assert result.qs == test_dict["test_obj"].winding.qs
    assert result.Ntcoil == test_dict["test_obj"].winding.Ntcoil
    assert result.Nlayer == test_dict["test_obj"].winding.Nlayer


@pytest.mark.parametrize("test_dict", exp_imp_list)
def test_export_import_Data_Full(test_dict):
    """Check that export/import works"""
    exp_shape = test_dict["exp_shape"]
    wind_name = "Wind_" + str(exp_shape[0]) + "_" + str(exp_shape[1])
    # Header=True, Skip=False
    save_path_2 = join(save_path, wind_name + "_" + "Data_Full.csv")
    test_dict["test_obj"].winding.export_to_csv(
        file_path=save_path_2, is_add_header=False, is_skip_empty=False
    )
    result = WindingUD()
    result.import_from_csv(save_path_2)
    assert result.get_connection_mat().shape == exp_shape
    assert array_equal(
        test_dict["test_obj"].winding.get_connection_mat(), result.get_connection_mat()
    )
    assert result.qs == test_dict["test_obj"].winding.qs
    assert result.Ntcoil == test_dict["test_obj"].winding.Ntcoil
    assert result.Nlayer == test_dict["test_obj"].winding.Nlayer


@pytest.mark.parametrize("test_dict", exp_imp_list)
def test_export_import_Head_Empty(test_dict):
    """Check that export/import works"""
    exp_shape = test_dict["exp_shape"]
    wind_name = "Wind_" + str(exp_shape[0]) + "_" + str(exp_shape[1])
    # Header=True, Skip=True
    save_path_3 = join(save_path, wind_name + "_" + "Head_Empty.csv")
    test_dict["test_obj"].winding.export_to_csv(
        file_path=save_path_3, is_add_header=True, is_skip_empty=True
    )
    result = WindingUD()
    result.import_from_csv(save_path_3)
    assert result.get_connection_mat().shape == exp_shape
    assert array_equal(
        test_dict["test_obj"].winding.get_connection_mat(), result.get_connection_mat()
    )
    assert result.qs == test_dict["test_obj"].winding.qs
    assert result.Ntcoil == test_dict["test_obj"].winding.Ntcoil
    assert result.Nlayer == test_dict["test_obj"].winding.Nlayer


@pytest.mark.parametrize("test_dict", exp_imp_list)
def test_export_import_Data_Empty(test_dict):
    """Check that export/import works"""
    exp_shape = test_dict["exp_shape"]
    wind_name = "Wind_" + str(exp_shape[0]) + "_" + str(exp_shape[1])
    # Header=False, Skip=True
    save_path_4 = join(save_path, wind_name + "_" + "Data_Empty.csv")
    test_dict["test_obj"].winding.export_to_csv(
        file_path=save_path_4, is_add_header=False, is_skip_empty=True
    )
    result = WindingUD()
    result.import_from_csv(save_path_4)
    assert result.get_connection_mat().shape == exp_shape
    assert array_equal(
        test_dict["test_obj"].winding.get_connection_mat(), result.get_connection_mat()
    )
    assert result.qs == test_dict["test_obj"].winding.qs
    assert result.Ntcoil == test_dict["test_obj"].winding.Ntcoil
    assert result.Nlayer == test_dict["test_obj"].winding.Nlayer


def test_import_periodicity():
    lam = LamSlotWind(slot=Slot(Zs=36))
    lam.winding = WindingUD()
    # With Header (Zs=12 instead of 36 to trigger periodicity)
    lam.winding.import_from_csv(
        join(TEST_DATA_DIR, "Load_GUI", "Winding", "Wind_2_1_Head_Empty_per.csv")
    )
    assert array_equal(wind_per, lam.winding.get_connection_mat())
    # Without Header
    lam.winding.import_from_csv(
        join(TEST_DATA_DIR, "Load_GUI", "Winding", "Wind_2_1_Data_Empty_per.csv")
    )
    assert array_equal(wind_per, lam.winding.get_connection_mat())


if __name__ == "__main__":
    for test_dict in exp_imp_list:
        test_export_import_Head_Full(test_dict)
        test_export_import_Data_Full(test_dict)
        test_export_import_Head_Empty(test_dict)
        test_export_import_Data_Empty(test_dict)
    test_import_periodicity()
    print("Done")

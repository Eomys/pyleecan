# -*- coding: utf-8 -*-

from os import remove, getcwd
from os.path import isfile, join
import pytest
from unittest.mock import patch  # for unittest of input

from numpy import pi

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MagnetType11 import MagnetType11
from pyleecan.Classes.SlotMPolar import SlotMPolar
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.Shaft import Shaft
from Tests import DATA_DIR, save_load_path as save_path
from pyleecan.Functions.load import (
    load,
    load_list,
    load_dict,
    LoadMissingFileError,
    LoadWrongDictClassError,
    LoadWrongTypeError,
    LoadSwitchError,
)
from pyleecan.Functions.save import save_data

load_file_1 = join(DATA_DIR, "test_wrong_slot_load_1.json")
load_file_2 = join(DATA_DIR, "test_wrong_slot_load_2.json")
load_file_3 = join(DATA_DIR, "test_wrong_slot_load_3.json")


"""test for save and load fonctions"""


def test_save_load_machine():
    """Check that you can save and load a machine object
    """
    # SetUp
    test_obj = MachineSIPMSM(name="test", desc="test\non\nseveral lines")
    test_obj.stator = LamSlotWind(L1=0.45)
    test_obj.stator.slot = SlotW10(Zs=10, H0=0.21, W0=0.23)
    test_obj.stator.winding = WindingDW1L(qs=5)
    test_obj.rotor = LamSlotMag(L1=0.55)
    test_obj.rotor.slot = SlotMPolar(W0=pi / 4)
    test_obj.rotor.slot.magnet = [MagnetType11(Wmag=pi / 4, Hmag=3)]
    test_obj.shaft = Shaft(Lshaft=0.65)
    test_obj.frame = None

    # Save Test
    file_path = join(save_path, "test_machine.json")
    if isfile(file_path):
        remove(file_path)
    assert isfile(file_path) == False
    test_obj.save(file_path)
    assert isfile(file_path)

    # Load Test
    result = load(file_path)
    assert type(result) is MachineSIPMSM
    assert result.name == "test"
    assert result.desc == "test\non\nseveral lines"

    assert type(result.stator) is LamSlotWind
    assert result.stator.L1 == 0.45

    assert type(result.stator.slot) is SlotW10
    assert result.stator.slot.Zs == 10
    assert result.stator.slot.H0 == 0.21
    assert result.stator.slot.W0 == 0.23

    assert type(result.stator.winding) is WindingDW1L
    assert result.stator.winding.qs == 5

    assert type(result.rotor) is LamSlotMag
    assert result.rotor.L1 == 0.55

    assert type(result.rotor.slot) is SlotMPolar
    assert result.rotor.slot.W0 == pi / 4
    assert type(result.rotor.slot.magnet) is list

    assert type(result.rotor.slot.magnet[0]) is MagnetType11
    assert len(result.rotor.slot.magnet) == 1
    assert result.rotor.slot.magnet[0].Wmag == pi / 4
    assert result.rotor.slot.magnet[0].Hmag == 3

    assert type(result.shaft) is Shaft
    assert result.shaft.Lshaft == 0.65

    assert result.frame == None


def test_save_folder_path():
    """Save with a folder path
    """

    test_obj = LamSlotWind(L1=0.45)

    file_path = join(save_path, "LamSlotWind.json")
    if isfile(file_path):
        remove(file_path)
    assert isfile(file_path) == False
    test_obj.save(save_path)
    assert isfile(file_path)


def test_save_load_just_name():
    """Save with a folder path
    """

    test_obj = SlotW10(Zs=10)

    file_path = join(getcwd(), "test_slot.json")
    if isfile(file_path):
        remove(file_path)
    assert isfile(file_path) == False
    test_obj.save("test_slot")
    assert isfile(file_path)

    result = load("test_slot")
    assert type(result) is SlotW10
    assert result.Zs == 10
    # remove(file_path)


def test_load_error_missing():
    """Test that the load function can detect missing file
    """
    with pytest.raises(LoadMissingFileError):
        load(save_path)


def test_load_error_wrong_type():
    """Test that the load function can detect wrong type
    """
    with pytest.raises(LoadWrongTypeError):
        load(load_file_3)
    with pytest.raises(LoadWrongTypeError):
        load_list(load_file_2)
    with pytest.raises(LoadWrongTypeError):
        load_dict(load_file_3)


def test_load_error_missing_class():
    """Test that the load function can detect missing __class__
    """
    with pytest.raises(
        LoadWrongDictClassError, match='Key "__class__" missing in loaded file'
    ):
        load(load_file_1)


def test_load_error_wrong_class():
    """Test that the load function can detect wrong __class__
    """
    with pytest.raises(
        LoadWrongDictClassError, match="SlotDoesntExist is not a pyleecan class"
    ):
        load(load_file_2)


@patch.dict("pyleecan.Functions.load_switch.load_switch", {"list": None})
def test_load_switch():
    """Test that the load function can detect wrong load_switch dict
    """
    with pytest.raises(LoadSwitchError):
        load_list(load_file_3)


def test_save_load_list():
    """Test the save and load function of data structures
    """
    # SetUp
    test_obj_1 = MachineSIPMSM(name="test", desc="test\non\nseveral lines")
    test_obj_1.stator = LamSlotWind(L1=0.45)
    test_obj_1.stator.slot = SlotW10(Zs=10, H0=0.21, W0=0.23)
    test_obj_1.stator.winding = WindingDW1L(qs=5)
    test_obj_1.rotor = LamSlotMag(L1=0.55)
    test_obj_1.rotor.slot = SlotMPolar(W0=pi / 4)
    test_obj_1.rotor.slot.magnet = [MagnetType11(Wmag=pi / 4, Hmag=3)]
    test_obj_1.shaft = Shaft(Lshaft=0.65)
    test_obj_1.frame = None

    test_obj_2 = LamSlotWind(L1=0.45)

    test_obj_3 = {"H0": 0.001, "Zs": 10, "__class__": "ClassDoesntExist"}

    test_obj_4 = tuple([1, 2, 3])

    test_list = [
        test_obj_4,
        [test_obj_1, None],
        {"test_obj_2": test_obj_2, "test_obj_list": [test_obj_3, None]},
    ]

    # Save Test
    file_path = join(save_path, "test_list.json")
    if isfile(file_path):
        remove(file_path)
    assert isfile(file_path) == False
    save_data(test_list, file_path)
    assert isfile(file_path)

    # Load Test
    result_list = load_list(file_path)
    # set tuple to None as save will do
    test_list[0] = None
    assert result_list == test_list


def test_save_load_dict():
    """Test the save and load function of data structures
        """
    # SetUp
    test_obj_1 = MachineSIPMSM(name="test", desc="test\non\nseveral lines")
    test_obj_1.stator = LamSlotWind(L1=0.45)
    test_obj_1.stator.slot = SlotW10(Zs=10, H0=0.21, W0=0.23)
    test_obj_1.stator.winding = WindingDW1L(qs=5)
    test_obj_1.rotor = LamSlotMag(L1=0.55)
    test_obj_1.rotor.slot = SlotMPolar(W0=pi / 4)
    test_obj_1.rotor.slot.magnet = [MagnetType11(Wmag=pi / 4, Hmag=3)]
    test_obj_1.shaft = Shaft(Lshaft=0.65)
    test_obj_1.frame = None

    test_obj_2 = LamSlotWind(L1=0.45)

    test_obj_3 = {"H0": 0.001, "Zs": 10, "__class__": "ClassDoesntExist"}

    test_obj_4 = tuple([1, 2, 3])

    test_dict = {
        "tuple": test_obj_4,
        "list": [test_obj_1, None],
        "dict": {"test_obj_2": test_obj_2, "test_obj_list": [test_obj_3, None]},
    }

    # Save Test
    file_path = join(save_path, "test_dict.json")
    if isfile(file_path):
        remove(file_path)
    assert isfile(file_path) == False
    save_data(test_dict, file_path)
    assert isfile(file_path)

    # Load Test
    result_dict = load_dict(file_path)
    # set tuple to None as save will do
    test_dict["tuple"] = None
    assert result_dict == test_dict

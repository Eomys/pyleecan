# -*- coding: utf-8 -*-

from os import getcwd, remove, listdir
from os.path import isfile, join, isdir
from unittest.mock import patch  # for unittest of input

import pytest
from numpy import array, ones, pi
from pyleecan.Classes._check import InitUnKnowClassError
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
from pyleecan.Classes.PostFunction import PostFunction
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.SlotM11 import SlotM11
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.SlotUD import SlotUD
from pyleecan.Classes.HoleUD import HoleUD
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Functions.load import (
    LoadWrongDictClassError,
    LoadWrongTypeError,
    load,
    load_dict,
    load_list,
)
from pyleecan.Functions.Load.load_json import LoadMissingFileError
from pyleecan.Functions.Save.save_json import save_json
from Tests import TEST_DATA_DIR
from Tests import save_load_path as save_path
from Tests import x as logger

from pyleecan.definitions import DATA_DIR

load_file_1 = join(TEST_DATA_DIR, "test_wrong_slot_load_1.json")
load_file_2 = join(TEST_DATA_DIR, "test_wrong_slot_load_2.json")
logger.info(save_path)

"""test for save and load functions"""


def test_save_load_machine():
    """Check that you can save and load a machine object"""
    # SetUp
    test_obj = MachineSIPMSM(name="test", desc="test\non\nseveral lines")
    test_obj.stator = LamSlotWind(L1=0.45)
    test_obj.stator.slot = SlotW10(Zs=10, H0=0.21, W0=0.23)
    test_obj.stator.winding = Winding(qs=5, Nlayer=1, p=3)
    test_obj.rotor = LamSlotMag(L1=0.55)
    test_obj.rotor.slot = SlotM11(W0=pi / 4, Wmag=pi / 4, Hmag=3)
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

    assert type(result.stator.winding) is Winding
    assert result.stator.winding.qs == 5
    assert result.stator.winding.p == 3
    assert result.stator.winding.Nlayer == 1

    assert type(result.rotor) is LamSlotMag
    assert result.rotor.L1 == 0.55

    assert type(result.rotor.slot) is SlotM11
    assert result.rotor.slot.W0 == pi / 4

    assert result.rotor.slot.Wmag == pi / 4
    assert result.rotor.slot.Hmag == 3

    assert type(result.shaft) is Shaft
    assert result.shaft.Lshaft == 0.65

    assert result.frame == None


def test_save_load_json_compressed():
    """Check that you can save/load a compressed json file"""
    test_obj = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    # Check save
    file_path = join(save_path, "Toyota_Prius_compressed")
    assert not isfile(file_path + ".json.gz")
    test_obj.save(file_path, type_compression=1)
    assert isfile(file_path + ".json.gz")
    # Check load
    test_obj2 = load(file_path + ".json.gz")
    assert test_obj == test_obj2


@pytest.mark.IPMSM
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_save_load_folder_path():
    """Save with a folder path"""
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    simu = Simu1(name="test_save_load_folder_path", machine=Toyota_Prius, struct=None)

    # Definition of the enforced output of the electrical module
    N0 = 3000
    Is = ImportMatrixVal(value=array([[2.25353053e02, 2.25353053e02, 2.25353053e02]]))
    time = ImportGenVectLin(start=0, stop=1, num=1, endpoint=True)
    angle = ImportGenVectLin(start=0, stop=2 * pi, num=1024, endpoint=False)

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        OP=OPdq(N0=N0),
        time=time,
        angle=angle,
        rot_dir=-1,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=2, type_BH_rotor=0, is_periodicity_a=True, is_sliding_band=False
    )
    simu.force = None
    simu.struct = None

    post1 = PostFunction(run="lambda x:x+2")
    post2 = PostFunction(run=join(TEST_DATA_DIR, "example_post.py"))
    simu.postproc_list = [post1, post2]

    test_obj = Output(simu=simu)
    test_obj.post.legend_name = "Slotless lamination"

    loc_save_path = join(save_path, "FolderSaved")
    file_path = join(loc_save_path, "FolderSaved.json")
    logger.debug(loc_save_path)
    logger.debug(file_path)

    if isfile(file_path):
        remove(file_path)

    # Check save
    assert isfile(file_path) == False
    test_obj.save(loc_save_path, is_folder=True)
    assert isfile(file_path)
    assert isfile(join(loc_save_path, "MagnetPrius.json"))
    assert isfile(join(loc_save_path, "MagnetPrius_00001.json"))
    assert isfile(join(loc_save_path, "M400-50A.json"))
    assert isfile(join(loc_save_path, "M400-50A_00001.json"))
    assert isfile(join(loc_save_path, "M400-50A_00002.json"))
    assert isfile(join(loc_save_path, "Insulator1.json"))
    assert isfile(join(loc_save_path, "Air.json"))
    assert isfile(join(loc_save_path, "Copper1.json"))
    assert isfile(join(loc_save_path, "Toyota_Prius.json"))
    assert isfile(join(loc_save_path, "test_save_load_folder_path.json"))  # Simu
    assert isfile(join(loc_save_path, "FolderSaved.json"))  # Output
    assert len(listdir(loc_save_path)) == 11
    # Check load
    test_obj2 = load(loc_save_path)
    assert test_obj == test_obj2
    assert callable(test_obj.simu.postproc_list[0]._run_func)
    assert callable(test_obj.simu.postproc_list[1]._run_func)
    # Check that material name are still the same
    assert test_obj2.simu.machine.stator.mat_type.name == "M400-50A"
    assert test_obj2.simu.machine.rotor.mat_type.name == "M400-50A"
    assert test_obj2.simu.machine.shaft.mat_type.name == "M400-50A"

    # Check that the machine can be updated
    test_obj2.simu.machine.stator.L1 = 999
    test_obj2.simu.machine.name = "Toyota2"
    # Check that empty materials are not save in separate file
    test_obj2.simu.machine.stator.winding.conductor.ins_mat._set_None()

    test_obj2.save(loc_save_path, is_folder=True, type_handle_old=1)
    assert isfile(join(loc_save_path, "MagnetPrius.json"))
    assert isfile(join(loc_save_path, "MagnetPrius_00001.json"))
    assert isfile(join(loc_save_path, "M400-50A.json"))
    assert isfile(join(loc_save_path, "M400-50A_00001.json"))
    assert isfile(join(loc_save_path, "M400-50A_00002.json"))
    assert not isfile(join(loc_save_path, "Insulator1.json"))  # Material removed
    assert not isfile(join(loc_save_path, "Material_00001.json"))  # Material removed
    assert isfile(join(loc_save_path, "Air.json"))
    assert isfile(join(loc_save_path, "Copper1.json"))
    assert isfile(join(loc_save_path, "Toyota2.json"))
    assert not isfile(join(loc_save_path, "Toyota_Prius.json"))
    assert isfile(join(loc_save_path, "test_save_load_folder_path.json"))  # Simu
    assert isfile(join(loc_save_path, "FolderSaved.json"))  # Output
    assert len(listdir(loc_save_path)) == 10
    test_obj3 = load(loc_save_path)

    assert test_obj2.simu.machine.stator.L1 == test_obj3.simu.machine.stator.L1
    assert len(test_obj2.compare(test_obj3)) == 0

    # Check save with backup folder
    test_obj2.save(loc_save_path, is_folder=True, type_handle_old=2)
    assert isfile(join(loc_save_path, "MagnetPrius.json"))
    assert isfile(join(loc_save_path, "MagnetPrius_00001.json"))
    assert isfile(join(loc_save_path, "M400-50A.json"))
    assert isfile(join(loc_save_path, "M400-50A_00001.json"))
    assert isfile(join(loc_save_path, "M400-50A_00002.json"))
    assert isfile(join(loc_save_path, "Air.json"))
    assert isfile(join(loc_save_path, "Copper1.json"))
    assert isfile(join(loc_save_path, "Toyota2.json"))
    assert isfile(join(loc_save_path, "test_save_load_folder_path.json"))  # Simu
    assert isfile(join(loc_save_path, "FolderSaved.json"))  # Output
    assert len(listdir(loc_save_path)) == 11

    back_path = join(loc_save_path, "Backup")
    assert isdir(back_path)
    assert len(listdir(back_path)) == 10


def test_save_load_just_name():
    """Save in a file and load"""

    test_obj = SlotW10(Zs=10)

    file_path = join(getcwd(), "test_slot.json")
    if isfile(file_path):
        remove(file_path)
    assert isfile(file_path) == False
    test_obj.save("test_slot")
    assert isfile(file_path)

    result = load("test_slot.json")
    assert type(result) is SlotW10
    assert result.Zs == 10
    # remove(file_path)


def test_save_load_DXF_flat():
    """Check that you can save/load a machine with dxf slot/hole in flat mode"""
    Prius_DXF = load(join(DATA_DIR, "Machine", "Toyota_Prius_DXF.json"))
    save_dir = join(save_path, "Toyota_Prius_DXF")
    # Check save
    assert not isdir(save_dir)
    Prius_DXF.save(save_path=save_dir, is_folder=True)
    assert isdir(save_dir)
    file_list = listdir(save_dir)
    assert len(file_list) == 12
    assert "hole.json" in file_list
    assert "slot.json" in file_list
    # Check load
    Prius_2 = load(save_dir)
    assert isinstance(Prius_2.stator.slot, SlotUD)
    assert isinstance(Prius_2.rotor.hole[0], HoleUD)
    assert len(Prius_DXF.compare(Prius_2)) == 0
    # Remove file and check None
    remove(join(save_dir, "hole.json"))
    remove(join(save_dir, "slot.json"))
    Prius_3 = load(save_dir)
    assert Prius_3.stator.slot is None
    assert Prius_3.rotor.hole[0] is None


def test_load_error_missing():
    """Test that the load function can detect missing file"""
    with pytest.raises(LoadMissingFileError):
        load(save_path)


def test_load_error_wrong_type():
    """Test that the load function can detect wrong type"""
    with pytest.raises(LoadWrongTypeError):
        load_list(load_file_2)


def test_load_error_missing_class():
    """Test that the load function can detect missing __class__"""
    with pytest.raises(
        LoadWrongDictClassError, match='Key "__class__" missing in loaded file'
    ):
        load(load_file_1)


def test_load_error_wrong_class():
    """Test that the load function can detect wrong __class__"""
    with pytest.raises(
        InitUnKnowClassError, match="Unknow class name SlotDoesntExist when loading"
    ):
        load(load_file_2)


@pytest.mark.skip
def test_save_load_list():
    """Test the save and load function of data structures"""
    # SetUp
    test_obj_1 = MachineSIPMSM(name="test", desc="test\non\nseveral lines")
    test_obj_1.stator = LamSlotWind(L1=0.45)
    test_obj_1.stator.slot = SlotW10(Zs=10, H0=0.21, W0=0.23)
    test_obj_1.stator.winding = Winding(qs=5, p=3, Nlayer=1)
    test_obj_1.rotor = LamSlotMag(L1=0.55)
    test_obj_1.rotor.slot = SlotM11(W0=pi / 4, Wmag=pi / 4, Hmag=3)
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
    save_json(test_list, file_path)
    assert isfile(file_path)

    # Load Test
    result_list = load_list(file_path)
    # set tuple to None as save will do
    test_list[0] = None
    assert result_list == test_list


@pytest.mark.skip
def test_save_load_dict():
    """Test the save and load function of data structures"""
    # SetUp
    test_obj_1 = MachineSIPMSM(name="test", desc="test\non\nseveral lines")
    test_obj_1.stator = LamSlotWind(L1=0.45)
    test_obj_1.stator.slot = SlotW10(Zs=10, H0=0.21, W0=0.23)
    test_obj_1.stator.winding = Winding(qs=5, p=3)
    test_obj_1.rotor = LamSlotMag(L1=0.55)
    test_obj_1.rotor.slot = SlotM11(W0=pi / 4, Wmag=pi / 4, Hmag=3)
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
    save_json(test_dict, file_path)
    assert isfile(file_path)

    # Load Test
    result_dict = load_dict(file_path)
    # set tuple to None as save will do
    test_dict["tuple"] = None
    assert result_dict == test_dict


@pytest.mark.MagFEMM
@pytest.mark.FEMM
@pytest.mark.IPMSM
@pytest.mark.SingleOP
@pytest.mark.periodicity
@pytest.mark.parametrize("type_file", ["json", "h5", "pkl"])
def test_save_load_simu(type_file):
    """Save in hdf5 file"""
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    simu = Simu1(name="test_save_load_simu", machine=Toyota_Prius, struct=None)

    # Definition of the enforced output of the electrical module
    N0 = 3000
    Is = ImportMatrixVal(value=array([[2.25353053e02, 2.25353053e02, 2.25353053e02]]))
    time = ImportGenVectLin(start=0, stop=1, num=1, endpoint=True)
    angle = ImportGenVectLin(start=0, stop=2 * pi, num=1024, endpoint=False)

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        OP=OPdq(N0=N0),
        time=time,
        angle=angle,
        rot_dir=-1,
    )

    # Definition of the magnetic simulation (no symmetry)
    simu.mag = MagFEMM(
        type_BH_stator=2, type_BH_rotor=0, is_periodicity_a=True, is_sliding_band=True
    )
    simu.force = None
    simu.struct = None

    test_obj = Output(simu=simu)
    test_obj.simu.run()
    test_obj.post.legend_name = "Slotless lamination"

    file_path = join(save_path, "test_save_{}.{}".format(type_file, type_file))
    logger.debug(file_path)

    if isfile(file_path):
        remove(file_path)

    assert isfile(file_path) == False
    test_obj.save(file_path)
    assert isfile(file_path)
    test_obj2 = load(file_path)
    assert test_obj == test_obj2


if __name__ == "__main__":
    test_save_load_folder_path()
    # test_save_load_DXF_flat()
    # test_save_load_simu("json")
    # test_save_load_simu("h5")
    # test_save_load_simu("pkl")
    print("Done")

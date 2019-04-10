# -*- coding: utf-8 -*-
"""
Created on Mon Dec 01 15:41:23 2014

@author: pierre_b
"""

from os import remove, getcwd
from os.path import isfile, join
from unittest import TestCase
from unittest.mock import patch  # for unittest of input

from ddt import data, ddt
from numpy import pi

from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MagnetType11 import MagnetType11
from pyleecan.Classes.SlotMPolar import SlotMPolar
from pyleecan.Classes.SlotW10 import SlotW10
from pyleecan.Classes.WindingDW1L import WindingDW1L
from pyleecan.Classes.Shaft import Shaft
from pyleecan.Tests import DATA_DIR, save_load_path as save_path
from pyleecan.Functions.load import load, LoadMissingFileError, LoadWrongDictClassError

load_file_1 = join(DATA_DIR, "test_wrong_slot_load_1.json")
load_file_2 = join(DATA_DIR, "test_wrong_slot_load_2.json")


class test_save_load_fct(TestCase):
    """unittest for save and load fonctions"""

    def test_save_load_machine(self):
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
        self.assertFalse(isfile(file_path))
        test_obj.save(file_path)
        self.assertTrue(isfile(file_path))

        # Load Test
        result = load(file_path)
        self.assertTrue(type(result) is MachineSIPMSM)
        self.assertEqual(result.name, "test")
        self.assertEqual(result.desc, "test\non\nseveral lines")

        self.assertTrue(type(result.stator) is LamSlotWind)
        self.assertEqual(result.stator.L1, 0.45)

        self.assertTrue(type(result.stator.slot) is SlotW10)
        self.assertEqual(result.stator.slot.Zs, 10)
        self.assertEqual(result.stator.slot.H0, 0.21)
        self.assertEqual(result.stator.slot.W0, 0.23)

        self.assertTrue(type(result.stator.winding) is WindingDW1L)
        self.assertEqual(result.stator.winding.qs, 5)

        self.assertTrue(type(result.rotor) is LamSlotMag)
        self.assertEqual(result.rotor.L1, 0.55)

        self.assertTrue(type(result.rotor.slot) is SlotMPolar)
        self.assertEqual(result.rotor.slot.W0, pi / 4)

        self.assertTrue(type(result.rotor.slot.magnet) is list)
        self.assertTrue(type(result.rotor.slot.magnet[0]) is MagnetType11)
        self.assertEqual(len(result.rotor.slot.magnet), 1)
        self.assertEqual(result.rotor.slot.magnet[0].Wmag, pi / 4)
        self.assertEqual(result.rotor.slot.magnet[0].Hmag, 3)

        self.assertTrue(type(result.shaft) is Shaft)
        self.assertEqual(result.shaft.Lshaft, 0.65)

        self.assertEqual(result.frame, None)

    def test_save_folder_path(self):
        """Save with a folder path
        """

        test_obj = LamSlotWind(L1=0.45)

        file_path = join(save_path, "LamSlotWind.json")
        if isfile(file_path):
            remove(file_path)
        self.assertFalse(isfile(file_path))
        test_obj.save(save_path)
        self.assertTrue(isfile(file_path))

    def test_save_load_just_name(self):
        """Save with a folder path
        """

        test_obj = SlotW10(Zs=10)

        file_path = join(getcwd(), "test_slot.json")
        if isfile(file_path):
            remove(file_path)
        self.assertFalse(isfile(file_path))
        test_obj.save("test_slot")
        self.assertTrue(isfile(file_path))

        result = load("test_slot")
        self.assertTrue(type(result) is SlotW10)
        self.assertEqual(result.Zs, 10)
        # remove(file_path)

    def test_load_error_missing(self):
        """Test that the load function can detect missing file
        """
        with self.assertRaises(LoadMissingFileError):
            load(save_path)

    def test_load_error_missing_class(self):
        """Test that the load function can detect missing __class__
        """
        with self.assertRaises(LoadWrongDictClassError) as context:
            load(load_file_1)
        self.assertEqual(
            'Key "__class__" missing in loaded file', str(context.exception)
        )

    def test_load_error_wrong_class(self):
        """Test that the load function can detect wrong __class__
        """
        with self.assertRaises(LoadWrongDictClassError) as context:
            load(load_file_2)
        self.assertEqual(
            "SlotDoesntExist is not a pyleecan class", str(context.exception)
        )

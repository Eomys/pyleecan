# -*- coding: utf-8 -*-

import pytest
from pyleecan.Classes.ConvertMC import ConvertMC
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.HoleM60 import HoleM60
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW21 import SlotW21


class TestConverterSIPMSM(object):
    def test_SIPMSM(self):
        """check if SIPMSM is correct define"""
        path = "/Users\LAP17\Documents/Documentation motor-CAD/fichier.mot/various_mot_files/VF_Manatee_Hairpin_winding.mot"

        conv = ConvertMC()
        # conversion file in machine
        machine = conv.convert_to_P(path)

        assert isinstance(machine, MachineIPMSM)

        # rotor
        assert isinstance(machine.rotor, LamHole)

        assert isinstance(machine.rotor.axial_vent[0], VentilationCirc)
        assert isinstance(machine.rotor.axial_vent[1], VentilationCirc)

        assert isinstance(machine.rotor.hole[0], HoleM60)
        assert isinstance(machine.rotor.hole[1], HoleM60)

        # stator
        assert isinstance(machine.stator, LamSlotWind)
        assert isinstance(machine.stator.slot, SlotW21)


if __name__ == "__main__":
    a = TestConverterSIPMSM()
    a.test_SIPMSM()
    print("Test Done")

# -*- coding: utf-8 -*-

import pytest
from pyleecan.Classes.ConvertMC import ConvertMC


class Test_converter_mot(object):
    def test_SIPMSM(self):
        """check if dict are equal"""
        path = "/Users\LAP17\Documents/Documentation motor-CAD/fichier.mot/various_mot_files/VF_Manatee_Hairpin_winding.mot"

        Conv = ConvertMC()
        # conversion file in machine
        machine = Conv.convert_to_P(path)

        assert type(machine).__name__ == "MachineIPMSM"

        # rotor
        assert type(machine.rotor).__name__ == "LamHole"

        assert type(machine.rotor.axial_vent[0]).__name__ == "VentilationCirc"
        assert type(machine.rotor.axial_vent[1]).__name__ == "VentilationCirc"
        assert type(machine.rotor.hole[0]).__name__ == "HoleM60"
        assert type(machine.rotor.hole[1]).__name__ == "HoleM60"

        # stator
        assert type(machine.stator).__name__ == "LamSlotWind"
        assert type(machine.stator.slot).__name__ == "SlotW21"


if __name__ == "__main__":
    a = Test_converter_mot()
    a.test_SIPMSM()
    print("Test Done")

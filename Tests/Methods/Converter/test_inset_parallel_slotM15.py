import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM15 import SlotM15


rule_list = list()

# add equation rules

other_dict = {}
other_dict["[Dimensions]"] = {}
other_dict["[Dimensions]"]["Magnet_Thickness"] = 4
other_dict["[Dimensions]"]["Magnet_Arc_[ED]"] = 120


class Test_converter_mot(object):
    def test_inset_parallel_slotM15(self):
        machine = MachineSIPMSM()
        machine.rotor = LamSlotMag()
        machine.rotor.slot = SlotM15()

        rule = RuleComplex(fct_name="inset_breadloaf_slotM12", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict, machine, {"ED": (2 / 8) * (pi / 180), "m": 1}
        )

        assert machine.rotor.slot.W1 == pytest.approx(2.5881904510252074)
        assert machine.rotor.slot.Rtopm == pytest.approx(0.001)


if __name__ == "__main__":
    a = Test_converter_mot()
    a.test_inset_parallel_slotM15()
    print("Test Done")

import pytest
from numpy import pi
from pyleecan.Classes.RuleSimple import RuleSimple

from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW11 import SlotW11


# creating a dictionary
other_dict = {
    "[Dimensions]": {
        "Slot_tooth": 15,
        "Slot_Opening": 12.5,
        "Slot_Depth": 90,
    }
}


class Test_converter_mot(object):
    def test_rule_simple_0(self):
        """test rule simple"""
        machine = MachineSIPMSM()
        machine.stator = LamSlotWind()
        machine.stator.slot = SlotW11()

        rule = RuleSimple(
            other_key_list=["[Dimensions]", "Slot_Opening"],
            P_obj_path=f"machine.stator.slot.W0",
            unit_type="m",
            scaling_to_P=1,
        )
        # rule simple to set slot.W0
        machine = rule.convert_to_P(other_dict, machine, other_unit_dict={"m": 1})
        msg = f"{machine.stator.slot.W0}, should be equal at 12.5"
        assert abs(machine.stator.slot.W0) == pytest.approx(12.5), msg

    def test_rule_simple_1(self):
        """test rule simple"""
        machine = MachineSIPMSM()
        machine.stator = LamSlotWind()
        machine.stator.slot = SlotW11()
        rule = RuleSimple(
            other_key_list=["[Dimensions]", "Slot_tooth"],
            P_obj_path=f"machine.stator.slot.W2",
            unit_type="m",
            scaling_to_P=0.5,
        )
        # rule simple to set value, with conversion
        machine = rule.convert_to_P(other_dict, machine, other_unit_dict={"m": 1})
        msg = f"{machine.stator.slot.W2}, should be equal at 7.5"
        assert abs(machine.stator.slot.W2) == pytest.approx(7.5), msg

    def test_rule_simple_2(self):
        """test rule simple"""
        machine = MachineSIPMSM()
        machine.stator = LamSlotWind()
        machine.stator.slot = SlotW11()
        rule = RuleSimple(
            other_key_list=["[Dimensions]", "Slot_Depth"],
            P_obj_path=f"machine.stator.slot.W1",
            unit_type="deg",
            scaling_to_P=0.5,
        )
        # rule simple to set value, with conversion
        machine = rule.convert_to_P(
            other_dict, machine, other_unit_dict={"deg": pi / 180}
        )
        msg = f"{machine.stator.slot.W1}, should be equal at pi / 4"
        assert abs(machine.stator.slot.W1) == pytest.approx(pi / 4), msg


if __name__ == "__main__":
    a = Test_converter_mot()
    a.test_rule_simple_0()
    a.test_rule_simple_1()
    a.test_rule_simple_2()
    print("Done")

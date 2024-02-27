import pytest
from numpy import pi
from pyleecan.Classes.RuleSimple import RuleSimple

from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW11 import SlotW11


class TestRuleSimple(object):
    @staticmethod
    def setup_class(cls):
        # other_dict of Motror-CAD converter
        cls.other_dict = {
            "[Dimensions]": {
                "Slot_tooth": 15,
                "Slot_Opening": 12.5,
                "Slot_Depth": 90,
            }
        }

    def test_identity(self):
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
        machine = rule.convert_to_P(self.other_dict, machine, other_unit_dict={"m": 1})

        # check the convertion
        expected_value = 12.5
        msg = f"{machine.stator.slot.W0}, should be equal at {expected_value}"
        assert abs(machine.stator.slot.W0) == pytest.approx(expected_value), msg

    def test_scaling(self):
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
        machine = rule.convert_to_P(self.other_dict, machine, other_unit_dict={"m": 1})

        # check the convertion
        expected_value = 7.5
        msg = f"{machine.stator.slot.W2}, should be equal at {expected_value}"
        assert abs(machine.stator.slot.W2) == pytest.approx(expected_value), msg

    def test_scaling_unit(self):
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
            self.other_dict, machine, other_unit_dict={"deg": pi / 180}
        )

        # check the convertion
        msg = f"{machine.stator.slot.W1}, should be equal at pi / 4"
        assert abs(machine.stator.slot.W1) == pytest.approx(pi / 4), msg

    def test_string(self):
        pass


if __name__ == "__main__":
    a = TestRuleSimple()
    a.test_identity()
    a.test_scaling()
    a.test_scaling_unit()
    print("Done")

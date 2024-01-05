import pytest

from pyleecan.Classes.RuleEquation import RuleEquation
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW11 import SlotW11


class Test_converter_mot(object):
    @staticmethod
    def setup_class(cls):
        # other_dict of Motror-CAD converter
        cls.other_dict = {
            "[Dimensions]": {
                "Slot_tooth": 15,
                "Slot_Opening": 12.5,
                "Slot_Depth": 72,
                "Slot_2": 6.75,
                "Slot_3": 6.75,
                "Slot_4": 3.25,
            }
        }

    def test_rule_equation_0(self):
        """test rule equation"""

        # Construct the machine in which the slot will be set
        machine = MachineSIPMSM()
        machine.stator = LamSlotWind()
        machine.stator.slot = SlotW11()
        machine.stator.slot.W0 = 4

        # Define and apply the slot rule
        rule = RuleEquation(
            param=[
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Slot_Depth"],
                    "variable": "y",
                },
                {
                    "src": "pyleecan",
                    "path": f"machine.stator.slot.H2",
                    "variable": "x",
                },
                {
                    "src": "pyleecan",
                    "path": f"machine.stator.slot.W0",
                    "variable": "b",
                },
            ],
            unit_type="m",
            equation="y/3 = b +2*x",
        )

        # 1/3 has any physic meening, only for testing
        machine = rule.convert_to_P(
            self.other_dict, machine, other_unit_dict={"m": 1 / 3}
        )

        # check the convertion
        expected_value = 2.0
        msg = f"{machine.stator.slot.H2}, should be equal at {expected_value}"
        assert abs(machine.stator.slot.H2) == pytest.approx(expected_value), msg

    def test_rule_equation_1(self):
        """test rule equation"""

        # Construct the machine in which the slot will be set
        machine = MachineSIPMSM()
        machine.stator = LamSlotWind()
        machine.stator.slot = SlotW11()
        machine.stator.slot.W0 = 12.5
        machine.stator.slot.H2 = 5.75

        # Define and apply the slot rule
        rule = RuleEquation(
            param=[
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Slot_Depth"],
                    "variable": "d",
                },
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Slot_2"],
                    "variable": "y",
                },
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Slot_3"],
                    "variable": "e",
                },
                {
                    "src": "other",
                    "path": ["[Dimensions]", "Slot_4"],
                    "variable": "f",
                },
                {
                    "src": "pyleecan",
                    "path": "machine.stator.slot.H2",
                    "variable": "a",
                },
                {
                    "src": "pyleecan",
                    "path": "machine.stator.slot.W0",
                    "variable": "b",
                },
                {
                    "src": "pyleecan",
                    "path": "machine.stator.slot.W1",
                    "variable": "x",
                },
            ],
            unit_type="m",
            equation="(y/3 - e )/f +d  = b +2*x -a ",
        )

        machine = rule.convert_to_P(self.other_dict, machine, other_unit_dict={"m": 1})

        # check the convertion
        expected_value = 31.9326923076923
        msg = f"{machine.stator.slot.W1} expected {expected_value}"
        assert abs(machine.stator.slot.W1) == pytest.approx(expected_value), msg


if __name__ == "__main__":
    a = Test_converter_mot()
    a.test_rule_equation_0()
    a.test_rule_equation_1()
    print("Done")

import pytest

from pyleecan.Classes.RuleComplex import RuleComplex

from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW11 import SlotW11


class TestComplexRulePolePairNumber(object):
    def test_set_pole_pair_number(self):
        """test rule complex"""

        other_dict = {
            "[Dimensions]": {
                "Pole_Number": 6,
            }
        }

        machine = MachineSIPMSM()
        machine.stator = LamSlotWind()
        machine.stator.slot = SlotW11()
        rule = RuleComplex(fct_name="set_pole_pair_number", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(other_dict, machine, other_unit_dict=None)
        pole_number = machine.get_pole_pair_number()
        assert pole_number == pytest.approx(3)

        other = rule.convert_to_other(other_dict, machine, other_unit_dict=None)
        assert other["[Dimensions]"]["Pole_Number"] == pytest.approx(6)


if __name__ == "__main__":
    a = TestComplexRulePolePairNumber()
    a.test_set_pole_pair_number()
    print("Done")

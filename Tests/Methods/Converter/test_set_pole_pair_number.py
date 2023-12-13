import pytest

from pyleecan.Classes.RuleComplex import RuleComplex

from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.SlotW11 import SlotW11
from pyleecan.Classes.HoleM50 import HoleM50


class TestComplexRulePolePairNumber(object):
    @staticmethod
    def setup_class(cls):
        # other_dict of Motror-CAD converter
        cls.other_dict = {
            "[Dimensions]": {
                "Pole_Number": 6,
            }
        }

    def test_set_pole_pair_number_SPMSM(self):
        """test rule complex"""

        machine = MachineSIPMSM()
        machine.stator = LamSlotWind()
        machine.stator.slot = SlotW11()
        rule = RuleComplex(fct_name="set_pole_pair_number", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(self.other_dict, machine, other_unit_dict=None)

        # check the convertion
        pole_number = machine.get_pole_pair_number()
        expected_value = 3
        msg = f"{pole_number} expected {expected_value}"
        assert pole_number == pytest.approx(expected_value), msg

        other = rule.convert_to_other(self.other_dict, machine, other_unit_dict=None)
        pole_number = other["[Dimensions]"]["Pole_Number"]
        expected_value = 6
        msg = f"{pole_number} expected {expected_value}"
        assert pole_number == pytest.approx(expected_value), msg

    def test_set_pole_pair_number_IPMSM(self):
        """test rule complex"""

        machine = MachineIPMSM()
        machine.stator = LamSlotWind()
        machine.stator.slot = SlotW11()

        machine.rotor = LamHole()
        machine.rotor.hole.append(HoleM50())
        rule = RuleComplex(fct_name="set_pole_pair_number", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(self.other_dict, machine, other_unit_dict=None)

        # check the convertion
        pole_number = machine.get_pole_pair_number()
        expected_value = 3
        msg = f"{pole_number} expected {expected_value}"
        assert pole_number == pytest.approx(expected_value), msg

        other = rule.convert_to_other(self.other_dict, machine, other_unit_dict=None)
        pole_number = other["[Dimensions]"]["Pole_Number"]
        expected_value = 6
        msg = f"{pole_number} expected {expected_value}"
        assert pole_number == pytest.approx(6), msg


if __name__ == "__main__":
    a = TestComplexRulePolePairNumber()
    a.test_set_pole_pair_number_SIPMSM()
    a.test_set_pole_pair_number_IPMSM()
    print("Done")

import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotW14 import SlotW14


class TestComplexRuleSlotW14(object):
    def test_slotW14_H1(self):
        """test rule complex"""

        # Construct the machine in which the slot will be set
        machine = MachineSIPMSM()
        machine.stator = LamSlot()
        machine.stator.slot = SlotW14()

        machine.stator.slot.W0 = 0.0024
        machine.stator.slot.W3 = 0.079
        machine.stator.slot.H0 = 0.0006
        machine.stator.slot.H1 = 38
        machine.stator.slot.H3 = 0.05
        machine.stator.slot.H1_is_rad = True

        # Define and apply the slot rule
        rule = RuleComplex(fct_name="slotW14_H1", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict={}, machine=machine, other_unit_dict={"deg": pi / 180}
        )

        # check the convertion
        excepted_value = 0.01412752
        msg = f"{machine.stator.slot.H1} expected {excepted_value}"
        assert machine.stator.slot.H1 == pytest.approx(excepted_value), msg


if __name__ == "__main__":
    a = TestComplexRuleSlotW14()
    a.test_slotW14_H1()
    print("Test Done")

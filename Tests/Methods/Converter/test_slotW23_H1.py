import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotW23 import SlotW23


class TestComplexRuleSlotW23(object):
    def test_slotW23_H1(self):
        """test rule complex"""

        # Construct the machine in which the slot will be set
        machine = MachineSIPMSM()
        machine.stator = LamSlot()
        machine.stator.slot = SlotW23()

        machine.stator.slot.W0 = 0.0024
        machine.stator.slot.W1 = 0.0044
        machine.stator.slot.W2 = 0.0034
        machine.stator.slot.H0 = 0.0006
        machine.stator.slot.H1 = 45
        machine.stator.slot.H2 = 0.033118584
        machine.stator.slot.H1_is_rad = True

        # Define and apply the slot rule
        rule = RuleComplex(fct_name="slotW23_H1", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict={}, machine=machine, other_unit_dict={"deg": pi / 180}
        )

        # check the convertion
        excepted_value = 0.001619775
        msg = f"{machine.stator.slot.H1} expected {excepted_value}"
        assert machine.stator.slot.H1 == pytest.approx(excepted_value), msg


if __name__ == "__main__":
    a = TestComplexRuleSlotW23()
    a.test_slotW23_H1()
    print("Test Done")

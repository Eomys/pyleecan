import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotW11 import SlotW11


class TestComplexRuleSlotW11(object):
    def test_slotW11_H1(self):
        """test rule complex"""

        # Construct the machine in which the slot will be set
        machine = MachineSIPMSM()
        machine.stator = LamSlot()
        machine.stator.slot = SlotW11()

        machine.stator.slot.W0 = 0.0024
        machine.stator.slot.W3 = 0.079
        machine.stator.slot.H0 = 0.0006
        machine.stator.slot.H1 = 38
        machine.stator.slot.H2 = 0.033118584
        machine.stator.slot.R1 = 0.00423
        machine.stator.slot.H1_is_rad = True
        machine.stator.slot.is_cstt_tooth = True

        # Define and apply the slot rule
        rule = RuleComplex(fct_name="slotW11_H1", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict={}, machine=machine, other_unit_dict={"deg": pi / 180}
        )

        # check the convertion
        excepted_value = 0.01070256
        msg = f"{machine.stator.slot.H1} expected {excepted_value}"
        assert machine.stator.slot.H1 == pytest.approx(excepted_value), msg


if __name__ == "__main__":
    a = TestComplexRuleSlotW11()
    a.test_slotW11_H1()
    print("Test Done")

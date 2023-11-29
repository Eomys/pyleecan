import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotW21 import SlotW21


class TestComplexRuleSlotW21(object):
    def test_slotW21_H1(self):
        """test rule complex"""
        machine = MachineSIPMSM()
        machine.stator = LamSlot()
        machine.stator.slot = SlotW21()

        machine.stator.slot.W0 = 0.0024
        machine.stator.slot.W1 = 0.0044
        machine.stator.slot.W2 = 0.0034
        machine.stator.slot.H0 = 0.0006
        machine.stator.slot.H1 = 45
        machine.stator.slot.H2 = 0.033118584
        machine.stator.slot.H1_is_rad = True

        rule = RuleComplex(fct_name="slotW21_H1", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict={}, machine=machine, other_unit_dict={"deg": pi / 180}
        )

        assert machine.stator.slot.H1 == pytest.approx(0.0016197751905438619)


if __name__ == "__main__":
    a = TestComplexRuleSlotW21()
    a.test_slotW21_H1()
    print("Test Done")

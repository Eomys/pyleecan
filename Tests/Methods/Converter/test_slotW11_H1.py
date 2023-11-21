import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.SlotW11 import SlotW11


rule_list = list()


class Test_converter_mot(object):
    def test_slotW11_H1(self):
        """test rule complex"""
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

        rule = RuleComplex(fct_name="slotW11_H1", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict={}, machine=machine, other_unit_dict={"deg": pi / 180}
        )

        assert machine.stator.slot.H1 == pytest.approx(0.010702566870304464)


if __name__ == "__main__":
    a = Test_converter_mot()
    a.test_slotW11_H1()
    print("Test Done")

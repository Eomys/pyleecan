import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotMag import LamSlotMag
from pyleecan.Classes.SlotM13 import SlotM13


other_dict = {
    "[Dimensions]": {
        "Magnet_Thickness": 4,
        "Magnet_Arc_[ED]": 120,
        "Magnet_Reduction": 1,
    }
}


class TestComplexRuleSlotM13(object):
    def test_surface_breadloaf_slotM13(self):
        """test rule complex"""
        machine = MachineSIPMSM()
        machine.rotor = LamSlotMag()
        machine.rotor.slot = SlotM13()

        machine.rotor.slot.H0 = 0.01
        machine.rotor.slot.H1 = 0.02

        rule = RuleComplex(fct_name="surface_breadloaf_slotM13", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict, machine, {"ED": (2 / 8) * (pi / 180), "m": 0.001}
        )

        assert machine.rotor.slot.W0 == pytest.approx(0.5197086425658616)
        assert machine.rotor.slot.W1 == pytest.approx(0.5197086425658616)
        assert machine.rotor.slot.Rtopm == pytest.approx(0.9726990498218554)


if __name__ == "__main__":
    a = TestComplexRuleSlotM13()
    a.test_surface_breadloaf_slotM13()
    print("Test Done")

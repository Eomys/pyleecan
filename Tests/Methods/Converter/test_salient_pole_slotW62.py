import pytest
from numpy import pi
from pyleecan.Classes.LamSlot import LamSlot
from pyleecan.Classes.LamSlotMag import LamSlotMag

from pyleecan.Classes.SlotW62 import SlotW62

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM


slotW62_test = list()

# Common values
other_dict = {
    "[Dimensions]": {
        "Pole_Tip_Depth": 50,
    }
}

# Internal Slot
lam = LamSlotMag(
    Rint=0.135,
    Rext=0.3,
    is_internal=True,
    is_stator=False,
)
lam.slot = SlotW62(
    Zs=12,
    H0=70e-3,
    W0=50e-3,
    H1=30e-3,
    W1=120e-3,
    W2=15e-3,
    H2=40e-3,
    W3=10e-3,
    H3=12e-3,
)

slotW62_test.append(
    {
        "test_obj": lam,
        "other_dict": other_dict,
        "H1": 0.0011558998,
    }
)


class TestComplexRuleSlotM13(object):
    @pytest.mark.parametrize("test_dict", slotW62_test)
    def test_salient_pole_slotW62(self, test_dict):
        """test rule complex"""

        # retreive other_dict
        other_dict = test_dict["other_dict"]
        lam = test_dict["test_obj"]

        machine = MachineSIPMSM()
        machine.rotor = lam

        # Define and apply the slot rule
        rule = RuleComplex(fct_name="salient_pole_slotW62", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict, machine, {"ED": (2 / 8) * (pi / 180), "m": 0.001}
        )

        # retreive expected value
        H1 = test_dict["H1"]

        # check the convertion
        msg = f"{machine.rotor.slot.H1} expected {H1}"
        assert machine.rotor.slot.H1 == pytest.approx(H1), msg


if __name__ == "__main__":
    a = TestComplexRuleSlotM13()
    for test_dict in slotW62_test:
        a.test_salient_pole_slotW62(test_dict)
    print("Test Done")

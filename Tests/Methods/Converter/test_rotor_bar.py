import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSCIM import MachineSCIM
from pyleecan.Classes.LamSquirrelCage import LamSquirrelCage
from pyleecan.Classes.SlotW11 import SlotW11

rotor_bar_test = list()
# Common values
other_dict = {
    "[Dimensions]": {
        "EndRing_Inner_Add_F": 60,
        "EndRing_Outer_Add_F": 60,
        "EndRing_Thickness_F": 50,
        "EndRing_Thickness_R": 50,
    }
}
rotor_bar_test.append(
    {
        "other_dict": other_dict,
        "Lscr": 0.005,
        "Hscr": 0.05642187087056365,
        "Lewout": 0,
    }
)


class TestComplexRuleRotorBar(object):
    @pytest.mark.parametrize("test_dict", rotor_bar_test)
    def test_rotor_bar(self, test_dict):
        """test rule complex"""

        # Construct the machine in which the slot will be set
        machine = MachineSCIM()
        machine.rotor = LamSquirrelCage()

        machine.rotor.slot = SlotW11()

        machine.rotor.slot.W0 = 0.0024
        machine.rotor.slot.W3 = 0.079
        machine.rotor.slot.H0 = 0.0006
        machine.rotor.slot.H1 = 38
        machine.rotor.slot.H2 = 0.033118584
        machine.rotor.slot.R1 = 0.00423
        machine.rotor.slot.H1_is_rad = True
        machine.rotor.slot.is_cstt_tooth = True

        other_dict = test_dict["other_dict"]

        # Define and apply the slot rule
        rule = RuleComplex(fct_name="rotor_bar", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict=other_dict,
            machine=machine,
            other_unit_dict={"deg": pi / 180, "m": 0.0001},
        )

        # check the convertion
        Lscr = test_dict["Lscr"]
        msg = f"{machine.rotor.Lscr} expected {Lscr}"
        assert machine.rotor.Lscr == pytest.approx(Lscr), msg

        Hscr = test_dict["Hscr"]
        msg = f"{machine.rotor.Hscr} expected {Hscr}"
        assert machine.rotor.Hscr == pytest.approx(Hscr), msg

        Lewout = test_dict["Lewout"]
        msg = f"{machine.rotor.winding.Lewout} expected {Lewout}"
        assert machine.rotor.winding.Lewout == pytest.approx(Lewout), msg


if __name__ == "__main__":
    a = TestComplexRuleRotorBar()
    for test_dict in rotor_bar_test:
        a.test_rotor_bar(test_dict)
    print("Test Done")

import pytest
from numpy import pi
from pyleecan.Classes.Winding import Winding
from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.LamSlotWind import LamSlotWind
from pyleecan.Classes.SlotW21 import SlotW21


winding_test = list()

# Common values
other_dict = {
    "[Winding_Design]": {
        "Liner_Layers": "Single_Layer",
    }
}

winding_test.append(
    {
        "other_dict": other_dict,
        "Nlayer": 1,
    }
)

# Common values
other_dict = {
    "[Winding_Design]": {
        "Liner_Layers": "Double_Layer",
    }
}

winding_test.append(
    {
        "other_dict": other_dict,
        "Nlayer": 2,
    }
)


class TestComplexRuleWindingLayer(object):
    @pytest.mark.parametrize("test_dict", winding_test)
    def test_winding_layer(self, test_dict):
        """test rule complex"""

        # retreive other_dict
        other_dict = test_dict["other_dict"]

        machine = MachineSIPMSM()
        machine.stator = LamSlotWind()
        machine.stator.winding = Winding()

        # Define and apply the slot rule
        rule = RuleComplex(fct_name="winding_layer", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict, machine, {"ED": (2 / 8) * (pi / 180), "m": 0.001, "": 1}
        )

        # retreive expected value
        Nlayer = test_dict["Nlayer"]

        # check the convertion
        msg = f"{machine.stator.winding.Nlayer} expected {Nlayer}"
        assert machine.stator.winding.Nlayer == pytest.approx(Nlayer), msg


if __name__ == "__main__":
    a = TestComplexRuleWindingLayer()
    for test_dict in winding_test:
        a.test_winding_layer(test_dict)
    print("Test Done")

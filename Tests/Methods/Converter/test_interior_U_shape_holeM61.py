import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM61 import HoleM61

HoleM61_test = list()

# Common values
other_dict = {
    "[Dimensions]": {
        "Magnet_Inner_Diameter": 4,
        "Magnet_Layer_Gap_Inner": 2,
        "Magnet_Thickness": 2,
        "Magnet_Fill_Outer": 80,
        "Magnet_Fill_Inner": 70,
    }
}
HoleM61_test.append(
    {"other_dict": other_dict, "W1": 0.003845917, "W2": 0.793921599, "H0": 0.998}
)

# test if Hole haven't magnet
other_dict = {
    "[Dimensions]": {
        "Magnet_Inner_Diameter": 4,
        "Magnet_Layer_Gap_Inner": 2,
        "Magnet_Thickness": 2,
        "Magnet_Fill_Outer": 0,
        "Magnet_Fill_Inner": 0,
    }
}
HoleM61_test.append({"other_dict": other_dict, "W1": None, "W2": None, "H0": 0.998})


class TestComplexRuleHoleM61(object):
    @pytest.mark.parametrize("test_dict", HoleM61_test)
    def test_interior_U_shape_holeM61(self, test_dict):
        """test rule complex"""

        # Construct the machine in which the hole will be set
        machine = MachineIPMSM()
        machine.rotor = LamHole()
        machine.rotor.hole.append(HoleM61())
        machine.rotor.is_stator = False
        machine.rotor.is_internal = True

        machine.rotor.hole[0].H0 = 0.024
        machine.rotor.hole[0].H1 = 0.004
        machine.rotor.hole[0].H2 = 0.002
        machine.rotor.hole[0].W0 = 0.002
        machine.rotor.hole[0].W3 = 0.002

        # Define and apply the slot rule
        rule = RuleComplex(
            fct_name="interior_U_shape_holeM61",
            folder="MotorCAD",
            param_dict={"hole_id": 0},
        )

        other_dict = test_dict["other_dict"]
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict,
            machine,
            other_unit_dict={"ED": (2 / 8) * (pi / 180), "m": 0.001, "": 1},
        )

        W1 = test_dict["W1"]
        W2 = test_dict["W2"]
        H0 = test_dict["H0"]

        # check the convertion
        msg = f"{machine.rotor.hole[0].W1} expected {W1}"
        assert machine.rotor.hole[0].W1 == pytest.approx(W1), msg

        msg = f"{machine.rotor.hole[0].W2} expected {W2}"
        assert machine.rotor.hole[0].W2 == pytest.approx(W2), msg

        msg = f"{machine.rotor.hole[0].H0} expected {H0}"
        assert machine.rotor.hole[0].H0 == pytest.approx(H0), msg


if __name__ == "__main__":
    a = TestComplexRuleHoleM61()
    for test_dict in HoleM61_test:
        a.test_interior_U_shape_holeM61(test_dict)
    print("Test Done")

import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM62 import HoleM62

holeM62_test = list()

# Common values
other_dict = {
    "[Dimensions]": {
        "Magnet_Embed_Depth": 4,
        "Magnet_Arc_[ED]": 120,
    }
}

holeM62_test.append(
    {
        "other_dict": other_dict,
        "W0": 0.5337547913227,
    }
)

# Common values
other_dict = {
    "[Dimensions]": {
        "Magnet_Embed_Depth": 8,
        "Magnet_Arc_[ED]": 80,
    }
}

holeM62_test.append(
    {
        "other_dict": other_dict,
        "W0": 0.3498327297,
    }
)

# Common values
other_dict = {
    "[Dimensions]": {
        "Magnet_Embed_Depth": 0,
        "Magnet_Arc_[ED]": 80,
    }
}

holeM62_test.append(
    {
        "other_dict": other_dict,
        "W0": 0.35265396141,
    }
)


class TestComplexRuleholeM62(object):
    @pytest.mark.parametrize("test_dict", holeM62_test)
    def test_embedded_parallel_holeM62(self, test_dict):
        """test rule complex"""

        # retreive other_dict
        other_dict = test_dict["other_dict"]

        # Construct the machine in which the hole will be set
        machine = MachineIPMSM()
        machine.rotor = LamHole()
        machine.rotor.hole.append(HoleM62())

        # Define and apply the hole rule
        rule = RuleComplex(fct_name="embedded_parallel_holeM62", folder="MotorCAD")
        # first rule complex use to define a hole

        rule.param_dict = {"hole_id": 0}
        machine = rule.convert_to_P(
            other_dict, machine, {"ED": (2 / 8) * (pi / 180), "m": 0.001}
        )

        # retreive expected values
        W0 = test_dict["W0"]

        # check the convertion
        msg = f"{machine.rotor.hole[0].W0} expected {W0}"
        assert machine.rotor.hole[0].W0 == pytest.approx(W0), msg


if __name__ == "__main__":
    a = TestComplexRuleholeM62()
    for test_dict in holeM62_test:
        a.test_embedded_parallel_holeM62(test_dict)
    print("Test Done")

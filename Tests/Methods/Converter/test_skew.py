import pytest

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineSIPMSM import MachineSIPMSM
from pyleecan.Classes.Skew import Skew
from numpy import pi

skew_l = list()

# skew in dict
other_dict = {
    "[Magnetics]": {
        "SkewType": 2,
        "RotorSkewSlices": 5,
        "RotorSkewAngle_Array[0]": -4,
        "RotorSkewAngle_Array[1]": -2,
        "RotorSkewAngle_Array[2]": 0,
        "RotorSkewAngle_Array[3]": 2,
        "RotorSkewAngle_Array[4]": 4,
    }
}
# expected value
skew_l.append(
    {
        "other_dict": other_dict,
        "type_skew": "user-defined",
        "is_step": True,
        "Nstep": 5,
        "angle_list": [
            -4 * pi / 180,
            -2 * pi / 180,
            0,
            2 * pi / 180,
            4 * pi / 180,
        ],  # Motor-Cad use deg contraty to pyleecan who use rad
    }
)


# skew with only two slice
other_dict = {
    "[Magnetics]": {
        "SkewType": 2,
        "RotorSkewSlices": 2,
        "RotorSkewAngle_Array[0]": -2,
        "RotorSkewAngle_Array[1]": 2,
    }
}
skew_l.append(
    {
        "other_dict": other_dict,
        "type_skew": "user-defined",
        "is_step": True,
        "Nstep": 2,
        "angle_list": [
            -2 * pi / 180,
            2 * pi / 180,
        ],  # Motor-Cad use deg contraty to pyleecan who use rad
    }
)


class TestComplexRuleSkew(object):
    @pytest.mark.parametrize("test_dict", skew_l)
    def test_skew(self, test_dict):
        """test rule complex"""

        # retreive other_dict
        other_dict = test_dict["other_dict"]

        # Construct the machine in which the slot will be set
        machine = MachineSIPMSM()
        machine.rotor.skew = Skew()

        # Define and apply the slot rule
        rule = RuleComplex(fct_name="skew", folder="MotorCAD")
        # first rule complex use to define a slot
        machine = rule.convert_to_P(other_dict, machine, {"m": 1})

        # retreive expected values
        type_skew = test_dict["type_skew"]
        is_step = test_dict["is_step"]
        Nstep = test_dict["Nstep"]
        angle_list = test_dict["angle_list"]

        # check the convertion
        msg = f"{machine.rotor.skew.Nstep} expected {Nstep}"
        assert machine.rotor.skew.Nstep == pytest.approx(Nstep), msg

        msg = f"{machine.rotor.skew.is_step} expected {is_step}"
        assert machine.rotor.skew.is_step == pytest.approx(is_step), msg

        msg = f"{machine.rotor.skew.angle_list} expected {angle_list}"
        assert machine.rotor.skew.angle_list == angle_list, msg

        msg = f"{machine.rotor.skew.type_skew} expected {type_skew}"
        assert machine.rotor.skew.type_skew == pytest.approx(type_skew), msg


if __name__ == "__main__":
    a = TestComplexRuleSkew()
    for test_dict in skew_l:
        a.test_skew(test_dict)
    print("Test Done")

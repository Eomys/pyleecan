import pytest
from numpy import pi

from pyleecan.Classes.RuleComplex import RuleComplex
from pyleecan.Classes.MachineIPMSM import MachineIPMSM
from pyleecan.Classes.LamHole import LamHole
from pyleecan.Classes.HoleM61 import HoleM61


other_dict = {
    "[Dimensions]": {
        "UShape_InnerDiameter_Array[0]": 4,
        "UMagnet_Length_Outer_Array[0]": 0,
        "UMagnet_Length_Inner_Array[0]": 0,
    }
}


class TestComplexRuleHoleM61(object):
    def test_interior_U_shape_holeM61(self):
        """test rule complex"""
        machine = MachineIPMSM()
        machine.rotor = LamHole()
        machine.rotor.hole.append(HoleM61())
        machine.rotor.is_stator = False
        machine.rotor.is_internal = True

        param_dict = {"hole_id": 0}
        rule = RuleComplex(
            fct_name="interior_U_shape_holeM61",
            folder="MotorCAD",
            param_dict=param_dict,
        )
        # first rule complex use to define a slot
        machine = rule.convert_to_P(
            other_dict, machine, {"ED": (2 / 8) * (pi / 180), "m": 0.001}
        )

        assert machine.rotor.hole[0].W1 == None
        assert machine.rotor.hole[0].W2 == None
        assert machine.rotor.hole[0].H0 == pytest.approx(0.998)


if __name__ == "__main__":
    a = TestComplexRuleHoleM61()
    a.test_interior_U_shape_holeM61()
    print("Test Done")

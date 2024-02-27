from ......Classes.RuleSimple import RuleSimple
from ......Classes.RuleEquation import RuleEquation
from ......Classes.RuleComplex import RuleComplex


def add_rule_holeM61(self, hole_id):
    """Create and adapt all the rules related to Hole
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    hole_id : int
        A int to know the number of hole
    """

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"Pole_Number"],
            P_obj_path=f"machine.rotor.hole[{hole_id}].Zh",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )
    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"Magnet_Thickness"],
            P_obj_path=f"machine.rotor.hole[{hole_id}].H1",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"BridgeThickness_Array[{hole_id}]"],
            P_obj_path=f"machine.rotor.hole[{hole_id}].H2",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"WebThickness_Array[{hole_id}]"],
            P_obj_path=f"machine.rotor.hole[{hole_id}].W3",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=["[Dimensions]", f"Magnet_Post"],
            P_obj_path=f"machine.rotor.hole[{hole_id}].W0",
            unit_type="m",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleComplex(
            fct_name="interior_U_shape_holeM61",
            folder="MotorCAD",
            param_dict={"hole_id": hole_id},
        )
    )

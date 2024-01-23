from .....Classes.RuleSimple import RuleSimple
from .....Classes.RuleEquation import RuleEquation
from .....Classes.RuleComplex import RuleComplex


def add_rule_material(self, path_P, material):
    """Create and adapt all the rules related to machine dimensions (lam radius,...)
    Extend rules_list within Converter object

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object
    """

    # elec
    self.rules_list.append(
        RuleSimple(
            other_key_list=[f"[{material}]", "ElectricalResistivity"],
            P_obj_path=f"{path_P}.elec.rho",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    self.rules_list.append(
        RuleSimple(
            other_key_list=[f"[{material}]", "TempCoefElectricalResistivity"],
            P_obj_path=f"{path_P}.elec.alpha",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    # Mechanics
    self.rules_list.append(
        RuleSimple(
            other_key_list=[f"[{material}]", "Density"],
            P_obj_path=f"{path_P}.struct.rho",
            unit_type="",
            scaling_to_P=1,
            file_name=__file__,
        )
    )

    if "PoissonsRatio" in self.other_dict[f"[{material}]"]:
        self.rules_list.append(
            RuleSimple(
                other_key_list=[f"[{material}]", "PoissonsRatio"],
                P_obj_path=f"{path_P}.struct.nu_xy",
                unit_type="",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=[f"[{material}]", "PoissonsRatio"],
                P_obj_path=f"{path_P}.struct.nu_xz",
                unit_type="",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

        self.rules_list.append(
            RuleSimple(
                other_key_list=[f"[{material}]", "PoissonsRatio"],
                P_obj_path=f"{path_P}.struct.nu_yz",
                unit_type="",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

    if "YoungsCoefficient" in self.other_dict[f"[{material}]"]:
        self.rules_list.append(
            RuleSimple(
                other_key_list=[f"[{material}]", "YoungsCoefficient"],
                P_obj_path=f"{path_P}.struct.Ex",
                unit_type="",
                scaling_to_P=1,
                file_name=__file__,
            )
        )
        self.rules_list.append(
            RuleSimple(
                other_key_list=[f"[{material}]", "YoungsCoefficient"],
                P_obj_path=f"{path_P}.struct.Ey",
                unit_type="",
                scaling_to_P=1,
                file_name=__file__,
            )
        )
        self.rules_list.append(
            RuleSimple(
                other_key_list=[f"[{material}]", "YoungsCoefficient"],
                P_obj_path=f"{path_P}.struct.Ez",
                unit_type="",
                scaling_to_P=1,
                file_name=__file__,
            )
        )

    if self.is_P_to_other == False:
        if (
            "YoungsCoefficient" in self.other_dict[f"[{material}]"]
            and "PoissonsRatio" in self.other_dict[f"[{material}]"]
        ):
            # into file .mot
            # a = YoungsCoefficient
            # b = PoissonsRatio
            # into Pyleecan
            # x = Gxy
            self.rules_list.append(
                RuleEquation(
                    param=[
                        {
                            "src": "other",
                            "path": [f"[{material}]", "YoungsCoefficient"],
                            "variable": "a",
                        },
                        {
                            "src": "other",
                            "path": [f"[{material}]", "PoissonsRatio"],
                            "variable": "b",
                        },
                        {
                            "src": "pyleecan",
                            "path": f"{path_P}.struct.Gxy",
                            "variable": "x",
                        },
                    ],
                    unit_type="",
                    equation="a/(2*(1+b))=x",
                    file_name=__file__,
                )
            )
            # into file .mot
            # a = YoungsCoefficient
            # b = PoissonsRatio
            # into Pyleecan
            # x = Gxz
            self.rules_list.append(
                RuleEquation(
                    param=[
                        {
                            "src": "other",
                            "path": [f"[{material}]", "YoungsCoefficient"],
                            "variable": "a",
                        },
                        {
                            "src": "other",
                            "path": [f"[{material}]", "PoissonsRatio"],
                            "variable": "b",
                        },
                        {
                            "src": "pyleecan",
                            "path": f"{path_P}.struct.Gxz",
                            "variable": "x",
                        },
                    ],
                    unit_type="",
                    equation="a/(2*(1+b))=x",
                    file_name=__file__,
                )
            )

            # into file .mot
            # a = YoungsCoefficient
            # b = PoissonsRatio
            # into Pyleecan
            # x = Gyz
            self.rules_list.append(
                RuleEquation(
                    param=[
                        {
                            "src": "other",
                            "path": [f"[{material}]", "YoungsCoefficient"],
                            "variable": "a",
                        },
                        {
                            "src": "other",
                            "path": [f"[{material}]", "PoissonsRatio"],
                            "variable": "b",
                        },
                        {
                            "src": "pyleecan",
                            "path": f"{path_P}.struct.Gyz",
                            "variable": "x",
                        },
                    ],
                    unit_type="",
                    equation="a/(2*(1+b))=x",
                    file_name=__file__,
                )
            )

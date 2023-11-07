# from pyleecan.Methods.Funcion.Rules.add_rules_duct_layer import add_rules_duct_layer
from pyleecan.Classes.VentilationCirc import VentilationCirc


def selection_lamination_rules(self, is_stator):
    print("lamination")
    if is_stator == True:
        lam_name = "Stator"
    else:
        lam_name = "Rotor"

    # sélection of number and type layers
    if not self.is_P_to_other:
        type_duct = self.other_dict["[Through_Vent]"][f"{lam_name}DuctType"]

        if self.other_dict["[Through_Vent]"][f"{lam_name}DuctType"] != 0:
            if type_duct == 1:
                name_type_duct = "ArcDuct"

            elif type_duct == 2:
                name_type_duct = "SahftSpoke"

            elif type_duct == 3:
                name_type_duct = "CircularDuct"

            elif type_duct == 4:
                name_type_duct = "RectangularDuct"

            temp = self.other_dict["[Through_Vent]"][
                f"{lam_name}{name_type_duct}Layers"
            ]
            for nb_duct in range(temp):
                # add_rules_duct_layer(
                self,
                lam_name,
                nb_duct,
                name_type_duct,
            # )

        else:
            pass
            # print("not axial cooling duct")

    return self.rules_list

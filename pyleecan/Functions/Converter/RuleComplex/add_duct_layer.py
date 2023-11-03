from pyleecan.Classes.VentilationCirc import VentilationCirc
from pyleecan.Classes.VentilationPolar import VentilationPolar
from pyleecan.Classes.VentilationTrap import VentilationTrap


def add_duct_layer(machine, other_dict, is_stator):
    if is_stator == True:
        lam_name = "Stator"
        dict_machine = machine.stator.as_dict()
        type_duct = other_dict["[Through_Vent]"][f"{lam_name}DuctType"]

        if type_duct == 1:  # arcduct
            name_type_duct = "ArcDuct"

        elif type_duct == 2:  # sahftspoke
            name_type_duct = "SahftSpoke"

        elif type_duct == 3:  # circularduct
            machine.stator = VentilationCirc(init_dict=dict_machine)

        elif type_duct == 4:  # circularduct
            machine.stator = VentilationTrap(init_dict=dict_machine)

    else:
        lam_name = "Rotor"

        dict_machine = machine.rotor.as_dict()

        type_duct = other_dict["[Through_Vent]"][f"{lam_name}DuctType"]

        if type_duct == 1:  # arcduct
            name_type_duct = "ArcDuct"

        elif type_duct == 2:  # sahftspoke
            name_type_duct = "SahftSpoke"

        elif type_duct == 3:  # circularduct
            machine.rotor = VentilationCirc(init_dict=dict_machine)

        elif type_duct == 4:  # circularduct
            machine.rotor = VentilationTrap(init_dict=dict_machine)

    return machine

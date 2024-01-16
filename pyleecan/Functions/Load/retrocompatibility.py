from logging import getLogger

from numpy import array

from ...Functions.labels import HOLEM_LAB, HOLEV_LAB
from ...Functions.Load.import_class import import_class
from ...loggers import GUI_LOG_NAME


class RetroCompatibilityError(Exception):
    pass


def convert_init_dict(init_dict):
    """Convert an init_dict from an old version of pyleecan to the current one
    (modification in place)

    Parameters
    ----------
    init_dict : dict
        The dictionnary to update
    """
    # Check file version to know what to update
    if "__version__" in init_dict:
        file_version = init_dict["__version__"].split("_")[1]
    else:
        file_version = None
    update_dict = create_update_dict(file_version)
    # If nothing to update, search is not called
    if any(update_dict.values()):
        _search_and_update(init_dict, update_dict=update_dict)


def _search_and_update(obj_dict, parent=None, parent_index=None, update_dict=None):
    """Scan a dict and its sub dict to update the content
    (update in place)

    Parameters
    ----------
    obj_dict : dict
        Dictionnary of the object to update
    parent : dict/list
        Object containing the obj_dict (to update)
    parent_index : str/int
        Key or index of the obj_dict in the parent
    update_dict : dict
        Dictionnary Key: What to update, value: is update needed

    """
    # add to list for later conversion
    if update_dict["HoleUD"] and is_HoleUD_dict(obj_dict):
        parent[parent_index] = convert_HoleUD(obj_dict)
    elif update_dict["OP"] and is_OP_dict(obj_dict):
        parent[parent_index] = convert_OP(obj_dict)
    elif update_dict["OP_matrix"] and is_OP_matrix_dict(obj_dict):
        parent[parent_index] = convert_OP_matrix(obj_dict)
    elif update_dict["Winding"] and is_Winding_dict(obj_dict):
        if (
            parent is not None
            and "slot" in parent.keys()
            and "Zs" in parent["slot"].keys()
        ):
            # Add Zs for wind_mat generation
            obj_dict["Zs"] = parent["slot"]["Zs"]
        parent[parent_index] = convert_Winding(obj_dict)
    elif update_dict["Yoke_Notch"] and is_yoke_notch(obj_dict):
        move_yoke_notch(obj_dict)
    elif update_dict["VarParam"] and is_VarParam_dict(obj_dict):
        rename_varparam(obj_dict)
    elif update_dict["OptiConstraint"] and is_OptiConstraint_dict(obj_dict):
        parent[parent_index] = convert_opticonstraint(obj_dict)
    elif update_dict["OptiDesignVar"] and is_OptiDesignVar_dict(obj_dict):
        parent[parent_index] = convert_optidesignvar(obj_dict)
    elif update_dict["WmagHmag"] and is_Wmag_Hmag(obj_dict):
        parent[parent_index] = convert_Wmag_Hmag(obj_dict)
    elif update_dict["MeshSolution"] and is_MeshSolution_dict(obj_dict):
        parent[parent_index] = convert_meshsolution_mesh(obj_dict)
    else:
        # walk through the dict
        for key, value in obj_dict.items():
            if isinstance(value, dict):
                # recursively search the dict
                _search_and_update(
                    value, parent=obj_dict, parent_index=key, update_dict=update_dict
                )
            elif isinstance(value, list):
                for ii, item in enumerate(value):
                    if isinstance(item, dict):
                        # recursively search the dict
                        _search_and_update(
                            item, parent=value, parent_index=ii, update_dict=update_dict
                        )


############################################
# V 1.3.8 => 1.4.0
# moved yoke_notch to notch (list)
############################################
Yoke_Notch_VERSION = "1.4.0"


def is_yoke_notch(obj_dict):
    """Check if the object need to be updated for yoke_notch"""
    return (
        "__class__" in obj_dict.keys()
        and "yoke_notch" in obj_dict.keys()
        and "notch" in obj_dict.keys()
        and obj_dict["yoke_notch"]
    )


def move_yoke_notch(obj_dict):
    """Move all yoke notches to notch property and set notch.is_yoke property to True"""
    # create notch list if not existent
    if obj_dict["notch"] is None:
        obj_dict["notch"] = []

    # move yoke notches to notch property
    while obj_dict["yoke_notch"]:
        yoke_notch = obj_dict["yoke_notch"].pop(0)
        obj_dict["notch"].append(yoke_notch)
        # set is_bore property to True
        if isinstance(yoke_notch, dict):
            yoke_notch["notch_shape"]["is_bore"] = False


############################################
# V 1.3.9 => 1.4.0
# Introducing OP_matrix object
############################################
OP_MAT_VERSION = "1.4.0"


def is_OP_matrix_dict(obj_dict):
    """Check if the object need to be updated for OP_matrix"""
    return (
        "__class__" in obj_dict.keys()
        and "VarLoad" in obj_dict["__class__"]
        and "type_OP_matrix" in obj_dict.keys()
    )


def convert_OP_matrix(obj_dict):
    OPMatrix = import_class("pyleecan.Classes", "OPMatrix")
    OP_mat_obj = OPMatrix()
    type_OP_matrix = obj_dict.pop("type_OP_matrix")
    if type_OP_matrix is None:
        type_OP_matrix = 1  # Default is Id/Iq

    if type_OP_matrix == 0:
        arg_list = ["N0", "I0", "Phi0"]
    elif type_OP_matrix == 1:
        arg_list = ["N0", "Id", "Iq"]
    elif type_OP_matrix == 2:
        arg_list = ["N0", "U0", "slip"]
    else:
        raise Exception(
            "Error in retrocompatibility: type_OP_matrix=="
            + str(type_OP_matrix)
            + " doesn't exist"
        )
    OP_matrix = obj_dict.pop("OP_matrix")
    if OP_matrix is None:
        obj_dict["OP_matrix"] = None
    else:
        OP_matrix = array(OP_matrix)
        if OP_matrix.shape[1] == 4:
            arg_list.append("Tem")
        elif OP_matrix.shape[1] == 5:
            arg_list.extend(["Tem", "Pem"])
        OP_mat_obj.set_OP_array(OP_matrix, *arg_list)
        obj_dict["OP_matrix"] = OP_mat_obj
    return obj_dict


############################################
# V 1.3.7 => 1.3.8
# Introducing OP object (assume all is OPdq)
############################################
OP_VERSION = "1.3.8"


def is_OP_dict(obj_dict):
    """Check if the object need to be updated for OP"""
    return (
        "__class__" in obj_dict.keys()
        and ("Input" in obj_dict["__class__"] or obj_dict["__class__"] == "OutElec")
        and "Id_ref" in obj_dict.keys()
    )


def convert_OP(obj_dict):
    obj_dict_new = obj_dict.copy()
    Class_obj = import_class("pyleecan.Classes", obj_dict_new["__class__"])
    N0 = obj_dict_new.pop("N0")
    Id = obj_dict_new.pop("Id_ref")
    Iq = obj_dict_new.pop("Iq_ref")
    Tem = obj_dict_new.pop("Tem_av_ref")
    class_obj = Class_obj(init_dict=obj_dict_new)
    OPdq = import_class("pyleecan.Classes", "OPdq")
    OP = OPdq(N0=N0, Id_ref=Id, Iq_ref=Iq, Tem_av_ref=Tem)
    class_obj.OP = OP
    return class_obj


############################################
# V  1.3.2 = > 1.3.3
# Updating HoleUD surface label
# Label reorganization
############################################
HoleUD_VERSION = "1.3.3"


def is_HoleUD_dict(obj_dict):
    """Check if the object need to be updated for HoleUD"""
    if "__class__" in obj_dict.keys() and obj_dict["__class__"] == "HoleUD":
        # Old label : Hole_Rotor_R0_T0_S0
        # Old label : HoleMagnet_Rotor_Parallel_N_R0_T0_S0
        return len(obj_dict["surf_list"][0]["label"].split("_")) > 3
    else:
        return False


def convert_HoleUD(hole_dict):
    """Update the content of the dict and instantiate object"""
    getLogger(GUI_LOG_NAME).info(
        "Old machine version detected, Updating the HoleUD object"
    )
    # Copy dict to keep original version
    hole_dict_new = hole_dict.copy()
    for ii in range(len(hole_dict["surf_list"])):
        if "HoleMagnet" in hole_dict["surf_list"][ii]["label"]:
            hole_dict_new["surf_list"][ii]["label"] = HOLEM_LAB
        else:
            hole_dict_new["surf_list"][ii]["label"] = HOLEV_LAB
    # Instantiate object
    HoleUD = import_class("pyleecan.Classes", "HoleUD")
    return HoleUD(init_dict=hole_dict_new)


######################
# v 1.2.1 => 1.2.2
# Winding star of slot
######################
WIND_VERSION = "1.2.2"


def is_Winding_dict(obj_dict):
    """Check if the object need to be updated for Winding"""
    return (
        "__class__" in obj_dict.keys()
        and obj_dict["__class__"]
        in [
            "WindingCW1L",
            "WindingCW2LR",
            "WindingCW2LT",
            "WindingDW1L",
            "WindingDW2L",
        ]
        or "__class__" in obj_dict.keys()
        and obj_dict["__class__"]
        in [
            "Winding",
            "WindingUD",
            "WindingSC",
        ]
        and "Npcpp" in obj_dict.keys()
    )


def convert_Winding(wind_dict):
    """Update the old Winding classes to WindingUD"""
    getLogger(GUI_LOG_NAME).info(
        "Old machine version detected, Updating the Winding object"
    )
    # Copy dict to keep original version
    wind_dict_new = wind_dict.copy()
    # Update Npcpp
    if "Npcpp" in wind_dict_new.keys():
        wind_dict_new["Npcp"] = wind_dict_new.pop("Npcpp")

    # Update user_wind_mat
    if wind_dict_new["__class__"] == "WindingUD":
        if "user_wind_mat" in wind_dict_new.keys():
            wind_dict_new["wind_mat"] = wind_dict_new["user_wind_mat"]

    # Update class
    if wind_dict_new["__class__"] in [
        "WindingCW1L",
        "WindingCW2LR",
        "WindingCW2LT",
        "WindingDW1L",
        "WindingDW2L",
    ]:
        # Load Winding main parameters
        if "qs" in wind_dict_new.keys():
            qs = wind_dict_new["qs"]
        else:
            qs = 3
        if "p" in wind_dict_new.keys():
            p = wind_dict_new["p"]
        else:
            p = 3
        if "coil_pitch" in wind_dict_new.keys():
            coil_pitch = wind_dict_new["coil_pitch"]
        else:
            coil_pitch = 0
        if "Ntcoil" in wind_dict_new.keys():
            Ntcoil = wind_dict_new["Ntcoil"]
        else:
            Ntcoil = 1

        if (
            qs is None
            or p is None
            or coil_pitch is None
            or "Zs" not in wind_dict_new
            or wind_dict_new["Zs"] is None
        ):
            # Winding not fully defined => Use Star of slot
            Winding = import_class("pyleecan.Classes", "Winding")
            return Winding(init_dict=wind_dict_new)
        else:
            # Generate old Winding matrix as UD
            old_class = wind_dict["__class__"]
            WindingUD = import_class("pyleecan.Classes", "WindingUD")
            new_wind = WindingUD(qs=qs, p=p, Ntcoil=Ntcoil, coil_pitch=coil_pitch)
            try:
                if old_class == "WindingCW1L":
                    new_wind.init_as_CW1L(Zs=wind_dict["Zs"])
                elif old_class == "WindingCW2LR":
                    new_wind.init_as_CW2LR(Zs=wind_dict["Zs"])
                elif old_class == "WindingCW2LT":
                    new_wind.init_as_CW2LT(Zs=wind_dict["Zs"])
                elif old_class == "WindingDW1L":
                    new_wind.init_as_DWL(Zs=wind_dict["Zs"], nlay=1)
                elif old_class == "WindingDW2L":
                    new_wind.init_as_DWL(Zs=wind_dict["Zs"], nlay=2)
                return new_wind
            except Exception:
                # Not able to generate winding matrix => Star of Slot
                Winding = import_class("pyleecan.Classes", "Winding")
                return Winding(init_dict=wind_dict_new)

    else:
        Winding_class = import_class("pyleecan.Classes", wind_dict_new["__class__"])
        return Winding_class(init_dict=wind_dict_new)


######################
# v 1.4.1 => 1.4.2
# VarParam is now VarParamSweep
######################
VARPARAM_VERSION = "1.4.2"


def is_VarParam_dict(obj_dict):
    """Check if the object need to be updated for Winding"""
    return "__class__" in obj_dict.keys() and obj_dict["__class__"] in [
        "VarParam",
    ]


def rename_varparam(varparam_dict):
    """Update the old VarParam class to VarParamSweep"""
    getLogger(GUI_LOG_NAME).info(
        "Old machine version detected, Updating the VarParam object"
    )
    # Copy dict to keep original version
    varparam_dict_new = varparam_dict.copy()
    # Instantiate object
    VarParamSweep = import_class("pyleecan.Classes", "VarParamSweep")
    return VarParamSweep(init_dict=varparam_dict_new)


######################
# v 1.4.1 => 1.4.2
# VarParam is now VarParamSweep
######################
OptiConstraint_VERSION = "1.4.2"


def is_OptiConstraint_dict(obj_dict):
    """Check if the object need to be updated for OptiConstraint"""
    return (
        "__class__" in obj_dict.keys()
        and obj_dict["__class__"]
        in [
            "OptiConstraint",
        ]
        and "get_variable" in obj_dict.keys()
    )


def convert_opticonstraint(opticonstraint_dict):
    """Update the old OptiConstraint to the new one inherited from DataKeeper without get_variable"""
    getLogger(GUI_LOG_NAME).info(
        "Old machine version detected, Updating the OptiConstraint object"
    )
    # Copy dict to keep original version
    opticonstraint_dict_new = opticonstraint_dict.copy()
    opticonstraint_dict_new["keeper"] = opticonstraint_dict_new["get_variable"]
    del opticonstraint_dict_new["get_variable"]
    # Instantiate object
    OptiConstraint = import_class("pyleecan.Classes", "OptiConstraint")
    return OptiConstraint(init_dict=opticonstraint_dict_new)


######################
# v 1.4.1 => 1.4.2
# VarParam is now VarParamSweep
######################
OptiDesignVar_VERSION = "1.4.2"


def is_OptiDesignVar_dict(obj_dict):
    """Check if the object need to be updated for OptiDesignVar"""
    return "__class__" in obj_dict.keys() and obj_dict["__class__"] in [
        "OptiDesignVar",
    ]


def convert_optidesignvar(optidesignvar_dict):
    """Update the old OptiDesignVar to the new ones OptiDesignVarSet & OptiDesignVarInterval"""
    getLogger(GUI_LOG_NAME).info(
        "Old machine version detected, Updating the OptiDesignVar object"
    )
    # Copy dict to keep original version
    optidesignvar_dict_new = optidesignvar_dict.copy()

    if optidesignvar_dict_new["type_var"] == "set":
        del optidesignvar_dict_new["type_var"]
        OptiDesignVarSet = import_class("pyleecan.Classes", "OptiDesignVarSet")
        return OptiDesignVarSet(init_dict=optidesignvar_dict_new)
    else:
        del optidesignvar_dict_new["type_var"]
        OptiDesignVarInterval = import_class(
            "pyleecan.Classes", "OptiDesignVarInterval"
        )
        return OptiDesignVarInterval(init_dict=optidesignvar_dict_new)


######################
# v 1.5.1 => 1.5.2
# Wmag/Hmag renamed as W1/H1
######################
WmagRenaming_VERSION = "1.5.2"


def is_Wmag_Hmag(obj_dict):
    """Check if the object need to be updated for Hmag/Wmag"""
    return "__class__" in obj_dict.keys() and (
        "Hmag" in obj_dict.keys() or "Wmag" in obj_dict.keys()
    )


def convert_Wmag_Hmag(Wmag_Hmag_dict):
    """Update the old Wmag_Hmag_dict to the new W1_H1_dict"""
    getLogger(GUI_LOG_NAME).info("Old machine version detected, Updating Wmag_Hmag")
    # Copy dict to keep original version
    Wmag_Hmag_dict_news = Wmag_Hmag_dict.copy()

    if (
        Wmag_Hmag_dict_news["__class__"] == "SlotM18"
        or Wmag_Hmag_dict_news["__class__"] == "SlotM19"
    ):
        if "Hmag" in Wmag_Hmag_dict_news.keys():
            Wmag_Hmag_dict_news["H0"] = Wmag_Hmag_dict_news.pop("Hmag")

    else:
        if "Hmag" in Wmag_Hmag_dict_news.keys():
            Wmag_Hmag_dict_news["H1"] = Wmag_Hmag_dict_news.pop("Hmag")

        if "Wmag" in Wmag_Hmag_dict.keys():
            Wmag_Hmag_dict_news["W1"] = Wmag_Hmag_dict_news.pop("Wmag")

    return Wmag_Hmag_dict_news


######################
# v 1.5.0 => 1.5.1
# MeshSolution.mesh is now a single mesh instead of a list of meshes
######################
MeshSolution_VERSION = "1.5.1"


def is_MeshSolution_dict(obj_dict):
    """Check if the object need to be updated for MeshSolution"""
    return "__class__" in obj_dict.keys() and obj_dict["__class__"] in [
        "MeshSolution",
    ]


def convert_meshsolution_mesh(meshsolution_dict):
    """Update MeshSolution with a single mesh"""
    getLogger(GUI_LOG_NAME).info(
        "Old simulation version detected, Updating the MeshSolution object"
    )
    # Copy dict to keep original version
    meshsolution_dict_new = meshsolution_dict.copy()

    MeshSolution = import_class("pyleecan.Classes", "MeshSolution")

    if isinstance(meshsolution_dict_new["mesh"], list):
        if len(meshsolution_dict_new["mesh"]) == 0:
            meshsolution_dict_new["mesh"] = None
        elif len(meshsolution_dict_new["mesh"]) == 1:
            meshsolution_dict_new["mesh"] = meshsolution_dict_new["mesh"][0]
        else:
            raise RetroCompatibilityError(
                f"MeshSolution object only supports one mesh for version >= {MeshSolution_VERSION}"
            )

    # Convert list of solution stored in solution to dict of solution stored in solution_dict
    list_solution = meshsolution_dict_new.get("solution", None)
    if isinstance(list_solution, list):
        list_label = [solution["label"] for solution in list_solution]

        # Check if solution labels are unique
        if len(set(list_label)) == len(list_label):
            meshsolution_dict_new["solution_dict"] = {
                solution["label"]: solution for solution in list_solution
            }
        else:  # Duplicated labels
            getLogger(GUI_LOG_NAME).warning(
                f"MeshSolution constains solutions with same label, instancing solution_dict with \"{meshsolution_dict_new['label']}_i\""
            )
            meshsolution_dict_new["solution_dict"] = {
                f"{meshsolution_dict_new['label']}_{k}": solution
                for k, solution in enumerate(list_solution, 1)
            }

        del meshsolution_dict_new["solution"]

    return MeshSolution(init_dict=meshsolution_dict_new)


def is_before_version(ref_version, check_version=None):
    """Check if a version str is before another version str

    Parameters
    ----------
    ref_version : str
        Reference version to compare with ("1.2.3" for instance)
    check_version : str
        Version to check if before reference ("1.3.4" for instance)

    Returns
    -------
    is_before : bool
        True if check_version is before ref_version
    """
    if ref_version == check_version:
        return False

    ref_list = [int(val) for val in ref_version.split(".")]
    check_list = [int(val) for val in check_version.split(".")]

    for ii in range(len(check_list)):
        if len(ref_list) < ii + 1:
            return False
        if ref_list[ii] > check_list[ii]:
            return True
        elif ref_list[ii] < check_list[ii]:
            return False

    # Case 2.1.14.2 vs 2.1.14
    if len(ref_list) > len(check_list):
        return True


# Match object type with compatibility change version
OBJECT_VERSION_DICT = {
    "Winding": WIND_VERSION,
    "HoleUD": HoleUD_VERSION,
    "OP": OP_VERSION,
    "OP_matrix": OP_MAT_VERSION,
    "Yoke_Notch": Yoke_Notch_VERSION,
    "VarParam": VARPARAM_VERSION,
    "OptiConstraint": OptiConstraint_VERSION,
    "OptiDesignVar": OptiDesignVar_VERSION,
    "WmagHmag": WmagRenaming_VERSION,
    "MeshSolution": MeshSolution_VERSION,
}


def create_update_dict(file_version):
    """Create a dict to know which parameter to update

    Parameters
    ----------
    file_version : str
        Version of the file to update

    Returns
    -------
    update_dict : dict
        Dictionnary Key: What to update, value: is update needed
    """

    # Set every parameter to update if the version is not defined
    if file_version is None:
        update_dict = {class_obj: True for class_obj in OBJECT_VERSION_DICT.keys()}
    else:
        update_dict = {
            class_obj: is_before_version(version, file_version)
            for class_obj, version in OBJECT_VERSION_DICT.items()
        }

    return update_dict

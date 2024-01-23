def convert_material_to_P(self, path_P):
    """Selects correct material path and return path in file.mot

    Parameters
    ----------
    self : ConvertMC
        A ConvertMC object

    Returns
    ---------
    material_path : string
        Path to select material in file .mot
    """

    # creation material dict
    dict_material = {
        "machine.shaft.mat_type": ("Material_Shaft_[A]"),
        "machine.frame.mat_type": (""),  # Material_Housing_Active
        "machine.rotor.slot.wedge_mat": ("Material_RotorWedge"),
        "machine.rotor.winding.conductor.cond_mat": ("Material_Copper_-_Active"),
        "machine.rotor.winding.conductor.ins_mat": (""),
        "machine.rotor.mat_type": ("Material_Rotor_Lam_Tooth"),
        "machine.rotor.ring_mat": ("Material_Rotor_Cage_Top"),
        "machine.stator.slot.wedge_mat": ("Material_SlotWedge"),
        "machine.rotor.magnet.mat_type": ("Material_Magnet"),
        "machine.stator.mat_type": ("Material_Stator_Lam_Tooth"),
        "machine.stator.winding.conductor.cond_mat": ("Material_Copper_-_Active"),
        "machine.stator.winding.conductor.ins_mat": (""),
    }

    if "[" in path_P:
        path_P_split = path_P.split("[")
        # check if material is a hole
        if path_P_split[0] == "machine.rotor.hole":
            material_path = "Material_Magnet"
        else:
            IndexError("Problem in material path")

    # select the correct position of material into dict
    else:
        material_path = dict_material[path_P]

    if material_path != "":
        try:
            material_path = self.other_dict["[Material]"][material_path]
        except:
            material_path = ""

    return material_path

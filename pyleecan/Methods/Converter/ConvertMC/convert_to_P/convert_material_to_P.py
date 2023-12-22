def convert_material_to_P(self, path_P):
    # dict

    dict_material = {
        "machine.shaft.mat_type": ("Material_Shaft_[A]"),
        "machine.frame.mat_type": (""),  # Material_Housing_Active
        "machine.rotor.slot.wedge_mat": ("Material_RotorWedge"),
        "machine.rotor.winding.conductor.cond_mat": ("Material_Copper_Active"),
        "machine.rotor.winding.conductor.ins_mat": (""),
        "machine.rotor.mat_type": ("Material_Rotor_Lam_Tooth"),
        "machine.rotor.ring_mat": ("Material_Rotor_Cage_Top"),
        "machine.stator.slot.wedge_mat": ("Material_SlotWedge"),
        "machine.rotor.magnet.mat_type": ("Material_Magnet"),
        "machine.stator.mat_type": ("Material_Stator_Lam_Tooth"),
        "machine.stator.winding.conductor.cond_mat": ("Material_Copper_Active"),
        "machine.stator.winding.conductor.ins_mat": (""),
        "machine.rotor.hole[0].magnet_0.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[1].magnet_0.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[2].magnet_0.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[3].magnet_0.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[4].magnet_0.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[0].magnet_1.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[1].magnet_1.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[2].magnet_1.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[3].magnet_1.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[4].magnet_1.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[0].magnet_2.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[1].magnet_2.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[2].magnet_2.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[3].magnet_2.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[4].magnet_2.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[0].magnet_3.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[1].magnet_3.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[2].magnet_3.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[3].magnet_3.mat_type": ("Material_Magnet"),
        "machine.rotor.hole[4].magnet_3.mat_type": ("Material_Magnet"),
    }

    type_material = dict_material[path_P]
    if type_material != "":
        try:
            type_material = self.other_dict["[Material]"][type_material]
        except:
            type_material = ""

    return type_material

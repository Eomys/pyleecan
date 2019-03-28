from femm import mo_seteditmode, mo_groupselectblock, mo_blockintegral


def comp_FEMM_torque(FEMM_dict, sym=1):
    """Compute the torque of the current FEMM simulation result
    """

    # Select rotor groups
    mo_seteditmode("area")
    mo_groupselectblock(FEMM_dict["groups"]["GROUP_RC"])
    mo_groupselectblock(FEMM_dict["groups"]["GROUP_RW"])
    # sym = 2 => Only half the machine
    return sym * mo_blockintegral(22)

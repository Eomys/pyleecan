def comp_FEMM_torque(femm, rotor_groups, sym=1):
    """Compute the torque of the current FEMM simulation result
    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
    FEMM_dict : dict
        dict containig FEMM parameters
    """

    # Select rotor groups
    femm.mo_seteditmode("area")
    for grp in rotor_groups:
        femm.mo_groupselectblock(grp)
    Tem = sym * femm.mo_blockintegral(22)

    femm.mo_clearblock()

    return Tem

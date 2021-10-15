# -*- coding: utf-8 -*-
from ..labels import (
    YSR_LAB,
    YSL_LAB,
    YSN_LAB,
    YSNR_LAB,
    YSNL_LAB,
    STATOR_LAB,
    YS_LAB,
    YOKE_LAB,
    LAM_LAB,
    SBS_TR_LAB,
    SBS_TL_LAB,
    SBS_BR_LAB,
    SBS_BL_LAB,
    SBR_B_LAB,
    SBR_T_LAB,
    AS_BR_LAB,
    AS_BL_LAB,
    decode_label,
)


def create_FEMM_boundary_conditions(femm, line_label, BC_dict):
    """Create the boundary conditions in FEMM

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
    sym : int
        Symmetry factor of the machine
    is_antiper : bool
        True if an anti-periodicity is considered

    Returns
    -------
    None
    """
    sym = BC_dict["sym"]
    is_antiper = BC_dict["is_antiper"]
    if sym == 1:
        is_antiper = False

    # anti periodic boundary conditions
    if is_antiper:
        BdPr = 5
    # even number of rotor poles /slots -> periodic boundary conditions
    else:
        BdPr = 4

    ## Dirichlet (no flux going out) (on ext lamination yoke)
    if LAM_LAB in line_label and YOKE_LAB in line_label:
        femm.mi_addboundprop("bc_A0", 0, 0, 0, 0, 0, 0, 0, 0, 0)
        BC_dict[line_label] = "bc_A0"
    ## Sliding Band radius
    elif line_label in [SBR_B_LAB, SBR_T_LAB]:
        femm.mi_addboundprop("bc_ag2", 0, 0, 0, 0, 0, 0, 0, 0, BdPr + 2)
        BC_dict[SBR_B_LAB] = "bc_ag2"
        BC_dict[SBR_T_LAB] = "bc_ag2"
    ## Sliding Band Bottom side
    elif line_label in [SBS_BR_LAB, SBS_BL_LAB]:
        femm.mi_addboundprop("bc_ag1", 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
        BC_dict[SBS_BR_LAB] = "bc_ag1"
        BC_dict[SBS_BL_LAB] = "bc_ag1"
    ## Sliding Band Top side
    elif line_label in [SBS_TR_LAB, SBS_TL_LAB]:
        femm.mi_addboundprop("bc_ag3", 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
        BC_dict[SBS_TR_LAB] = "bc_ag3"
        BC_dict[SBS_TL_LAB] = "bc_ag3"
    ##  Airgap Side
    elif line_label in [AS_BR_LAB, AS_BL_LAB]:
        femm.mi_addboundprop("bc_ag1", 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
        BC_dict[AS_BR_LAB] = "bc_ag1"
        BC_dict[AS_BL_LAB] = "bc_ag1"
    ## Lamination YokeSide for Notches
    elif YSN_LAB in line_label:
        # Create BC name (bc_ys_s0_N for instance - yoke side stator 0 Notche)
        label_dict = decode_label(line_label)
        bc_name = "bc_ys_"
        if STATOR_LAB in label_dict["lam_type"]:
            bc_name += "s"
        else:
            bc_name += "r"
        bc_name += str(label_dict["lam_id"])
        bc_name += "_N"
        # Create BC
        femm.mi_addboundprop(bc_name, 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
        # Update dict
        BC_dict[label_dict["lam_label"] + "_" + YSNL_LAB] = bc_name
        BC_dict[label_dict["lam_label"] + "_" + YSNR_LAB] = bc_name
    ## Lamination YokeSide
    elif YS_LAB in line_label:
        # cf Lamination.get_yoke_side_line for label creation
        # Create BC name (bc_ys_s0_1 for instance - yoke side stator 0 line 1)
        label_dict = decode_label(line_label)
        bc_name = "bc_ys_"
        if STATOR_LAB in label_dict["lam_type"]:
            bc_name += "s"
        else:
            bc_name += "r"
        bc_name += str(label_dict["lam_id"])
        line_id = line_label.split("-")[-1]
        bc_name += "_" + line_id
        # Create BC
        femm.mi_addboundprop(bc_name, 0, 0, 0, 0, 0, 0, 0, 0, BdPr)
        # Update dict
        BC_dict[label_dict["lam_label"] + "_" + YSL_LAB + "-" + line_id] = bc_name
        BC_dict[label_dict["lam_label"] + "_" + YSR_LAB + "-" + line_id] = bc_name

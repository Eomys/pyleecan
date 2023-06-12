# -*- coding: utf-8 -*-
from numpy import exp, pi
import cmath

from ...Classes.Arc import Arc
from ...Classes.Arc1 import Arc1
from ...Classes.Arc2 import Arc2
from ...Classes.Circle import Circle
from ...Classes.Segment import Segment
from ...Classes.SurfLine import SurfLine
from ...Classes.SurfRing import SurfRing
from ...Classes.MachineSIPMSM import MachineSIPMSM
from ...Functions.labels import (
    AIRGAP_LAB,
    SLID_LAB,
    AIRBOX_LAB,
    NO_LAM_LAB,
    BOT_LAB,
    TOP_LAB,
    BOUNDARY_PROP_LAB,
    SBS_TR_LAB,
    SBS_TL_LAB,
    SBS_BR_LAB,
    SBS_BL_LAB,
    SBR_B_LAB,
    SBR_T_LAB,
    AS_TR_LAB,
    AS_TL_LAB,
    AS_BR_LAB,
    AS_BL_LAB,
    AR_B_LAB,
    AR_T_LAB,
    AIRBOX_R_LAB,
)


def get_sliding_band(sym, machine):
    """Returns  a list of surface in the airgap including the sliding band surface

    Parameters
    ----------
    sym: int
        Symmetry factor (1= full machine, 2= half of the machine...)
    machine: Machine
        Machine to draw

    Returns
    -------
    surf_list: list
        List of surface in the airgap including the sliding band surface
    """
    lam_list = machine.get_lam_list()
    lam_int = lam_list[0]
    lam_ext = lam_list[1]
    lab_int = lam_int.get_label()
    lab_ext = lam_ext.get_label()

    Rgap_mec_int = lam_int.comp_radius_mec()
    Rgap_mec_ext = lam_ext.comp_radius_mec()
    Sor = lam_ext.Rext
    Wgap_mec = Rgap_mec_ext - Rgap_mec_int
    W_sb = Wgap_mec / 4  # Width sliding band
    tol = 0.1e-3  # Tolerance


    surf_list = list()
    if sym == 1:  # Complete machine
        # Internal AirGap
        int_airgap_cir = Circle(
                center=0,
                radius=Rgap_mec_int + W_sb,
                label=lab_int + "_" + AIRGAP_LAB + BOT_LAB,
                point_ref=(Rgap_mec_int + W_sb / 2) * exp(1j * pi / 2),
                prop_dict={BOUNDARY_PROP_LAB: AR_B_LAB},
        )
        surf_list.append(int_airgap_cir)
        # Internal Sliding band
        int_sb_cir = Circle(
                center=0,
                radius=Rgap_mec_int + 2 * W_sb - tol / 10,
                label=NO_LAM_LAB + "_" + SLID_LAB + BOT_LAB,
                point_ref=(Rgap_mec_ext - W_sb / 2) * exp(1j * pi / 2),
                prop_dict={BOUNDARY_PROP_LAB: SBR_B_LAB},
        )
        surf_list.append(
            SurfRing(
                out_surf=int_sb_cir,
                in_surf=int_airgap_cir,
                label=NO_LAM_LAB + "_" + SLID_LAB + BOT_LAB,
                point_ref=(Rgap_mec_ext - W_sb / 2) * exp(1j * pi / 2),
            )            
        )
        ext_sb_cir = Circle(
                center=0,
                radius=Rgap_mec_int + 2 * W_sb + tol / 10,
                label=NO_LAM_LAB + "_" + SLID_LAB + TOP_LAB,
                point_ref=(Rgap_mec_ext - W_sb / 2) * exp(1j * pi / 2),
                prop_dict={BOUNDARY_PROP_LAB: SBR_T_LAB},
        )
        ext_airgap_cir = Circle(
                center=0,
                radius=Rgap_mec_int + 3 * W_sb,
                label=lab_ext + "_" + AIRGAP_LAB + TOP_LAB,
                point_ref=(Rgap_mec_ext - W_sb / 2) * exp(1j * pi / 2),
                prop_dict={BOUNDARY_PROP_LAB: AR_T_LAB},
        )
        # External Sliding band
        surf_list.append(
            SurfRing(
                out_surf=ext_airgap_cir,
                in_surf=ext_sb_cir,
                label=NO_LAM_LAB + "_" + SLID_LAB + TOP_LAB,
                point_ref=(Rgap_mec_ext - W_sb / 2) * exp(1j * pi / 2),
            )            
        )
        lam_ext_cir = Circle(
                center=0,
                radius=1.1*Rgap_mec_ext, # Hopefully enough to reach the windings
                label=lab_ext + "_" + AIRBOX_LAB + BOT_LAB,
                point_ref=(Rgap_mec_ext - W_sb / 2) * exp(1j * pi / 2),
                prop_dict={BOUNDARY_PROP_LAB: AIRBOX_R_LAB},
        )
        # External AirGap
        surf_list.append(
            SurfRing(
                out_surf=lam_ext_cir,
                in_surf=ext_airgap_cir,
                label=lab_ext + "_" + AIRGAP_LAB + TOP_LAB,
                point_ref=(Rgap_mec_ext - W_sb / 2) * exp(1j * pi / 2),
            )
        )

    else:  # Symmetry
        # Internal AirGap
        Z0 = 0 * exp(1j * 2 * pi / sym)
        Z2 = Rgap_mec_int + W_sb
        Z3 = Z2 * exp(1j * 2 * pi / sym)
        airgap_lines = list()
        airgap_lines.append(
            Segment(begin=Z0, end=Z2, prop_dict={BOUNDARY_PROP_LAB: AS_BR_LAB})
        )
        int_airgap_arc = Arc1(
            begin=Z2,
            end=Z3,
            radius=Rgap_mec_int + W_sb,
            prop_dict={BOUNDARY_PROP_LAB: AR_B_LAB},
            is_trigo_direction=True,
        )
        airgap_lines.append(int_airgap_arc)
        airgap_lines.append(
            Segment(begin=Z3, end=Z0, prop_dict={BOUNDARY_PROP_LAB: AS_BL_LAB})
        )

        surf_list.append(
            SurfLine(
                line_list=airgap_lines,
                point_ref=(Z2 - W_sb / 2) * exp(1j * pi / sym),
                label=lab_int + "_" + AIRGAP_LAB + BOT_LAB,
            )
        )

        # Internal Sliding Band
        Z4 = Rgap_mec_int + 2 * W_sb - tol / 10
        Z5 = Z4 * exp(1j * 2 * pi / sym)
        airgap_lines = list()
        airgap_lines.append(
            Segment(begin=Z2, end=Z4, prop_dict={BOUNDARY_PROP_LAB: SBS_BR_LAB})
        )
        int_sb_arc = Arc1(
            begin=Z4,
            end=Z5,
            radius=Rgap_mec_int + 2 * W_sb - tol / 10,
            prop_dict={BOUNDARY_PROP_LAB: SBR_B_LAB},
            is_trigo_direction=True,
        )
        airgap_lines.append(int_sb_arc)
        airgap_lines.append(
            Segment(begin=Z5, end=Z3, prop_dict={BOUNDARY_PROP_LAB: SBS_BL_LAB})
        )
        int_airgap_arc_copy = Arc1(
            begin=Z2,
            end=Z3,
            radius=Rgap_mec_int + W_sb,
            # label="int_airgap_arc_copy",
            prop_dict={BOUNDARY_PROP_LAB: AR_B_LAB},
            is_trigo_direction=True,
        )
        int_airgap_arc_copy.reverse()
        airgap_lines.append(int_airgap_arc_copy)
        surf_list.append(
            SurfLine(
                line_list=airgap_lines,
                point_ref=(Z4 - W_sb / 2) * exp(1j * pi / sym),
                label=NO_LAM_LAB + "_" + SLID_LAB + BOT_LAB,
            )
        )

        # External Sliding Band
        Z6 = Rgap_mec_int + 2 * W_sb + tol / 10
        Z7 = Z6 * exp(1j * 2 * pi / sym)
        Z8 = Rgap_mec_int + 3 * W_sb
        Z9 = Z8 * exp(1j * 2 * pi / sym)
        airgap_lines = list()
        airgap_lines.append(  # Right Top SB
            Segment(begin=Z6, end=Z8, prop_dict={BOUNDARY_PROP_LAB: SBS_TR_LAB})
        )
        ext_airgap_arc = Arc1(
            begin=Z8,
            end=Z9,
            radius=Rgap_mec_int + 3 * W_sb,
            prop_dict={BOUNDARY_PROP_LAB: AR_T_LAB},  # Top Radius SB
            is_trigo_direction=True,
        )
        airgap_lines.append(ext_airgap_arc)
        airgap_lines.append(  # Left Top SB
            Segment(begin=Z9, end=Z7, prop_dict={BOUNDARY_PROP_LAB: SBS_TL_LAB})
        )
        ext_sb_arc = Arc1(
            begin=Z6,
            end=Z7,
            radius=Rgap_mec_int + 2 * W_sb + tol / 10,
            # label="ext_sb_arc",
            prop_dict={BOUNDARY_PROP_LAB: SBR_T_LAB},
            is_trigo_direction=True,
        )
        ext_sb_arc.reverse()
        airgap_lines.append(ext_sb_arc)
        surf_list.append(
            SurfLine(
                line_list=airgap_lines,
                point_ref=(Z8 - W_sb / 2) * exp(1j * pi / sym),
                label=NO_LAM_LAB + "_" + SLID_LAB + TOP_LAB,
            )
        )

        # External AirGap
        Z10 = Sor
        Z11 = Z10 * exp(1j * 2 * pi / sym)
        airgap_lines = list()
        airgap_lines.append(
            Segment(begin=Z8, end=Z10, prop_dict={BOUNDARY_PROP_LAB: AS_TR_LAB})
        )
        lam_ext_arc = Arc1(
            begin=Z10,
            end=Z11,
            radius=Sor,
            # label="int_airgap_arc_copy",
            is_trigo_direction=True,
        )
        airgap_lines.append(lam_ext_arc)
        airgap_lines.append(
            Segment(begin=Z11, end=Z9, prop_dict={BOUNDARY_PROP_LAB: AS_TL_LAB})
        )
        ext_airgap_arc_copy = Arc1(
            begin=Z8,
            end=Z9,
            radius=Rgap_mec_int + 3 * W_sb,
            # label="ext_airgap_arc_copy",
            prop_dict={BOUNDARY_PROP_LAB: AR_T_LAB},
            is_trigo_direction=True,
        )
        ext_airgap_arc_copy.reverse()
        airgap_lines.append(ext_airgap_arc_copy)
        surf_list.append(
            SurfLine(
                line_list=airgap_lines,
                point_ref=(Z8 + W_sb / 2) * exp(1j * pi / sym),
                label=lab_ext + "_" + AIRGAP_LAB + TOP_LAB,
            )
        )
    return surf_list

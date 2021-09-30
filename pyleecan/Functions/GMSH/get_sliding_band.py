# -*- coding: utf-8 -*-
from numpy import exp, pi
import cmath

from ...Classes.Arc import Arc
from ...Classes.Arc1 import Arc1
from ...Classes.Arc2 import Arc2
from ...Classes.Circle import Circle
from ...Classes.Segment import Segment
from ...Classes.SurfLine import SurfLine
from ...Classes.MachineSIPMSM import MachineSIPMSM
from ...Functions.labels import (
    AIRGAP_LAB,
    SLID_LAB,
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
)


def get_sliding_band(sym, machine):
    """Returns  a list of surface in the airgap including the sliding band surface

    Parameters
    ----------
    sym: int
        Symmetry factor (1= full machine, 2= half of the machine...)
    Rgap_mec_int: float
        Internal lamination mechanic radius
    Rgap_mec_ext: float
        External lamination mechanic radius

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

    stator_list = machine.stator.build_geometry(sym=sym)
    rotor_list = machine.rotor.build_geometry(sym=sym)
    slot_height = machine.stator.slot.comp_height()
    wind_slot_height = machine.stator.slot.comp_height_active()
    wedge_height = slot_height - wind_slot_height
    Rgap_mec_int = lam_int.comp_radius_mec()
    Rgap_mec_ext = lam_ext.comp_radius_mec()
    Rgap_mag_int = lam_int.Rext
    Rgap_mag_ext = lam_ext.Rint
    Sor = lam_ext.Rext
    Wgap_mec = Rgap_mec_ext - Rgap_mec_int
    W_sb = Wgap_mec / 4  # Width sliding band
    tol = 0.1e-3  # Tolerance
    max_radius_Airgap_ext = Rgap_mec_ext + wedge_height + tol
    min_radius_Airgap_int = Rgap_mec_int - tol

    # Find lines that are between Stator Inner Diam and slot wedge area
    stator_airgap_ext_lines = list()
    first_points = list()  # To check the loop and find inverted lines
    for surf in stator_list:
        for line in surf.get_lines():
            p1 = line.get_begin()
            p2 = line.get_end()
            if abs(p1) < max_radius_Airgap_ext and abs(p2) < max_radius_Airgap_ext:
                r_p1, phi_p1 = cmath.polar(p1)
                r_p2, phi_p2 = cmath.polar(p2)
                if isinstance(line, Arc):
                    p3 = line.get_center()
                    r_p3, phi_p3 = cmath.polar(p3)
                    radius = r_p1 - r_p3
                    line_copy = Arc1(
                        begin=p1,
                        end=p2,
                        radius=radius,
                        prop_dict=line.prop_dict,
                        is_trigo_direction=True,
                    )
                    # if phi_p2 > phi_p1:
                    #    line_copy.reverse()
                else:
                    line_copy = Segment(begin=p1, end=p2, prop_dict=line.prop_dict)
                new_p1 = p1
                for p in first_points:
                    if abs(p1.real - p.real) < tol and abs(p1.imag - p.imag) < tol:
                        line_copy.reverse()
                        new_p1 = p2
                        break
                stator_airgap_ext_lines.append(line_copy)
                first_points.append(new_p1)

    # Find lines that are between Rotor Outer Diam and ...
    rotor_airgap_int_lines = list()
    if isinstance(machine, MachineSIPMSM):
        min_radius_Airgap_int = min(Rgap_mec_int, Rgap_mag_int) - tol
        for surf in rotor_list:
            if "Magnet" in surf.label:
                continue
            for line in surf.get_lines():
                if line.comp_length() < tol:
                    continue
                p1 = line.get_begin()
                p2 = line.get_end()

                if abs(p1) > min_radius_Airgap_int and abs(p2) > min_radius_Airgap_int:
                    r_p1, phi_p1 = cmath.polar(p1)
                    r_p2, phi_p2 = cmath.polar(p2)
                    if isinstance(line, Arc):
                        p3 = line.get_center()
                        r_p3, phi_p3 = cmath.polar(p3)
                        radius = r_p1 - r_p3
                        line_copy = Arc1(
                            begin=p1,
                            end=p2,
                            radius=radius,
                            prop_dict=line.prop_dict,
                            is_trigo_direction=True,
                        )
                        if phi_p2 > phi_p1:
                            line_copy.reverse()
                    else:
                        line_copy = Segment(begin=p1, end=p2, prop_dict=line.prop_dict)
                        if phi_p2 > phi_p1:
                            line_copy.reverse()
                    rotor_airgap_int_lines.append(line_copy)
    else:
        for surf in rotor_list:
            for line in surf.get_lines():
                p1 = line.get_begin()
                p2 = line.get_end()
                if abs(p1) > min_radius_Airgap_int and abs(p2) > min_radius_Airgap_int:
                    r_p1, phi_p1 = cmath.polar(p1)
                    r_p2, phi_p2 = cmath.polar(p2)
                    if isinstance(line, Arc):
                        p3 = line.get_center()
                        r_p3, phi_p3 = cmath.polar(p3)
                        radius = r_p1 - r_p3
                        line_copy = Arc1(
                            begin=p1,
                            end=p2,
                            radius=radius,
                            prop_dict=line.prop_dict,
                            is_trigo_direction=True,
                        )
                        if phi_p2 > phi_p1:
                            line_copy.reverse()
                    else:
                        line_copy = Segment(begin=p1, end=p2, prop_dict=line.prop_dict)
                        if phi_p2 > phi_p1:
                            line_copy.reverse()
                    rotor_airgap_int_lines.append(line_copy)

    surf_list = list()
    if sym == 1:  # Complete machine
        # TODO: Sliding Band Full Machine no implemented yet.
        # Internal AirGap
        surf_list.append(
            Circle(
                center=0,
                radius=Rgap_mec_int + W_sb,
                label=lab_int + "_" + AIRGAP_LAB + BOT_LAB,
                point_ref=(Rgap_mec_int + W_sb / 2) * exp(1j * pi / 2),
                prop_dict={BOUNDARY_PROP_LAB: AR_B_LAB},
            )
        )
        # Internal Sliding band
        surf_list.append(
            Circle(
                center=0,
                radius=Rgap_mec_int + 2 * W_sb,
                label=NO_LAM_LAB + "_" + SLID_LAB,
                point_ref=(Rgap_mec_ext - W_sb / 2) * exp(1j * pi / 2),
                prop_dict={BOUNDARY_PROP_LAB: SBR_B_LAB},
            )
        )
        # External AirGap
        surf_list.append(
            Circle(
                center=0,
                radius=Rgap_mec_int + 3 * W_sb,
                label=lab_ext + "_" + AIRGAP_LAB + TOP_LAB,
                point_ref=(Rgap_mec_ext - W_sb / 2) * exp(1j * pi / 2),
                prop_dict={BOUNDARY_PROP_LAB: AR_T_LAB},
            )
        )

    else:  # Symmetry
        # Internal AirGap
        Z1 = Rgap_mec_int
        if isinstance(machine, MachineSIPMSM):
            Z1 = Rgap_mag_int
        Z0 = Z1 * exp(1j * 2 * pi / sym)
        Z2 = Rgap_mec_int + W_sb
        Z3 = Z2 * exp(1j * 2 * pi / sym)
        airgap_lines = list()
        airgap_lines.append(
            Segment(begin=Z1, end=Z2, prop_dict={BOUNDARY_PROP_LAB: AS_BR_LAB})
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
        airgap_lines.extend(rotor_airgap_int_lines)
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
            radius=Rgap_mec_int + 2 * W_sb,
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
            prop_dict={BOUNDARY_PROP_LAB: SBR_T_LAB},  # Top Radius SB
            is_trigo_direction=True,
        )
        airgap_lines.append(ext_airgap_arc)
        airgap_lines.append(  # Left Top SB
            Segment(begin=Z9, end=Z7, prop_dict={BOUNDARY_PROP_LAB: SBS_TL_LAB})
        )
        ext_sb_arc = Arc1(
            begin=Z6,
            end=Z7,
            radius=Rgap_mec_int + 2 * W_sb,
            # label="ext_sb_arc",
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
        Z10 = Rgap_mec_ext
        Z11 = Z10 * exp(1j * 2 * pi / sym)
        airgap_lines = list()
        airgap_lines.append(
            Segment(begin=Z8, end=Z10, prop_dict={BOUNDARY_PROP_LAB: AS_TR_LAB})
        )
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
        airgap_lines.extend(stator_airgap_ext_lines)
        surf_list.append(
            SurfLine(
                line_list=airgap_lines,
                point_ref=(Z8 + W_sb / 2) * exp(1j * pi / sym),
                label=lab_ext + "_" + AIRGAP_LAB + TOP_LAB,
            )
        )

    return surf_list

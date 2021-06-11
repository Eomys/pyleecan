from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Classes.Arc1 import Arc1
from ....Functions.labels import HOLEV_LAB, HOLEM_LAB, MAGNET_PROP_LAB


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Segment) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : HoleM50
        A HoleM50 object
    alpha : float
        Angle to rotate the slot (Default value = 0) [rad]
    delta : complex
        Complex to translate the slot (Default value = 0)
    is_simplified : bool
       True to avoid line superposition

    Returns
    -------
    surf_list: list
        List of SurfLine needed to draw the HoleM50

    """

    # Get correct label for surfaces
    lam_label = self.parent.get_label()
    R_id = "R" + str(self.parent.hole.index(self)) + "-"
    vent_label = lam_label + "_" + HOLEV_LAB + "_" + R_id
    mag_label = lam_label + "_" + HOLEM_LAB + "_" + R_id

    # Get all the points
    point_dict = self._comp_point_coordinate()
    Z1 = point_dict["Z1"]
    Z2 = point_dict["Z2"]
    Z3 = point_dict["Z3"]
    Z4 = point_dict["Z4"]
    Z5 = point_dict["Z5"]
    Z6 = point_dict["Z6"]
    Z7 = point_dict["Z7"]
    Z8 = point_dict["Z8"]
    Z9 = point_dict["Z9"]
    Z10 = point_dict["Z10"]
    Z11 = point_dict["Z11"]
    Z8c = point_dict["Z8c"]
    Z8b = point_dict["Z8b"]
    Z1s = point_dict["Z1s"]
    Z2s = point_dict["Z2s"]
    Z3s = point_dict["Z3s"]
    Z4s = point_dict["Z4s"]
    Z5s = point_dict["Z5s"]
    Z6s = point_dict["Z6s"]
    Z7s = point_dict["Z7s"]
    Z8s = point_dict["Z8s"]
    Z9s = point_dict["Z9s"]
    Z10s = point_dict["Z10s"]
    Z11s = point_dict["Z11s"]
    Z8cs = point_dict["Z8cs"]
    Z8bs = point_dict["Z8bs"]
    Rext = self.get_Rext()

    # Create all the lines
    L_1_2 = Segment(Z1, Z2, prop_dict=None)
    L_1s_2s = Segment(Z1s, Z2s, prop_dict=None)
    L_1s_11s = Segment(Z1s, Z11s, prop_dict=None)
    L_2_3 = Segment(Z2, Z3, prop_dict=None)
    L_2s_1s = Segment(Z2s, Z1s, prop_dict=None)
    L_2s_3s = Segment(Z2s, Z3s, prop_dict=None)
    L_3_4 = Segment(Z3, Z4, prop_dict={MAGNET_PROP_LAB: "Rotor_Magnet_0_Right"})
    L_3s_2s = Segment(Z3s, Z2s, prop_dict=None)
    L_3s_4s = Segment(Z3s, Z4s, prop_dict={MAGNET_PROP_LAB: "Rotor_Magnet_1_Left"})
    L_3_8c = Segment(Z3, Z8c, prop_dict={MAGNET_PROP_LAB: "Rotor_Hole_0_Right"})
    L_3s_8cs = Segment(Z3s, Z8cs, prop_dict={MAGNET_PROP_LAB: "Rotor_Hole_1_Left"})
    L_4_5 = Segment(Z4, Z5, prop_dict={MAGNET_PROP_LAB: "Rotor_Magnet_0_Bottom"})
    L_4s_3s = Segment(Z4s, Z3s, prop_dict=None)
    L_4s_5s = Segment(Z4s, Z5s, prop_dict={MAGNET_PROP_LAB: "Rotor_Magnet_1_Bottom"})
    L_5_6 = Segment(Z5, Z6, prop_dict={MAGNET_PROP_LAB: "Rotor_Magnet_0_Left"})
    L_5s_4s = Segment(Z5s, Z4s, prop_dict=None)
    L_5s_6s = Segment(Z5s, Z6s, prop_dict={MAGNET_PROP_LAB: "Rotor_Magnet_1_Right"})
    L_6_7 = Segment(Z6, Z7, prop_dict=None)
    L_6s_5s = Segment(Z6s, Z5s, prop_dict=None)
    L_6s_7s = Segment(Z6s, Z7s, prop_dict=None)
    L_6_8b = Segment(Z6, Z8b, prop_dict=None)
    L_6s_8bs = Segment(Z6s, Z8bs, prop_dict=None)
    L_7_6s = Segment(Z7, Z6s, prop_dict=None)
    L_7_8 = Segment(Z7, Z8, prop_dict={MAGNET_PROP_LAB: "Rotor_Radial_Bridge"})
    L_7s_6 = Segment(Z7s, Z6, prop_dict=None)
    L_7s_8s = Segment(Z7s, Z8s, prop_dict={MAGNET_PROP_LAB: "Rotor_Radial_Bridge"})

    L_8_8b = Segment(Z8, Z8b, prop_dict=None)
    L_8_9 = Segment(Z8, Z9, prop_dict=None)
    L_8s_8bs = Segment(Z8s, Z8bs, prop_dict={MAGNET_PROP_LAB: "Rotor_Hole_1_Top"})
    L_8s_8b = Segment(Z8s, Z8b, prop_dict={MAGNET_PROP_LAB: "Rotor_Hole_0_Top"})
    L_8s_9 = Segment(Z8s, Z9, prop_dict=None)
    L_8s_9s = Segment(Z8s, Z9s, prop_dict=None)

    L_8b_6 = Segment(Z8b, Z6, prop_dict={MAGNET_PROP_LAB: "Rotor_Hole_0_Left"})
    L_8bs_6s = Segment(Z8bs, Z6s, prop_dict={MAGNET_PROP_LAB: "Rotor_Hole_1_Right"})
    L_8b_8c = Segment(Z8b, Z8c, prop_dict={MAGNET_PROP_LAB: "Rotor_Magnet_0_Top"})
    L_8b_8s = Segment(Z8b, Z8s, prop_dict=None)
    L_8bs_8 = Segment(Z8bs, Z8, prop_dict=None)
    L_8bs_8s = Segment(Z8bs, Z8s, prop_dict={MAGNET_PROP_LAB: "Rotor_Hole_1_Top"})
    L_8bs_8cs = Segment(Z8bs, Z8cs, prop_dict={MAGNET_PROP_LAB: "Rotor_Magnet_1_Top"})

    L_8c_3 = Segment(Z8c, Z3, prop_dict=None)
    L_8cs_3s = Segment(Z8cs, Z3s, prop_dict=None)
    L_8c_9 = Segment(Z8c, Z9, prop_dict={MAGNET_PROP_LAB: "Rotor_Hole_0_Top"})
    L_8cs_9s = Segment(Z8cs, Z9s, prop_dict={MAGNET_PROP_LAB: "Rotor_Hole_1_Top"})

    L_9_10 = Segment(Z9, Z10, prop_dict=None)
    L_9s_8s = Segment(Z9s, Z8s, prop_dict=None)
    L_9s_10s = Segment(Z9s, Z10s, prop_dict=None)
    L_10_11 = Arc1(
        Z10,
        Z11,
        -Rext + self.H1,
        is_trigo_direction=False,
        prop_dict={MAGNET_PROP_LAB: "Rotor_Tangential_Bridge"},
    )
    L_10s_9s = Segment(Z10s, Z9s, prop_dict=None)
    L_10s_11s = Arc1(
        Z10s,
        Z11s,
        Rext - self.H1,
        is_trigo_direction=True,
        prop_dict={MAGNET_PROP_LAB: "Rotor_Tangential_Bridge"},
    )
    L_11_1 = Segment(Z11, Z1, prop_dict=None)
    L_11s_1s = Segment(Z11s, Z1s, prop_dict=None)
    L_11s_10s = Arc1(Z11s, Z10s, -Rext + self.H1, is_trigo_direction=False)

    # Create all the surfaces for all the cases
    surf_list = list()
    # Air surface (W3) with magnet_0
    curve_list = [L_1_2, L_2_3, L_3_8c, L_8c_9]
    if self.H4 > 0:
        curve_list.append(L_9_10)
    curve_list.append(L_10_11)
    if self.H4 > 0:
        curve_list.append(L_11_1)
    point_ref = (Z1 + Z2 + Z3 + Z8c + Z9 + Z10 + Z11) / 7
    S1 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Magnet_0 surface
    curve_list = list()
    if is_simplified:
        curve_list.append(L_8c_3)
        curve_list.append(L_6_8b)
    else:
        if Z3 != Z4:  # Z3 == Z4 if H2 = 0
            curve_list.append(L_3_4)
        curve_list.append(L_4_5)
        if Z5 != Z6:  # Z5 == Z6 if H2 = 0
            curve_list.append(L_5_6)
        curve_list.append(L_6_8b)
        curve_list.append(L_8b_8c)
        curve_list.append(L_8c_3)
    point_ref = (Z3 + Z4 + Z5 + Z6 + Z8b + Z8c) / 6

    S2 = SurfLine(line_list=curve_list, label=mag_label + "T0-S0", point_ref=point_ref)

    # Air surface with magnet_0 and W1 > 0
    curve_list = list()
    curve_list.append(L_6_7)
    curve_list.append(L_7_8)
    if self.W2 > 0:  # if W2=0 Z8 = Z8b
        curve_list.append(L_8_8b)
    curve_list.append(L_8b_6)
    point_ref = (Z6 + Z7 + Z8 + Z8b) / 4

    S3 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Symmetry Air surface (W3) with magnet_1
    curve_list = list()
    curve_list.append(L_1s_2s)
    curve_list.append(L_2s_3s)
    curve_list.append(L_3s_8cs)
    curve_list.append(L_8cs_9s)
    if self.H4 > 0:
        curve_list.append(L_9s_10s)
    curve_list.append(L_10s_11s)
    if self.H4 > 0:
        curve_list.append(L_11s_1s)
    point_ref = (Z1s + Z2s + Z3s + Z8cs + Z9s + Z10s + Z11s) / 7

    S4 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # magnet_1 surface
    curve_list = list()
    if is_simplified:
        curve_list.append(L_8cs_3s.copy())
        curve_list.append(L_6s_8bs.copy())
    else:
        if Z3s != Z4s:  # Z3 == Z3 if H2 = 0
            curve_list.append(L_3s_4s.copy())
        curve_list.append(L_4s_5s.copy())
        if Z5s != Z6s:  # Z5 == Z6 if H2 = 0
            curve_list.append(L_5s_6s.copy())
        curve_list.append(L_6s_8bs.copy())
        curve_list.append(L_8bs_8cs.copy())
        curve_list.append(L_8cs_3s.copy())
    point_ref = (Z3s + Z4s + Z5s + Z6s + Z8bs + Z8cs) / 6
    S5 = SurfLine(line_list=curve_list, label=mag_label + "T1-S0", point_ref=point_ref)

    # Air surface with magnet_1 and W1 > 0
    curve_list = list()
    curve_list.append(L_6s_7s)
    curve_list.append(L_7s_8s)  # rad. bridge
    if self.W2 > 0:  # if W2=0: Z8s = Z8bs
        curve_list.append(L_8s_8bs)
    curve_list.append(L_8bs_6s)
    point_ref = (Z6s + Z7s + Z8s + Z8bs) / 4

    S6 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Air surface both magnets and W1 = 0 (S6 + S3)
    curve_list = list()
    curve_list.append(L_6_7.copy())
    curve_list.append(L_7_6s.copy())
    curve_list.append(L_6s_8bs.copy())
    if self.W2 > 0:  # If W2 = 0: Z8b = Z8 = Z8bs
        curve_list.append(L_8bs_8s.copy())
        curve_list.append(L_8s_8b.copy())
    curve_list.append(L_8b_6.copy())  # == Magnet_0_Left
    point_ref = (Z6 + Z7 + Z6s + Z8s + Z8bs + Z8b) / 6
    S7 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Air surface without magnet_0 and W1 > 0 (S1 + S2 + S3)
    curve_list = list()
    curve_list.append(L_1_2)
    curve_list.append(L_2_3)
    if self.H2 > 0:
        curve_list.append(L_3_4)
    curve_list.append(L_4_5)
    if self.H2 > 0:
        curve_list.append(L_5_6)
    curve_list.append(L_6_7)
    curve_list.append(L_7_8)
    curve_list.append(L_8_9)
    if self.H4 > 0:
        curve_list.append(L_9_10)
    curve_list.append(L_10_11)
    if self.H4 > 0:
        curve_list.append(L_11_1)
    point_ref = (Z1 + Z2 + Z3 + Z8c + Z9 + Z10 + Z11) / 7
    S8 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Air surface without magnet_1 and W1 > 0
    curve_list = list()
    curve_list.append(L_1s_2s)
    curve_list.append(L_2s_3s)
    if self.H2 > 0:
        curve_list.append(L_3s_4s)
    curve_list.append(L_4s_5s)
    if self.H2 > 0:
        curve_list.append(L_5s_6s)
    curve_list.append(L_6s_7s)
    curve_list.append(L_7s_8s)
    curve_list.append(L_8s_9s)
    if self.H4 > 0:
        curve_list.append(L_9s_10s)
    curve_list.append(
        Arc1(Z10s, Z11s, Rext - self.H1, is_trigo_direction=True, prop_dict=None)
    )
    if self.H4 > 0:
        curve_list.append(L_11s_1s)
    point_ref = (Z1s + Z2s + Z3s + Z8cs + Z9s + Z10s + Z11s) / 7
    S9 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Air surface with magnet_0 without magnet_1 and W1 = 0
    # (S4 + S5 + S7)
    curve_list = list()
    curve_list.append(L_1s_2s.copy())
    curve_list.append(L_2s_3s.copy())
    if self.H2 > 0:
        curve_list.append(L_3s_4s.copy())
    curve_list.append(L_4s_5s.copy())
    if self.H2 > 0:
        curve_list.append(L_5s_6s.copy())
    curve_list.append(L_6s_7s.copy())
    curve_list.append(L_7s_6.copy())
    curve_list.append(L_6_8b.copy())
    if Z8b != Z8s:
        curve_list.append(L_8b_8s.copy())
    curve_list.append(L_8s_9s.copy())
    if self.H4 > 0:
        curve_list.append(L_9s_10s.copy())
    curve_list.append(L_10s_11s.copy())
    if self.H4 > 0:
        curve_list.append(L_11s_1s.copy())
    point_ref = (Z1s + Z2s + Z3s + Z8cs + Z9s + Z10s + Z11s) / 7
    S10 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Air surface with magnet_1 without magnet_0 and W1 = 0
    # (S1 + S2 + S7)
    curve_list = list()
    curve_list.append(L_1_2)
    curve_list.append(L_2_3)
    if self.H2 > 0:
        curve_list.append(L_3_4)
    curve_list.append(L_4_5)
    if self.H2 > 0:
        curve_list.append(L_5_6)
    curve_list.append(L_6_7)
    curve_list.append(L_7_6s)
    curve_list.append(L_6s_8bs)
    if Z8bs != Z8:
        curve_list.append(L_8bs_8)
    curve_list.append(L_8_9)
    if self.H4 > 0:
        curve_list.append(L_9_10)
    curve_list.append(L_10_11)
    if self.H4 > 0:
        curve_list.append(L_11_1)
    point_ref = (Z1 + Z2 + Z3 + Z8c + Z9 + Z10 + Z11) / 7
    S11 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Air surface without magnets and W1 = 0
    # (S4 + S5 + S7 + S2 + S1)
    curve_list = list()
    curve_list.append(L_1_2)
    curve_list.append(L_2_3)
    if Z3 != Z4:  # if H2 = 0
        curve_list.append(L_3_4)
    curve_list.append(L_4_5)
    if Z5 != Z6:  # if H2 = 0
        curve_list.append(L_5_6)
    curve_list.append(L_6_7)
    curve_list.append(L_7_6s)
    if Z5s != Z6s:
        curve_list.append(L_6s_5s)
    curve_list.append(L_5s_4s)
    if Z3s != Z4s:
        curve_list.append(L_4s_3s)
    curve_list.append(L_3s_2s)
    curve_list.append(L_2s_1s)
    if self.H4 > 0:
        curve_list.append(L_1s_11s)
    curve_list.append(L_11s_10s)
    if self.H4 > 0:
        curve_list.append(L_10s_9s)
    curve_list.append(L_9s_8s)
    curve_list.append(L_8s_9)
    if self.H4 > 0:
        curve_list.append(L_9_10)
    curve_list.append(L_10_11)
    if self.H4 > 0:
        curve_list.append(L_11_1)

    point_ref = (Z6 + Z8b + Z7 + Z8 + Z6s + Z8bs) / 6
    S12 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Create the surface list by selecting the correct ones
    if self.magnet_0 and self.magnet_1 and self.W1 > 0:
        S1.label = vent_label + "T0-S0"  # Hole
        S3.label = vent_label + "T1-S0"  # Hole
        S6.label = vent_label + "T2-S0"  # Hole
        S4.label = vent_label + "T3-S0"  # Hole
        surf_list = [S1, S2, S3, S6, S5, S4]
    elif self.magnet_0 and self.magnet_1 and self.W1 == 0:
        S1.label = vent_label + "T0-S0"  # Hole
        S7.label = vent_label + "T1-S0"  # Hole
        S4.label = vent_label + "T2-S0"  # Hole
        surf_list = [S1, S2, S7, S5, S4]
    elif self.magnet_0 and not self.magnet_1 and self.W1 > 0:
        S1.label = vent_label + "T0-S0"  # Hole
        S3.label = vent_label + "T1-S0"  # Hole
        S9.label = vent_label + "T2-S0"  # Hole
        surf_list = [S1, S2, S3, S9]
    elif self.magnet_0 and not self.magnet_1 and self.W1 == 0:
        S1.label = vent_label + "T0-S0"  # Hole
        S10.label = vent_label + "T1-S0"  # Hole
        surf_list = [S1, S2, S10]
    elif not self.magnet_0 and self.magnet_1 and self.W1 > 0:
        S8.label = vent_label + "T0-S0"  # Hole
        S6.label = vent_label + "T1-S0"  # Hole
        S4.label = vent_label + "T2-S0"  # Hole
        surf_list = [S8, S6, S5, S4]
    elif not self.magnet_0 and self.magnet_1 and self.W1 == 0:
        S11.label = vent_label + "T0-S0"  # Hole
        S4.label = vent_label + "T1-S0"  # Hole
        surf_list = [S11, S5, S4]
    elif not self.magnet_0 and not self.magnet_1 and self.W1 > 0:
        S8.label = vent_label + "T0-S0"  # Hole
        S9.label = vent_label + "T1-S0"  # Hole
        surf_list = [S8, S9]
    elif not self.magnet_0 and not self.magnet_1 and self.W1 == 0:
        S12.label = vent_label + "T0-S0"  # Hole
        surf_list = [S12]

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list

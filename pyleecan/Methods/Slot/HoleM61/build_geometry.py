from numpy import pi

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Segment import Segment
from pyleecan.Classes.SurfLine import SurfLine
from pyleecan.Functions.labels import HOLEV_LAB, HOLEM_LAB


def build_geometry(self, alpha=0, delta=0, is_simplified=False):
    """Compute the curve (Segment) needed to plot the Slot.
    The ending point of a curve is the starting point of the next curve in
    the list

    Parameters
    ----------
    self : HoleM61
        A HoleM61 object
    alpha : float
        Angle to rotate the slot (Default value = 0) [rad]
    delta : complex
        Complex to translate the slot (Default value = 0)
    is_simplified : bool
        True to avoid line superposition

    Returns
    -------
    surf_list: list
        List of SurfLine needed to draw the HoleM58

    """
    Rbo = self.get_Rbo()

    # Get correct label for surfaces
    lam_label = self.parent.get_label()
    R_id, surf_type = self.get_R_id()
    vent_label = lam_label + "_" + surf_type + "_R" + str(R_id) + "-"
    mag_label = lam_label + "_" + HOLEM_LAB + "_R" + str(R_id) + "-"

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
    Z12 = point_dict["Z12"]

    # add possibility to create hole without magnet
    if self.W1 != None and self.W2 != None:
        ZM1 = point_dict["ZM1"]
        ZM2 = point_dict["ZM2"]
        ZM3 = point_dict["ZM3"]
        ZM4 = point_dict["ZM4"]
        ZM5 = point_dict["ZM5"]
        ZM6 = point_dict["ZM6"]
        ZM7 = point_dict["ZM7"]
        ZM8 = point_dict["ZM8"]
        ZM9 = point_dict["ZM9"]
        ZM10 = point_dict["ZM10"]
        ZM11 = point_dict["ZM11"]
        ZM12 = point_dict["ZM12"]
        ZM13 = point_dict["ZM13"]
        ZM14 = point_dict["ZM14"]
        ZM15 = point_dict["ZM15"]
        ZM16 = point_dict["ZM16"]

    surf_list = list()
    # Create all the surfaces for all the cases

    # surface Hole without magnet
    curve_list = list()
    curve_list.append(Segment(Z1, Z2))
    curve_list.append(Segment(Z2, Z3))
    curve_list.append(Segment(Z3, Z4))
    curve_list.append(
        Arc1(
            begin=Z4,
            end=Z5,
            radius=Rbo - self.H2,
            is_trigo_direction=True,
        )
    )
    curve_list.append(Segment(Z5, Z6))
    curve_list.append(Segment(Z6, Z1))
    point_ref = (Z3 + Z6) / 2
    S2 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # surface Hole without magnet
    curve_list = list()
    curve_list.append(Segment(Z7, Z8))
    curve_list.append(Segment(Z8, Z9))
    curve_list.append(Segment(Z9, Z10))
    curve_list.append(
        Arc1(
            begin=Z10,
            end=Z11,
            radius=Rbo - self.H2,
            is_trigo_direction=True,
        )
    )
    curve_list.append(Segment(Z11, Z12))
    curve_list.append(Segment(Z12, Z7))

    point_ref = (Z9 + Z12) / 2
    S1 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # add possibility to create hole without magnet
    if self.W1 != None and self.W2 != None:
        # Magnet_2 surface
        curve_list = list()
        curve_list.append(Segment(ZM1, ZM2))
        curve_list.append(Segment(ZM2, ZM3))
        curve_list.append(Segment(ZM3, ZM4))
        curve_list.append(Segment(ZM4, ZM1))
        point_ref = (ZM1 + ZM3) / 2
        SM2 = SurfLine(line_list=curve_list, point_ref=point_ref)

        # Air surface between magnet_2 and magnet_3
        curve_list = list()
        curve_list.append(Segment(ZM4, ZM3))
        curve_list.append(Segment(ZM3, Z3))
        curve_list.append(Segment(Z3, ZM5))
        curve_list.append(Segment(ZM5, ZM8))
        curve_list.append(Segment(ZM8, Z6))
        curve_list.append(Segment(Z6, ZM4))
        point_ref = (Z3 + ZM4) / 2
        S23 = SurfLine(line_list=curve_list, point_ref=point_ref)

        # Surface for magnet_3
        curve_list = list()
        curve_list.append(Segment(ZM5, ZM6))
        curve_list.append(Segment(ZM6, ZM7))
        curve_list.append(Segment(ZM7, ZM8))
        curve_list.append(Segment(ZM8, ZM5))

        point_ref = (ZM5 + ZM7) / 2
        SM3 = SurfLine(line_list=curve_list, point_ref=point_ref)

        # Air surface between magnet_3 and top of slot
        curve_list = list()
        curve_list.append(Segment(ZM6, Z4))
        curve_list.append(
            Arc1(begin=Z4, end=Z5, radius=Rbo - self.H2, is_trigo_direction=True)
        )
        curve_list.append(Segment(Z5, ZM7))
        curve_list.append(Segment(ZM7, ZM6))

        point_ref = (Z5 + ZM6) / 2
        S3T = SurfLine(line_list=curve_list, point_ref=point_ref)

        # Air surface without magnet_2 but with magnet_3
        curve_list = list()
        curve_list.append(Segment(Z1, Z2))
        curve_list.append(Segment(Z2, Z3))
        curve_list.append(Segment(Z3, ZM5))
        curve_list.append(Segment(ZM5, ZM8))
        curve_list.append(Segment(ZM8, Z6))
        curve_list.append(Segment(Z6, Z1))
        point_ref = (Z1 + Z3) / 2
        SW02 = SurfLine(line_list=curve_list, point_ref=point_ref)

        # Air surface without magnet_3 but with magnet_2
        curve_list = list()
        curve_list.append(Segment(ZM3, Z3))
        curve_list.append(Segment(Z3, Z4))
        curve_list.append(
            Arc1(begin=Z4, end=Z5, radius=Rbo - self.H2, is_trigo_direction=True)
        )
        curve_list.append(Segment(Z5, Z6))
        curve_list.append(Segment(Z6, ZM4))
        curve_list.append(Segment(ZM4, ZM3))

        point_ref = (Z5 + Z3) / 2
        SW03 = SurfLine(line_list=curve_list, point_ref=point_ref)

        # Magnet_1 surface
        curve_list = list()
        curve_list.append(Segment(ZM9, ZM10))
        curve_list.append(Segment(ZM10, ZM11))
        curve_list.append(Segment(ZM11, ZM12))
        curve_list.append(Segment(ZM12, ZM9))
        point_ref = (ZM10 + ZM12) / 2
        SM1 = SurfLine(line_list=curve_list, point_ref=point_ref)

        # Air surface between magnet_1 and magnet_0
        curve_list = list()
        curve_list.append(Segment(ZM11, ZM12))
        curve_list.append(Segment(ZM12, Z12))
        curve_list.append(Segment(Z12, ZM16))
        curve_list.append(Segment(ZM16, ZM13))
        curve_list.append(Segment(ZM13, Z9))
        curve_list.append(Segment(Z9, ZM11))
        point_ref = (Z9 + ZM12) / 2
        S10 = SurfLine(line_list=curve_list, point_ref=point_ref)

        # Surface for magnet_0
        curve_list = list()
        curve_list.append(Segment(ZM13, ZM14))
        curve_list.append(Segment(ZM14, ZM15))
        curve_list.append(Segment(ZM15, ZM16))
        curve_list.append(Segment(ZM16, ZM13))

        point_ref = (ZM13 + ZM15) / 2
        SM0 = SurfLine(line_list=curve_list, point_ref=point_ref)

        # Air surface between magnet_0 and top of slot
        curve_list = list()
        curve_list.append(Segment(ZM15, Z11))
        curve_list.append(
            Arc1(begin=Z11, end=Z10, radius=Rbo - self.H2, is_trigo_direction=True)
        )
        curve_list.append(Segment(Z10, ZM14))
        curve_list.append(Segment(ZM14, ZM15))

        point_ref = (Z10 + ZM15) / 2
        S0T = SurfLine(line_list=curve_list, point_ref=point_ref)

        # Air surface without magnet_1 but with magnet_0
        curve_list = list()
        curve_list.append(Segment(Z7, Z8))
        curve_list.append(Segment(Z8, Z9))
        curve_list.append(Segment(Z9, ZM13))
        curve_list.append(Segment(ZM13, ZM16))
        curve_list.append(Segment(ZM16, Z12))
        curve_list.append(Segment(Z12, Z7))
        point_ref = (Z12 + Z8) / 2
        SW01 = SurfLine(line_list=curve_list, point_ref=point_ref)

        # Air surface without magnet_0 but with magnet_1
        curve_list = list()
        curve_list.append(Segment(ZM11, Z9))
        curve_list.append(Segment(Z9, Z10))
        curve_list.append(
            Arc1(begin=Z10, end=Z11, radius=Rbo - self.H2, is_trigo_direction=True)
        )
        curve_list.append(Segment(Z11, Z12))
        curve_list.append(Segment(Z12, ZM12))
        curve_list.append(Segment(ZM12, ZM11))

        point_ref = (Z10 + Z12) / 2
        SW00 = SurfLine(line_list=curve_list, point_ref=point_ref)

    # Create the surface list by selecting the correct ones

    # add possibility to create hole without magnet
    surf_list = list()
    if self.W1 != None and self.W2 != None:
        if self.magnet_0:
            SM0.label = mag_label + "T0-S0"
            S0T.label = vent_label + "T0-S0"
            surf_list += [SM0, S0T]
            if self.magnet_1:
                SM1.label = mag_label + "T1-S0"
                S10.label = vent_label + "T1-S0"
                surf_list += [
                    S10,
                    SM1,
                ]
                if self.magnet_2:
                    SM2.label = mag_label + "T2-S0"
                    surf_list += [SM2]
                    if self.magnet_3:
                        SM3.label = mag_label + "T3-S0"
                        S23.label = vent_label + "T2-S0"
                        S3T.label = vent_label + "T3-S0"
                        surf_list += [S23, SM3, S3T]
                    else:
                        SW03.label = vent_label + "T2-S0"
                        surf_list += [SW03]
                else:
                    if self.magnet_3:
                        SW02.label = vent_label + "T2-S0"
                        SM3.label = mag_label + "T2-S0"
                        S3T.label = vent_label + "T3-S0"
                        surf_list += [SW02, SM3, S3T]
                    else:
                        S2.label = vent_label + "T2-S0"
                        surf_list += [S2]

            else:
                SW01.label = vent_label + "T1-S0"
                surf_list += [SW01]
                if self.magnet_2:
                    SM2.label = mag_label + "T1-S0"
                    surf_list += [SM2]
                    if self.magnet_3:
                        SM3.label = mag_label + "T2-S0"
                        S23.label = vent_label + "T1-S0"
                        S3T.label = vent_label + "T3-S0"
                        surf_list += [S23, SM3, S3T]
                    else:
                        SW03.label = vent_label + "T2-S0"
                        surf_list += [SW03]
                else:
                    if self.magnet_3:
                        SW02.label = vent_label + "T2-S0"
                        SM3.label = mag_label + "T1-S0"
                        S3T.label = vent_label + "T3-S0"
                        surf_list += [SW02, SM3, S3T]
                    else:
                        S2.label = vent_label + "T1-S0"
                        surf_list += [S2]
        else:
            if self.magnet_1:
                SW00.label = vent_label + "T0-S0"
                SM1.label = mag_label + "T0-S0"
                surf_list += [SW00, SM1]
                if self.magnet_2:
                    SM2.label = mag_label + "T1-S0"
                    surf_list += [SM2]
                    if self.magnet_3:
                        SM3.label = mag_label + "T2-S0"
                        S23.label = vent_label + "T1-S0"
                        S3T.label = vent_label + "T2-S0"
                        surf_list += [S23, SM3, S3T]
                    else:
                        SW03.label = vent_label + "T1-S0"
                        surf_list += [SW03]
                else:
                    if self.magnet_3:
                        SW02.label = vent_label + "T1-S0"
                        SM3.label = mag_label + "T1-S0"
                        S3T.label = vent_label + "T2-S0"
                        surf_list += [SW02, SM3, S3T]
                    else:
                        S2.label = vent_label + "T1-S0"
                        surf_list += [S2]
            else:
                S1.label = vent_label + "T0-S0"
                surf_list += [S1]
                if self.magnet_2:
                    SM2.label = mag_label + "T0-S0"
                    surf_list += [SM2]
                    if self.magnet_3:
                        SM3.label = mag_label + "T1-S0"
                        S23.label = vent_label + "T1-S0"
                        S3T.label = vent_label + "T2-S0"
                        surf_list += [S23, SM3, S3T]
                    else:
                        SW03.label = vent_label + "T1-S0"
                        surf_list += [SW03]
                else:
                    if self.magnet_3:
                        SW02.label = vent_label + "T1-S0"
                        SM3.label = mag_label + "T1-S0"
                        S3T.label = vent_label + "T2-S0"
                        surf_list += [SW02, SM3, S3T]
                    else:
                        S2.label = vent_label + "T1-S0"
                        surf_list += [S2]

    else:
        S1.label = vent_label + "T0-S0"
        surf_list += [S1]
        S2.label = vent_label + "T1-S0"
        surf_list += [S2]

    # Apply the transformations
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)

    return surf_list

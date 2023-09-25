from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Functions.labels import (
    WIND_LAB,
    COND_BOUNDARY_PROP_LAB,
    YSMR_LAB,
    YSML_LAB,
    YOKE_LAB,
)


def build_geometry_active(self, Nrad, Ntan, alpha=0, delta=0):
    """Split the slot active area in several zone

    Parameters
    ----------
    self : SlotM18_2
        A SlotM18_2 object
    Nrad : int
        Number of radial layer
    Ntan : int
        Number of tangentiel layer
    alpha : float
        float number for rotation (Default value = 0) [rad]
    delta : complex
        complex number for translation (Default value = 0)

    Returns
    -------
    surf_list: list
        List of surface delimiting the active zone

    """

    # get the name of the lamination
    lam_label = self.parent.get_label()
    Rbo = self.get_Rbo()

    if Nrad == 1 and Ntan == 1:
        surf_list = [self.get_surface_active()]
        surf_list[0].label = lam_label + "_" + WIND_LAB + "_R0-T0-S0"
    elif Nrad == 2 and Ntan == 1:
        point_dict = self._comp_point_coordinate()
        ZM1 = point_dict["ZM1"]
        ZM2 = point_dict["ZM2"]
        ZM3 = point_dict["ZM3"]
        ZM4 = point_dict["ZM4"]
        ZM5 = point_dict["ZM5"]
        ZM6 = point_dict["ZM6"]

        # Bore Magnet
        surf_list = list()
        curve_list = list()
        curve_list.append(
            Segment(ZM1, ZM2, prop_dict={COND_BOUNDARY_PROP_LAB: YSMR_LAB})
        )

        if self.is_outwards():
            curve_list.append(
                Arc1(ZM2, ZM5, (Rbo - self.Hmag_bore), is_trigo_direction=True)
            )
        else:
            curve_list.append(
                Arc1(ZM2, ZM5, (Rbo + self.Hmag_bore), is_trigo_direction=True)
            )

        curve_list.append(
            Segment(ZM5, ZM6, prop_dict={COND_BOUNDARY_PROP_LAB: YSML_LAB})
        )

        if self.is_outwards():
            curve_list.append(Arc1(ZM6, ZM1, -Rbo, is_trigo_direction=False))
        else:
            curve_list.append(Arc1(ZM6, ZM1, -Rbo, is_trigo_direction=False))
        # If no lamination, BC is required on bore
        curve_list[-1].prop_dict = {COND_BOUNDARY_PROP_LAB: YOKE_LAB}

        Zmid = (abs(ZM1) + abs(ZM2)) / 2

        surf_list.append(
            SurfLine(
                line_list=curve_list,
                label=lam_label + "_" + WIND_LAB + "_R0-T0-S0",
                point_ref=Zmid,
            )
        )

        # Airgap magnet
        curve_list = list()
        curve_list.append(
            Segment(ZM2, ZM3, prop_dict={COND_BOUNDARY_PROP_LAB: YSMR_LAB})
        )

        if self.is_outwards():
            curve_list.append(
                Arc1(
                    ZM3,
                    ZM4,
                    (Rbo - self.Hmag_bore - self.Hmag_gap),
                    is_trigo_direction=True,
                )
            )
        else:
            curve_list.append(
                Arc1(
                    ZM3,
                    ZM4,
                    (Rbo + self.Hmag_bore + self.Hmag_gap),
                    is_trigo_direction=True,
                )
            )

        curve_list.append(
            Segment(ZM4, ZM5, prop_dict={COND_BOUNDARY_PROP_LAB: YSML_LAB})
        )

        if self.is_outwards():
            curve_list.append(
                Arc1(ZM5, ZM2, -Rbo + self.Hmag_bore, is_trigo_direction=False)
            )
        else:
            curve_list.append(
                Arc1(ZM5, ZM2, -Rbo - self.Hmag_bore, is_trigo_direction=False)
            )

        Zmid = (abs(ZM2) + abs(ZM3)) / 2

        surf_list.append(
            SurfLine(
                line_list=curve_list,
                label=lam_label + "_" + WIND_LAB + "_R1-T0-S0",
                point_ref=Zmid,
            )
        )
    else:
        raise Exception(
            "Error Nrad=" + str(Nrad) + ", Ntan=" + str(Ntan) + ", is not available"
        )

    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)
    return surf_list

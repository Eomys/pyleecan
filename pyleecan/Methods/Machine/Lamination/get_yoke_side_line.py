from ....Functions.labels import (
    BOUNDARY_PROP_LAB,
    YS_LAB,
    YSR_LAB,
    YSL_LAB,
)
from numpy import exp, pi, angle as np_angle

DELTA = 1e-6
from ....Classes.Segment import Segment


def get_yoke_side_line(self, sym, vent_surf_list):
    """Define the Yoke Side lines of a Lamination by taking into account sym and vent

    Parameters:
    self: Lamination
        a Lamination object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    vent_surf_list :
        List of the ventilation surfaces

    Returns:
    right_list, left_list: ([Line], [Line])
        List of the lines to draw the left and right side of the yoke
    """

    # Find the ventilation lines that collide with the Yoke Side
    inter_line_list_R, inter_line_list_L = list(), list()
    for surf in vent_surf_list:
        for line in surf.get_lines():
            if (
                line.prop_dict is not None
                and BOUNDARY_PROP_LAB in line.prop_dict
                and YS_LAB in line.prop_dict[BOUNDARY_PROP_LAB]
            ):
                # Find if the line collide on right or left
                if abs(np_angle(line.get_middle())) < DELTA:
                    inter_line_list_R.append(line)
                else:
                    inter_line_list_L.append(line)

    # Yoke Limit point
    Z0 = self.Rint
    Z1 = self.Rext
    alpha = 2 * pi / sym
    Z3 = Z0 * exp(1j * alpha)
    Z2 = Z1 * exp(1j * alpha)

    lam_lab = self.get_label()
    if self.is_internal:
        right_list = merge_line_list(Z0, Z1, lam_lab + "_" + YSR_LAB, inter_line_list_R)
        left_list = merge_line_list(Z2, Z3, lam_lab + "_" + YSL_LAB, inter_line_list_L)
    else:
        left_list = merge_line_list(Z3, Z2, lam_lab + "_" + YSL_LAB, inter_line_list_L)
        right_list = merge_line_list(Z1, Z0, lam_lab + "_" + YSR_LAB, inter_line_list_R)

    return right_list, left_list


def merge_line_list(Z1, Z2, label, inter_list):
    """Merge the ventilation lines and the yoke side line"""
    is_int_to_ext = abs(Z1) < abs(Z2)
    #  Always number the lines from int to out (to match both sides)
    if not is_int_to_ext:
        Z1, Z2 = Z2, Z1
    # Sort the inter_list by begin (assume that the vents doesn't collide)
    inter_list.sort(key=lambda x: abs(x.get_begin()), reverse=False)

    line_list = list()
    Zb = Z1  # Current Begin
    ii = 0  # Line index
    for line in inter_list:
        line_list.append(
            Segment(
                Zb,
                line.get_begin(),
                prop_dict={BOUNDARY_PROP_LAB: label + "-" + str(ii)},
            )
        )
        ii += 1
        line.prop_dict[BOUNDARY_PROP_LAB] = label + "-" + str(ii)
        ii += 1
        Zb = line.get_end()
    # Add last line (or Z1 to Z2 if no intersection)
    line_list.append(
        Segment(Zb, Z2, prop_dict={BOUNDARY_PROP_LAB: label + "-" + str(ii)})
    )
    # reverse the lines if needed
    if not is_int_to_ext:
        line_list = line_list[::-1]
        for line in line_list:
            line.reverse()

    return line_list

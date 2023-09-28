from numpy import exp, angle, abs as np_abs

from ....Classes.Segment import Segment
from ....definitions import PACKAGE_NAME

DELTA = 1e-7  # To remove computing/DXF noise


def split_line(self, Z1, Z2, is_join=False, prop_dict_join=None):
    """Cut the Arc according to a line defined by two complex
    "Above" is in the coordinate system with Z1 in 0 and Z2 on the X>0 axis

    Parameters
    ----------
    self : Segment
        An Segment object
    Z1 : complex
        First point of the cutting Line
    Z2 : complex
        Second point of the cutting Line
    is_join : bool
        True to join the split_list with Segment if there is more that one remaining parts
    prop_dict_join : dict
        Property dict to set on the join line

    Returns
    -------
    top_split_list, bot_split_list : ([Line], [Line])
        Both part of the arc
    """

    # Dynamic import of Arc1 to prevent import loop from code generator
    module = __import__(PACKAGE_NAME + ".Classes.Arc1", fromlist=["Arc1"])
    Arc1 = getattr(module, "Arc1")

    # Get the intersection point
    Z_int = self.intersect_line(Z1, Z2)
    # Begin and end point in the line coordonate system
    Zb = (self.get_begin() - Z1) * exp(-1j * angle(Z2 - Z1))
    Ze = (self.get_end() - Z1) * exp(-1j * angle(Z2 - Z1))
    # Center of the arc (for later check)
    Zc = self.get_center()

    if len(Z_int) == 0:
        # No intersection copy the line
        line = self.copy()
        # Begin and end on top
        if Zb.imag >= 0 and Ze.imag >= 0:
            return [line], []
        # Begin and end on bot
        elif Zb.imag <= 0 and Ze.imag <= 0:
            return [], [line]
        else:
            raise Exception("Split Arc error (case 0 int)")
    if len(Z_int) == 1:
        # One intersection => Three possible lines
        # Begin => Intersection
        line1 = Arc1(
            begin=self.get_begin(),
            end=Z_int[0],
            radius=self.comp_radius(),
            is_trigo_direction=bool(self.get_angle() > 0),
        )
        # Fix radius if needed
        if (
            np_abs(line1.begin - line1.end) > 1e-6  # Avoid error for center
            and np_abs(line1.get_center() - Zc) > 1e-6
        ):
            line1.radius = -1 * line1.radius
        # Intersection => End
        line2 = Arc1(
            begin=Z_int[0],
            end=self.get_end(),
            radius=self.comp_radius(),
            is_trigo_direction=bool(self.get_angle() > 0),
        )
        # Fix radius if needed
        if (
            np_abs(line2.begin - line2.end) > 1e-6
            and np_abs(line2.get_center() - Zc) > 1e-6  # Avoid error for center
        ):
            line2.radius = -1 * line2.radius

        # Copy of the complete line (begin or end on cutting line, or cutting line is tangent)
        line3 = self.copy()

        # If the line is tangent, begin and end are on the same side of the line
        if (Zb.imag > DELTA and Ze.imag > DELTA) or (
            Zb.imag < -DELTA and Ze.imag < -DELTA
        ):
            # Begin (and end) on top
            if Zb.imag > DELTA:
                return [line3], []
            # Begin (and end) on bot
            elif Zb.imag < -DELTA:
                return [], [line3]
            else:
                raise Exception("Split Arc error (case 1 int-Tangent)")
        # Return the correct line according to the points position
        elif Zb.imag > DELTA and abs(Ze.imag) > DELTA:  # Begin on top; End!=Int
            return [line1], [line2]
        elif Zb.imag > DELTA:  # Begin on top; End==Int
            return [line3], []
        elif Zb.imag < -DELTA and abs(Ze.imag) > DELTA:  # Begin on bot; End!=Int
            return [line2], [line1]
        elif Zb.imag < -DELTA:  # Begin on bot; End==Int
            return [], [line3]
        # Zb.imag == 0 => begin on cutting line
        elif Ze.imag > DELTA:  # Begin==Int, End on Top
            return [line3], []
        elif Ze.imag < -DELTA:  # Begin==Int, End on Bot
            return [], [line3]
        else:
            raise Exception("Split Arc error (case 1 int-Non Tangent)")
    elif len(Z_int) == 2:
        # Two intersection => Three possible lines
        # Begin => Intersection1 (intersection are ordered along the arc)
        line1 = Arc1(
            begin=self.get_begin(),
            end=Z_int[0],
            radius=self.comp_radius(),
            is_trigo_direction=bool(self.get_angle() > 0),
        )
        # Fix radius if needed
        if (
            np_abs(line1.begin - line1.end) > 1e-6  # Avoid error for center
            and np_abs(line1.get_center() - Zc) > 1e-6
        ):
            line1.radius = -1 * line1.radius
        # Intersection 1 => Intersection 2
        line2 = Arc1(
            begin=Z_int[0],
            end=Z_int[1],
            radius=self.comp_radius(),
            is_trigo_direction=bool(self.get_angle() > 0),
        )
        # Fix radius if needed
        if (
            np_abs(line2.begin - line2.end) > 1e-6  # Avoid error for center
            and np_abs(line2.get_center() - Zc) > 1e-6
        ):
            line2.radius = -1 * line2.radius
        # Intersection 2 => End
        line3 = Arc1(
            begin=Z_int[1],
            end=self.get_end(),
            radius=self.comp_radius(),
            is_trigo_direction=bool(self.get_angle() > 0),
        )
        # Fix radius if needed
        if (
            np_abs(line3.begin - line3.end) > 1e-6  # Avoid error for center
            and np_abs(line3.get_center() - Zc) > 1e-6
        ):
            line3.radius = -1 * line3.radius
        # Line Intersection 1 => Intersection 2 for join
        seg_join = Segment(begin=Z_int[0], end=Z_int[1], prop_dict=prop_dict_join)
        # If both intersection are Begin and end
        line4 = self.copy()
        if is_join:
            line_list = [line1, seg_join, line3]
        else:
            line_list = [line1, line3]
        if np_abs(Z_int[0] - self.get_begin()) < DELTA:  # Begin==Int1
            line_list.pop(0)
        if np_abs(Z_int[1] - self.get_end()) < DELTA:
            line_list.pop(-1)

        # If the intersetion points are begin and end
        if (
            np_abs(Z_int[0] - self.get_begin()) < DELTA
            and np_abs(Z_int[1] - self.get_end()) < DELTA
        ):
            Zm = (self.get_middle() - Z1) * exp(-1j * angle(Z2 - Z1))
            # begin and end are on the line => Zm.imag != 0
            if Zm.imag > 0:
                return [line4], []
            elif Zm.imag < 0:
                return [], [line4]
            else:
                raise Exception("Split Arc error (case 2 int-Both)")
        elif Zb.imag > DELTA:  # Begin on top
            return line_list, [line2]
        elif Zb.imag < -DELTA:  # Begin on bot
            return [line2], line_list
        elif Ze.imag > DELTA:  # Begin== Int1, End on Top
            return line_list, [line2]
        elif Ze.imag < -DELTA:  # Begin== Int1, End on Bot
            return [line2], line_list
        else:
            Exception("Split Arc error (case 2 int)")

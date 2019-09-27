from numpy import exp, angle, abs as np_abs

DELTA = 1e-9  # To remove computing noise


def split_line(self, Z1, Z2, is_top=True):
    """Cut the Arc according to a line defined by two complex

    Parameters
    ----------
    self : Segment
        An Segment object
    Z1 : complex
        First point of the cutting Line
    Z2 : complex
        Second point of the cutting Line
    is_top : bool
        True to keep the part above the cutting line.
        "Above" is in the coordinate system with Z1 in 0 and Z2 on the X>0 axis 

    Returns
    -------
    split_list : list(Arc)
        The selected part of the arc (0, 1 or 2 arc depending on cutting point)
    """

    # Dynamic import of Arc1 to prevent import loop from code generator
    module = __import__("pyleecan.Classes.Arc1", fromlist=["Arc1"])
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
        line = type(self)(init_dict=self.as_dict())
        if Zb.imag >= 0 and Ze.imag >= 0 and is_top:
            return [line]
        if Zb.imag >= 0 and Ze.imag >= 0 and not is_top:
            return list()
        if Zb.imag <= 0 and Ze.imag <= 0 and is_top:
            return list()
        return [line]
    if len(Z_int) == 1:
        # One intersection => Three possible lines
        # Begin => Intersection
        if np_abs(Z_int[0] - self.begin) > DELTA:
            line1 = Arc1(
                begin=self.get_begin(),
                end=Z_int[0],
                radius=self.comp_radius(),
                is_trigo_direction=bool(self.get_angle() > 0),
            )
            # Fix radius if needed
            if np_abs(line1.get_center() - Zc) > 1e-6:
                line1.radius = -1 * line1.radius
        else:  # Begin == Intersection
            line1 = None
        # Intersection => End
        if np_abs(Z_int[0] - self.end) > DELTA:
            line2 = Arc1(
                begin=Z_int[0],
                end=self.get_end(),
                radius=self.comp_radius(),
                is_trigo_direction=bool(self.get_angle() > 0),
            )
            # Fix radius if needed
            if np_abs(line2.get_center() - Zc) > 1e-6:
                line2.radius = -1 * line2.radius
        else:  # Intersection == End
            line2 = None
        # Copy of the complete line (begin or end on cutting line)
        line3 = type(self)(init_dict=self.as_dict())

        # Return the correct line according to the points position
        if Zb.imag > DELTA and is_top:
            if line1:
                return [line1]
            return []
        if Zb.imag > DELTA and not is_top:
            if line2:
                return [line2]
            return []
        if Zb.imag < -DELTA and is_top:
            if line2:
                return [line2]
            return []
        if Zb.imag < -DELTA and not is_top:
            if line1:
                return [line1]
            return []
        # Zb.imag == 0 => begin on cutting line
        if Ze.imag > DELTA and is_top:
            return [line3]
        if Ze.imag > DELTA and not is_top:
            return []
        if Ze.imag < -DELTA and is_top:
            return []
        if Ze.imag < -DELTA and not is_top:
            return [line3]
    # if len(Z_int) == 2:
    #     # The segment is on the line => Copy the line
    #     return type(self)(init_dict=self.as_dict())

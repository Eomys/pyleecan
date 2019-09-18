from numpy import exp, angle, abs as np_abs

DELTA = 1e-9  # To remove computing noise


def split_line(self, Z1, Z2, is_top=True):
    """Cut the Segment according to a line defined by two complex

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
    line : Segment
        The selected part of the line (can be a copy of self, a new line or None)
    """

    Z_int = self.intersect_line(Z1, Z2)
    # Begin and end point in the line coordonate system
    Zb = (self.begin - Z1) * exp(-1j * angle(Z2 - Z1))
    Ze = (self.end - Z1) * exp(-1j * angle(Z2 - Z1))

    if len(Z_int) == 0:
        # No intersection copy the line
        line = type(self)(init_dict=self.as_dict())
        if Zb.imag >= 0 and Ze.imag >= 0 and is_top:
            return line
        if Zb.imag >= 0 and Ze.imag >= 0 and not is_top:
            return None
        if Zb.imag <= 0 and Ze.imag <= 0 and is_top:
            return None
        return line
    if len(Z_int) == 1:
        # One intersection => Three possible lines
        # Begin => Intersection
        if np_abs(Z_int[0] - self.begin) > DELTA:
            line1 = type(self)(init_dict=self.as_dict())
            line1.end = Z_int[0]
        else:  # Begin == Intersection
            line1 = None
        # Intersection => End
        if np_abs(Z_int[0] - self.end) > DELTA:
            line2 = type(self)(init_dict=self.as_dict())
            line2.begin = Z_int[0]
        else:  # Intersection == End
            line2 = None
        # Copy of the complete line (begin or end on cutting line)
        line3 = type(self)(init_dict=self.as_dict())

        # Return the correct line according to the points position
        if Zb.imag > DELTA and is_top:
            return line1
        if Zb.imag > DELTA and not is_top:
            return line2
        if Zb.imag < -DELTA and is_top:
            return line2
        if Zb.imag < -DELTA and not is_top:
            return line1
        # Zb.imag == 0 => begin on cutting line
        if Ze.imag > DELTA and is_top:
            return line3
        if Ze.imag > DELTA and not is_top:
            return None
        if Ze.imag < -DELTA and is_top:
            return None
        if Ze.imag < -DELTA and not is_top:
            return line3
    if len(Z_int) == 2:
        # The segment is on the line => Copy the line
        return type(self)(init_dict=self.as_dict())

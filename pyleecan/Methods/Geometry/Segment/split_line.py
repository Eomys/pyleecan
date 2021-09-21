from numpy import exp, angle, abs as np_abs

DELTA = 1e-9  # To remove computing noise


def split_line(self, Z1, Z2, is_join=False, prop_dict_join=None):
    """Cut the Segment according to a line defined by two complex
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
    top_split_list, bot_split_list : ([Segment], [Segment])
        Both part of the Segment (1 or 2 segment depending on cutting point)
    """

    Z_int = self.intersect_line(Z1, Z2)
    # Begin and end point in the line coordonate system
    Zb = (self.begin - Z1) * exp(-1j * angle(Z2 - Z1))
    Ze = (self.end - Z1) * exp(-1j * angle(Z2 - Z1))

    if len(Z_int) == 0:
        # No intersection copy the line
        if Zb.imag >= 0 and Ze.imag >= 0:
            # Begin and end on top
            return [self.copy()], []
        elif Zb.imag <= 0 and Ze.imag <= 0:
            # Begin and end on bot
            return [], [self.copy()]
        else:
            raise Exception("Split Segment error (case 0 int)")
        # return [self.copy()], []
    elif len(Z_int) == 1:
        # One intersection => Three possible lines
        # Begin => Intersection
        line1 = self.copy()
        line1.end = Z_int[0]
        # Intersection => End
        line2 = self.copy()
        line2.begin = Z_int[0]
        # begin or end on cutting line
        line3 = self.copy()

        # Return the correct line according to the points position
        if Zb.imag > DELTA and abs(Ze.imag) > DELTA:  # begin on top, end != Int
            return [line1], [line2]
        elif Zb.imag > DELTA:
            return [line3], []
        elif Zb.imag < -DELTA and abs(Ze.imag) > DELTA:  # begin on bot, end != Int
            return [line2], [line1]
        elif Zb.imag < -DELTA:
            return [], [line3]
        # Zb.imag == 0 => begin on cutting line
        elif Ze.imag > DELTA:  # End on top
            return [line3], []
        elif Ze.imag < -DELTA:  # End on bot
            return [], [line3]
        else:
            raise Exception("Split Segment error (case 1 int)")
    elif len(Z_int) == 2:
        # The segment is on the line => Copy the line twice
        return [self.copy()], [self.copy()]

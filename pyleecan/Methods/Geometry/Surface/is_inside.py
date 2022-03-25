# -*- coding: utf-8 -*


def is_inside(self, Z, if_online=False):
    """Determine if a given point is inside the surface.
       If the point is on the line defining the surface, by default it will be considered as outside

    Parameters
    ----------
    self : Surface
        A Surface object
    Z : complex
        Point that we want to check if it is in the surface
    if_online : bool
        True to consider the point  on the line as in the surface
        False to consider the point on the line as out of the surface

    Returns
    -------
    is_inside : bool
        True : the point is inside the surface
        False : the point is outside the surface
    """

    # Half of the width of the branch where we will check is there is a point
    eps = 0.0001

    # Recovering the point cloud that compose the surface
    line_list = self.get_lines()

    pointcloud = list()
    for line in line_list:
        line_len = line.comp_length()
        Npoint = max(int(line_len / eps), 4)
        pointcloud.extend(line.discretize(nb_point=Npoint))

    # Step 1 : Checking if the point is on the line that define the surface
    # First, we call the is_online method for each segment to check is the point is on one of the segment
    for line in line_list:
        if line.is_on_line(Z):
            return if_online

    # Step 2 : Checking if the point is inside the surface
    # Then, we are creating a cross on both axes with a width of 2*eps centered on Z
    # We check that at least one point is inside each branch of the cross

    # To determine which branch the point is in, we check the distance to Z
    is_top, is_left, is_bot, is_right = False, False, False, False
    for point in pointcloud:
        # If the point selected is inside the branch on the x-axis
        if (point.real > Z.real - eps) and (point.real < Z.real + eps):
            if point.imag - Z.imag > 0:
                # The point is on top of Z
                is_top = True
            else:
                # The point is below Z
                is_bot = True

        else:
            # If the point selected is inside the branch on the y-axis
            if (point.imag > Z.imag - eps) and (point.imag < Z.imag + eps):
                if point.real - Z.real > 0:
                    # The point is on the left of Z
                    is_left = True
                else:
                    # The point is on the right of Z
                    is_right = True

    return is_top and is_left and is_right and is_bot

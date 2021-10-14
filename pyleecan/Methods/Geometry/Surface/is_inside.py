# -*- coding: utf-8 -*

from numpy import real, imag


def is_inside(self, Z, is_online=False):
    """Determine if a given point is inside the surface.
       If the point is on the line defining the surface, by default it will be considered as outside

    Parameters
    ----------
    self : Surface
        A Surface object
    Z : complex
        Point that we want to check if it is in the surface

    is_online : bool
        True to consider the point  on the line as in the surface
        False to consider the point on the line as out of the surface


    Returns
    -------
    is_inside : bool
        True : the point is inside the surface
        False : the point is outside the surface
    """

    eps = 0.1  # The width of the window where we will check is there is a distance between the point and the outside line of the surface

    # Recovering the point cloud that compose the surface
    segment_list = self.get_lines()

    pointcloud = list()
    for seg in segment_list:
        seg_len = seg.comp_length()
        pointcloud.extend(seg.discretize(nb_point=int(seg_len / eps)))

    dx = list()
    dy = list()
    for point in pointcloud:
        if (real(point) > real(Z) - eps) and (real(point) < real(Z) + eps):
            dy.append(imag(point) - imag(Z))

        if (imag(point) > imag(Z) - eps) and (imag(point) < imag(Z) + eps):
            dx.append(real(point) - real(Z))

    pos_val_x = list()
    neg_val_x = list()
    pos_val_y = list()
    neg_val_y = list()

    if is_online:
        for val in dx:
            pos_val_x.append(val >= 0)
            neg_val_x.append(val <= 0)

        for val in dy:
            pos_val_y.append(val >= 0)
            neg_val_y.append(val <= 0)
    else:
        for val in dx:
            pos_val_x.append(val > 0)
            neg_val_x.append(val < 0)

        for val in dy:
            pos_val_y.append(val > 0)
            neg_val_y.append(val < 0)

    if any(pos_val_x) and any(neg_val_x) and any(pos_val_y) and any(neg_val_y):
        return True
    else:
        return False

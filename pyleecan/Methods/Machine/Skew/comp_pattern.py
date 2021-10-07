def comp_pattern(self, is_reverse_z=False, is_reverse_angle=False):
    """Compute skew pattern by duplicating points in case of stepped skew

    Parameters
    ----------
    self : Skew
        a Skew object
    is_reverse_z : bool
        True to reverse slice position
    is_reverse_angle : bool
        True to reverse slice angle

    Returns
    -------
    angle_list : list
        list of skew angles
    z_list : list
        list of slice positions

    """

    if self.angle_list is None or self.z_list is None:
        self.comp_angle()

    is_step = self.is_step
    z_list = self.z_list
    angle_list = self.angle_list

    if is_step:
        # Duplicate points at z_start and z_end of each segment
        angle_list_new = [angle_list[0]]
        z_list_new = list()
        for i, z in enumerate(z_list[:-1]):
            # Duplicate z_start and z_end
            z_list_new += [z, z_list[i + 1]]
            if i < len(angle_list) - 1:
                # If it is not the last segment
                # Assign skew angle value at z_start and z_end
                angle_list_new += [angle_list[i], angle_list[i + 1]]
            elif i < len(angle_list):
                # If it is the last segment
                # Only assign skew angle value to last point
                angle_list_new.append(angle_list[i])

    else:
        # Return points as they are
        angle_list_new = angle_list
        z_list_new = z_list

    if is_reverse_z:
        angle_list_new = list(reversed(angle_list_new))

    if is_reverse_angle:
        angle_list_new = [-a for a in angle_list_new]

    return angle_list_new, z_list_new

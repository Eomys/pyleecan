from numpy import exp, angle, pi


def cut_lines_between_angles(line_list, begin_angle, end_angle):
    """Cut a list of lines between two angles
    Assume that the lines draw a closed surface centered on O
    Constraint: end_angle - begin_angle < pi (first cut remove half the lines)

    Parameters
    ----------
    line_list : [Line]
        list of line to cut
    begin_angle : float
        Begin angle of the cut [rad]
    end_angle : float
        End angle of the cut [rad]

    Returns
    -------
    cut_lines : [Line]
        Cut lines between the two angles
    """

    first_cut = list()
    cut_lines = list()
    # First cut
    for line in line_list:
        top_split_list, _ = line.split_line(0, exp(1j * begin_angle))
        first_cut.extend(top_split_list)
    # Second cut
    for line in first_cut:
        _, bot_split_list = line.split_line(0, exp(1j * end_angle))
        cut_lines.extend(bot_split_list)

    # Check that lines are in the correct way
    if (angle(cut_lines[0].get_begin()) % (2 * pi)) - (begin_angle % (2 * pi)) > 1e-6:
        cut_lines = cut_lines[::-1]

    return cut_lines

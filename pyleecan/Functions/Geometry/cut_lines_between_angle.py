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
    # normalize angles according to numpy.angle range, i.e. (-pi, pi]
    begin_angle = angle(exp(1j * begin_angle))
    end_angle = angle(exp(1j * end_angle))

    # rotate list in case first/last line is in between begin and end angle
    # first copy list
    rotated_list = [line for line in line_list]
    # rotate until first line is before begin angle
    rotate = True
    ii = 0
    while rotate:
        ang = angle(rotated_list[0].get_begin())
        if (begin_angle <= end_angle) and (ang < begin_angle or ang > end_angle):
            rotate = False
        elif (
            end_angle < ang < begin_angle
        ):  # begin and end angle cross -pi, pi boundary
            rotate = False
        if rotate:
            rotated_list.append(rotated_list.pop(0))
        ii += 1
        if ii >= len(rotated_list):  # rotation failed
            rotate = False

    first_cut = list()
    cut_lines = list()
    # First cut
    for line in rotated_list:
        top_split_list, _ = line.split_line(0, exp(1j * begin_angle))
        first_cut.extend(top_split_list)
    # Second cut
    for line in first_cut:
        _, bot_split_list = line.split_line(0, exp(1j * end_angle))
        cut_lines.extend(bot_split_list)

    # plot_cut_line(line_list, begin_angle, end_angle, first_cut, cut_lines)

    # Check that lines are in the correct way
    if len(cut_lines) > 1:
        EPS = 1e-6
        c1 = abs(angle(cut_lines[0].get_begin() * exp(-1j * end_angle)))
        c2 = abs(angle(cut_lines[0].get_end() * exp(-1j * end_angle)))
        c3 = abs(angle(cut_lines[-1].get_begin() * exp(-1j * begin_angle)))
        c4 = abs(angle(cut_lines[-1].get_end() * exp(-1j * begin_angle)))
        if (c1 < EPS or c2 < EPS) and (c3 < EPS or c4 < EPS):
            cut_lines = cut_lines[::-1]

    return cut_lines


def plot_cut_line(line_list, begin_angle, end_angle, first_cut, cut_lines):
    """Plot the original lines and the cut lines
    Parameters
    ----------
    line_list : [Line]
        list of line to cut
    begin_angle : float
        Begin angle of the cut [rad]
    end_angle : float
        End angle of the cut [rad]

    """
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111)

    r = 0
    for line in line_list:
        z1 = line.get_begin()
        z2 = line.get_end()
        ax.plot([z1.real, z2.real], [z1.imag, z2.imag], color="gray")
        r = max(r, abs(z1), abs(z2))

    # plot cut lines
    z1 = r * exp(1j * begin_angle)
    z2 = r * exp(1j * end_angle)

    ax.plot([z1.real, -z1.real], [z1.imag, -z1.imag], color="r")
    ax.plot([z2.real, -z2.real], [z2.imag, -z2.imag], color="b")

    for line in first_cut:
        z1 = line.get_begin()
        z2 = line.get_end()
        ax.plot([z1.real, z2.real], [z1.imag, z2.imag], color="k")
        r = max(r, abs(z1), abs(z2))

    for line in cut_lines:
        z1 = line.get_begin()
        z2 = line.get_end()
        ax.plot([z1.real, z2.real], [z1.imag, z2.imag], color="k", marker=".")
        r = max(r, abs(z1), abs(z2))

    # axis to equal size
    ax.axis("equal")

    plt.show()

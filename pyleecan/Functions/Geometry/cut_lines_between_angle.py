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
    # normalize angles according to numpy.angle range
    begin_angle = angle(exp(1j * begin_angle))
    end_angle = angle(exp(1j * end_angle))
    mean_angle = angle(exp(1j * begin_angle) + exp(1j * end_angle))

    # rotate list in case first/last line is in between begin and end angle
    # first copy list
    sorted_list = [line for line in line_list]
    # rotate until first line is before begin angle
    

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
        ax.plot([z1.real, z2.real], [z1.imag, z2.imag], color='gray',label=f'split line')
        r = max(r, abs(z1), abs(z2))
    
    # plot cut lines
    z1 = r * exp(1j * begin_angle)
    z2 = r * exp(1j * end_angle)

    ax.plot([z1.real, -z1.real], [z1.imag, -z1.imag], color='r',label=f'cut')
    ax.plot([z2.real, -z2.real], [z2.imag, -z2.imag], color='b',label=f'cut')

    for line in first_cut:
        z1 = line.get_begin()
        z2 = line.get_end()
        ax.plot([z1.real, z2.real], [z1.imag, z2.imag], color='k',label=f'split line')
        r = max(r, abs(z1), abs(z2))

    for line in cut_lines:
        z1 = line.get_begin()
        z2 = line.get_end()
        ax.plot([z1.real, z2.real], [z1.imag, z2.imag], color='k',label=f'split line', marker='.')
        r = max(r, abs(z1), abs(z2))


    # plt.legend()
    #axis to equal size
    ax.axis('equal')

    plt.show()


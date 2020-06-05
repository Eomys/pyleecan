# -*- coding: utf-8 -*-

from random import choice

from ...Methods.Machine import PHASE_COLOR, PHASE_NAME


def gen_color(N):
    """Generate a list of phase color

    Parameters
    ----------
    N : int
        number of color to generate

    Returns
    -------
    Color_list: list
        A list of hexa representation of colors (str)

    """

    color_list = PHASE_COLOR
    if N < len(color_list):
        return color_list[:N]
    else:
        Hexa = [
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
        ]
        for ii in range(N - len(color_list)):
            color = "#"
            for i in range(6):
                color += choice(Hexa)
            color_list.append(color)
    return color_list


def gen_name(N, is_add_phase=False):
    """Generate a list of phase name

    Parameters
    ----------
    N : int
        number of name the generate
    is_add_phase : bool
        True to add "Phase " in the resulting names

    Returns
    -------
    Name_list: list
        A list of phase name

    """

    Alpha = PHASE_NAME

    Name_list = list()
    for i in range(N):
        if is_add_phase:
            name = "Phase "
        else:
            name = ""
        if i // 26 > 0:
            name += Alpha[(i // 26) - 1]
        name += Alpha[i % 26]
        Name_list.append(name)

    return Name_list

from numpy import sqrt, exp, angle

# Import for Plot debug
# import matplotlib.pyplot as plt
# from ...Functions.Load.import_class import import_class
# from ...definitions import config_dict
# PATCH_COLOR_ALPHA = config_dict["PLOT"]["COLOR_DICT"]["PATCH_COLOR_ALPHA"]


def inter_circle_circle(Zc1, R1, Zc2, R2):
    """INTER_CIRCLE_CIRCLE find the intersection between two circles
    defined by center and radius

    Parameters
    ----------
    Zc1 : complex
        Complex coordinate of the center of the first circle
    R1 : float
        Radius of the first circle
    Zc2 : complex
        Complex coordinate of the center of the second circle
    R2 : float
        Radius of the second circle

    Returns
    -------
    Zlist: list
        List of the complex coordinates of the intersection
    """

    D = abs(Zc1 - Zc2)

    # # Plot for debug
    # Circle = import_class("pyleecan.Classes", "Circle")
    # C1 = Circle(radius=R1, center=Zc1)
    # C2 = Circle(radius=R2, center=Zc2)
    # fig, ax = C1.plot(color=PATCH_COLOR_ALPHA, edgecolor="r")
    # C2.plot(fig=fig, ax=ax, color=PATCH_COLOR_ALPHA, edgecolor="b")
    # ax.plot(0, 0, "kx", zorder=0)
    # ax.plot(Zc1.real, Zc1.imag, "rx", zorder=0)
    # ax.plot(Zc2.real, Zc2.imag, "bx", zorder=0)
    # plt.show()

    # Set the coordinate system center Zc1, Zc2 on Ox+
    Zc1p = 0
    Zc2p = (Zc2 - Zc1) * exp(-1j * angle(Zc2 - Zc1))

    if D > R1 + R2:
        # The two circle are not big enought
        return []
    elif D == (R1 + R2):
        # Only one point between the two circles
        return [(Zc2p - R2) * exp(1j * angle(Zc2 - Zc1)) + Zc1]
    elif R2 > D + R1:
        # Particular cases First circle inside second circle
        return list()
    elif R1 > D + R2:
        # Particular cases Second circle inside first circle
        return list()
    elif R2 == D + R1:
        # Particular cases First circle inside second circle and one intersection
        return [(-R1) * exp(1j * angle(Zc2 - Zc1)) + Zc1]
    elif R1 == D + R2:
        # Particular cases First circle inside second circle and one intersection
        return [(Zc2p + R2) * exp(1j * angle(Zc2 - Zc1)) + Zc1]
    else:  # D < R1 and D < R2:
        # Intersection between the two circles
        # cf https://mathworld.wolfram.com/Circle-CircleIntersection.html
        x = (D ** 2 - R2 ** 2 + R1 ** 2) / (2 * D)
        y = sqrt(R1 ** 2 - x ** 2)
        Z1 = (x + 1j * y) * exp(1j * angle(Zc2 - Zc1)) + Zc1
        Z2 = (x - 1j * y) * exp(1j * angle(Zc2 - Zc1)) + Zc1
        return [Z1, Z2]

    # In fact two points formula seems to work in all other cases
    # elif R1 > D:
    #     # Intersections after Zc2p
    #     raise Exception("Not implemented yet")
    # elif R2 > D:
    #     # Intersections beforz Zc1p
    #     raise Exception("Not implemented yet")
    # else:
    #     raise Exception("Case should not happend")

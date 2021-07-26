# -*- coding: utf-8 -*-
from ....Classes.Circle import Circle
from ....Classes.Arc1 import Arc1
from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from numpy import exp, pi
from ....Functions.labels import (
    SHAFT_LAB,
    BOUNDARY_PROP_LAB,
    SHAFTSR_LAB,
    SHAFTSL_LAB,
    SHAFTR_LAB,
)


def build_geometry(self, sym=1, alpha=0, delta=0):
    """Build the geometry of the shaft

    Parameters
    ----------
    self : Shaft
        Shaft Object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the lamination

    """
    surf_list = list()

    if sym == 1:
        surf_list.append(
            Circle(radius=self.Drsh / 2, label=SHAFT_LAB, center=0, point_ref=0)
        )
    else:
        begin = self.Drsh / 2
        end = begin * exp(1j * 2 * pi / sym)
        surface = SurfLine(
            line_list=[
                Segment(0, begin, prop_dict={BOUNDARY_PROP_LAB: SHAFTSR_LAB}),
                Arc1(
                    begin, end, self.Drsh / 2, prop_dict={BOUNDARY_PROP_LAB: SHAFTR_LAB}
                ),
                Segment(end, 0, prop_dict={BOUNDARY_PROP_LAB: SHAFTSL_LAB}),
            ],
            label=SHAFT_LAB,
            point_ref=0,
        )

        surf_list.append(surface)
    for surf in surf_list:
        surf.rotate(alpha)
        surf.translate(delta)
    return surf_list

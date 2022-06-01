from ....Functions.Geometry.transform_hole_surf import transform_hole_surf
from ....Functions.labels import NOTCH_LAB, YSNR_LAB, YSNL_LAB

from ....Classes.Segment import Segment
from ....Classes.SurfLine import SurfLine
from ....Functions.labels import DRAW_PROP_LAB, BOUNDARY_PROP_LAB

from numpy import pi, exp


def get_notches_surf(self, sym):
    """Return the list of surfaces for notches

    Parameters
    ----------
    self : Lamination
        A Lamination object
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)

    Return
    ------
    surf_list : list
        list of surfaces needed for the notches
    """

    if self.notch is None:
        self.notch = list()

    # TODO Add yoke notches surfaces (issue with BC on yoke line)
    Rbo = self.get_Rbo()

    surf_list = list()
    notch_list = self.get_notch_list(sym=1, is_bore=True)
    for ii, notch in enumerate(notch_list):
        # Add closing Line
        Zbegin = notch["obj"][-1].get_end()
        Zend = notch["obj"][0].get_begin()
        notch["obj"].append(Segment(Zbegin, Zend))

        # create a surface
        surf = SurfLine(line_list=notch["obj"], label="Slot")
        surf.comp_point_ref(is_set=True)

        surf.label = self.get_label() + "_" + NOTCH_LAB + "_R" + str(ii) + "-T0-S0"
        surf_list.append(surf)

    # Label definition
    BC_prop_right = self.get_label() + "_" + YSNR_LAB
    BC_prop_left = self.get_label() + "_" + YSNL_LAB

    # split surfaces for symmetry if needed (code from transform_hole_surf.py)
    cut_list = list()
    for surf in surf_list:
        # Cut Ox axis
        top, _ = surf.split_line(
            0,
            1.2 * Rbo,
            is_join=True,
            prop_dict_join={BOUNDARY_PROP_LAB: BC_prop_right},
        )
        if top is not None and sym > 2:
            # Cut O-"sym angle" axis
            _, bot = top.split_line(
                0,
                1.2 * Rbo * exp(1j * 2 * pi / sym),
                is_join=True,
                prop_dict_join={BOUNDARY_PROP_LAB: BC_prop_left},
            )
            if bot is not None:
                cut_list.append(bot)
        elif top is not None:  # Half the machine => Only one cut required
            cut_list.append(top)
    surf_list = cut_list

    return surf_list

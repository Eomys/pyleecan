from ....Functions.Geometry.transform_hole_surf import transform_hole_surf
from ....Classes.NotchEvenDist import NotchEvenDist
from ....Functions.labels import NOTCH_LAB,YSNR_LAB, YSNL_LAB


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

    surf_list = list()
    for ii, notch in enumerate(self.notch):
        # Method used for symetry (for now) so only NotchEvenDist
        assert isinstance(notch, NotchEvenDist)
        # Get the original surface
        Nsurf = notch.notch_shape.get_surface()
        Nsurf.label = self.get_label() + "_" + NOTCH_LAB + "_R" + str(ii) + "-T0-S0"
        Nsurf.rotate(angle=notch.alpha)
        # Label definition
        BC_prop_right = self.get_label() +"_"+YSNR_LAB
        BC_prop_left = self.get_label() +"_"+YSNL_LAB
        # Generate all the surfaces
        surf_list.extend(
            transform_hole_surf(
                hole_surf_list=[Nsurf],
                Zh=notch.notch_shape.Zs,
                sym=sym,
                alpha=0,
                delta=0,
                is_split=True,
                BC_prop_right=BC_prop_right,
                BC_prop_left=BC_prop_left,
            )
        )

    return surf_list

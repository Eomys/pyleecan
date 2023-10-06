from ....Functions.Geometry.transform_hole_surf import transform_hole_surf
from ....Functions.labels import KEY_LAB, YSNR_LAB, YSNL_LAB

from numpy import pi, exp


def build_geometry_key(self, index=0, sym=1, alpha=0, delta=0):
    """Build the geometry of the keys inside the notch

    Parameters
    ----------
    self : NotchEvenDist
        The NotchEvenDist to build the key surfaces from
    index : int
        Index of the Notch in the list
    sym : int
        Symmetry factor (1= full machine, 2= half of the machine...)
    alpha : float
        Angle for rotation [rad]
    delta : complex
        Complex value for translation

    Returns
    -------
    surf_list : list
        list of surfaces needed to draw the keys

    """

    surf_list = list()

    # Get the original surface
    Nsurf = self.notch_shape.get_surface_active()
    Nsurf.label = self.get_label() + "_" + KEY_LAB + "_R" + str(index) + "-T0-S0"
    Nsurf.rotate(angle=self.alpha)
    # Label definition
    BC_prop_right = self.get_label() + "_" + YSNR_LAB
    BC_prop_left = self.get_label() + "_" + YSNL_LAB
    # Generate all the surfaces (handle cut on sym axis)
    surf_list.extend(
        transform_hole_surf(
            hole_surf_list=[Nsurf],
            Zh=self.notch_shape.Zs,
            sym=sym,
            alpha=0,
            delta=0,
            is_split=True,
            BC_prop_right=BC_prop_right,
            BC_prop_left=BC_prop_left,
        )
    )

    # apply the transformation
    for surf in surf_list:
        if alpha != 0:
            surf.rotate(alpha)
        if delta != 0:
            surf.translate(delta)

    return surf_list

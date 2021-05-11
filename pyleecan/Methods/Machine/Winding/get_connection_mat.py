from ....Functions.Winding.reverse_wind_mat import (
    reverse_wind_mat,
    reverse_layer,
    change_layer,
    permute_B_C,
)
from ....Functions.Winding.shift_wind_mat import shift_wind_mat


def get_connection_mat(self, Zs=None, p=None):
    """Get the Winding Matrix

    Parameters
    ----------
    self : Winding
        A: Winding object
    Zs : int
        Number of Slot (Integer >0)
    p : int
        Number of pole pairs (Integer >0)

    Returns
    -------
    wind_mat: numpy.ndarray
        Winding Matrix (1, 1, Zs, qs)


    """

    if self.wind_mat is None:
        self.wind_mat = self.comp_connection_mat(Zs=Zs, p=p)

    wind_mat = self.wind_mat.copy()
    # Apply the transformations
    if self.is_reverse_wind:
        wind_mat = reverse_wind_mat(wind_mat)
    if self.Nslot_shift_wind > 0:
        wind_mat = shift_wind_mat(wind_mat, self.Nslot_shift_wind)
    if self.is_reverse_layer:
        wind_mat = reverse_layer(wind_mat)
    if self.is_change_layer:
        wind_mat = change_layer(wind_mat)
    if self.is_permute_B_C:
        wind_mat = permute_B_C(wind_mat)
    return wind_mat

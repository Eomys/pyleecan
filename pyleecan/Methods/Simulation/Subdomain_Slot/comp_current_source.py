from numpy import kron, sin, pi, einsum, mean as np_mean


def comp_current_source(self, I_val, lam):
    """Method description

    Parameters
    ----------
    self: Subdomain_Slot
        a Subdomain_Slot object

    """

    wind_mat = lam.winding.comp_connection_mat()
    slot_surf = lam.slot.comp_surface()
    Nslot = self.number_per_a

    # If there are two layers in the stator slot
    if wind_mat.shape[1] == 2:
        # current density in left and right windings
        Ji_lr = einsum("ij, klmi -> lmj", I_val / slot_surf, wind_mat[:, :, :Nslot, :])
        # mean value of current density in each slot
        self.Ji = np_mean(Ji_lr, axis=0)
        # Jik is the amplitude of the spatial fourier series of the current density within the slot
        Jdiff = Ji_lr[0, ...] - Ji_lr[1, ...]
        self.Jik = kron(Jdiff.T, sin(self.k * pi / 2) / (self.k * pi / 2)).T
    else:
        # both parts are equal is there is a single winding in the slots
        self.Ji = einsum("ij, klmi -> mj", I_val / slot_surf, wind_mat[:, :, :Nslot, :])

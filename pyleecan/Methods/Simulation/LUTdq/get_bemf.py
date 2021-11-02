def get_bemf(self):
    """Get the phase to phase back electromotive force magnitude [V] from ELUT flux linkage data
    Parameters
    ----------
    self : LUTdq
        a LUTdq object

    Returns
    ----------
    bemf : ndarray
        (0,:) back emf waveform magnitude as a function of rotor position [V]
        (1,:) rotor position [rad]
    """

    # TODO

    # # calculating bemf from MLUT
    # Phi_dqh = self.Phi_dqh
    # I_dqh = self.I_dqh

    # # Phi0_dqh = Phi_dqh[I_dqh.index([0,0,0]),:]

    # return bemf

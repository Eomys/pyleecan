from numpy import sum as np_sum, zeros


def comp_joule_losses(self, group, freqs):
    """Calculate joule losses in stator windings

    Parameters
    ----------
    self: LossFEMM
        a LossFEMM object
    group: str
        Name of part in which to calculate joule losses
    freqs: ndarray
        frequency vector [Hz]

    Returns
    -------
    Pjoule : float
        Overall joule losses [W]
    Pjoule_density : ndarray
        Joule loss density function of frequency and elements [W/m3]
    """

    if self.parent.parent is None:
        raise Exception("Cannot calculate joule losses if simu is not in an Output")
    else:
        output = self.parent.parent

    if output.elec is None:
        raise Exception("Cannot calculate joule losses if OutElec is None")

    if self.is_get_meshsolution and output.mag is None:
        raise Exception("Cannot calculate joule losses if OutMag is None")

    machine = output.simu.machine

    OP = output.elec.OP

    felec = OP.get_felec()

    p = machine.get_pole_pair_number()

    if "stator" in group:
        lam = machine.stator
    else:
        lam = machine.rotor

    Rs = lam.comp_resistance_wind(T=self.Tsta)
    qs = lam.winding.qs
    Lst = lam.L1

    # Calculate overall joule losses
    Pjoule = qs * Rs * (OP.Id_ref ** 2 + OP.Iq_ref ** 2)

    if self.is_get_meshsolution:
        ms_group = output.mag.meshsolution.get_group(group)

        Se = ms_group.mesh[0].get_cell_area()

        # Constant component and twice the electrical frequency have same joule density values
        Pjoule_density = zeros((freqs.size, Se.size))
        amp = Pjoule / (2 * p * Lst * np_sum(Se))
        Pjoule_density[freqs == 0, :] = amp / 2
        Pjoule_density[freqs == 2 * felec, :] = amp / 2
    else:
        Pjoule_density = None

    return Pjoule, Pjoule_density

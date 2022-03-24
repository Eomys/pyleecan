from numpy import sum as np_sum, zeros, array


def comp_loss_density_joule(self, group, coeff_dict):
    """Calculate joule losses in stator windings

    Parameters
    ----------
    self: LossFEMM
        a LossFEMM object
    group: str
        Name of part in which to calculate joule losses
    coeff_dict: dict
        Dict containing coefficient A and B to calculate overall losses such as P = sum(A*f^2 + B*f) + C

    Returns
    -------
    Pjoule_density : ndarray
        Joule loss density function of frequency and elements [W/m3]
    freqs: ndarray
        frequency vector [Hz]
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

    if "stator" in group:
        lam = machine.stator
    else:
        lam = machine.rotor

    Rs = lam.comp_resistance_wind(T=self.Tsta)
    qs = lam.winding.qs

    # Calculate overall joule losses
    Pjoule = qs * Rs * (OP.Id_ref ** 2 + OP.Iq_ref ** 2)

    felec = OP.get_felec()
    per_a = output.geo.per_a
    if output.geo.is_antiper_a:
        per_a *= 2

    Lst = lam.L1

    # Get surface cells for windings
    ms = output.mag.meshsolution
    Se = ms.mesh[0].get_cell_area()[ms.group[group]]

    # Constant component and twice the electrical frequency have same joule density values
    freqs = array([felec])
    Pjoule_density = zeros((freqs.size, Se.size))
    Pjoule_density[0, :] = Pjoule / (per_a * Lst * np_sum(Se))

    # Store coefficient to get joule losses the same as for other losses
    coeff_dict[group + " joule"] = {"A": 0, "B": 0, "C": Pjoule}

    return Pjoule_density, freqs

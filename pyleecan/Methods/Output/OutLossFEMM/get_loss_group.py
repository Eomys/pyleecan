from numpy import sum as np_sum


def get_loss_group(self, group, freqs):
    """Get loss power for given group from coefficients stored in coeff dict

    Parameter
    ---------
    self : OutLossFEMM
        an OutLossFEMM object
    group: str
        Name of part for which to calculate loss function
    freqs: ndarray
        frequency vector [Hz]

    Return
    ------
    Ploss : float
        loss power for given group [W]
    Ploss_density: None
        loss density cannot be calculated, only for compatibility

    """

    if group in self.coeff_dict:
        coeff_dict = self.coeff_dict[group]
    else:
        raise Exception("Cannot calculate loss function for group=" + group)

    Ploss = np_sum(coeff_dict["A"] * freqs + coeff_dict["B"] * freqs ** 2)

    return Ploss, None

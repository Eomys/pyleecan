def get_loss_group(self, group, felec):
    """Get loss power for given group from coefficients stored in coeff dict

    Parameter
    ---------
    self : OutLossFEMM
        an OutLossFEMM object
    group: str
        Name of part for which to calculate loss function

    Return
    ------
    Ploss : float
        loss power for given group [W]

    """

    if group in self.coeff_dict:
        coeff_dict = self.coeff_dict[group]
        Ploss = coeff_dict["A"] * felec ** 2 + coeff_dict["B"] * felec + coeff_dict["C"]
    else:
        Ploss = 0

    return Ploss

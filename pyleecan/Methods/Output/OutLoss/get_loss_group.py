def get_loss_group(self, group, felec):
    """Get loss power for given group from coefficients stored in coeff dict

    Parameters
    ----------
    self : OutLoss
        an OutLoss object
    group: str
        Name of part for which to calculate loss function

    Returns
    -------
    Ploss : float
        loss power for given group [W]

    """

    if group in self.coeff_dict:
        coeff_dict = self.coeff_dict[group]
        Ploss = (
            coeff_dict["A"] * felec ** coeff_dict["a"]
            + coeff_dict["B"] * felec ** coeff_dict["b"]
            + coeff_dict["C"] * felec ** coeff_dict["c"]
        )
    else:
        Ploss = 0

    return Ploss

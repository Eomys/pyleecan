def get_loss_group(self, group, felec):
    """Get loss power for given group from coefficients stored in coeff dict

    Parameter
    ---------
    self : OutLoss
        an OutLoss object
    group: str
        Name of part for which to calculate loss function

    Return
    ------
    Ploss : float
        loss power for given group [W]

    """
    coeff_dict = self.loss_dict[group]["coefficients"]
    Ploss = (
        coeff_dict["A"] * felec ** coeff_dict["a"]
        + coeff_dict["B"] * felec ** coeff_dict["b"]
        + coeff_dict["C"] * felec ** coeff_dict["c"]
    )
    
    return Ploss

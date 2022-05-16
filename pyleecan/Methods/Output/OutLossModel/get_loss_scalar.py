def get_loss_scalar(self, felec):
    """Get loss power from coefficients stored in coeff_dict

    Parameter
    ---------
    self : OutLossModel
        an OutLossModel object
    felec : float
        the electrical frequency
    Return
    ------
    Ploss : float
        loss power for the specified frequency [W]

    """
    
    if self.coeff_dict is None:
        if self.scalar_value is None:
            return None
        else:
            return self.scalar_value
    else:
        Ploss = 0
        for key, value in self.coeff_dict.items():
            Ploss += value * felec ** key
    return Ploss

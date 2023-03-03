def get_loss_scalar(self, felec=None):
    """Get loss power from coefficients stored in coeff_dict

    Parameters
    ----------
    self : OutLossModel
        an OutLossModel object
    felec : float
        the electrical frequency [Hz]

    Returns
    -------
    Ploss : float
        loss power for the specified frequency [W]
    """

    if self.coeff_dict is None:
        return self.scalar_value  # Can be None
    else:
        if felec is None:
            output = self.parent.parent
            felec = output.elec.OP.felec
        Ploss = 0
        for key, value in self.coeff_dict.items():
            Ploss += value * felec ** float(key)
        self.scalar_value = Ploss
    return self.scalar_value

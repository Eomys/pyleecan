def get_loss_overall(self):
    """Get overall loss by summing all losses in OutLoss

    Parameters
    ----------
    self : OutLoss
        an OutLoss object

    Returns
    -------
    loss : float
        overall loss [W]

    """

    loss = 0

    if self.Pstator is not None:
        loss += self.Pstator
    if self.Protor is not None:
        loss += self.Protor
    if self.Pprox is not None:
        loss += self.Pprox
    if self.Pmagnet is not None:
        loss += self.Pmagnet
    if self.Pjoule is not None:
        loss += self.Pjoule

    return loss

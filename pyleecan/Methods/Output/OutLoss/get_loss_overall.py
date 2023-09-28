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

    overall_loss = 0

    for loss in self.loss_dict.values():
        if loss.scalar_value is not None:
            overall_loss += loss.scalar_value

    return overall_loss

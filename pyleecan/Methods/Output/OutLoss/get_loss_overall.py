def get_loss_overall(self):
    """Get overall loss by summing all losses in OutLoss

    Parameter
    ---------
    self : OutLoss
        an OutLoss object

    Return
    ------
    loss : float
        overall loss [W]

    """

    overall_loss = 0

    for loss in self.loss_dict.values():
        if "scalar_value" in loss:
            overall_loss += loss["scalar_value"]

    self.loss_dict["overall"]["scalar_value"] = overall_loss

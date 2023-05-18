def get_power_dict(self):
    """Return a dictionnary with all the scalar losses

    Parameters
    ----------
    self : OutLoss
        An OutLoss object

    Returns
    -------
    power_dict : {float}
        Dictionnary of all the scalar losses
    """

    if self.parent is None:
        raise Exception("Error: OutLoss is not in Output object")
    out = self.parent
    if out.elec is None or out.elec.OP is None:
        raise Exception("Error: OP is not set")

    power_dict = dict(
        [
            (o.name, o.get_loss_scalar(out.elec.OP.felec))
            for o in self.loss_dict.values()
        ]
    )

    if out.mag is not None and out.mag.Pem_av is not None:
        power_dict["total_power"] = out.mag.Pem_av

    return power_dict

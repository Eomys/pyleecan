def comp_losses(self, output, freqs):
    """Calculate losses in electrical machine assuming power density is calculated as described given
    by (cf. https://www.femm.info/wiki/SPMLoss)

    Parameters
    ----------
    self: LossFEMM
        a LossFEMM object
    output: Output
        an Output object
    freqs: ndarray
        frequency vector [Hz]

    Returns
    -------
    out_dict : dict
        Dict of output loss and loss density
    """

    coeff_dict = output.loss.coeff_dict

    machine = output.simu.machine

    # Comp stator core losses
    group = "stator core"
    if group in coeff_dict and not self.is_get_meshsolution:
        # Use coefficients stored in OutLoss
        Pstator, Pstator_density = output.loss.get_loss_group(freqs)
    else:
        Pstator, Pstator_density = self.comp_core_losses(
            group, freqs, Ce=self.Ce, Ch=self.Ch
        )

    # Comp rotor core losses
    group = "rotor core"
    if group in coeff_dict and not self.is_get_meshsolution:
        # Use coefficients stored in OutLoss
        Protor, Protor_density = output.loss.get_loss_group(freqs)
    else:
        Protor, Protor_density = self.comp_core_losses(
            group, freqs, Ce=self.Ce, Ch=self.Ch
        )

    # Compute Joule losses in stator windings
    group = "stator winding"
    Pjoule, Pjoule_density = self.comp_joule_losses(group, freqs)

    # Comp proximity losses in stator windings (same expression as core losses with Ce=C)
    if group in coeff_dict and not self.is_get_meshsolution:
        # Use coefficients stored in OutLoss
        Pprox, Pprox_density = output.loss.get_loss_group(freqs)
    else:
        Pprox, Pprox_density = self.comp_core_losses(group, freqs, Ce=self.Cp, Ch=0)

    if machine.is_synchronous() and machine.rotor.has_magnet():
        # Comp eddy current losses in rotor magnets
        group = "rotor magnets"
        if group in coeff_dict and not self.is_get_meshsolution:
            # Use coefficients stored in OutLoss
            Pmagnet, Pmagnet_density = output.loss.get_loss_group(freqs)
        else:
            Pmagnet, Pmagnet_density = self.comp_magnet_losses(group, freqs)
    else:
        Pmagnet, Pmagnet_density = None, None

    # Init dict of outputs
    out_dict = dict()

    # Store scalar losses
    out_dict["Pstator"] = Pstator
    out_dict["Protor"] = Protor
    out_dict["Pjoule"] = Pjoule
    out_dict["Pprox"] = Pprox
    out_dict["Pmagnet"] = Pmagnet

    # Store loss density values
    if self.is_get_meshsolution:
        if Pstator_density is not None:
            out_dict["Pstator_density"] = Pstator_density
        if Protor_density is not None:
            out_dict["Protor_density"] = Protor_density
        if Pjoule_density is not None:
            out_dict["Pjoule_density"] = Pjoule_density
        if Pprox_density is not None:
            out_dict["Pprox_density"] = Pprox_density
        if Pmagnet_density is not None:
            out_dict["Pmagnet_density"] = Pmagnet_density

    return out_dict

from numpy import zeros, argmin, abs as np_abs, array


def comp_losses(self, output, axes_dict):
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
        Pstator, Pstator_density = output.loss.get_loss_group(group)
    else:
        Pstator, Pstator_density, fstator = self.comp_core_losses(
            group, Ce=self.Ce, Ch=self.Ch
        )

    # Comp rotor core losses
    group = "rotor core"
    if group in coeff_dict and not self.is_get_meshsolution:
        # Use coefficients stored in OutLoss
        Protor, Protor_density = output.loss.get_loss_group(group)
    else:
        Protor, Protor_density, frotor = self.comp_core_losses(
            group, Ce=self.Ce, Ch=self.Ch
        )

    # Compute Joule losses in stator windings
    group = "stator winding"
    Pjoule, Pjoule_density, fjoule = self.comp_joule_losses(group)

    # Comp proximity losses in stator windings (same expression as core losses with Ce=C)
    if group in coeff_dict and not self.is_get_meshsolution:
        # Use coefficients stored in OutLoss
        Pprox, Pprox_density = output.loss.get_loss_group(group)
    else:
        Pprox, Pprox_density, fprox = self.comp_core_losses(group, Ce=self.Cp, Ch=0)

    if machine.is_synchronous() and machine.rotor.has_magnet():
        # Comp eddy current losses in rotor magnets
        group = "rotor magnets"
        if group in coeff_dict and not self.is_get_meshsolution:
            # Use coefficients stored in OutLoss
            Pmagnet, Pmagnet_density = output.loss.get_loss_group(group)
        else:
            Pmagnet, Pmagnet_density, fmagnet = self.comp_magnet_losses(group)
    else:
        Pmagnet, Pmagnet_density, fmagnet = None, None, None

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

        meshsol = output.mag.meshsolution
        group = meshsol.group
        freqs = axes_dict["freqs"].get_values()
        Nelem = meshsol.mesh[0].cell["triangle"].nb_cell

        loss_density = zeros((freqs.size, Nelem))

        if Pstator_density is not None:
            If = argmin(np_abs(freqs[:, None] - fstator[None, :]), axis=0)[:, None]
            Ie = array(group["stator core"])[None, :]
            loss_density[If, Ie] += Pstator_density
        if Protor_density is not None:
            If = argmin(np_abs(freqs[:, None] - frotor[None, :]), axis=0)[:, None]
            Ie = array(group["rotor core"])[None, :]
            loss_density[If, Ie] += Protor_density
        if Pjoule_density is not None:
            If = argmin(np_abs(freqs[:, None] - fjoule[None, :]), axis=0)[:, None]
            Ie = array(group["stator winding"])[None, :]
            loss_density[If, Ie] += Pjoule_density
        if Pprox_density is not None:
            If = argmin(np_abs(freqs[:, None] - fprox[None, :]), axis=0)[:, None]
            Ie = array(group["stator winding"])[None, :]
            loss_density[If, Ie] += Pprox_density
        if Pmagnet_density is not None:
            If = argmin(np_abs(freqs[:, None] - fmagnet[None, :]), axis=0)[:, None]
            Ie = array(group["rotor magnets"])[None, :]
            loss_density[If, Ie] += Pmagnet_density

        out_dict["loss_density"] = loss_density

    return out_dict

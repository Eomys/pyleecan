from numpy import zeros, argmin, abs as np_abs, array
from pyleecan.Functions.load import load


def comp_loss(self, output, axes_dict):
    """Computing the losses in electrical machines

    Parameters
    ----------
    output : Output
        an Output object with magnetic quantities previously computed
    axes_dict : {axes}
        A dict of axes

    Returns
    -------
    out_dict : dict
        Dict of output loss and loss density
    """

    machine = output.simu.machine

    coeff_dict = dict()

    loss_model = self.model_dict["stator core"]
    if None in [
        loss_model.k_hy,
        loss_model.k_ed,
        loss_model.alpha_f,
        loss_model.alpha_B,
    ]:
        material = machine.stator.mat_type
        loss_model.comp_coeff(material)

    loss_model = self.model_dict["rotor core"]
    if None in [
        loss_model.k_hy,
        loss_model.k_ed,
        loss_model.alpha_f,
        loss_model.alpha_B,
    ]:
        material = machine.rotor.mat_type
        loss_model.comp_coeff(material)

    # Comp stator core losses
    if "stator core" in self.model_dict:
        # Comp stator core losses
        Pstator_density, fstator = self.comp_loss_density_core(
            "stator core", coeff_dict=coeff_dict
        )
    else:
        Pstator_density, fstator = None, None

    if "rotor core" in self.model_dict:
        # Comp rotor core losses
        Protor_density, frotor = self.comp_loss_density_core(
            "rotor core", coeff_dict=coeff_dict
        )
    else:
        Protor_density, frotor = None, None

    if self.Cp > 0:
        # Comp proximity losses in stator windings (same expression as core losses with Ce=C)
        Pprox_density, fprox = self.comp_loss_density_core(
            "stator winding", coeff_dict=coeff_dict
        )
    else:
        Pprox_density, fprox = None, None

    if machine.is_synchronous() and machine.rotor.has_magnet():
        # Comp eddy current losses in rotor magnets
        Pmagnet_density, fmagnet = self.comp_loss_density_magnet(
            "rotor magnets", coeff_dict=coeff_dict
        )
    else:
        Pmagnet_density, fmagnet = None, None

    # Init dict of outputs
    out_dict = {"coeff_dict": coeff_dict}

    # Store loss density values
    if self.is_get_meshsolution:

        # Compute Joule losses in stator windings
        Pjoule_density, fjoule = self.comp_loss_density_joule("stator winding")

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

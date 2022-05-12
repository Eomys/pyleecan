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

    out_dict = dict()

    if self.is_get_meshsolution:
        meshsol = output.mag.meshsolution
        group = meshsol.group
        freqs = axes_dict["freqs"].get_values()
        Nelem = meshsol.mesh[0].cell["triangle"].nb_cell

        loss_density = zeros((freqs.size, Nelem))

    for key, model in self.model_dict.items():
        P_density, f = model.comp_loss()
        out_dict[key] = {
            "loss_density": P_density,
            "frequency": f,
            "coefficients": model.coeff_dict,
        }
        if self.is_get_meshsolution:
            If = argmin(np_abs(freqs[:, None] - f[None, :]), axis=0)[:, None]
            Ie = array(group[model.group])[None, :]
            temp_loss_density = zeros((freqs.size, Nelem))
            temp_loss_density[If, Ie] += P_density
            loss_density += temp_loss_density
            out_dict[key]["global_loss_density"] = temp_loss_density
    out_dict["overall"] = {"global_loss_density": loss_density}

    # # Comp stator core losses
    # if "stator core" in self.model_dict:
    #     # Comp stator core losses
    #     Pstator_density, fstator = self.model_dict["stator core"].comp_loss(
    #         "stator core"
    #     )
    # else:
    #     Pstator_density, fstator = None, None

    # if "rotor core" in self.model_dict:
    #     # Comp rotor core losses
    #     Protor_density, frotor = self.model_dict["rotor core"].comp_loss(
    #         "rotor core"
    #     )
    # else:
    #     Protor_density, frotor = None, None

    # if "proximity" in self.model_dict:
    #     Pprox_density, fprox = self.model_dict["proximity"].comp_loss(
    #         "stator winding"
    #     )
    # else:
    #     Pprox_density, fprox = None, None

    # if machine.is_synchronous() and machine.rotor.has_magnet():
    #     Pmagnet_density, fmagnet = self.model_dict["magnets"].comp_loss(
    #         "rotor magnets"
    #     )
    # else:
    #     Pmagnet_density, fmagnet = None, None

    # Store loss density values
    if False:  # self.is_get_meshsolution:

        # Compute Joule losses in stator windings
        Pjoule_density, fjoule = self.model_dict["Joule"].comp_loss("stator winding")

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

import numpy as np

from ....Classes.OutLossModel import OutLossModel


def comp_all_losses(
    self,
    axes_dict=None,
):
    """Compute all the losses models set in model_dict

    Parameters
    ----------
    self : Loss
        A Loss object
    axes_dict : dict
        Dict containing axes for loss calculation
    """

    output = self.parent.parent
    out_loss = output.loss
    # Store dict of axes
    if axes_dict is not None:
        out_loss.axes_dict = axes_dict

    meshsol = output.mag.meshsolution
    group = meshsol.group
    freqs = axes_dict["freqs"].get_values()
    Nelem = meshsol.mesh.element_dict["triangle"].nb_element

    out_loss.loss_dict = dict()
    for key, model in self.model_dict.items():
        # Compute losses for each model
        P_density, f_array = model.comp_loss()
        if self.is_get_meshsolution:
            loss_density = np.zeros((freqs.size, Nelem))
            If = np.argmin(np.abs(freqs[:, None] - f_array[None, :]), axis=0)[:, None]
            Ie = np.array(group[model.group])[None, :]
            loss_density[If, Ie] += P_density
        else:
            loss_density = None
        # Store results of each model in a different object
        out_loss_model = OutLossModel(
            name=key,
            loss_density=loss_density,
            scalar_value=None,
            coeff_dict=model.coeff_dict,
            group=model.group,
            loss_model=type(model).__name__,
        )
        out_loss.loss_dict[key] = out_loss_model

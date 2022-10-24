import numpy as np

from SciDataTool import DataFreq

from ....Classes.SolutionData import SolutionData
from ....Classes.MeshSolution import MeshSolution
from pyleecan.Classes.OutLossModel import OutLossModel

from ....Functions.Electrical.comp_loss_joule import comp_loss_joule


def store(
    self,
    model_dict,
    axes_dict=None,
    is_get_meshsolution=True,
):
    """Store the outputs of LossFEMM model that are temporarily in out_dict

    Parameters
    ----------
    self : OutLoss
        the OutLoss object to update
    model_dict : {LossModel}
        Dict containing all the losses models to compute
    axes_dict : dict
        Dict containing axes for loss calculation
    is_get_meshsolution: bool
        True to store meshsolution of each loss model
    """

    # Store dict of axes
    if axes_dict is not None:
        self.axes_dict = axes_dict

    meshsol = self.parent.mag.meshsolution
    group = meshsol.group
    freqs = axes_dict["freqs"].get_values()
    Nelem = meshsol.mesh[0].cell["triangle"].nb_cell

    for key, model in model_dict.items():
        # Compute losses for each model
        P_density, f_array = model.comp_loss()
        if is_get_meshsolution:
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
            coeff_dict=model.coeff_dict,
            group=model.group,
            loss_model=type(model).__name__,
        )
        self.loss_list.append(out_loss_model)

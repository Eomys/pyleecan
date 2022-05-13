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
    is_get_meshsolution=False,
    lam=None,
    OP=None,
    Tsta=20,
    Pem=None,
):
    """Store the outputs of LossFEMM model that are temporarily in out_dict

    Parameters
    ----------
    self : OutLoss
        the OutLoss object to update
    out_dict : dict
        Dict containing all losses quantities that have been calculated in comp_losses
    axes_dict : dict
        Dict containing axes for loss calculation
    is_get_meshsolution: bool
        True to store meshsolution of loss density
    """

    # Store dict of axes
    if axes_dict is not None:
        self.axes_dict = axes_dict

    if lam is None:
        lam = self.parent.simu.machine.stator

    if OP is None:
        OP = self.parent.elec.OP

    if Pem is None:
        Pem = self.parent.mag.Pem_av

    felec = OP.get_felec(p=lam.get_pole_pair_number())

    meshsol = self.parent.mag.meshsolution
    group = meshsol.group
    freqs = axes_dict["freqs"].get_values()
    Nelem = meshsol.mesh[0].cell["triangle"].nb_cell
    loss_density = np.zeros((freqs.size, Nelem))

    for key, model in model_dict.items():
        P_density, f_array = model.comp_loss()
        out_loss_model = OutLossModel(
            name=key,
            loss_density=P_density,
            coeff_dict=model.coeff_dict,
            freqs=f_array,
            group=model.group,
            f = felec
        )
        out_loss_model.scalar_value = out_loss_model.get_loss_scalar(felec)
        self.loss_list.append(out_loss_model)

        temp_loss_density = np.zeros((freqs.size, Nelem))
        If = np.argmin(np.abs(freqs[:, None] - f_array[None, :]), axis=0)[:, None]
        Ie = np.array(group[model.group])[None, :]
        temp_loss_density[If, Ie] += P_density
        loss_density += temp_loss_density
    self.loss_list.append(
        OutLossModel(name="overall",
                     loss_density=loss_density,
                     f=felec,
                     freqs=freqs
                     )
    )

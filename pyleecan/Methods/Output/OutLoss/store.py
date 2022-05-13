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


    for key, model in model_dict.items():
        P_density, f = model.comp_loss()
        out_loss_model=OutLossModel(
            name=key,
            loss_density=P_density,
            coeff_dict=model.coeff_dict,
            frequency=f,
            group=model.group,
        )
        out_loss_model.scalar_value = out_loss_model.get_loss_scalar(felec)
        self.loss_list.append(out_loss_model)

        if False:  # is_get_meshsolution:

            ms_mag = self.parent.mag.meshsolution

            Loss_density_df = DataFreq(
                name=f"{key} Loss density",
                unit="W/m3",
                symbol="L",
                values=self.loss_dict[key]["global_loss_density"],
                is_real=True,
                axes=[axes_dict["freqs"], axes_dict["indice"]],
            )

            Loss_density_sd = SolutionData(
                label=Loss_density_df.name,
                field=Loss_density_df,
                unit=Loss_density_df.unit,
            )

            ms_loss = MeshSolution(
                label=Loss_density_sd.label,
                group=ms_mag.group,
                is_same_mesh=True,
                mesh=ms_mag.mesh,
                solution=[Loss_density_sd],
                dimension=2,
            )

            self.meshsol_dict[key] = ms_loss

    self.get_loss_overall()

    # Store loss density as meshsolution

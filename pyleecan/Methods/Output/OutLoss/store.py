from SciDataTool import DataFreq

from ....Classes.SolutionData import SolutionData
from ....Classes.MeshSolution import MeshSolution

from ....Functions.Electrical.comp_loss_joule import comp_loss_joule


def store(
    self,
    out_dict,
    axes_dict=None,
    is_get_meshsolution=False,
    lam=None,
    OP=None,
    type_skin_effect=1,
    Tsta=20,
    Pem=None
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

    self.loss_dict = out_dict

    # Store coeff_dict
    if "coeff_dict" in out_dict:
        self.coeff_dict = out_dict.pop("coeff_dict")

    if lam is None:
        lam = self.parent.simu.machine.stator

    if OP is None:
        OP = self.parent.elec.OP
    
    if Pem is None:
        Pem=self.parent.mag.Pem_av

    felec = OP.get_felec(p=lam.get_pole_pair_number())

    for key in out_dict.keys():
        # if key == "Joule":
        #     self.loss_dict[key]["scalar_value"] = comp_loss_joule(lam, Tsta, OP, type_skin_effect)
        if key != "overall":
            self.loss_dict[key]["scalar_value"] = self.get_loss_group(key, felec)

    self.get_loss_overall()

    # Store loss density as meshsolution
    if False:  # is_get_meshsolution:

        ms_mag = self.parent.mag.meshsolution

        Loss_density_df = DataFreq(
            name="Loss density",
            unit="W/m3",
            symbol="L",
            values=out_dict["loss_density"],
            is_real=True,
            axes=[axes_dict["freqs"], axes_dict["indice"]],
        )

        Loss_density_sd = SolutionData(
            label=Loss_density_df.name, field=Loss_density_df, unit=Loss_density_df.unit
        )

        ms_loss = MeshSolution(
            label=Loss_density_sd.label,
            group=ms_mag.group,
            is_same_mesh=True,
            mesh=ms_mag.mesh,
            solution=[Loss_density_sd],
            dimension=2,
        )

        self.meshsol_list = [ms_loss]

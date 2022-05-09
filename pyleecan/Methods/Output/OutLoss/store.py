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

    # Store coeff_dict
    if "coeff_dict" in out_dict:
        self.coeff_dict = out_dict.pop("coeff_dict")

    if lam is None:
        lam = self.parent.simu.machine.stator

    if OP is None:
        OP = self.parent.elec.OP

    felec = OP.get_felec(p=lam.get_pole_pair_number())

    # Calculate and store scalar losses
    self.Pstator = self.get_loss_group("stator core", felec)
    self.Protor = self.get_loss_group("rotor core", felec)
    self.Pprox = self.get_loss_group("stator winding", felec)
    self.Pmagnet = self.get_loss_group("rotor magnets", felec)
    self.Pjoule = comp_loss_joule(lam, Tsta, OP, type_skin_effect)

    # Store loss density as meshsolution
    if False:# is_get_meshsolution:

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

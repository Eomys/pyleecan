from SciDataTool import DataFreq

from ....Classes.SolutionData import SolutionData
from ....Classes.MeshSolution import MeshSolution


def store(self, out_dict, axes_dict=None, is_get_meshsolution=False, felec=None):
    """Store the outputs of LossFEMM model that are temporarily in out_dict

    Parameters
    ----------
    self : OutLossFEMM
        the OutLossFEMM object to update
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

    if felec is None:
        felec = self.parent.elec.OP.get_felec()

    # Calculate and store scalar losses
    self.Pstator = self.get_loss_group("stator core", felec)
    self.Protor = self.get_loss_group("rotor core", felec)
    self.Pprox = self.get_loss_group("stator winding", felec)
    self.Pmagnet = self.get_loss_group("rotor magnets", felec)
    self.Pjoule = self.get_loss_group("stator winding joule", felec)

    # Store loss density as meshsolution
    if is_get_meshsolution:

        meshsol = self.parent.mag.meshsolution

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

        self.meshsolution = MeshSolution(
            label=Loss_density_sd.label,
            group=meshsol.group,
            is_same_mesh=True,
            mesh=meshsol.mesh,
            solution=[Loss_density_sd],
            dimension=2,
        )

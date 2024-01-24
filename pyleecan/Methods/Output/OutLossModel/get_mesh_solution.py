import numpy as np
from SciDataTool import DataFreq

from ....Classes.MeshSolution import MeshSolution
from ....Classes.SolutionData import SolutionData


def get_mesh_solution(self):
    """Returns the MeshSolution object corresponding to the losses

    Parameters
    ----------
    self : OutLossModel
        Result of a Loss model computation

    Returns
    -------
    MS : MeshSolution
        Losses as fct(freq) on the machine mesh
    """
    output = self.parent.parent
    # group = meshsol.group
    axes_dict = self.parent.axes_dict
    # freqs = axes_dict["freqs"].get_values()
    # Nelem = meshsol.mesh.element["triangle"].nb_element

    # If = np.argmin(np.abs(freqs[:, None] - self.freqs[None, :]), axis=0)[:, None]
    # Ie = np.array(group[self.group])[None, :]
    # global_loss_density = np.zeros((freqs.size, Nelem))
    # global_loss_density[If, Ie] += self.loss_density

    ms_mag = output.mag.meshsolution

    Loss_density_df = DataFreq(
        name=f"{self.name} loss density",
        unit="W/m3",
        symbol="L",
        values=self.loss_density,
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
        mesh=ms_mag.mesh,
        solution_dict={Loss_density_sd.label: Loss_density_sd},
        dimension=2,
    )

    return ms_loss

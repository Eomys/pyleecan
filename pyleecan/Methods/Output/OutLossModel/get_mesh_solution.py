import numpy as np

from SciDataTool import DataFreq
from ....Classes.SolutionData import SolutionData
from ....Classes.MeshSolution import MeshSolution


def get_mesh_solution(self):
    output = self.parent.parent
    meshsol = output.mag.meshsolution
    group = meshsol.group
    axes_dict = self.parent.axes_dict
    freqs = axes_dict["freqs"].get_values()
    Nelem = meshsol.mesh[0].cell["triangle"].nb_cell

    If = np.argmin(np.abs(freqs[:, None] - self.frequency[None, :]), axis=0)[:, None]
    Ie = np.array(group[self.group])[None, :]
    global_loss_density = np.zeros((freqs.size, Nelem))
    global_loss_density[If, Ie] += self.loss_density

    ms_mag = output.mag.meshsolution

    Loss_density_df = DataFreq(
        name=f"{self.name} Loss density",
        unit="W/m3",
        symbol="L",
        values=global_loss_density,
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

    return ms_loss

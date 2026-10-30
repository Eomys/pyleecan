import numpy as np

from ....Functions.labels import ROTOR_LAB, STATOR_LAB
from ....Functions.MeshSolution.build_meshsolution import build_meshsolution
from ....Functions.MeshSolution.build_solution_data import build_solution_data


def get_meshsolution(self):
    """Get loss density meshsolution

    Parameters
    ----------
    self : OutLoss
        an OutLoss object

    Returns
    -------
    ms_loss : MeshSolution
        Losses as function of time on the machine mesh

    """

    if self.meshsolution is None:
        # Get magnetic output
        outmag = self.parent.mag

        if outmag.meshsolution is None:
            # Get magnetic meshsolutions from Magnetic output
            meshsol_S = outmag.meshsolution_dict[STATOR_LAB + "-0"]
            meshsol_R = outmag.meshsolution_dict[ROTOR_LAB + "-0"]
            mesh = meshsol_S.mesh

            # Merge stator and rotor groups
            group = dict()
            group = {"airgap": list(meshsol_S.group["airgap_S"])}
            group["airgap"].extend(list(meshsol_R.group["airgap_R"]))
            for key, val in meshsol_S.group.items():
                if "airgap" not in key:
                    group[key] = list(val)
            for key, val in meshsol_R.group.items():
                if "airgap" not in key:
                    group[key] = list(val)

        else:
            meshsol = outmag.meshsolution
            mesh = meshsol.mesh
            group = meshsol.group

        # Get axes
        Ndim1 = list(self.loss_dict.values())[0].loss_density.shape[0]
        Indice_Element = self.axes_dict["indice_element"]
        Nelem = Indice_Element.get_length()
        if list(self.loss_dict.values())[0].loss_density.shape[0] == 1:
            axis_list = [self.axes_dict["freqs"].copy(), Indice_Element.copy()]
        else:
            axis_list = [self.axes_dict["time"].copy(), Indice_Element.copy()]

        # Get loss density values stored in OutLossModelTime objects
        loss_density = np.ndarray((Ndim1, Nelem), dtype=float)
        for outloss in self.loss_dict.values():
            Igrp = group[outloss.group]
            loss_density[:, Igrp] += outloss.loss_density

        # Build SolutionData
        solution_data = build_solution_data(
            field=loss_density,
            axis_list=axis_list,
            name="Loss density",
            symbol="L",
            unit="W/m3",
            type_element="triangle",
        )

        # Build meshsolution
        self.meshsolution = build_meshsolution(
            solution_dict={solution_data.label: solution_data},
            label=solution_data.label,
            mesh=mesh,
            group=group,
        )

    return self.meshsolution

from numpy import zeros

from SciDataTool import DataFreq

from ....Classes.SolutionData import SolutionData
from ....Classes.MeshSolution import MeshSolution
from ....Classes.OutLossFEMM import OutLossFEMM

from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the LossFEMM module"""
    if self.parent is None:
        raise InputError("The Loss object must be in a Simulation object to run")
    if self.parent.parent is None:
        raise InputError("The Loss object must be in an Output object to run")

    self.get_logger().info("Running LossFEMM module")

    # get output
    output = self.parent.parent

    machine = output.simu.machine

    L1 = machine.stator.L1
    L2 = machine.rotor.L1
    Lmag = machine.rotor.magnet.Lmag
    p = machine.get_pole_pair_number()
    Rs = machine.stator.comp_resistance_wind()
    sigma_m = 1 / machine.rotor.magnet.mat_type.elec.rho  # conductivity in S/m

    OP = output.elec.OP

    axes_dict = self.comp_axes(output)

    output.loss = OutLossFEMM()

    fft_dict = output.loss.get_fft_dict()
    surf_dict = output.loss.get_surf_dict()

    freqs = axes_dict["freqs"].get_values()

    # Comp stator core losses
    grp = "stator core"
    Pstator, Pstator_density = self.comp_core_losses(
        fft_dict["B " + grp], freqs, surf_dict[grp], L1, p, Ce=self.Ce, Ch=self.Ch
    )

    # Comp rotor core losses
    grp = "rotor core"
    Protor, Protor_density = self.comp_core_losses(
        fft_dict["B " + grp], freqs, surf_dict[grp], L2, p, Ce=self.Ce, Ch=self.Ch
    )

    # Comp proximity losses in stator windings
    grp = "stator winding"
    Pprox, Pprox_density = self.comp_core_losses(
        fft_dict["B " + grp], freqs, surf_dict[grp], L2, p, Ce=self.Cp, Ch=0
    )

    # Comp eddy current losses in rotor magnets
    grp = "rotor magnets"
    Pmagnet, Pmagnet_density = self.comp_magnet_losses(
        fft_dict["A_z " + grp], freqs, surf_dict[grp], Lmag, p, sigma_m
    )

    # Compute Joule losses in stator windings
    Pjoule = Rs * (OP.Id_ref ** 2 + OP.Iq_ref ** 2)

    # Store dict of axes
    output.loss.axes_dict = axes_dict

    # Store scalar losses
    output.loss.Pstator = Pstator
    output.loss.Protor = Protor
    output.loss.Pprox = Pprox
    output.loss.Pmagnet = Pmagnet
    output.loss.Pjoule = Pjoule

    # Store loss density as meshsolution
    if self.is_get_meshsolution:

        meshsol = output.mag.meshsolution

        Nfreq = freqs.size
        Nelem = meshsol.mesh[0].cell["triangle"].nb_cell

        loss_density = zeros((Nfreq, Nelem), dtype=complex)
        loss_density[:, meshsol.group["stator core"]] = Pstator_density
        loss_density[:, meshsol.group["rotor core"]] = Protor_density
        loss_density[:, meshsol.group["stator winding"]] = Pprox_density
        loss_density[:, meshsol.group["rotor magnets"]] = Pmagnet_density

        Loss_density_df = DataFreq(
            name="Loss density",
            unit="W/m3",
            symbol="L",
            values=loss_density,
            is_real=True,
            axes=[axes_dict["freqs"], axes_dict["indice"]],
        )

        Loss_density_sd = SolutionData(
            label=Loss_density_df.name, field=Loss_density_df, unit=Loss_density_df.unit
        )

        output.loss.meshsolution = MeshSolution(
            label=Loss_density_sd.label,
            group=meshsol.group,
            is_same_mesh=True,
            mesh=meshsol.mesh,
            solution=[Loss_density_sd],
        )

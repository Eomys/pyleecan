import numpy as np

from numpy import zeros, pi, roll, mean, max as np_max, min as np_min
from os.path import basename, splitext
from SciDataTool import DataTime, VectorField, Data1D
from os.path import join

from ....Functions.Winding.gen_phase_list import gen_name


def solve_FEA(self, output, sym, axes_dict):
    """
    Solve Elmer model to calculate airgap flux density, torque instantaneous/average/ripple values,
    flux induced in stator windings and flux density, field and permeability maps

    Parameters
    ----------
    self: MagElmer
        A MagElmer object
    output: Output
        An Output object
    sym: int
        Spatial symmetry factor
    axes_dict: {Data}
        Dict of axes used for magnetic calculation
    """

    # Get time and angular axes
    Angle = axes_dict["Angle"]
    Time = axes_dict["Time"]
    Time_Tem = axes_dict["Time_Tem"]

    # Check if the angular axis is anti-periodic
    _, is_antiper_a = Angle.get_periodicity()

    # Import angular vector from Data object
    angle = Angle.get_values(
        is_oneperiod=self.is_periodicity_a,
        is_antiperiod=is_antiper_a and self.is_periodicity_a,
    )

    # Number of angular steps
    Na_comp = angle.size

    # Check if the time axis is anti-periodic
    _, is_antiper_t = Time.get_periodicity()

    # Number of time steps
    Nt_comp = Time.get_length(
        is_oneperiod=True,
        is_antiperiod=is_antiper_t and self.is_periodicity_t,
    )

    # Loading parameters for readibility
    L1 = output.simu.machine.stator.comp_length()
    save_path = self.get_path_save(output)
    FEM_dict = output.mag.FEM_dict

    if (
        hasattr(output.simu.machine.stator, "winding")
        and output.simu.machine.stator.winding is not None
    ):
        qs = output.simu.machine.stator.winding.qs  # Winding phase number
        Npcpp = output.simu.machine.stator.winding.Npcpp
        Phi_wind_stator = zeros((Nt_comp, qs))
    else:
        Phi_wind_stator = None

    # Initialize results matrix
    Br = zeros((Nt_comp, Na_comp))
    Bt = zeros((Nt_comp, Na_comp))
    Tem = zeros((Nt_comp))

    # compute the data for each time step
    # TODO Other than FEMM, in Elmer I think it's possible to compute
    #      all time steps at once
    self.get_logger().debug("Solving Simulation")

    # run the computation
    if self.nb_worker > 1:
        # TODO run solver in parallel
        pass
    else:
        # TODO run solver 'normal'
        pass

    # get the air gap flux result
    # TODO add function (or method)
    # ii -> Time, jj -> Angle
    # Br[ii, jj], Bt[ii, jj] = get_airgap_flux()

    # get the torque
    # TODO add function (or method)
    # Tem[ii] = comp_Elmer_torque(FEM_dict, sym=sym)

    # flux linkage computation
    if (
        hasattr(output.simu.machine.stator, "winding")
        and output.simu.machine.stator.winding is not None
    ):
        # TODO
        # Phi_wind[ii, :] = comp_Elmer_Phi_wind()
        pass

    # store mesh data & solution if requested
    if (Nt_comp == 1) and (self.is_get_mesh or self.is_save_FEA):
        output.mag.meshsolution = self.get_meshsolution()

    # The following code may be unified with FEMM post processing
    """
    # Shift to take into account stator position
    roll_id = int(self.angle_stator * Na_comp / (2 * pi))
    Br = roll(Br, roll_id, axis=1)
    Bt = roll(Bt, roll_id, axis=1)

    Br_data = DataTime(
        name="Airgap radial flux density",
        unit="T",
        symbol="B_r",
        axes=[Time, Angle],
        values=Br,
    )
    Bt_data = DataTime(
        name="Airgap tangential flux density",
        unit="T",
        symbol="B_t",
        axes=[Time, Angle],
        values=Bt,
    )
    output.mag.B = VectorField(
        name="Airgap flux density",
        symbol="B",
        components={"radial": Br_data, "tangential": Bt_data},
    )

    output.mag.Tem = DataTime(
        name="Electromagnetic torque",
        unit="Nm",
        symbol="T_{em}",
        axes=[Time_Tem],
        values=Tem,
    )
    output.mag.Tem_av = mean(Tem)
    self.get_logger().debug("Average Torque: " + str(output.mag.Tem_av) + " N.m")
    output.mag.Tem_rip_pp = abs(np_max(Tem) - np_min(Tem))  # [N.m]
    if output.mag.Tem_av != 0:
        output.mag.Tem_rip_norm = output.mag.Tem_rip_pp / output.mag.Tem_av  # []
    else:
        output.mag.Tem_rip_norm = None

    if (
        hasattr(output.simu.machine.stator, "winding")
        and output.simu.machine.stator.winding is not None
    ):
        Phase = Data1D(
            name="phase",
            unit="",
            values=gen_name(qs),
            is_components=True,
        )
        output.mag.Phi_wind_stator = DataTime(
            name="Stator Winding Flux",
            unit="Wb",
            symbol="Phi_{wind}",
            axes=[Time, Phase],
            values=Phi_wind_stator,
        )

    output.mag.FEMM_dict = FEMM_dict

    if self.is_get_mesh:
        output.mag.meshsolution = self.build_meshsolution(
            Nt_comp, meshFEM, Time, B_elem, H_elem, mu_elem, groups
        )

    if self.is_save_FEA:
        save_path_fea = join(save_path, "MeshSolutionFEMM.h5")
        output.mag.meshsolution.save(save_path_fea)

    if (
        hasattr(output.simu.machine.stator, "winding")
        and output.simu.machine.stator.winding is not None
    ):
        # Electromotive forces computation (update output)
        self.comp_emf()
    else:
        output.mag.emf = None
    """

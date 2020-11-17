import numpy as np

from numpy import zeros, pi, roll, mean, max as np_max, min as np_min
from os.path import basename, splitext
from SciDataTool import DataTime, VectorField, Data1D
from os.path import join

from ....Functions.Winding.gen_phase_list import gen_name


def solve_FEA(self, output, sym, angle, time, angle_rotor, Is, Ir):
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
    time: ndarray
        Time vector for calculation
    angle: ndarray
        Angle vector for calculation
    Is : ndarray
        Stator current matrix (qs,Nt) [A]
    Ir : ndarray
        Stator current matrix (qs,Nt) [A]
    angle_rotor: ndarray
        Rotor angular position vector (Nt,)
    """

    Na = angle.size
    Nt = time.size

    # Loading parameters for readibility
    L1 = output.simu.machine.stator.comp_length()
    save_path = self.get_path_save(output)
    # FEM_dict = output.mag.FEM_dict
    #
    if (
        hasattr(output.simu.machine.stator, "winding")
        and output.simu.machine.stator.winding is not None
    ):
        qs = output.simu.machine.stator.winding.qs  # Winding phase number
        Phi_wind_stator = zeros((Nt, qs))
    else:
        Phi_wind_stator = None

    # Initialize results matrix
    Br = zeros((Nt, Na))
    Bt = zeros((Nt, Na))
    Bz = zeros((Nt, Na))
    Tem = zeros((Nt))
    # Phi_wind_stator = zeros((Nt, qs))

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
    # if Phi_wind_stator is not None:
    #     # TODO
    #     # Phi_wind[ii, :] = comp_Elmer_Phi_wind()
    #     pass

    return Br, Bt, Bz, Tem, Phi_wind_stator

from multiprocessing import cpu_count
from multiprocessing.dummy import Pool
from os import remove

from shutil import copyfile

from numpy import concatenate


def solve_FEMM_parallel(
    self,
    femm,
    output,
    Br,
    Bt,
    Tem,
    Phi_wind_stator,
    sym,
    Nt,
    angle,
    Is,
    Ir,
    angle_rotor,
):
    """
    Same as solve_FEMM including parallelization on several workers
    /!\ Any changes in solve_FEMM must be also made in solve_FEMM_parallel

    Parameters
    ----------
    self: MagFEMM
        A MagFEMM object
    femm: FEMMHandler
        Object to handle FEMM
    output: Output
        An Output object
    output: Output
        An Output object
    Br : ndarray
        Airgap radial flux density (Nt,Na) [T]
    Bt : ndarray
        Airgap tangential flux density (Nt,Na) [T]
    Tem : ndarray
        Electromagnetic torque over time (Nt,) [Nm]
    Phi_wind_stator : ndarray
        Stator winding flux (qs,Nt) [Wb]
    sym: int
        Spatial symmetry factor
    Nt: int
        Number of time steps for calculation
    angle: ndarray
        Angle vector for calculation
    Is : ndarray
        Stator current matrix (qs,Nt) [A]
    Ir : ndarray
        Stator current matrix (qs,Nt) [A]
    angle_rotor: ndarray
        Rotor angular position vector (Nt,)

    Returns
    -------
    B: ndarray
        3D Magnetic flux density for all time steps and each element (Nt, Nelem, 3) [T]
    H : ndarray
        3D Magnetic field for all time steps and each element (Nt, Nelem, 3) [A/m]
    mu : ndarray
        Magnetic relative permeability for all time steps and each element (Nt, Nelem) []
    mesh: MeshMat
        Object containing magnetic mesh at first time step
    groups: dict
        Dict whose values are group label and values are array of indices of related elements
    """

    # The following function must be in solve_FEMM_parallel to access
    # to its variable without passing them in arguments
    def solve_FEMM_single(filename, start_t, end_t):
        """
        Call FEMM to compute airgap flux density from start_t to end_t timesteps

        This function is called in threads, the shared memory enable to modify global variable
        defined in solve_FEMM_parallel such as Br and Bt

        Parameters
        ----------

        filename : str
            .fem file path
        start_t : int
            first timestep to compute
        end_t: int
            last timestep to compute

        Returns
        -------
        B: ndarray
            3D Magnetic flux density for time steps of the current FEMM instance and each element (Nt0, Nelem, 3) [T]
        H : ndarray
            3D Magnetic field for time steps of the current FEMM instance and each element (Nt0, Nelem, 3) [A/m]
        mu : ndarray
            Magnetic relative permeability for time steps of the current FEMM instance and each element (Nt0, Nelem) []
        mesh: MeshMat
            Object containing magnetic mesh at first time step of the current FEMM instance
        groups: dict
            Dict whose values are group label and values are array of indices of related elements

        """

        B_elem, H_elem, mu_elem, meshFEMM, groups = self.solve_FEMM(
            femm,
            output,
            Br,
            Bt,
            Tem,
            Phi_wind_stator,
            sym=sym,
            Nt=Nt,
            angle=angle,
            Is=Is,
            Ir=Ir,
            angle_rotor=angle_rotor,
            is_close_femm=True,
            filename=filename,
            start_t=start_t,
            end_t=end_t,
        )

        return B_elem, H_elem, mu_elem, meshFEMM, groups

    # Init mesh solution as None since array allocation can only be done once
    # number of elements is known, i.e. after first time step resolution
    B_elem, H_elem, mu_elem, meshFEMM, groups = None, None, None, None, None

    # Loading parameters for readibility
    fem_file = self.get_path_save_fem(output)
    nb_worker = self.nb_worker
    logger = self.get_logger()

    # Check method parameters
    if nb_worker > cpu_count():
        logger.warning(
            "Parallelization is set on {} threads while your computer only has {}.".format(
                nb_worker, cpu_count()
            )
        )

    # Copy femm file and create lists to split the tasks
    nb_task_worker = []  # nb of task for each worker
    nb_task_to_split = Nt  # number of task remaining to split
    for w in range(nb_worker, 0, -1):
        # Copy the file
        copyfile(fem_file, fem_file[:-4] + "_" + str(w) + ".fem")
        # Compute the number of task for this worker
        nb_task_worker.append(nb_task_to_split // w + ((nb_task_to_split % w) > 0))
        # Remove the number of task of this worker from the number of remaining tasks
        nb_task_to_split -= nb_task_worker[-1]

    # Define the argument lists:
    #   - femm_file
    #   - start_time : index of the first time step to compute
    #   - end_time : index of the last time step to compute

    femm_files = [
        fem_file[:-4] + "_" + str(i) + ".fem" for i in range(1, nb_worker + 1)
    ]
    start_time_list = [sum(nb_task_worker[:i]) for i in range(nb_worker)]
    end_time_list = [sum(nb_task_worker[: i + 1]) for i in range(nb_worker)]

    # Gathering the different arguments for each instance
    args = [[i, j, k] for i, j, k in zip(femm_files, start_time_list, end_time_list)]

    # Creating threads pool
    pool = Pool(nb_worker)

    # Computing FEMM in parallel
    results = pool.starmap(solve_FEMM_single, args)

    # Building mesh solution
    if self.is_get_mesh:
        B_elem = concatenate([res[0] for res in results], axis=0)
        H_elem = concatenate([res[1] for res in results], axis=0)
        mu_elem = concatenate([res[2] for res in results], axis=0)
        meshFEMM = results[0][3]
        groups = results[0][4]

    # Remove temporary .fem and .ans files
    for w in range(nb_worker, 0, -1):
        remove(fem_file[:-4] + "_" + str(w) + ".fem")
        remove(fem_file[:-4] + "_" + str(w) + ".ans")

    return B_elem, H_elem, mu_elem, meshFEMM, groups

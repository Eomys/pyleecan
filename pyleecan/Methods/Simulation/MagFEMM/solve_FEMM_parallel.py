from multiprocessing import cpu_count
from multiprocessing.dummy import Pool
from os import remove
from os.path import basename, splitext
from os.path import join
from shutil import copyfile

import numpy as np
from SciDataTool import DataTime, VectorField, Data1D
from numpy import zeros, pi, roll, mean, max as np_max, min as np_min

from ....Classes._FEMMHandler import FEMMHandler
from ....Functions.FEMM.comp_FEMM_Phi_wind import comp_FEMM_Phi_wind
from ....Functions.FEMM.comp_FEMM_torque import comp_FEMM_torque
from ....Functions.FEMM.update_FEMM_simulation import update_FEMM_simulation
from ....Functions.Winding.gen_phase_list import gen_name


def solve_FEMM_parallel(self, femm, output, sym, axes_dict):
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
    sym: int
        Spatial symmetry factor
    axes_dict: {Data}
        Dict of axes used for magnetic calculation
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
        """
        # Opening femm
        femm = FEMMHandler()
        femm.openfemm(1)
        # femm.main_minimize()
        femm.opendocument(filename)

        # Creating returned variables
        B_elem, H_elem, mu_elem = None, None, None

        # Create the mesh
        femm.mi_createmesh()

        # Compute the data for each time step
        for ii in range(start_t, end_t + 1):
            # Update rotor position and currents
            update_FEMM_simulation(
                femm=femm,
                output=output,
                materials=FEMM_dict["materials"],
                circuits=FEMM_dict["circuits"],
                is_mmfs=self.is_mmfs,
                is_mmfr=self.is_mmfr,
                j_t0=ii,
                is_sliding_band=self.is_sliding_band,
            )
            # try "previous solution" for speed up of FEMM calculation
            if self.is_sliding_band:
                try:
                    base = basename(self.get_path_save_fem(output))
                    ans_file = splitext(base)[0] + ".ans"
                    femm.mi_setprevious(ans_file, 0)
                except:
                    pass

            # Run the computation
            femm.mi_analyze()
            femm.mi_loadsolution()

            # Get the flux result
            if self.is_sliding_band:
                for jj in range(Na_comp):
                    Br[ii, jj], Bt[ii, jj] = femm.mo_getgapb(
                        "bc_ag2", angle[jj] * 180 / pi
                    )
            else:
                for jj in range(Na_comp):
                    B = femm.mo_getb(Rag * np.cos(angle[jj]), Rag * np.sin(angle[jj]))
                    Br[ii, jj] = B[0] * np.cos(angle[jj]) + B[1] * np.sin(angle[jj])
                    Bt[ii, jj] = -B[0] * np.sin(angle[jj]) + B[1] * np.cos(angle[jj])

            # Compute the torque
            Tem[ii] = comp_FEMM_torque(femm, FEMM_dict, sym=sym)

            if (
                hasattr(output.simu.machine.stator, "winding")
                and output.simu.machine.stator.winding is not None
            ):
                # Phi_wind_stator computation
                Phi_wind_stator[ii, :] = comp_FEMM_Phi_wind(
                    femm,
                    qs,
                    Npcpp,
                    is_stator=True,
                    Lfemm=FEMM_dict["Lfemm"],
                    L1=L1,
                    sym=sym,
                )

            if (
                hasattr(output.simu.machine.stator, "winding")
                and output.simu.machine.stator.winding is not None
            ):
                # Phi_wind_rotor computation
                Phi_wind_rotor[ii, :] = comp_FEMM_Phi_wind(
                    femm,
                    qs_rotor,
                    Npcpp_rotor,
                    is_stator=False,
                    Lfemm=FEMM_dict["Lfemm"],
                    L1=L1,
                    sym=sym,
                )

            # Load mesh data & solution
            if (self.is_sliding_band or Nt_comp == 1) and (
                self.is_get_mesh or self.is_save_FEA
            ):
                (
                    tmpmeshFEMM,
                    tmpB,
                    tmpH,
                    tmpmu,
                    tmpgroups,
                ) = self.get_meshsolution_parallel(
                    femm=femm,
                    save_path=save_path,
                    j_t0=ii,
                    id_worker=start_t,  # Just has to be different from other threads
                    is_get_mesh=ii == start_t,
                )

                if ii == start_t:
                    meshFEMM = [tmpmeshFEMM]
                    groups = [tmpgroups]
                    B_elem = np.zeros(
                        [Nt_comp, meshFEMM[0].cell["triangle"].nb_cell, 3]
                    )
                    H_elem = np.zeros(
                        [Nt_comp, meshFEMM[0].cell["triangle"].nb_cell, 3]
                    )
                    mu_elem = np.zeros([Nt_comp, meshFEMM[0].cell["triangle"].nb_cell])

                B_elem[ii, :, 0:2] = tmpB
                H_elem[ii, :, 0:2] = tmpH
                mu_elem[ii, :] = tmpmu
        femm.closefemm()

        # Return data for mesh solution
        if self.is_get_mesh:
            if start_t == 0:  # return meshFEMM and groups for the first instance
                return B_elem, H_elem, mu_elem, meshFEMM, groups
            else:
                return B_elem, H_elem, mu_elem

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

    # Check if the angular axis is anti-periodic
    _, is_antiper_t = Time.get_periodicity()

    # Number of time steps
    Nt_comp = Time.get_length(
        is_oneperiod=True,
        is_antiperiod=is_antiper_t and self.is_periodicity_t,
    )

    # Loading parameters for readibility
    L1 = output.simu.machine.stator.comp_length()
    save_path = self.get_path_save(output)
    fem_file = self.get_path_save_fem(output)
    FEMM_dict = output.mag.FEA_dict
    nb_worker = self.nb_worker
    logger = self.get_logger()

    # Check method parameters
    if nb_worker > cpu_count():
        logger.warning(
            "Parallelization is set on {} threads while your computer only has {}.".format(
                nb_worker, cpu_count()
            )
        )

    if (
        hasattr(output.simu.machine.stator, "winding")
        and output.simu.machine.stator.winding is not None
    ):
        qs = output.simu.machine.stator.winding.qs  # Winding phase number
        Npcpp = output.simu.machine.stator.winding.Npcpp
        Phi_wind_stator = zeros((Nt_comp, qs))
    else:
        Phi_wind_stator = None

    if (
        hasattr(output.simu.machine.rotor, "winding")
        and output.simu.machine.rotor.winding is not None
    ):
        qs_rotor = output.simu.machine.rotor.winding.qs  # Winding phase number
        Npcpp_rotor = output.simu.machine.rotor.winding.Npcpp
        Phi_wind_rotor = zeros((Nt_comp, qs_rotor))
    else:
        Phi_wind_rotor = None

    # Initialize results matrix
    Br = zeros((Nt_comp, Na_comp))
    Bt = zeros((Nt_comp, Na_comp))
    Tem = zeros((Nt_comp))

    Rag = output.simu.machine.comp_Rgap_mec()

    # Copy femm file and create lists to split the tasks
    nb_task_worker = []  # nb of task for each worker
    nb_task_to_split = Nt_comp  # number of task remaining to split
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
    end_time_list = [sum(nb_task_worker[: i + 1]) - 1 for i in range(nb_worker)]

    # Gathering the different arguments for each instance
    args = [[i, j, k] for i, j, k in zip(femm_files, start_time_list, end_time_list)]

    # Creating threads pool
    pool = Pool(nb_worker)

    # Computing FEMM in parallel
    results = pool.starmap(solve_FEMM_single, args)

    # Shift to take into account stator position
    roll_id = int(self.angle_stator * Na_comp / (2 * pi))
    Br = roll(Br, roll_id, axis=1)
    Bt = roll(Bt, roll_id, axis=1)

    # Store the results
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

    if (
        hasattr(output.simu.machine.rotor, "winding")
        and output.simu.machine.rotor.winding is not None
    ):
        Phase = Data1D(
            name="phase",
            unit="",
            values=gen_name(qs_rotor),
            is_components=True,
        )
        output.mag.Phi_wind_rotor = DataTime(
            name="Rotor Winding Flux",
            unit="Wb",
            symbol="Phi_{wind}",
            axes=[Time, Phase],
            values=Phi_wind_rotor,
        )

    output.mag.FEA_dict = FEMM_dict

    # Building mesh solution
    if self.is_get_mesh:
        B_elem = sum([res[0] for res in results])
        H_elem = sum([res[1] for res in results])
        mu_elem = sum([res[2] for res in results])
        meshFEMM = results[0][3]
        groups = results[0][4]
        output.mag.meshsolution = self.build_meshsolution(
            Nt_comp, meshFEMM, Time, B_elem, H_elem, mu_elem, groups
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

    # Remove tmp fem files
    for w in range(nb_worker, 0, -1):
        remove(fem_file[:-4] + "_" + str(w) + ".fem")

    if self.is_close_femm:
        femm.closefemm()

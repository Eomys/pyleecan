from os import makedirs
from os.path import join, isdir
import pytest
from shutil import copyfile

import matplotlib.pyplot as plt
from numpy import array, linspace, ones, pi, zeros

from pyleecan.Classes.import_all import *

try:
    from pyleecan.Functions.GMSH.gen_3D_mesh import gen_3D_mesh
except ImportError as error:
    gen_3D_mesh = error
from Tests import save_plot_path
from Tests.Plot.LamWind import wind_mat
from pyleecan.Functions.load import load
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Output import Output
from pyleecan.Classes.SlotUD2 import SlotUD2
from pyleecan.Classes.OptiDesignVar import OptiDesignVar
from pyleecan.Classes.OptiObjective import OptiObjective
from pyleecan.Classes.OptiProblem import OptiProblem
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.OptiGenAlgNsga2Deap import OptiGenAlgNsga2Deap

import numpy as np
import random
from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

# Gather results in the same folder
save_path = join(save_plot_path, "ICEM_2020")
if not isdir(save_path):
    makedirs(save_path)


@pytest.mark.skip
@pytest.mark.long_5s
@pytest.mark.SPMSM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_Optimization_problem():
    """
    Figure19: Machine topology before optimization
    Figure20: Individuals in the fitness space
    Figure21: Pareto Front in the fitness space
    Figure22: Topology to maximize first torque harmonic
    Figure22: Topology to minimize second torque harmonic

    WARNING: The computation takes 6 hours on a single 3GHz CPU core.
    The algorithm uses randomization at different steps so
    the results won't be exactly the same as the one in the publication
    """
    # ------------------ #
    # DEFAULT SIMULATION #
    # ------------------ #

    # First, we need to define a default simulation.
    # This simulation will the base of every simulation during the optimization process

    # Load the machine
    Benchmark = load(join(DATA_DIR, "Machine", "Benchmark.json"))

    # Definition of the enforced output of the electrical module
    Na_tot = 1024  # Angular steps
    Nt_tot = 4  # Time step
    Is = ImportMatrixVal(
        value=np.array(
            [
                [1.73191211247099e-15, 24.4948974278318, -24.4948974278318],
                # [-0.925435413499285, 24.9445002597334, -24.0190648462341],
                # [-1.84987984757817, 25.3673918959653, -23.5175120483872],
                # [-2.77234338398183, 25.7631194935712, -22.9907761095894],
                # [-3.69183822565029, 26.1312592975275, -22.4394210718773],
                # [-4.60737975447626, 26.4714170945114, -21.8640373400352],
                # [-5.51798758565886, 26.7832286350338, -21.2652410493749],
                # [-6.42268661752422, 27.0663600234871, -20.6436734059628],
                # # [-7.32050807568877, 27.3205080756888, -20.0000000000000],
                # # [-8.21049055044714, 27.5454006435389, -19.3349100930918],
                [-9.09168102627374, 27.7407969064430, -18.6491158801692],
                # [-9.96313590233562, 27.9064876291883, -17.9433517268527],
                # [-10.8239220029239, 28.0422953859991, -17.2183733830752],
                # [-11.6731175767218, 28.1480747505277, -16.4749571738058],
                # [-12.5098132838389, 28.2237124515809, -15.7138991677421],
                # [-13.3331131695549, 28.2691274944141, -14.9360143248592],
                # [-14.1421356237309, 28.2842712474619, -14.1421356237310],
                # [-14.9360143248592, 28.2691274944141, -13.3331131695549],
                # [-15.7138991677420, 28.2237124515809, -12.5098132838389],
                # [-16.4749571738058, 28.1480747505277, -11.6731175767219],
                [-17.2183733830752, 28.0422953859991, -10.8239220029240],
                # [-17.9433517268527, 27.9064876291883, -9.96313590233564],
                # [-18.6491158801692, 27.7407969064430, -9.09168102627375],
                # [-19.3349100930918, 27.5454006435389, -8.21049055044716],
                # [-20, 27.3205080756888, -7.32050807568879],
                # [-20.6436734059628, 27.0663600234871, -6.42268661752424],
                # [-21.2652410493749, 26.7832286350338, -5.51798758565888],
                # [-21.8640373400352, 26.4714170945114, -4.60737975447627],
                # [-22.4394210718772, 26.1312592975275, -3.69183822565031],
                # [-22.9907761095894, 25.7631194935712, -2.77234338398184],
                # [-23.5175120483872, 25.3673918959653, -1.84987984757819],
                [-24.0190648462341, 24.9445002597334, -0.925435413499304],
            ]
        )
    )
    N0 = 400
    Ir = ImportMatrixVal(value=np.zeros((Nt_tot, 28)))

    Benchmark.name = (
        "Default SPMSM machine"  # Rename the machine to have the good plot title
    )

    # Definition of the simulation
    simu = Simu1(name="test_Optimization_problem", machine=Benchmark)

    simu.input = InputCurrent(
        Is=Is,
        Ir=Ir,  # zero current for the rotor
        OP=OPdq(N0=N0),
        Nt_tot=Nt_tot,
        Na_tot=Na_tot,
        angle_rotor_initial=0.39,
    )

    # Definition of the magnetic simulation
    simu.mag = MagFEMM(type_BH_stator=2, type_BH_rotor=2, is_periodicity_a=True,)

    simu.struct = None

    # Default Output
    output = Output(simu=simu)

    # Modify magnet width and the slot opening height
    output.simu.machine.stator.slot.H0 = 0.001
    output.simu.machine.rotor.slot.Wmag *= 0.98

    # FIG21 Display default machine
    output.simu.machine.plot(is_show_fig=False)
    fig = plt.gcf()
    fig.savefig(join(save_path, "fig_21_Machine_topology_before_optimization.png"))
    fig.savefig(
        join(save_path, "fig_21_Machine_topology_before_optimization.svg"), format="svg"
    )
    plt.close("all")
    # -------------------- #
    # OPTIMIZATION PROBLEM #
    # -------------------- #

    # Objective functions
    """Return the average torque opposite (opposite to be maximized)"""
    tem_av = "lambda output: -abs(output.mag.Tem_av)"

    """Return the torque ripple """
    Tem_rip_pp = "lambda output: abs(output.mag.Tem_rip_pp)"

    my_objs = [
        OptiObjective(
            name="Maximization of the average torque",
            symbol="Tem_av",
            unit="N.m",
            keeper=tem_av,
        ),
        OptiObjective(
            name="Minimization of the torque ripple",
            symbol="Tem_rip_pp",
            unit="N.m",
            keeper=Tem_rip_pp,
        ),
    ]

    # Design variables
    my_vars = [
        OptiDesignVar(
            name="Stator slot opening",
            symbol="W0",
            unit="m",
            type_var="interval",
            space=[
                0.2 * output.simu.machine.stator.slot.W2,
                output.simu.machine.stator.slot.W2,
            ],
            get_value="lambda space: random.uniform(*space)",
            setter="simu.machine.stator.slot.W0",
        ),
        OptiDesignVar(
            name="Rotor magnet width",
            symbol="Wmag",
            unit="m",
            type_var="interval",
            space=[
                0.5 * output.simu.machine.rotor.slot.W0,
                0.99 * output.simu.machine.rotor.slot.W0,
            ],  # May generate error in FEMM
            get_value="lambda space: random.uniform(*space)",
            setter="simu.machine.rotor.slot.Wmag",
        ),
    ]

    # Problem creation
    my_prob = OptiProblem(simu=simu, design_var=my_vars, obj_func=my_objs)

    # Solve problem with NSGA-II
    solver = OptiGenAlgNsga2Deap(problem=my_prob, size_pop=12, nb_gen=40, p_mutate=0.5)
    res = solver.solve()

    # ------------- #
    # PLOTS RESULTS #
    # ------------- #

    res.plot_generation(x_symbol="Tem_av", y_symbol="Tem_rip_pp")
    fig = plt.gcf()
    fig.savefig(join(save_path, "fig_20_Individuals_in_fitness_space.png"))
    fig.savefig(
        join(save_path, "fig_20_Individuals_in_fitness_space.svg"), format="svg"
    )

    res.plot_pareto(x_symbol="Tem_av", y_symbol="Tem_rip_pp")
    fig = plt.gcf()
    fig.savefig(join(save_path, "Pareto_front_in_fitness_space.png"))
    fig.savefig(join(save_path, "Pareto_front_in_fitness_space.svg"), format="svg")

    # Extraction of best topologies for every objective
    pareto_index = (
        res.get_pareto_index()
    )  # Extract individual index in the pareto front

    idx_1 = pareto_index[0]  # First objective
    idx_2 = pareto_index[0]  # Second objective

    Tem_av = res["Tem_av"].result
    Tem_rip_pp = res["Tem_rip_pp"].result

    for i in pareto_index:
        # First objective
        if Tem_av[i] < Tem_av[idx_1]:
            idx_1 = i
        # Second objective
        if Tem_rip_pp[i] < Tem_rip_pp[idx_2]:
            idx_2 = i

    # Get corresponding simulations
    simu1 = res.get_simu(idx_1)
    simu2 = res.get_simu(idx_2)

    # Rename machine to modify the title
    name1 = "Machine that maximizes the average torque ({:.3f} Nm)".format(
        abs(Tem_av[idx_1])
    )
    simu1.machine.name = name1
    name2 = "Machine that minimizes the torque ripple ({:.4f}Nm)".format(
        abs(Tem_rip_pp[idx_2])
    )
    simu2.machine.name = name2

    # plot the machine
    simu1.machine.plot(is_show_fig=False)
    fig = plt.gcf()
    fig.savefig(
        join(save_path, "fig_21_Topology_to_maximize_average_torque.png"), format="png"
    )
    fig.savefig(
        join(save_path, "fig_21_Topology_to_maximize_average_torque.svg"), format="svg"
    )

    simu2.machine.plot(is_show_fig=False)
    fig = plt.gcf()
    fig.savefig(
        join(save_path, "fig_21_Topology_to_minimize_torque_ripple.png"), format="png"
    )
    fig.savefig(
        join(save_path, "fig_21_Topology_to_minimize_torque_ripple.svg"), format="svg"
    )


if __name__ == "__main__":
    test_Optimization_problem()
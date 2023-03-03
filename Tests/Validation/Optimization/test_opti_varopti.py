#!/usr/bin/env python
# coding: utf-8
"""
Test Pyleecan optimization module using Binh and Korn Function
 
Binh, T. and U. Korn, "MOBES: A multiobjective evolution strategy for constrained optimization problems. 
In Proceedings of the third international Conference on Genetic Algorithms (Mendel97), ", Brno, Czech Republic, pp. 176-182, 1997 
"""
# Imports
from os.path import join
import pytest
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.DataKeeper import DataKeeper
from pyleecan.Classes.OptiDesignVarInterval import OptiDesignVarInterval
from pyleecan.Classes.OptiDesignVarSet import OptiDesignVarSet
from pyleecan.Classes.OptiObjective import OptiObjective
from pyleecan.Classes.OptiConstraint import OptiConstraint
from pyleecan.Classes.OptiGenAlgNsga2Deap import OptiGenAlgNsga2Deap
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.VarOpti import VarOpti
from pyleecan.Classes.Output import Output

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import random
from Tests import save_validation_path as save_path
from pyleecan.definitions import DATA_DIR, TEST_DIR


def harm1(output):
    """Return the first torque harmonic """
    harm_list = output.mag.Tem.get_magnitude_along("freqs")["T_{em}"]

    # Return the first torque harmonic
    return harm_list[1]


@pytest.mark.SCIM
@pytest.mark.MagFEMM
def test_opti_varopti():
    # Import the machine from a script
    Toyota_Prius = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))
    Toyota_Prius.plot()
    rotor_speed = 2000  # [rpm]

    # Create the Simulation
    simu_ref = Simu1(name="EM_SIPMSM_AL_001", machine=Toyota_Prius, layer=0)

    # Defining Simulation Input
    simu_ref.input = InputCurrent()

    # time discretization [s]
    simu_ref.input.Nt_tot = 16

    # Angular discretization along the airgap circonference for flux density calculation
    simu_ref.input.Na_tot = 1024

    # Defining Operating Point
    simu_ref.input.OP = OPdq()
    simu_ref.input.OP.N0 = rotor_speed  # Rotor speed as a function of time [rpm]
    # Stator sinusoidal currents
    simu_ref.input.OP.Id_ref = -100  # [Arms]
    simu_ref.input.OP.Iq_ref = 200  # [Arms]

    # Definition of the magnetic simulation (is_mmfr=False => no flux from the magnets)
    simu_ref.mag = MagFEMM(
        type_BH_stator=0,  # 0 to use the B(H) curve,
        # 1 to use linear B(H) curve according to mur_lin,
        # 2 to enforce infinite permeability (mur_lin =100000)
        type_BH_rotor=0,  # 0 to use the B(H) curve,
        # 1 to use linear B(H) curve according to mur_lin,
        # 2 to enforce infinite permeability (mur_lin =100000)
        file_name="",  # Name of the file to save the FEMM model
        is_periodicity_a=True,  # Use Angular periodicity
        is_periodicity_t=True,  # Use time periodicity,
        is_sliding_band=True,
        # Kmesh_fineness = 0.2, # Decrease mesh precision
        # Kgeo_fineness = 0.2, # Decrease mesh precision
    )

    # We only use the magnetic part
    simu_ref.force = None
    simu_ref.struct = None

    my_obj = [
        OptiObjective(
            name="Maximization of the average torque",
            symbol="Tem_av",
            unit="N.m",
            keeper="lambda output: -abs(output.mag.Tem_av)",  # keeper can be saved
        ),
        OptiObjective(
            name="Minimization of the first torque harmonic",
            symbol="Tem_h1",
            unit="N.m",
            keeper=harm1,  # keeper will be cleaned in save
        ),
    ]

    # Design variables
    my_design_var = [
        OptiDesignVarInterval(
            name="Stator slot opening",
            symbol="SW0",
            unit="m",
            space=[
                0 * simu_ref.machine.stator.slot.W2,
                simu_ref.machine.stator.slot.W2,
            ],
            get_value="lambda space: random.uniform(*space)",  # To initiate randomly the first generation
            setter="simu.machine.stator.slot.W0",  # Variable to edit
        ),
        OptiDesignVarSet(
            name="Rotor ext radius",
            symbol="Rext",
            unit="m",
            space=[
                0.998 * simu_ref.machine.rotor.Rext,
                0.999 * simu_ref.machine.rotor.Rext,
                simu_ref.machine.rotor.Rext,
                1.001 * simu_ref.machine.rotor.Rext,
            ],
            get_value="lambda space: random.choice(space)",
            setter="simu.machine.rotor.Rext",
        ),
    ]

    my_constraint = [
        OptiConstraint(
            name="const1",
            type_const="<=",
            value=700,
            keeper="lambda output: abs(output.mag.Tem_rip_pp)",
        )
    ]

    # Solving the problem
    solver = OptiGenAlgNsga2Deap(size_pop=8, nb_gen=8, p_mutate=0.5)

    # Creating a VarOpti and launch the simulation
    simu_ref.var_simu = VarOpti(
        paramexplorer_list=my_design_var,
        objective_list=my_obj,
        constraint_list=my_constraint,
        solver=solver,
        var_simu=simu_ref.var_simu,
    )
    simu_ref.var_simu.check()
    res = simu_ref.run()

    # Create a figure containing 4 subfigures (axes)
    fig, axs = plt.subplots(2, 2, figsize=(8, 8))

    # Plot every individual in the fitness space
    res.plot_generation(
        x_symbol="Tem_av",  # symbol of the first objective function or design variable
        y_symbol="Tem_h1",  # symbol of the second objective function or design variable
        ax=axs[0, 0],  # ax to plot
    )

    # Plot every individual in the design space
    res.plot_generation(x_symbol="SW0", y_symbol="Rext", ax=axs[0, 1])

    # Plot pareto front in fitness space
    res.plot_pareto(x_symbol="Tem_av", y_symbol="Tem_h1", ax=axs[1, 0])

    # Plot pareto front in design space
    res.plot_pareto(x_symbol="SW0", y_symbol="Rext", ax=axs[1, 1])

    fig.tight_layout()

    fig.savefig(join(save_path, "test_opti_varopti.png"))


if __name__ == "__main__":
    test_opti_varopti()

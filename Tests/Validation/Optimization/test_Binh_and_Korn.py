#!/usr/bin/env python
# coding: utf-8
"""
Test Pyleecan optimization module using Binh and Korn Function
 
Binh, T. and U. Korn, "MOBES: A multiobjective evolution strategy for constrained optimization problems. 
In Proceedings of the third international Conference on Genetic Algorithms (Mendel97), ", Brno, Czech Republic, pp. 176-182, 1997 
"""
# Imports

import pytest
from pyleecan.definitions import PACKAGE_NAME
from Tests.Validation.Machine.SCIM_001 import SCIM_001
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Output import Output
from pyleecan.Classes.OptiDesignVar import OptiDesignVar
from pyleecan.Classes.OptiObjFunc import OptiObjFunc
from pyleecan.Classes.OptiConstraint import OptiConstraint
from pyleecan.Classes.OptiProblem import OptiProblem
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.OptiGenAlgNsga2Deap import OptiGenAlgNsga2Deap

import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import random


@pytest.mark.validation
@pytest.mark.long
@pytest.mark.DEAP
def test_Binh_and_Korn():
    # Defining reference Output
    # Definition of the enforced output of the electrical module
    Nt = 2
    Nr = ImportMatrixVal(value=np.ones(Nt) * 3000)
    Is = ImportMatrixVal(
        value=np.array(
            [
                [6.97244193e-06, 2.25353053e02, -2.25353060e02],
                [-2.60215295e02, 1.30107654e02, 1.30107642e02],
                #             [-6.97244208e-06, -2.25353053e02, 2.25353060e02],
                #             [2.60215295e02, -1.30107654e02, -1.30107642e02],
            ]
        )
    )
    Ir = ImportMatrixVal(value=np.zeros(30))
    time = ImportGenVectLin(start=0, stop=0.015, num=Nt, endpoint=True)
    angle = ImportGenVectLin(
        start=0, stop=2 * np.pi, num=64, endpoint=False
    )  # num=1024

    # Definition of the simulation
    simu = Simu1(name="Test_machine", machine=SCIM_001)

    simu.input = InputCurrent(
        Is=Is,
        Ir=Ir,  # zero current for the rotor
        Nr=Nr,
        angle_rotor=None,  # Will be computed
        time=time,
        angle=angle,
        angle_rotor_initial=0.5216 + np.pi,
    )

    # Definition of the magnetic simulation
    simu.mag = MagFEMM(
        type_BH_stator=2, type_BH_rotor=2, is_symmetry_a=True, is_antiper_a=False
    )
    simu.mag.Kmesh_fineness = 0.01
    # simu.mag.Kgeo_fineness=0.02
    simu.mag.sym_a = 4
    simu.struct = None

    output = Output(simu=simu)

    # ### Design variable
    my_vars = {
        "RH0": OptiDesignVar(
            name="output.simu.machine.rotor.slot.H0",
            type_var="interval",
            space=[0, 5],  # May generate error in FEMM
            function=lambda space: random.uniform(*space),
        ),
        "SH0": OptiDesignVar(
            name="output.simu.machine.stator.slot.H0",
            type_var="interval",
            space=[0, 3],  # May generate error in FEMM
            function=lambda space: random.uniform(*space),
        ),
    }

    # ### Constraints
    cstrs = {
        "first": OptiConstraint(
            get_variable=lambda output: (output.simu.machine.rotor.slot.H0 - 5) ** 2
            + output.simu.machine.stator.slot.H0 ** 2,
            type_const="<=",
            value=25,
        ),
        "second": OptiConstraint(
            get_variable=lambda output: (output.simu.machine.rotor.slot.H0 - 5) ** 2
            + (output.simu.machine.stator.slot.H0 + 3) ** 2,
            type_const=">=",
            value=7.7,
        ),
    }

    # ### Objectives
    objs = {
        "obj1": OptiObjFunc(
            description="Maximization of the torque average",
            func=lambda output: output.mag.Tem_av,
        ),
        "obj2": OptiObjFunc(
            description="Minimization of the torque ripple",
            func=lambda output: output.mag.Tem_rip,
        ),
    }

    # ### Evaluation function
    def evaluate(output):
        x = output.simu.machine.rotor.slot.H0
        y = output.simu.machine.stator.slot.H0
        output.mag.Tem_av = 4 * x ** 2 + 4 * y ** 2
        output.mag.Tem_rip = (x - 5) ** 2 + (y - 5) ** 2

    # ### Defining the problem

    my_prob = OptiProblem(
        output=output,
        design_var=my_vars,
        obj_func=objs,
        constraint=cstrs,
        eval_func=evaluate,
    )

    # ### Solving the problem

    solver = OptiGenAlgNsga2Deap(problem=my_prob, size_pop=20, nb_gen=40, p_mutate=0.5)
    res = solver.solve()

    # ### Plot results

    def plot_pareto(self):
        """Plot every fitness values with the pareto front for 2 fitness
        
        Parameters
        ----------
        self : OutputMultiOpti
        """

        # TODO Add a feature to return the design_varibles of each indiv from the Pareto front

        # Get fitness and ngen
        is_valid = np.array(self.is_valid)
        fitness = np.array(self.fitness)
        ngen = np.array(self.ngen)

        # Keep only valid values
        indx = np.where(is_valid)[0]

        fitness = fitness[indx]
        ngen = ngen[indx]

        # Get pareto front
        pareto = list(np.unique(fitness, axis=0))

        # Get dominated values
        to_remove = []
        N = len(pareto)
        for i in range(N):
            for j in range(N):
                if all(pareto[j] <= pareto[i]) and any(pareto[j] < pareto[i]):
                    to_remove.append(pareto[i])
                    break

        # Remove dominated values
        for i in to_remove:
            for l in range(len(pareto)):
                if all(i == pareto[l]):
                    pareto.pop(l)
                    break

        pareto = np.array(pareto)

        fig, axs = plt.subplots(1, 2, figsize=(16, 6))

        # Plot Pareto front
        axs[0].scatter(
            pareto[:, 0],
            pareto[:, 1],
            facecolors="b",
            edgecolors="b",
            s=0.8,
            label="Pareto Front",
        )
        axs[0].autoscale()
        axs[0].legend()
        axs[0].set_title("Pyleecan results")
        axs[0].set_xlabel(r"$f_1(x)$")
        axs[0].set_ylabel(r"$f_2(x)$")
        try:
            img_to_find = img.imread("Tests\\Validation\\Optimization\\Binh_and_Korn_function.jpg", format="jpg")
            axs[1].imshow(img_to_find, aspect="auto")
            axs[1].axis("off")
            axs[1].set_title("Pareto front of the problem")
        except (TypeError, ValueError):
            print("Pillow is needed to import jpg files")

        return fig

    fig = plot_pareto(res)
    fig.savefig("Tests/Results/Validation/test_Binh_and_Korn.png")

# coding: utf-8

"""
Test Pyleecan optimization module using Zitzler–Deb–Thiele's function N. 3
"""
import pytest
from pyleecan.Tests.Validation.Machine.SCIM_001 import SCIM_001
from pyleecan.Classes.InCurrent import InCurrent
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
@pytest.mark.optimization
def test_zdt3():
    # ### Defining reference Output

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

    simu.input = InCurrent(
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
        is_stator_linear_BH=2,
        is_rotor_linear_BH=2,
        is_symmetry_a=True,
        is_antiper_a=False,
    )
    simu.mag.Kmesh_fineness = 0.01
    # simu.mag.Kgeo_fineness=0.02
    simu.mag.sym_a = 4
    simu.struct = None

    output = Output(simu=simu)

    # ### Design variable
    my_vars = {}

    for i in range(30):
        my_vars["var_" + str(i)] = OptiDesignVar(
            name="output.simu.input.Ir.value[" + str(i) + "]",
            type_var="interval",
            space=[0, 1],
            function=lambda space: np.random.uniform(*space),
        )

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

    # ### Evaluation
    def evaluate(output):
        x = output.simu.input.Ir.value
        f1 = lambda x: x[0]
        g = lambda x: 1 + (9 / 29) * np.sum(x[1:])
        h = lambda f1, g: 1 - np.sqrt(f1 / g) - (f1 / g) * np.sin(10 * np.pi * f1)
        output.mag.Tem_av = f1(x)
        output.mag.Tem_rip = g(x) * h(f1(x), g(x))

    # ### Defining the problem
    my_prob = OptiProblem(
        output=output, design_var=my_vars, obj_func=objs, eval_func=evaluate
    )

    solver = OptiGenAlgNsga2Deap(problem=my_prob, size_pop=40, nb_gen=100, p_mutate=0.5)
    res = solver.solve()

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
            img_to_find = img.imread(
                "pyleecan\\Tests\\Validation\\Optimization\\zdt3.jpg", format="jpg"
            )
            axs[1].imshow(img_to_find, aspect="auto")
            axs[1].axis("off")
            axs[1].set_title("Pareto front of the problem")
        except TypeError:
            print("Pillow is needed to import jpg files")

        return fig

    fig = plot_pareto(res)
    plt.savefig("pyleecan\\Tests\\Results\\Validation\\test_zdt3.png")

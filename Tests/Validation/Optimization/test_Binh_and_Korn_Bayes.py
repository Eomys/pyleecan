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
from pyleecan.definitions import PACKAGE_NAME
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.OPslip import OPslip
from pyleecan.Classes.Output import Output
from pyleecan.Classes.OptiDesignVarInterval import OptiDesignVarInterval
from pyleecan.Classes.OptiObjective import OptiObjective
from pyleecan.Classes.OptiConstraint import OptiConstraint
from pyleecan.Classes.OptiProblem import OptiProblem
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.OptiBayesAlgSmoot import OptiBayesAlgSmoot

import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import random
from Tests import save_validation_path as save_path

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR, TEST_DIR


@pytest.mark.long_5s
@pytest.mark.SCIM
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_Binh_and_Korn():
    # Defining reference Output
    # Definition of the enforced output of the electrical module
    Railway_Traction = load(join(DATA_DIR, "Machine", "Railway_Traction.json"))
    Nt = 2
    N0 = 3000
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
    Na_tot = 64

    # Definition of the simulation
    simu = Simu1(name="test_Binh_and_Korn_Bayes", machine=Railway_Traction)

    simu.input = InputCurrent(
        Is=Is,
        Ir=Ir,  # zero current for the rotor
        OP=OPslip(N0=N0),
        time=time,
        Na_tot=Na_tot,
        angle_rotor_initial=0.5216 + np.pi,
    )

    # Definition of the magnetic simulation
    simu.mag = MagFEMM(type_BH_stator=2, type_BH_rotor=2, is_periodicity_a=True)
    simu.mag.Kmesh_fineness = 0.01
    # simu.mag.Kgeo_fineness = 0.02
    simu.struct = None

    # ### Design variable
    my_vars = [
        OptiDesignVarInterval(
            name="Rotor slot height",
            symbol="RH0",
            space=[0, 5],  # May generate error in FEMM
            get_value="lambda space: random.uniform(*space)",
            setter="simu.machine.rotor.slot.H0",
        ),
        OptiDesignVarInterval(
            name="Stator slot height",
            symbol="SH0",
            space=[0, 3],  # May generate error in FEMM
            get_value="lambda space: random.uniform(*space)",
            setter="simu.machine.stator.slot.H0",
        ),
    ]

    # ### Constraints
    cstrs = [
        OptiConstraint(
            name="first",
            keeper="lambda output: (output.simu.machine.rotor.slot.H0 - 5) ** 2 + output.simu.machine.stator.slot.H0 ** 2",
            type_const="<=",
            value=25,
        ),
        OptiConstraint(
            name="second",
            keeper="lambda output: (output.simu.machine.rotor.slot.H0 - 5) ** 2 + (output.simu.machine.stator.slot.H0 + 3) ** 2",
            type_const=">=",
            value=7.7,
        ),
    ]

    # ### Objectives
    objs = [
        OptiObjective(
            name="Maximization of the torque average",
            symbol="obj1",
            unit="N.m",
            keeper="lambda output: output.mag.Tem_av",
        ),
        OptiObjective(
            name="Minimization of the torque ripple",
            symbol="obj2",
            unit="N.m",
            keeper="lambda output: output.mag.Tem_rip_norm",
        ),
    ]

    # ### Evaluation function
    def evaluate(output):
        x = output.simu.machine.rotor.slot.H0
        y = output.simu.machine.stator.slot.H0
        output.mag.Tem_av = 4 * x ** 2 + 4 * y ** 2
        output.mag.Tem_rip_norm = (x - 5) ** 2 + (y - 5) ** 2

    # ### Defining the problem

    my_prob = OptiProblem(
        simu=simu,
        design_var=my_vars,
        obj_func=objs,
        constraint=cstrs,
        eval_func=evaluate,
    )

    # ### Solving the problem

    solver = OptiBayesAlgSmoot(problem=my_prob, nb_start=10, nb_iter=1)
    res = solver.solve()

    # ### Plot results
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))

    try:
        img_to_find = img.imread(
            join(TEST_DIR, "Validation", "Optimization", "Binh_and_Korn_function.jpg"),
            format="jpg",
        )
        axs[1].imshow(img_to_find, aspect="auto")
        axs[1].axis("off")
        axs[1].set_title("Pareto front of the problem")
    except (TypeError, ValueError):
        print("Pillow is needed to import jpg files")

    res.plot_pareto(x_symbol="obj1", y_symbol="obj2", ax=axs[0], is_show_fig=False)
    fig.savefig(join(save_path, "test_Binh_and_Korn.png"))


if __name__ == "__main__":
    test_Binh_and_Korn()

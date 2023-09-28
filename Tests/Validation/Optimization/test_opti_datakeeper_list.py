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
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.DataKeeper import DataKeeper
from pyleecan.Classes.OptiDesignVarInterval import OptiDesignVarInterval
from pyleecan.Classes.OptiObjective import OptiObjective
from pyleecan.Classes.OptiProblem import OptiProblem
from pyleecan.Classes.OptiGenAlgNsga2Deap import OptiGenAlgNsga2Deap

import random

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR


@pytest.mark.SCIM
@pytest.mark.MagFEMM
@pytest.mark.SingleOP
def test_opti_datakeeper_list():
    # Defining reference Output
    # Definition of the enforced output of the electrical module
    Railway_Traction = load(join(DATA_DIR, "Machine", "Railway_Traction.json"))

    # Definition of the simulation
    simu = Simu1(name="test_opti_datakeeper_list", machine=Railway_Traction)

    # Design variable
    my_vars = [
        OptiDesignVarInterval(
            name="Rotor slot height",
            symbol="RH0",
            space=[0, 5],  # May generate error in FEMM
            get_value=lambda space: random.uniform(*space),
            setter="simu.machine.rotor.slot.H0",
        ),
        OptiDesignVarInterval(
            name="Stator slot height",
            symbol="SH0",
            space=[0, 3],  # May generate error in FEMM
            get_value=lambda space: random.uniform(*space),
            setter="simu.machine.stator.slot.H0",
        ),
    ]

    # Objectives
    objs = [
        OptiObjective(
            name="Minimization of the rotor slot width",
            symbol="R_s_w0",
            unit="m",
            keeper="lambda output: output.simu.machine.rotor.slot.W0",
        )
    ]

    datakeeper_list = [
        DataKeeper(
            name="Minimization of the rotor slot width",
            symbol="R_s_w0_bis",
            unit="m",
            keeper="lambda output: output.simu.machine.rotor.slot.W0",
        )
    ]

    def evaluate(output):
        """Skip calculations"""
        pass

    # Defining the problem
    my_prob = OptiProblem(
        simu=simu,
        design_var=my_vars,
        obj_func=objs,
        datakeeper_list=datakeeper_list,
        eval_func=evaluate,
    )

    # Solving the problem

    solver = OptiGenAlgNsga2Deap(problem=my_prob, size_pop=4, nb_gen=2, p_mutate=0)
    res = solver.solve()

    assert res["R_s_w0"].result == res["R_s_w0_bis"].result


if __name__ == "__main__":
    test_opti_datakeeper_list()

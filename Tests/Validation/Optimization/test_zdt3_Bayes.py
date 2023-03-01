# coding: utf-8

"""
Test Pyleecan optimization module using Zitzler–Deb–Thiele's function N. 3
"""
from os.path import join
import pytest
from pyleecan.Classes.OPslip import OPslip
from pyleecan.definitions import PACKAGE_NAME
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.Output import Output
from pyleecan.Classes.OptiDesignVarInterval import OptiDesignVarInterval
from pyleecan.Classes.OptiObjective import OptiObjective
from pyleecan.Classes.OptiConstraint import OptiConstraint
from pyleecan.Classes.OptiProblem import OptiProblem
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.OptiBayesAlgSmoot import OptiBayesAlgSmoot
from Tests import save_validation_path as save_path
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import random

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR, TEST_DIR


@pytest.mark.long_5s
@pytest.mark.SCIM
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.SingleOP
def test_zdt3_Bayes():
    # ### Defining reference Output
    Railway_Traction = load(join(DATA_DIR, "Machine", "Railway_Traction.json"))

    # Definition of the enforced output of the electrical module
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
    simu = Simu1(name="test_zdt3", machine=Railway_Traction)

    simu.input = InputCurrent(
        Is=Is,
        Ir=Ir,  # zero current for the rotor
        OP=OPslip(N0=N0),
        time=time,
        Na_tot=Na_tot,
        angle_rotor_initial=0.5216 + np.pi,
    )

    # Definition of the magnetic simulation
    simu.mag = MagFEMM(
        type_BH_stator=2,
        type_BH_rotor=2,
        is_periodicity_a=True,
    )
    simu.mag.Kmesh_fineness = 0.01
    # simu.mag.Kgeo_fineness=0.02
    simu.struct = None

    # ### Design variable
    my_vars = []

    def gen_setter(i):
        def new_setter(simu, value):
            simu.input.Ir.value[i] = value

        return new_setter

    for i in range(30):
        my_vars.append(
            OptiDesignVarInterval(
                name="Ir({})".format(i),
                symbol="var_" + str(i),
                space=[0, 1],
                get_value=lambda space: np.random.uniform(*space),
                setter=gen_setter(i),
            )
        )

    # ### Objectives
    objs = [
        OptiObjective(
            symbol="obj1",
            name="Maximization of the torque average",
            keeper="lambda output: output.mag.Tem_av",
        ),
        OptiObjective(
            symbol="obj2",
            name="Minimization of the torque ripple",
            keeper="lambda output: output.mag.Tem_rip_norm",
        ),
    ]

    # ### Evaluation
    def evaluate(output):
        x = output.simu.input.Ir.value
        f1 = lambda x: x[0]
        g = lambda x: 1 + (9 / 29) * np.sum(x[1:])
        h = lambda f1, g: 1 - np.sqrt(f1 / g) - (f1 / g) * np.sin(10 * np.pi * f1)
        output.mag.Tem_av = f1(x)
        output.mag.Tem_rip_norm = g(x) * h(f1(x), g(x))

    # ### Defining the problem
    my_prob = OptiProblem(
        simu=simu, design_var=my_vars, obj_func=objs, eval_func=evaluate
    )

    solver = OptiBayesAlgSmoot(problem=my_prob, nb_start=300, nb_iter=1)
    res = solver.solve()

    #
    fig, axs = plt.subplots(1, 2, figsize=(16, 6))
    try:
        img_to_find = img.imread(
            join(TEST_DIR, "Validation", "Optimization", "zdt3.jpg"), format="jpg"
        )
        axs[1].imshow(img_to_find, aspect="auto")
        axs[1].axis("off")
        axs[1].set_title("Pareto front of the problem")
    except (TypeError, ValueError):
        print("Pillow is needed to import jpg files")

    res.plot_pareto("obj1", "obj2", ax=axs[0], is_show_fig=False)
    axs[0].set_title("Pyleecan results")
    axs[0].set_xlabel(r"$f_1(x)$")
    axs[0].set_ylabel(r"$f_2(x)$")
    fig.savefig(join(save_path, "test_zdt3_bayes.png"))


if __name__ == "__main__":
    test_zdt3_Bayes()

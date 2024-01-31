# -*- coding: utf-8 -*-
import csv
from multiprocessing import cpu_count
from os.path import join

import matplotlib.pyplot as plt
import numpy as np
import pytest
from numpy import exp, mean, meshgrid, pi, real, zeros
from numpy.testing import assert_array_almost_equal
from SciDataTool import Data1D, DataTime, VectorField

from pyleecan.Classes.ForceTensor import ForceTensor
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.SolutionVector import SolutionVector
from pyleecan.definitions import DATA_DIR
from pyleecan.Functions.load import load
from Tests import save_plot_path as save_path

DELTA = 1e-6


@pytest.mark.skip
@pytest.mark.SIPMSM
@pytest.mark.periodicity
@pytest.mark.long_5s
@pytest.mark.ForceTensor
@pytest.mark.MeshSol
def test_Benchmark_Tensor():
    """Validation of the AGSF spectrum calculation for IPMSM machine"""

    # Load machine
    Benchmark = load(join(DATA_DIR, "Machine", "Benchmark.json"))
    # Prepare simulation
    simu = Simu1(name="Benchmark_Tensor", machine=Benchmark)

    simu.input = InputCurrent(
        OP=OPdq(N0=1200, Id_ref=0, Iq_ref=0),
        Ir=None,
        Na_tot=2 ** 6,
        Nt_tot=1,
    )

    simu.elec = None

    simu.mag = MagFEMM(
        type_BH_stator=1,  # 0 for saturated
        type_BH_rotor=1,
        is_periodicity_a=False,
        is_periodicity_t=False,
        is_get_meshsolution=True,
        is_sliding_band=False,
        # nb_worker=cpu_count(),
        Kmesh_fineness=1,
    )
    simu.force = ForceTensor(
        is_periodicity_a=False,
        is_periodicity_t=False,
        tensor={
            "magnetostriction": True,
        },
    )

    # Run simulation
    out = simu.run()

    # CSV import
    path = save_path.replace("Results/Plot", "Data/Benchmark_model_stator_ms.csv")
    with open(path, "r") as file:
        reader = csv.reader(file, skipinitialspace=True)
        l1 = next(reader)
        l2 = next(reader)
        l3 = next(reader)
        nb_node = int(l2[1])
        dim = int(l2[2])
        Nt_tot = int(l2[3])
        f2 = np.zeros((nb_node, dim))
        node_number_list = []
        indices_nodes = []
        for row in reader:
            f2[int(row[0])][0] = 1000 * float(row[3])
            f2[int(row[0])][1] = 1000 * float(row[4])
            node_number_list.append(int(row[10]))
            indices_nodes.append(int(row[11]))

    # Little trick to reshape f2 so that it can be compared to f, since Indices_Points2 isn't taken into account yet
    _, _, connectivity = np.intersect1d(
        indices_nodes, node_number_list, return_indices=True
    )
    f2 = f2[connectivity, :]

    f2 = f2.reshape((Nt_tot, nb_node, dim))

    components2 = {}
    Indices_Point2 = Data1D(
        name="indice", values=np.array(node_number_list), is_components=True
    )

    Time = out.force.meshsolution.get_solution().field.get_axes()[0]

    fx2_data = DataTime(
        name="Nodal force 2 (x)",
        unit="N",
        symbol="Fx2",
        axes=[Time, Indices_Point2],
        values=f2[..., 0],
    )
    components2["comp_x"] = fx2_data

    fy2_data = DataTime(
        name="Nodal force 2 (y)",
        unit="N",
        symbol="Fy2",
        axes=[Time, Indices_Point2],
        values=f2[..., 1],
    )
    components2["comp_y"] = fy2_data

    vec_force2 = VectorField(name="Nodal forces 2", symbol="F2", components=components2)
    solforce2 = SolutionVector(field=vec_force2, type_element="node", label="F2")
    out.force.meshsolution.solution.append(solforce2)

    out.force.meshsolution.plot_glyph(
        label="F",
        is_point_arrow=True,
        # is_show_fig=True,
        save_path=join(save_path, "magneto_plot_glyph.png"),
    )

    out.force.meshsolution.plot_glyph(
        label="F2",
        is_point_arrow=True,
        # is_show_fig=True,
        save_path=join(save_path, "magneto_plot_glyph2.png"),
    )

    # Comparisons

    computed_forces_x = (
        out.force.meshsolution.get_solution().field.components["comp_x"].values
    )
    reference_forces_x = f2[..., 0]
    computed_forces_y = (
        out.force.meshsolution.get_solution().field.components["comp_y"].values
    )
    reference_forces_y = f2[..., 1]

    relevant_mask_x = reference_forces_x > 1e-3 * np.max(reference_forces_x)
    relevant_mask_y = reference_forces_y > 1e-3 * np.max(reference_forces_y)

    relevant_computed_forces_x = computed_forces_x[relevant_mask_x]
    relevant_reference_forces_x = reference_forces_x[relevant_mask_x]
    relevant_computed_forces_y = computed_forces_y[relevant_mask_y]
    relevant_reference_forces_y = reference_forces_y[relevant_mask_y]

    big_diff_mask_x = np.logical_and(
        np.abs(computed_forces_x - reference_forces_x) / np.abs(reference_forces_x)
        > 0.2,
        np.abs(computed_forces_x - reference_forces_x) / np.abs(reference_forces_x)
        < 1.5,
    )
    big_diff_mask_y = np.logical_and(
        np.abs(computed_forces_y - reference_forces_y) / np.abs(reference_forces_y)
        > 0.2,
        np.abs(computed_forces_y - reference_forces_y) / np.abs(reference_forces_y)
        < 1.5,
    )

    big_diff_x = np.where(
        big_diff_mask_x,
        computed_forces_x - reference_forces_x,
        np.zeros(computed_forces_x.shape),
    )
    big_diff_y_x = np.where(
        big_diff_mask_x,
        computed_forces_y - reference_forces_y,
        np.zeros(computed_forces_y.shape),
    )

    components_diff_x = {}
    fx_diff_data = DataTime(
        name="Nodal force diff x (x)",
        unit="N",
        symbol="Fxdx",
        axes=[Time, Indices_Point2],
        values=big_diff_x,
    )
    components_diff_x["comp_x"] = fx_diff_data

    fy_diff_data = DataTime(
        name="Nodal force diff x (y)",
        unit="N",
        symbol="Fydx",
        axes=[Time, Indices_Point2],
        values=big_diff_y_x,
    )
    components_diff_x["comp_y"] = fx_diff_data

    vec_force_dx = VectorField(
        name="Nodal forces dx", symbol="Fdx", components=components_diff_x
    )
    solforce_dx = SolutionVector(field=vec_force_dx, type_element="node", label="Fdx")
    out.force.meshsolution.solution.append(solforce_dx)

    out.force.meshsolution.plot_glyph(
        label="Fdx",
        is_point_arrow=True,
        # is_show_fig=True,
        save_path=join(save_path, "magneto_plot_glyph2.png"),
    )

    return out


if __name__ == "__main__":
    out = test_Benchmark_Tensor()

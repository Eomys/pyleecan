from genericpath import exists
from os.path import join, exists

import pytest

import numpy as np
from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.Simu1 import Simu1
from pyleecan.Classes.OPdq import OPdq
from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Loss import Loss
from pyleecan.Classes.LossModelSteinmetz import LossModelSteinmetz
from pyleecan.Classes.VarLoadCurrent import VarLoadCurrent


from pyleecan.Functions.load import load

from pyleecan.definitions import DATA_DIR

from SciDataTool.Functions.Plot.plot_2D import plot_2D


is_show_fig = False


@pytest.mark.long_5s
@pytest.mark.FEMM
@pytest.mark.MagFEMM
@pytest.mark.periodicity
@pytest.mark.SPMSM
@pytest.mark.SingleOP
@pytest.mark.Loss
@pytest.mark.skip(reason="Work in progress")
def test_FEMM_Loss_Prius():
    """Test to calculate losses in Toyota_Prius for different values of input current"""

    machine = load(join(DATA_DIR, "Machine", "Toyota_Prius.json"))

    simu = Simu1(name="Multi simulation with varying current", machine=machine)

    SPEED = 1200

    OP_MATRIX = np.array(
        [
            [SPEED, 0, 0],
            [SPEED, -200, 0],
            [SPEED, 0, 200],
            [SPEED, -125, 125],
            [SPEED, -50, 100],
            [SPEED, -150, 100],
        ]
    )
    simu.var_simu = VarLoadCurrent(
        OP_matrix=OP_MATRIX, type_OP_matrix=1, is_keep_all_output=True
    )

    simu.input = InputCurrent(
        Nt_tot=4 * 10 * 8 * 5,
        Na_tot=200 * 8,
        OP=OPdq(),
        is_periodicity_t=True,
        is_periodicity_a=True,
    )
    simu.input.set_OP_from_array(OP_MATRIX, type_OP_matrix=1)

    simu.mag = MagFEMM(
        is_periodicity_a=True,
        is_periodicity_t=True,
        nb_worker=4,
        is_get_meshsolution=True,
        is_fast_draw=True,
        is_calc_torque_energy=False,
    )

    simu.loss = Loss(
        is_get_meshsolution=True,
        Tsta=100,
        model_dict={
            "stator core": LossModelSteinmetz(group="stator core"),
            "rotor core": LossModelSteinmetz(group="rotor core"),
        },
    )

    xout = simu.run()

    for i, out in enumerate(xout):
        # if not exists(
        #     "C:\Users\LAP10\Documents\Loss\plot_B_mesh\Id={OP_MATRIX[i,1]}, Iq={OP_MATRIX[i,2]}.gif"
        # ):
        #     out.plot_B_mesh(
        #         is_animated=True,
        #         save_path="C:\Users\LAP10\Documents\Loss\plot_B_mesh\Id={OP_MATRIX[i,1]}, Iq={OP_MATRIX[i,2]}.gif",
        #     )
        out.plot_B_mesh()
        power_dict = {
            "total_power": out.mag.Pem_av,
            "torque": out.mag.Tem_av,
            "current_density": out.elec.get_Jrms() / 1e6,
            **dict(
                [
                    (o.name, o.get_loss_scalar(out.elec.OP.felec))
                    for o in out.loss.loss_list
                ]
            ),
            "efficiency": (
                out.mag.Pem_av
                - out.loss.loss_list[-1].get_loss_scalar(out.elec.OP.felec)
            )
            / out.mag.Pem_av,
        }
        print(power_dict)

    colormap = "jet"
    group_names = ["stator core", "rotor core"]
    out_list = xout.output_list

    for i, out in enumerate(out_list):
        out.loss.loss_list.append(out.loss.loss_list[0] + out.loss.loss_list[1])
        out.loss.loss_list[2].name = f"(Id={OP_MATRIX[i,1]}, Iq={OP_MATRIX[i,2]})"
        out.loss.loss_list[2].get_mesh_solution().plot_contour(
            "freqs=sum",
            label=f"{out.loss.loss_list[2].name}",
            group_names=group_names,
            colormap=colormap,
        )

    for i, out in enumerate(out_list[:-1]):
        for j, other in enumerate(out_list[i + 1 :], start=i + 1):
            out.loss.loss_list.append(out.loss.loss_list[2] - other.loss.loss_list[2])
            out.loss.loss_list[
                -1
            ].name = f"(Id={OP_MATRIX[i,1]}, Iq={OP_MATRIX[i,2]}) - (Id={OP_MATRIX[j,1]}, Iq={OP_MATRIX[j,2]})"
            out.loss.loss_list[-1].get_mesh_solution().plot_contour(
                "freqs=sum",
                label=f"{out.loss.loss_list[-1].name}",
                group_names=group_names,
                colormap=colormap,
            )


# To run it without pytest
if __name__ == "__main__":

    test_FEMM_Loss_Prius()

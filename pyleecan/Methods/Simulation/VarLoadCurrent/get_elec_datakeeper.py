from ....Classes.DataKeeper import DataKeeper
from ....Methods.Simulation.VarLoad.get_elec_datakeeper import (
    get_elec_datakeeper as get_dk,
)
from numpy import abs as np_abs, angle, pi


def get_elec_datakeeper(self):
    """
    Generate DataKeepers to store by default results from electric module

    Parameters
    ----------
    self: VarLoad object

    Returns
    -------
    dk_list: list
        list of DataKeeper
    """
    dk_list = get_dk(self)
    if self.type_OP_matrix == 0:  # I0 and Phi0
        # Save I0
        dk_list.append(
            DataKeeper(
                name="I0",
                symbol="I0",
                unit="A",
                keeper=lambda output: np_abs(
                    output.elec.Id_ref + 1j * output.elec.Iq_ref
                ),
            )
        )
        # Save Phi0
        dk_list.append(
            DataKeeper(
                name="Phi0",
                symbol="Phi0",
                unit="",
                keeper=lambda output: angle(
                    output.elec.Id_ref + 1j * output.elec.Iq_ref
                )
                % (2 * pi),
            )
        )
    # Keep torque
    if self.is_torque:
        dk_list.append(
            DataKeeper(
                name="Reference Average Torque",
                symbol="Tem_av_ref",
                unit="N.m",
                keeper=lambda output: output.elec.Tem_av_ref,
            )
        )

    # TODO Save power
    # if self.is_power:
    #     datakeeper_list.append(
    #         DataKeeper(
    #             name="Power",
    #             symbol="Tem",
    #             unit="N.m",
    #             keeper=lambda output: output.simu.mag.power,
    #         ),
    #     )

    return dk_list

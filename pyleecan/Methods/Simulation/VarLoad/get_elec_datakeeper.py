from ....Classes.DataKeeper import DataKeeper


def get_elec_datakeeper(self):
    """
    Generate DataKeepers to store by default results from electric module

    Parameters
    ----------
    self: VarLoadFlux object

    Returns
    -------
    dk_list: list
        list of DataKeeper
    """
    dk_list = []
    # Save Id
    dk_list.append(
        DataKeeper(
            name="Id", symbol="Id", unit="A", keeper=lambda output: output.elec.Id_ref
        )
    )
    # Save Iq
    dk_list.append(
        DataKeeper(
            name="Iq", symbol="Iq", unit="A", keeper=lambda output: output.elec.Iq_ref
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

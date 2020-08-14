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

    return dk_list

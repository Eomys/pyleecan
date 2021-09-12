from ....Classes.DataKeeper import DataKeeper


def get_elec_datakeeper(self, symbol_list, is_multi=False):
    """
    Generate DataKeepers to store by default results from electric module

    Parameters
    ----------
    self: VarLoad
        A VarLoad object
    symbol_list : list
        List of the existing datakeeper (to avoid duplicate)
    is_multi : bool
        True for multi-simulation of multi-simulation

    Returns
    -------
    dk_list: list
        list of DataKeeper
    """
    dk_list = []
    # Save Id
    if not is_multi and "Id" not in symbol_list:
        dk_list.append(
            DataKeeper(
                name="Id",
                symbol="Id",
                unit="Arms",
                keeper="lambda output: output.elec.Id_ref",
            )
        )
    # Save Iq
    if not is_multi and "Iq" not in symbol_list:
        dk_list.append(
            DataKeeper(
                name="Iq",
                symbol="Iq",
                unit="Arms",
                keeper="lambda output: output.elec.Iq_ref",
            )
        )

    return dk_list

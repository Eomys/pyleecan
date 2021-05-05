from ....Classes.DataKeeper import DataKeeper


def get_force_datakeeper(self, symbol_list, is_multi=False):
    """
    Generate DataKeepers to store by default results from force module

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

    return dk_list

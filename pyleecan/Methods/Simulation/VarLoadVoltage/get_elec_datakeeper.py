from numpy import isnan

from ....Functions.Simulation.VarSimu.get_elec_datakeeper_dict import (
    get_elec_datakeeper_dict,
)


def get_elec_datakeeper(self, symbol_list, is_multi=False):
    """Generate DataKeepers to store by default results from electric module
    Parameters
    ----------
    self: VarLoadVoltage
        A VarLoadVoltage object
    symbol_list : list
        List of the existing datakeeper (to avoid duplicate)
    is_multi : bool
        True for multi-simulation of multi-simulation
    Returns
    -------
    dk_list: list
        list of DataKeeper
    """

    dk_dict = get_elec_datakeeper_dict()
    dk_list = []

    if not is_multi:
        if self.type_OP_matrix == 0:  # U0 and Phi0
            quantity_list = ["U0", "UPhi0", "Ud", "Uq"]
        elif self.type_OP_matrix == 1:  # Id and Iq
            quantity_list = ["Ud", "Uq"]
        elif self.type_OP_matrix == 2:  # Id and Iq
            quantity_list = ["U0", "Ud", "Uq", "slip"]

        if self.OP_matrix.shape[1] > 3 and not isnan(self.OP_matrix[0, 3]):
            quantity_list.append("Tem_av_ref")

    # Save Id
    if not is_multi:
        for key in quantity_list:
            if key not in symbol_list:
                dk_list.append(dk_dict[key])

    return dk_list

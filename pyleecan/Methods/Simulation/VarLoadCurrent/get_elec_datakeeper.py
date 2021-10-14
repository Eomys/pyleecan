from ....Classes.DataKeeper import DataKeeper
from ....Classes.VarLoad import VarLoad


def get_elec_datakeeper(self, symbol_list, is_multi=False):
    """
    Generate DataKeepers to store by default results from electric module

    Parameters
    ----------
    self: VarLoadCurrent
        A VarLoadCurrent object
    symbol_list : list
        List of the existing datakeeper (to avoid duplicate)
    is_multi : bool
        True for multi-simulation of multi-simulation

    Returns
    -------
    dk_list: list
        list of DataKeeper
    """
    dk_list = VarLoad.get_elec_datakeeper(self, symbol_list)
    if self.type_OP_matrix == 0:  # I0 and Phi0
        if not is_multi and "I0" not in symbol_list:
            # Save I0
            dk_list.append(
                DataKeeper(
                    name="I0",
                    symbol="I0",
                    unit="A",
                    keeper="lambda output: output.elec.OP.get_I0_Phi0()['I0']",
                )
            )
        # Save Phi0
        if not is_multi and "Phi0" not in symbol_list:
            dk_list.append(
                DataKeeper(
                    name="Phi0",
                    symbol="Phi0",
                    unit="",
                    keeper="lambda output: output.elec.OP.get_I0_Phi0()['Phi0']",
                )
            )
    # Keep torque
    if not is_multi and self.OP_matrix.shape[1] > 3 and "Tem_av_ref" not in symbol_list:
        dk_list.append(
            DataKeeper(
                name="Reference Average Torque",
                symbol="Tem_av_ref",
                unit="N.m",
                keeper="lambda output: output.elec.Tem_av_ref",
            )
        )

    # Keep power
    if not is_multi and self.OP_matrix.shape[1] > 4 and "Pem_av_ref" not in symbol_list:
        dk_list.append(
            DataKeeper(
                name="Reference Power",
                symbol="Pem_av_ref",
                unit="W",
                keeper="lambda output: output.elec.Pem_av_ref",
            )
        )

    return dk_list

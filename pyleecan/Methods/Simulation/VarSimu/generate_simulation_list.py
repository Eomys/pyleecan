class VarSimuError(Exception):
    pass


def generate_simulation_list(self, ref_simu=None):
    """Generate all the simulation for the multi-simulation

    Parameters
    ----------
    self : VarSimu
        A VarSimu object
    ref_simu : Simulation
        Reference simulation to copy / update

    Returns
    -------
    multisim_dict : dict
        dictionary containing the simulation and paramexplorer list
    """
    raise VarSimuError(
        "VarSimu is an abstract class, please create one of its daughters."
    )

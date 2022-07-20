import itertools
import numpy as np
from ....Classes.ParamExplorerSet import ParamExplorerSet


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

    # Build the list
    setter_list = []  # Store ParamExplorer setters
    params_value_dict = {}  # Store parameter value list per ParamExplorer
    params_symbol_list = []  # Store ParamExplorer symbols
    params_value_list = []  # Store ParamExplorer values to perform cartesian product
    multisim_shape = []

    n_param = 0
    # Add values and shape in the list
    for param_explorer in self.paramexplorer_list:
        n_param += 1
        params_value_dict[param_explorer.symbol] = []
        params_symbol_list.append(param_explorer.symbol)
        setter_list.append(param_explorer.setter)

        # Generate values
        values = param_explorer.get_value()
        params_value_list.append(values)
        multisim_shape.append(len(values))

    multisim_dict = {
        "paramexplorer_list": [],  # Setter's values
        "simulation_list": [],
    }

    # Cartesian product to generate every simulation
    for simu_param_values in itertools.product(*params_value_list):
        # Generate the simulation
        new_simu = ref_simu.copy()

        # Edit it using setter
        for setter, value, symbol in zip(
            setter_list, simu_param_values, params_symbol_list
        ):
            params_value_dict[symbol].append(value)
            setter(new_simu, value)

        # Add the simulation
        multisim_dict["simulation_list"].append(new_simu)

    # Create slices to extract ndarrays from multisim_values
    slices = ()
    for _ in multisim_shape:
        slices += (slice(None),)

    # Create ParamExplorerSet to be stored in XOutput
    for param_explorer in self.paramexplorer_list:
        multisim_dict["paramexplorer_list"].append(
            ParamExplorerSet(init_dict=param_explorer.as_dict(keep_function=True))
        )
        multisim_dict["paramexplorer_list"][-1].value = params_value_dict[
            param_explorer.symbol
        ]

    return multisim_dict

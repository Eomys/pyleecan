import itertools
import numpy as np
from ....Classes.ParamExplorerSet import ParamExplorerSet


def get_simulations(self):
    """Create simulations and returns them

    Returns
    -------
    multisim_dict : dict
        dictionary containing simulation shape, setters, parameter values and simulations generated
    """
    # Get reference simulation
    ref_simu = self.parent

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

    if len(params_value_list) > 0:
        self.nb_simu = 1
        for values in params_value_list:
            self.nb_simu *= len(values)

    multisim_dict = {
        "nb_simu": self.nb_simu,  # Shape simulation
        "paramexplorer_list": [],  # Setter's values
        "simulation_list": [],
    }

    # Cartesian product to generate every simulation
    for simu_param_values in itertools.product(*params_value_list):
        # Generate the simulation
        new_simu = ref_simu.copy()

        # Remove its multisimulation to avoid infinite simulations
        new_simu.var_simu = None

        # Store simulation input_values and setters
        input_values = []

        # Edit it using setter
        for setter, value, symbol in zip(
            setter_list, simu_param_values, params_symbol_list
        ):
            setter(new_simu, value)
            params_value_dict[symbol].append(value)

        # Add the simulation
        multisim_dict["simulation_list"].append(new_simu)

    # Create slices to extract ndarrays from multisim_values
    slices = ()
    for _ in multisim_shape:
        slices += (slice(None),)

    # Create ParamExplorerValue to be stored in XOutput
    for param_explorer in self.paramexplorer_list:
        multisim_dict["paramexplorer_list"].append(
            ParamExplorerSet(
                name=param_explorer.name,
                symbol=param_explorer.symbol,
                unit=param_explorer.unit,
                setter=param_explorer.setter,
                value=params_value_dict[param_explorer.symbol],
            )
        )

    return multisim_dict

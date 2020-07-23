import itertools
import numpy as np
from ....Classes.ParamExplorerValue import ParamExplorerValue


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
    params_setter_list = []
    params_value_list = []
    multisim_shape = []

    n_param = 0
    # Add values and shape in the list
    for param_explorer in self.paramexplorer_list:
        n_param += 1
        params_setter_list.append(param_explorer.setter)
        params_value_list.append(param_explorer.get_value())
        multisim_shape.append(len(param_explorer.value_list))

    if len(params_value_list) > 0:
        self.nb_simu = 1
        for values in params_value_list:
            self.nb_simu *= len(values)

    multisim_dict = {
        "shape": tuple(multisim_shape),  # Shape simulation
        "paramexplorer_list": [],  # Setter's values
        "simulation_list": [],
    }

    multisim_values = np.ndarray(multisim_shape + [n_param], dtype="O")

    idx_simu_list = [range(len(value_list)) for value_list in params_value_list]

    # Cartesian product to generate every simulation
    for idx_simu, simu_param_values in zip(
        itertools.product(*idx_simu_list), itertools.product(*params_value_list)
    ):
        # Generate the simulation
        new_simu = ref_simu.copy()

        # Remove its multisimulation to avoid infinite simulations
        new_simu.var_simu = None

        # Store simulation input_values and setters
        input_values = []

        # Edit it using setter
        for setter, value in zip(params_setter_list, simu_param_values):
            setter(new_simu, value)
            input_values.append(value)

        # Add the simulation
        multisim_values[idx_simu] = input_values
        multisim_dict["simulation_list"].append(new_simu)

    # Create slices to extract ndarrays from multisim_values
    slices = ()
    for _ in multisim_shape:
        slices += (slice(None),)

    # Create ParamExplorerValue to be stored in XOutput
    for i, param_explorer in enumerate(self.paramexplorer_list):
        multisim_dict["paramexplorer_list"].append(
            ParamExplorerValue(
                name=param_explorer.name,
                symbol=param_explorer.symbol,
                unit=param_explorer.unit,
                setter=param_explorer.setter,
                value=np.array(multisim_values[slices + (i,)]),
            )
        )

    return multisim_dict

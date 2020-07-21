import itertools
import numpy as np


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
    params_value_list = []
    params_setter_list = []
    multisim_shape = []
    for param_setter in self.paramsetter_list:
        params_value_list.append(param_setter.value_list)
        params_setter_list.append(param_setter.setter)
        multisim_shape.append(len(param_setter.value_list))

    if len(params_value_list) > 0:
        self.nb_simu = 1
        for values in params_value_list:
            self.nb_simu *= len(values)

    multisim_dict = {
        "shape": multisim_shape,  # Shape simulation
        "setter": params_setter_list,  # Setters
        "value": np.ndarray(multisim_shape, dtype="O"),  # setter's values
        "simulation": np.ndarray(multisim_shape, dtype="O"),
    }

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
        multisim_dict["value"][idx_simu] = input_values
        multisim_dict["simulation"][idx_simu] = new_simu

    return multisim_dict

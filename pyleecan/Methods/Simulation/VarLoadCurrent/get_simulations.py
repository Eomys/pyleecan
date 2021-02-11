import itertools
import numpy as np
from ....Classes.ParamExplorerSet import ParamExplorerSet
from ....Functions.Simulation.VarLoad.setter_simu import setter_simu


def get_simulations(self):
    """Create simulations and ParamExplorer associated

    Returns
    -------
    multisim_dict : dict
        dictionary containing simulation shape, setters, parameter values and simulations generated
    """
    # Get reference simulation
    ref_simu = self.parent

    # Get InputFlux list
    list_input = self.get_input_list()

    # Build the list
    self.nb_simu = len(list_input)

    multisim_dict = {
        "nb_simu": self.nb_simu,  # Shape simulation
        "paramexplorer_list": [],  # Setter's values
        "simulation_list": [],
    }

    # Create Simulations 1 per load
    for input_obj in list_input:
        # Generate the simulation
        new_simu = ref_simu.copy()
        # set the next multisimulation layer
        # TODO this will break the 'parent' prop., so this have to be investigated
        # TODO maybe a copy of var_simu could solve this but it may break the setters
        if ref_simu.var_simu.var_simu is not None:
            new_simu.var_simu = ref_simu.var_simu.var_simu
        else:
            new_simu.var_simu = None

        # Edit simulation
        # setter current
        setter_simu(new_simu, input_obj)
        # Add simulation to the list
        multisim_dict["simulation_list"].append(new_simu)

    # Create ParamExplorerSet
    #   This version uses a single ParamExplorerSet to define the simulation
    #   Other parameters can be stored in a dedicated ParamExplorerSet if needed
    multisim_dict["paramexplorer_list"].append(
        ParamExplorerSet(
            name="InputCurrent",
            symbol="",
            unit="",
            setter=setter_simu,
            value=list_input,
        )
    )

    # Generate default datakeeper
    self.gen_datakeeper_list()

    return multisim_dict

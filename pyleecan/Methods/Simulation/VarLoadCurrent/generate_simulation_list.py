from ....Classes.ParamExplorerSet import ParamExplorerSet


def generate_simulation_list(self, ref_simu=None):
    """Generate all the simulation for the multi-simulation

    Parameters
    ----------
    self : VarLoadCurrent
        A VarLoadCurrent object
    ref_simu : Simulation
        Reference simulation to copy / update

    Returns
    -------
    multisim_dict : dict
        dictionary containing the simulation and paramexplorer list
    """

    # Get InputCurrent list
    list_input = self.get_input_list()

    multisim_dict = {
        "paramexplorer_list": [],  # Setter's values
        "simulation_list": [],
    }

    # Create Simulations 1 per load
    for input_obj in list_input:
        # Generate the simulation
        new_simu = ref_simu.copy()

        # Edit simulation
        new_simu.input = input_obj
        # Add simulation to the list
        multisim_dict["simulation_list"].append(new_simu)

    # Create ParamExplorerSet
    #   This version uses a single ParamExplorerSet to define the simulation
    #   Other parameters can be stored in a dedicated ParamExplorerSet if needed
    multisim_dict["paramexplorer_list"].append(
        ParamExplorerSet(
            name="InputCurrent",
            symbol="In",
            unit="-",
            setter="simu.input",
            getter="simu.input",
            value=list_input,
        )
    )

    return multisim_dict

from ....Classes.ParamExplorerSet import ParamExplorerSet
from ....Classes.PostCleanVS import PostCleanVS

from ....Methods.Simulation.Simulation import reuse_list


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

    # Update is_reuse for all parameters in REUSE_LIST if needed
    for attr in reuse_list:
        if getattr(self, attr) is None:
            # If is_reuse is not forced by user, set it to True
            setattr(self, attr, True)

    # Don't reuse eccentricity model if slice model is not reused
    if self.is_reuse_eccentricity is True and self.is_reuse_slice is False:
        self.get_logger().info(
            "Reset self.is_reuse_eccentricity to False if self.is_reuse_slice is False"
        )
    self.is_reuse_eccentricity = self.is_reuse_slice

    # Get InputCurrent list
    list_input = self.get_input_list()

    multisim_dict = {
        "paramexplorer_list": [],  # Setter's values
        "simulation_list": [],
    }

    # Create Simulations 1 per load
    for input_obj in list_input:
        # Generate the simulation
        new_simu = ref_simu.copy(keep_function=True)

        # Edit simulation
        new_simu.input = input_obj
        # Add simulation to the list
        multisim_dict["simulation_list"].append(new_simu)

    # Automatically clean what is not releavant for VS post
    if self.is_clean:
        if self.post_keeper_postproc_list is None:
            self.post_keeper_postproc_list = list()
        self.post_keeper_postproc_list.append(PostCleanVS())

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

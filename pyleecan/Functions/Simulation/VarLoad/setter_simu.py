def setter_simu(simu, input_obj):
    """Set simulation input with input_obj
    
    Parameters
    ----------
    simu: Simulation
        Pyleecan Simulation
    input_obj: Input
        Object defining the starting point of the simulation 
    """

    simu.input = input_obj

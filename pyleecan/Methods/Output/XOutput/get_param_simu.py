def get_param_simu(self, idx):
    """
    Return the list of parameter values for a specific simulation
    """
    assert len(idx) == len(self.shape)

    # Create a list to store values
    param_value = []
    for pe in self.paramexplorer_list:
        param_value.append(pe.value[idx])

    return param_value

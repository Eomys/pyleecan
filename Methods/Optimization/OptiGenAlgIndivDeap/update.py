def update(self):
    """Update the individual output after the mutation"""

    # Sort the keys to ensure the right order in the list
    keys = list(self.design_var.keys())
    keys.sort()

    is_change = False
    for k in range(len(keys)):
        if eval("self." + self.design_var[keys[k]].name + "!=self[k]"):
            exec("self." + self.design_var[keys[k]].name + "=self[k]")
            is_change = True

    # Delete the fitness if a change occurred
    if is_change:
        del self.fitness.values

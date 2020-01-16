def update(indiv):
    """Update the individual output after the mutation"""

    is_change = False
    for k in range(len(indiv.keys)):
        if eval("indiv." + indiv.design_var[indiv.keys[k]].name + "!=indiv[k]"):
            exec("indiv." + indiv.design_var[indiv.keys[k]].name + "=indiv[k]")
            is_change = True

    # Delete the fitness if a change occurred
    if is_change:
        del indiv.fitness.values

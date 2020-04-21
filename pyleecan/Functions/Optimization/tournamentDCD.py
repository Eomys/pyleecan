from random import sample, choice


def choseDCD(indiv_1, indiv_2):
    """Chose between two individuals
    
        Parameters
        ----------
        indiv_1 : individual 
        indiv_2 : individual 

        Returns
        -------
        individual selected

    """
    if indiv_1.cstr_viol == 0 and indiv_2.cstr_viol > 0:  # only indiv_1 feasible
        return indiv_1
    elif indiv_1.cstr_viol > 0 and indiv_2.cstr_viol == 0:  # only indiv_2 feasible
        return indiv_2
    elif (
        indiv_1.cstr_viol > 0 and indiv_2.cstr_viol > 0
    ):  # indiv_1 and indiv_2 unfeasible
        # Compare the number of constraint violations
        if indiv_1.cstr_viol < indiv_2.cstr_viol:
            return indiv_1
        elif indiv_1.cstr_viol > indiv_2.cstr_viol:
            return indiv_2
        else:
            return choice([indiv_1, indiv_2])
    else:  # Both indiv feasible
        # Check domination, else check crowding distance, else random choice
        if indiv_1.fitness.dominates(indiv_2.fitness):
            return indiv_1
        elif indiv_2.fitness.dominates(indiv_1.fitness):
            return indiv_2
        elif indiv_1.fitness.crowding_dist > indiv_2.fitness.crowding_dist:
            return indiv_1
        elif indiv_1.fitness.crowding_dist < indiv_2.fitness.crowding_dist:
            return indiv_2
        else:
            return choice([indiv_1, indiv_2])


def tournamentDCD(pop, size):
    """Select individuals from the population with a tournament based on the domination and the crowding distance
        This function is inspired by DEAP selTournamentDCD function at https://github.com/DEAP/deap/blob/master/deap/tools/emo.py

        Parameters
        ----------
        pop : list
            list of individuals created with the DEAP toolbox

        size : int 
            number of individual to select

        Returns
        -------
        selection : list
            list of individuals selected
    """

    if len(pop) % 4 != 0:
        raise ValueError("TournamentDCD: pop length must be a multiple of 4")

    if size % 4 != 0:
        raise ValueError(
            "TournamentDCD: number of individuals to select must be a multiple of 4"
        )

    # Sample the population
    indiv_1 = sample(pop, len(pop))
    indiv_2 = sample(pop, len(pop))

    selection = []

    # Select individuals
    for i in range(0, size, 4):
        selection.append(choseDCD(indiv_1[i], indiv_1[i + 1]))
        selection.append(choseDCD(indiv_2[i], indiv_2[i + 1]))
        selection.append(choseDCD(indiv_1[i + 2], indiv_1[i + 3]))
        selection.append(choseDCD(indiv_2[i + 2], indiv_2[i + 3]))

    return selection

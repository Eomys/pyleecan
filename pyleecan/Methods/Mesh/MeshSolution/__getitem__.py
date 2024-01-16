from pyleecan.Classes.Solution import Solution


def __getitem__(self, label) -> Solution:
    """Mimic dict behaviour

    Parameters
    ----------
    label : str
        label of the solution

    Returns
    -------
    Solution
        solution stored in solution_dict
    """
    try:
        return self.solution_dict[label]
    except KeyError:
        keys = list(self.keys())
        if keys:
            raise KeyError(
                f'Wrong solution label "{label}", please use one of the following values: {keys}.'
            )
        else:
            raise KeyError(
                f'Wrong solution label "{label}", the MeshSolution is empty.'
            )

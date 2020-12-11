class VarSimuError(Exception):
    pass


def get_simulations(self):
    """Check VarParam parameters validity"""
    raise VarSimuError(
        "VarSimu is an abstract class, please create one of its daughters."
    )

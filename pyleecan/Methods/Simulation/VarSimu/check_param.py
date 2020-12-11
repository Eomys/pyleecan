class VarSimuError(Exception):
    pass


def check_param(self):
    """Check VarParam parameters validity"""
    raise VarSimuError(
        "VarSimu is an abstract class, please create one of its daughters."
    )

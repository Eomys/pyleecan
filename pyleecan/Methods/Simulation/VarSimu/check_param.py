from ....Classes.Simulation import Simulation


class VarSimuError(Exception):
    pass


def check_param(self):
    """Check VarParam parameters validity"""
    if type(self).__name__ == "VarSimu":
        raise VarSimuError(
            "VarSimu is an abstract class, please create one of its daughters."
        )

    # Check for simulation or VarSimu
    if self.parent is None or (
        not isinstance(self.parent, Simulation) and not hasattr(self.parent, "var_simu")
    ):
        raise VarSimuError(
            "VarSimu object must be inside a Simulation object "
            + " or a VarSimu object."
        )

    # Check for infinite loops
    if self.var_simu is not None:
        pass

from ....Functions.Load.import_class import import_class


class VarSimuError(Exception):
    pass


def check_param(self):
    """Check VarParamSweep parameters validity"""
    if type(self).__name__ == "VarSimu":
        raise VarSimuError(
            "VarSimu is an abstract class, please create one of its daughters."
        )

    Simulation = import_class("pyleecan.Classes", "Simulation")
    # Check for simulation or VarSimu
    if self.parent is None or not isinstance(self.parent, Simulation):
        raise VarSimuError("VarSimu object must be inside a Simulation object")

from ..Functions.Load.import_class import import_class


def copy(self, **kwargs):
    """Return a copy of the class"""

    # To avoid copying big data in Simulation object
    Simulation = import_class("pyleecan.Classes", "Simulation")
    if isinstance(self, Simulation):
        # Remove big object from simulation
        if hasattr(self, "elec") and self.elec is not None:
            # LUT
            LUT = self.elec.LUT_enforced
            self.elec.LUT_enforced = None

        # Copy
        other = type(self)(init_dict=self.as_dict(**kwargs))

        # Reset pointer
        if hasattr(self, "elec") and self.elec is not None:
            # LUT
            self.elec.LUT_enforced = LUT
            other.elec.LUT_enforced = LUT

        return other

    else:
        return type(self)(init_dict=self.as_dict(**kwargs))

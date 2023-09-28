from ....Classes.OutForce import OutForce
from ....Classes.InputCurrent import InputCurrent
from ....Methods.Simulation.Input import InputError


def gen_input(self):
    """Generate the input for the structural module (skip force computation)

    Parameters
    ----------
    self : InputForce
        An InputForce object
    """

    if self.parent.parent is None:
        raise InputError("The Simulation object must be in an Output object to run")

    if self.AGSF is None and self.AGSF_enforced is None:
        raise InputError("Input AGSF are missing")
    else:
        # generate OutElec from parent InputCurrent
        super(type(self), self).gen_input()

        # generate OutForce
        outforce = OutForce()

        if self.AGSF_enforced is not None:
            outforce.AGSF = self.AGSF_enforced
        else:
            if self.AGSF.name is None:
                self.AGSF.name = "Magnetic airgap surface force"
            if self.AGSF.symbol is None:
                self.AGSF.symbol = "AGSF"
            AGSF = self.AGSF.get_data()
            outforce.AGSF = AGSF

        # Update axes_dict
        outforce.axes_dict = dict()
        axes_list = outforce.AGSF.get_axes()
        for ax in axes_list:
            outforce.axes_dict[ax.name] = ax

        # Save the Output in the correct place
        self.parent.parent.force = outforce

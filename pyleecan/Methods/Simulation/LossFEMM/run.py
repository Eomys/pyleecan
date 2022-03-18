from ....Classes.OutLossFEMM import OutLossFEMM

from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the LossFEMM module"""
    if self.parent is None:
        raise InputError("The Loss object must be in a Simulation object to run")
    if self.parent.parent is None:
        raise InputError("The Loss object must be in an Output object to run")

    self.get_logger().info("Running LossFEMM module")

    # get output
    output = self.parent.parent

    axes_dict = self.comp_axes(output)

    output.loss = OutLossFEMM()

    out_dict = self.comp_loss(output, axes_dict)

    output.loss.store(out_dict, axes_dict, self.is_get_meshsolution)

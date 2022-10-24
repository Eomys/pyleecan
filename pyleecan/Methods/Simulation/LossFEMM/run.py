from ....Classes.LossModelMagnet import LossModelMagnet
from ....Classes.LossModelProximity import LossModelProximity
from ....Classes.LossModelSteinmetz import LossModelSteinmetz
from ....Classes.LossModelJoule import LossModelJoule
from ....Methods.Simulation.Input import InputError


def run(self):
    """Run the LossFEMM module

    Paramaters
    ----------
    self : LossFEMM
        A LossFEMM object
    """
    if self.parent is None:
        raise InputError("The Loss object must be in a Simulation object to run")
    if self.parent.parent is None:
        raise InputError("The Loss object must be in an Output object to run")

    self.get_logger().info("Running LossFEMM module")

    # get output
    output = self.parent.parent
    machine = output.simu.machine
    axes_dict = self.comp_axes(output)

    # Define all relevant loss models
    self.model_dict = {
        "stator core": LossModelSteinmetz(
            group="stator core", k_hy=self.k_hy, k_ed=self.k_ed, alpha_f=1, alpha_B=2
        ),
        "rotor core": LossModelSteinmetz(
            group="rotor core", k_hy=self.k_hy, k_ed=self.k_ed, alpha_f=1, alpha_B=2
        ),
        "joule": LossModelJoule(
            group="stator winding", type_skin_effect=self.type_skin_effect
        ),
        "proximity": LossModelProximity(group="stator winding", k_p=self.k_p),
    }
    if machine.is_synchronous() and machine.rotor.has_magnet():
        self.model_dict["magnets"] = LossModelMagnet(group="rotor magnets")

    # Store calls "comp_loss" on each model from model_dict
    output.loss.store(
        self.model_dict,
        axes_dict,
        self.is_get_meshsolution,
        Tsta=self.Tsta,
    )

    # Add overall by adding all losses sources
    output.loss.loss_list.append(sum(output.loss.loss_list))
    output.loss.loss_list[-1].name = "overall"

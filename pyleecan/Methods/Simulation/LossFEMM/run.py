from pyleecan.Classes.LossModelMagnet import LossModelMagnet
from pyleecan.Classes.LossModelProximity import LossModelProximity
from pyleecan.Classes.LossModelSteinmetz import LossModelSteinmetz
from pyleecan.Classes.LossModelWinding import LossModelWinding
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

    self.model_dict = {
        "stator core": LossModelSteinmetz(
            group="stator core", k_hy=self.Ch, k_ed=self.Ce, alpha_f=1, alpha_B=2
        ),
        "rotor core": LossModelSteinmetz(
            group="rotor core", k_hy=self.Ch, k_ed=self.Ce, alpha_f=1, alpha_B=2
        ),
        "joule": LossModelWinding(
            group="stator winding", type_skin_effect=self.type_skin_effect
        ),
        "proximity": LossModelProximity(group="stator winding"),
        "magnets": LossModelMagnet(group="rotor magnets"),
    }

    output.loss.store(
        self.model_dict,
        axes_dict,
        self.is_get_meshsolution,
        Tsta=self.Tsta,
    )

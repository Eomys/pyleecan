from ....Methods.Simulation.Input import InputError
from numpy import linspace, sqrt, pi
from scipy.stats import norm


def get_distribution(self):
    """Returns the slice distribution

    Parameters
    ----------
    self : SliceModel
        a SliceModel object

    Returns
    -------
    z_list : list
        list of slice positions (to be multiplied by lamination length)
    """

    if self.Nslices == 1:
        z_list = [0]

    else:
        type_distribution = self.type_distribution

        if type_distribution not in ["uniform", "gauss", "user-defined"]:
            raise InputError(
                "Unknow skew slice distribution: "
                + type_distribution
                + ". Choose from "
                "uniform"
                ", "
                "gauss"
                " or "
                "user-defined"
                ""
            )

        if type_distribution == "uniform":
            z_list = linspace(-0.5, 0.5, self.Nslices).tolist()

        elif type_distribution == "gauss":
            Npoints = self.Nslices
            if Npoints % 2 == 0:
                x = linspace(-1, 0, int(Npoints))
                dist = norm.pdf(x, 0, 1)
                # Rescale so that max = 0.5
                dist = dist / (1 / sqrt(2 * pi) - dist[0]) * 0.5
                dist_list = (dist - dist[-1]).tolist()
                z_list = [z for (i, z) in enumerate(dist_list) if i % 2 == 0]
                z_list = z_list + [-z for z in reversed(z_list)]
            else:
                x = linspace(-1, 0, int((Npoints + 1) / 2))
                dist = norm.pdf(x, 0, 1)
                # Rescale so that max = 0.5
                dist = dist / (1 / sqrt(2 * pi) - dist[0]) * 0.5
                z_list = (dist - dist[-1]).tolist()
                z_list = z_list[:-1] + [-z for z in reversed(z_list)]

        elif type_distribution == "user-defined":
            if self.z_list is None:
                raise InputError(
                    "Missing z_list for skew user-defined slice distribution"
                )
            for z in self.z_list:
                if z < -0.5 or z > 0.5:
                    raise InputError(
                        "In skew model with user-defined distribution: z_list should be distributed between -0.5 and 0.5"
                    )
            z_list = self.z_list

    return z_list

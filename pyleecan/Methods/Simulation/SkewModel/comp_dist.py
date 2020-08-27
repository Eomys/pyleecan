# -*- coding: utf-8 -*-

from ....Methods.Simulation.Input import InputError
from numpy import linspace, sqrt, pi
from scipy.stats import norm


def comp_dist(self, is_odd=False, is_even=False):
    """Computes the slice distribution 
    
    Parameters
    ----------
    self : SkewModel
        a SkewModel object
    is_odd : bool
        if at least one lamination is vshape
    is_even : bool
        if at least one lamination is step

    Returns
    -------
    z_list : list
        list of slice positions (to be multiplied by lamination length)
    """

    logger = self.get_logger()
    if is_odd and self.Nslices % 2 == 0:
        logger.warning(
            "WARNING: Nslices should be odd for step v-shape skew, adding one slice."
        )
        self.Nslices = self.Nslices + 1
    elif is_even and self.Nslices % 2 != 0:
        logger.warning(
            "WARNING: Nslices should be even for v-shape skew, adding one slice."
        )
        self.Nslices = self.Nslices + 1

    if self.type_dist == "uniform":
        self.z_list = linspace(-0.5, 0.5, self.Nslices + 1).tolist()

    elif self.type_dist == "gauss":
        Npoints = self.Nslices + 1
        if Npoints % 2 == 0:
            x = linspace(-1, 0, int(Npoints))
            dist = norm.pdf(x, 0, 1)
            # Rescale so that max = 0.5
            dist = dist / (1 / sqrt(2 * pi) - dist[0]) * 0.5
            dist_list = (dist - dist[-1]).tolist()
            z_list = [z for (i, z) in enumerate(dist_list) if i % 2 == 0]
            self.z_list = z_list + [-z for z in reversed(z_list)]
        else:
            x = linspace(-1, 0, int((Npoints + 1) / 2))
            dist = norm.pdf(x, 0, 1)
            # Rescale so that max = 0.5
            dist = dist / (1 / sqrt(2 * pi) - dist[0]) * 0.5
            z_list = (dist - dist[-1]).tolist()
            self.z_list = z_list[:-1] + [-z for z in reversed(z_list)]

    elif self.type_dist == "user-defined":
        if self.z_list is None:
            raise InputError("Missing z_list for skew user-defined slice distribution")
        for z in self.z_list:
            if z < -0.5 or z > 0.5:
                raise InputError(
                    "In skew model with user-defined distribution: z_list should be distributed between -0.5 and 0.5"
                )
    else:
        raise InputError(
            "Unknow skew slice distribution: " + self.type_dist + ". Choose from "
            "uniform"
            ", "
            "gauss"
            " or "
            "user-defined"
            ""
        )

import numpy as np

from ....Functions.labels import ROTOR_LAB, STATOR_LAB


def comp_loss_time(self, axes_dict, is_mirror):
    """Calculate loss density over time in iron core given by group "stator core" or "rotor core"
    assuming power density is given by a Bertotti model

    The equations are given in :
    A Dynamic Core Loss Model for Soft Ferromagnetic and Power Ferrite Materials in Transient Finite Element Analysis.
    Lin, D. & Zhou, P. & Fu, Weinong & Badics, Zsolt & Cendes, Z.J.. (2004).
    IEEE Transactions on Magnetics. 40. 1318-1321. 10.1109/TMAG.2004.825025.

    Parameters
    ----------
    self: LossModelBertotti
        a LossModelBertotti object
    axes_dict: {Data}
        Dict containing Time (including (anti-)periodicties) and Indices axes used in any Loss module
    is_mirror : bool
        True to mirror magnetic mesh quantities calculate in stator and rotor frames to get the same Time axis

    Returns
    -------
    Pcore_density : ndarray
        Core loss density function of time and elements [W/m3]
    Pcore_dict: {ndarray}
        Dict containing the array of core losses over time
    """

    if self.parent.parent.parent is None:
        raise ValueError("Cannot calculate core losses if simu is not in an Output")
    else:
        output = self.parent.parent.parent

    machine = output.simu.machine

    lamination = machine.stator if "stator" in self.group else machine.rotor

    Lst = lamination.L1
    # Taking into account the stacking factor
    if self.is_stacking_factor:
        Kf = lamination.Kf1
    else:
        Kf = 1
    rho = lamination.mat_type.struct.rho

    # Compute the coefficients only if at least one is not provided
    if None in [self.k_hy, self.k_ed, self.k_ex]:
        material = lamination.mat_type
        self.comp_coeff(material)

    # Get loss coefficients
    # The loss data are given in W/kg, but the loss density in pyleecan are computed in W/m^3
    k_hy = self.k_hy * rho  # Not used in Bertotti time-dependant model
    k_ed = self.k_ed * rho
    k_ex = self.k_ex * rho

    # B exponent in hysteresis loss model
    alpha_B = self.alpha_B

    if output.mag is None:
        raise ValueError("Cannot calculate core losses if OutMag is None")

    if output.mag.meshsolution is not None:
        # Case with same time periodicities in both stator and rotor frames
        meshsol = output.mag.meshsolution

    elif output.mag.meshsolution_dict is None:
        raise ValueError(
            "Cannot calculate core losses if OutMag.meshsolution and OutMag.meshsolution_dict are both None"
        )
    else:
        if is_mirror:
            # Rebuild magnet mesh quantities on time steps given by axes_dict
            meshsol = output.mag.get_meshsolution(Time=axes_dict["time"])
        else:
            # No need to mirror mesh data, fetching the meshsolution matching with the lamination of interest
            if "stator" in self.group:
                meshsol = output.mag.meshsolution_dict[STATOR_LAB + "-0"]
            else:
                meshsol = output.mag.meshsolution_dict[ROTOR_LAB + "-0"]

    group_list = list(meshsol.group.keys())

    if self.group not in group_list:
        raise ValueError("Cannot calculate core losses for group=" + self.group)

    if "B" in meshsol:
        Bvect = meshsol["B"].field
    else:
        raise ValueError("Cannot calculate core losses if B is not in meshsolution")

    if "H" in meshsol:
        Hvect = meshsol["H"].field
    else:
        raise ValueError("Cannot calculate core losses if H is not in meshsolution")

    # Get mesh spatial symmetries (including (anti)-periodicities)
    per_a = meshsol.mesh.sym

    # Get surface and number of all elements
    Se_all = meshsol.mesh.get_element_area()

    # Get element indices associated to group
    Igrp = meshsol.group[self.group]

    # Get element surface associated to group
    Se = Se_all[Igrp]

    # Compute magnetic flux density derivative over time
    dB_dt_v = Bvect.get_vectorfield_along("time=derivate", "indice", "z")

    if is_mirror:
        # Rebuild magnet mesh quantities on time steps given by axes_dict
        time_val = axes_dict["time"].get_values(is_smallestperiod=True)
        H = Hvect.get_xyz_along(
            "time=axis_data",
            "indice=" + str(Igrp),
            "z=mean",
            axis_data={"time": time_val},
        )
        dB_dt = dB_dt_v.get_xyz_along(
            "time=axis_data",
            "indice=" + str(Igrp),
            "z=mean",
            axis_data={"time": time_val},
        )
    else:
        H = Hvect.get_xyz_along("time[smallestperiod]", "indice=" + str(Igrp), "z=mean")
        dB_dt = dB_dt_v.get_xyz_along(
            "time[smallestperiod]", "indice=" + str(Igrp), "z=mean"
        )

    # Compute the loss density for each element function of time
    # XXX problem hysterisys loss formula in time domain (losses are way too higher)
    Pcore_density_hys = (
        np.abs(H["comp_x"] * dB_dt["comp_x"]) ** (2 / alpha_B)
        + np.abs(H["comp_y"] * dB_dt["comp_y"]) ** (2 / alpha_B)
    ) ** (alpha_B / 2) / Kf

    # Pcore_density_hys = (
    #     1
    #     / (2 * np.pi**2)
    #     * k_hy
    #     * (
    #         np.abs(dB_dt["comp_x"]) ** (2 / alpha_B)
    #         + np.abs(dB_dt["comp_y"]) ** (2 / alpha_B)
    #     )
    #     ** (alpha_B / 2)
    # )

    Pcore_density_edd = (
        k_ed / Kf / (2 * np.pi**2) * (dB_dt["comp_x"] ** 2 + dB_dt["comp_y"] ** 2)
    )

    Pcore_density_exc = (
        k_ex / Kf / 8.763363 * (dB_dt["comp_x"] ** 2 + dB_dt["comp_y"] ** 2) ** 0.75
    )

    # Integrate volumic density over core volume
    Pcore_hys = Lst * per_a * np.matmul(Pcore_density_hys, Se)
    Pcore_edd = Lst * per_a * np.matmul(Pcore_density_edd, Se)
    Pcore_exc = Lst * per_a * np.matmul(Pcore_density_exc, Se)

    # Sum all core losses contribution
    Pcore = Pcore_hys + Pcore_edd + Pcore_exc

    Pcore_density = Pcore_density_hys + Pcore_density_edd + Pcore_density_exc

    Pcore_dict = {
        self.group + " losses": Pcore,
        self.group + " hysteresis": Pcore_hys,
        self.group + " eddy current": Pcore_edd,
        self.group + " excess": Pcore_exc,
    }

    # Get fundamental frequency
    felec = output.elec.OP.get_felec()

    # Save coefficients to rebuild losses for same (Id,Iq) but at a different speed
    A = Pcore_hys.mean() / felec
    B = Pcore_edd.mean() / felec**2
    C = Pcore_exc.mean() / felec**1.5
    self.coeff_dict = {"1": A, "2": B, "1.5": C}

    return Pcore_density, Pcore_dict

import numpy as np

from ....Functions.labels import ROTOR_LAB, STATOR_LAB


def comp_loss_time(self, axes_dict, is_mirror):
    """Calculate Joule losses in stator windings over time

    Parameters
    ----------
    self: LossModelJoule
        a LossModelJoule object
    axes_dict: {Data}
            Dict containing Time (including (anti-)periodicties) and Indices axes used in any Loss module
    is_mirror : bool
            True to mirror magnetic mesh quantities calculate in stator and rotor frames to get the same Time axis

    Returns
    -------
    Pjoule_density : ndarray
        Joule loss density function of time and elements [W/m3]
    Pjoule_dict: {ndarray}
        Dict containing the array of Joule losses over time
    """

    if self.parent.parent is None:
        raise ValueError("Cannot calculate Joule losses if simu is not in an Output")
    else:
        output = self.parent.parent.parent

    if output.elec is None:
        raise ValueError("Cannot calculate Joule losses if OutElec is None")

    if self.parent.is_get_meshsolution and output.mag is None:
        raise ValueError("Cannot calculate Joule losses if OutMag is None")

    if output.mag.meshsolution is not None:
        # Case with same time periodicities in both stator and rotor frames
        meshsol = output.mag.meshsolution

    elif output.mag.meshsolution_dict is None:
        raise ValueError(
            "Cannot calculate Joule losses if OutMag.meshsolution and OutMag.meshsolution_dict are both None"
        )

    else:
        if is_mirror:
            # Rebuild mesh quantities on time steps given by axes_dict
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

    machine = output.simu.machine
    lam = machine.stator if "stator" in self.group else machine.rotor
    T_op = self.parent.Tsta if "stator" in self.group else self.parent.Trot
    Lst = lam.L1
    Rs = lam.comp_resistance_wind(T=T_op)

    if self.type_skin_effect > 0:
        # Account for skin effect
        k = self.comp_coeff(
            T_op=T_op,
        )
    else:
        k = 0

    # Get mesh spatial symmetries (including (anti)-periodicities)
    per_a = meshsol.mesh.sym

    # Get stator currents over time and phases
    Is = output.elec.get_Is()
    if is_mirror:
        # Rebuild mesh quantities on time steps given by axes_dict
        time_val = axes_dict["time"].get_values(is_smallestperiod=True)
        Is_val = Is.get_along(
            "time=axis_data", "phase[]", axis_data={"time": time_val}
        )[Is.symbol]
    else:
        Is_val = Is.get_along("time[smallestperiod]", "phase[]")[Is.symbol]

    # Calculate Joule losses over time
    Pjoule = Rs * (1 + k) * np.sum(Is_val**2, axis=1)  # Sum over phases

    # Get surface and number of all elements
    Se_all = meshsol.mesh.get_element_area()

    # Get element indices associated to group
    Igrp = meshsol.group[self.group]

    # Get element surface associated to group
    Se = Se_all[Igrp]

    # Calculate uniform element density
    Pjoule_density = Pjoule[:, None] / (per_a * Lst * Se.sum())

    Pjoule_dict = {self.group + " losses": Pjoule}

    OP = output.elec.OP
    felec = OP.get_felec()
    Pjoule_val = Pjoule.mean()
    A = Pjoule_val / (1 + k * felec**2) * k
    B = Pjoule_val / (1 + k * felec**2)

    self.coeff_dict = {"2": A, "0": B}

    return Pjoule_density, Pjoule_dict

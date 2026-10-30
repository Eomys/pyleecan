import numpy as np

from ....Functions.labels import ROTOR_LAB, STATOR_LAB


def comp_loss_time(self, axes_dict, is_mirror):
    """Calculate windage losses and assume they are constant over time

    Parameters
    ----------
    self: LossModelWindagePyrhonen
        a LossModelWindagePyrhonen object
    axes_dict: {Data}
        Dict containing Time (including (anti-)periodicties) and Indices axes used in any Loss module
    is_mirror : bool
        True to mirror magnetic mesh quantities calculate in stator and rotor frames to get the same Time axis

    Returns
    -------
    Pwindage_density : ndarray
        Windage loss density function of time and elements [W/m3]
    Pwindage_dict: {ndarray}
        Dict containing the array of windage losses over time
    """

    if self.parent.parent is None:
        raise ValueError("Cannot calculate windage losses if simu is not in an Output")
    else:
        output = self.parent.parent.parent

    if output.elec is None:
        raise ValueError("Cannot calculate windage losses if OutElec is None")

    if self.parent.is_get_meshsolution and output.mag is None:
        raise ValueError("Cannot calculate windage losses if OutMag is None")

    if output.mag.meshsolution is not None:
        # Case with same time periodicities in both stator and rotor frames
        meshsol = output.mag.meshsolution
        Nt = axes_dict["time"].get_length(is_smallestperiod=True)
        Igrp = list(meshsol.group["airgap"])

    elif output.mag.meshsolution_dict is None:
        raise ValueError(
            "Cannot calculate windage losses if OutMag.meshsolution and OutMag.meshsolution_dict are both None"
        )
    else:
        if is_mirror:
            # Rebuild mesh quantities on time steps given by axes_dict
            meshsol = output.mag.get_meshsolution(Time=axes_dict["time"])
            Nt = axes_dict["time"].get_length(is_smallestperiod=True)
            # Get element indices associated to airgap group
            Igrp = meshsol.group["airgap"]
            if self.group not in meshsol.group:
                raise ValueError(
                    "Cannot calculate windage losses for group=" + self.group
                )
        else:
            if (
                self.group + "_S"
                not in output.mag.meshsolution_dict[STATOR_LAB + "-0"].group
            ):
                raise ValueError(
                    "Cannot calculate windage losses for group=" + self.group
                )
            if (
                self.group + "_R"
                not in output.mag.meshsolution_dict[ROTOR_LAB + "-0"].group
            ):
                raise ValueError(
                    "Cannot calculate windage losses for group=" + self.group
                )

            Nt = axes_dict["time"].get_length(is_smallestperiod=True)

            # Get element indices associated to airgap group at stator side
            Igrp = list(
                output.mag.meshsolution_dict[STATOR_LAB + "-0"].group["airgap_S"]
            )
            # Extend with element indices associated to airgap group at rotor side
            Igrp.extend(
                list(output.mag.meshsolution_dict[ROTOR_LAB + "-0"].group["airgap_R"])
            )

            meshsol = output.mag.meshsolution_dict[STATOR_LAB + "-0"]

    # Get mesh spatial symmetries (including (anti)-periodicities)
    per_a = meshsol.mesh.sym

    machine = output.simu.machine
    Lst = machine.stator.L1

    # Get airgap windage losses
    Ploss = self.comp_loss_value()

    # Assign same airgap windage losses at every time step
    Pwindage = Ploss * np.ones(Nt, dtype=float)

    # Get surface and number of all elements
    Se_all = meshsol.mesh.get_element_area()

    # Get element surface associated to group
    Se = Se_all[Igrp]

    # Compute the loss density for each element
    # When distributing windage losses on airgap elements, missing area of sliding band
    Pwindage_density = Pwindage[:, None] / (per_a * Lst * Se.sum())

    Pwindage_dict = {"Airgap windage losses": Pwindage}

    # Get fundamental frequency
    felec = output.elec.OP.get_felec()

    # Save coefficients to rebuild losses for same (Id,Iq) but at a different speed
    self.coeff_dict = {"3": Ploss / felec**3}

    return Pwindage_density, Pwindage_dict

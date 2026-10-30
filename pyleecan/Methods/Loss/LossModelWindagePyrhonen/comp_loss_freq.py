import numpy as np

from ....Functions.labels import ROTOR_LAB, STATOR_LAB


def comp_loss_freq(self):
    """Calculate Windage losses
    Equation from "Design of Rotating Electrical Machines", Second Edition, Pyrhönen, Jokinen, Hrabovcovà p528

    Parameters
    ----------
    self: LossModelWindagePyrhonen
        a LossModelWindagePyrhonen object

    Returns
    -------
    Pjoule_density : ndarray
        loss density function of frequency and elements [W/m3]
    freqs: ndarray
        frequency vector [Hz]
    """

    if self.parent.parent is None:
        raise ValueError("Cannot calculate losses if simu is not in an Output")
    else:
        output = self.parent.parent.parent

    if output.elec is None:
        raise ValueError("Cannot calculate losses if OutElec is None")

    if self.parent.is_get_meshsolution and output.mag is None:
        raise ValueError("Cannot calculate losses if OutMag is None")

    if output.mag.meshsolution is not None:
        # Case with same time periodicities in both stator and rotor frames
        meshsol = output.mag.meshsolution
        Igrp = list(meshsol.group["airgap"])

    elif output.mag.meshsolution_dict is None:
        raise ValueError(
            "Cannot calculate windage losses if OutMag.meshsolution and OutMag.meshsolution_dict are both None"
        )
    else:
        if (
            self.group + "_S"
            not in output.mag.meshsolution_dict[STATOR_LAB + "-0"].group
        ):
            raise ValueError("Cannot calculate windage losses for group=" + self.group)
        if (
            self.group + "_R"
            not in output.mag.meshsolution_dict[ROTOR_LAB + "-0"].group
        ):
            raise ValueError("Cannot calculate windage losses for group=" + self.group)

        # Get element indices associated to airgap group at stator side
        Igrp = list(output.mag.meshsolution_dict[STATOR_LAB + "-0"].group["airgap_S"])
        # Extend with element indices associated to airgap group at rotor side
        Igrp.extend(
            list(output.mag.meshsolution_dict[ROTOR_LAB + "-0"].group["airgap_R"])
        )

        meshsol = output.mag.meshsolution_dict[STATOR_LAB + "-0"]

    machine = output.simu.machine
    L = machine.rotor.L1
    OP = output.elec.OP
    felec = OP.get_felec()

    Ploss = self.comp_loss_value()

    power = 3

    coeff = Ploss / felec**power

    # Get mesh spatial symmetries (including (anti)-periodicities)
    per_a = meshsol.mesh.sym

    # Get surface elements for airgap
    Se = meshsol.mesh.get_element_area()[Igrp]

    # Compute the loss density for each element
    # When distributing windage losses on airgap elements, missing area of sliding band
    freqs = np.array([felec])
    Pwindage_density = np.zeros((freqs.size, Se.size))
    Pwindage_density[0, :] = Ploss / (per_a * L * np.sum(Se))

    Pwindage_dict = {"Airgap windage losses": np.array([Ploss])}

    self.coeff_dict = {str(power): coeff}

    return Pwindage_density, Pwindage_dict, freqs

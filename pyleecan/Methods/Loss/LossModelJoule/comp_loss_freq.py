import numpy as np

from ....Functions.labels import ROTOR_LAB, STATOR_LAB


def comp_loss_freq(self):
    """Calculate joule losses in stator windings

    Parameters
    ----------
    self: LossModelJoule
        a LossModelJoule object

    Returns
    -------
    Pjoule_density : ndarray
        Joule loss density function of frequency and elements [W/m3]
    freqs: ndarray
        frequency vector [Hz]
    """

    if self.parent.parent is None:
        raise ValueError("Cannot calculate joule losses if simu is not in an Output")
    else:
        output = self.parent.parent.parent

    if output.elec is None:
        raise ValueError("Cannot calculate joule losses if OutElec is None")

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

    OP = output.elec.OP
    felec = OP.get_felec()

    Rs = lam.comp_resistance_wind(T=T_op)
    qs = lam.winding.qs

    if self.type_skin_effect > 0:
        # Account for skin effect
        k = self.comp_coeff(
            T_op=T_op,
        )
    else:
        k = 0

    # Get mesh spatial symmetries (including (anti)-periodicities)
    per_a = meshsol.mesh.sym

    # Get stator currents over frequency and phases
    Is = output.elec.get_Is()
    result = Is.get_along("freqs", "phase[]")
    Is_val = result[Is.symbol]
    freqs = result["freqs"]

    # Calculate Joule losses over time (Assuming fundamental skin correction factor the same for all harmonics)
    Pjoule = (
        Rs * (1 + k * felec**2) * np.sum(0.5 * np.abs(Is_val) ** 2, axis=1)
    )  # Sum over phases

    # Get surface and number of all elements
    Se_all = meshsol.mesh.get_element_area()

    # Get element indices associated to group
    Igrp = meshsol.group[self.group]

    # Get element surface associated to group
    Se = Se_all[Igrp]

    # Calculate uniform element density and sum over frequencies to get average loss density value per element
    Pjoule_density = np.zeros((1, Se.size))
    Pjoule_val = Pjoule.sum()
    Pjoule_density[0, :] = Pjoule_val / (per_a * Lst * Se.sum())

    # Store losses contribution for each frequency in dict
    Pjoule_dict = {self.group + " losses": Pjoule}

    # Get eddy-current proximity loss polynomial coefficient
    A = Pjoule_val / (1 + k * felec**2) * k
    B = Pjoule_val / (1 + k * felec**2)
    self.coeff_dict = {"2": A, "0": B}

    return Pjoule_density, Pjoule_dict, freqs

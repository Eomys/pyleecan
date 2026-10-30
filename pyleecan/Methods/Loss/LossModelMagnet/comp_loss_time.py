import numpy as np

from ....Classes.LamHole import LamHole
from ....Classes.LamSlotMag import LamSlotMag
from ....Functions.labels import ROTOR_LAB, STATOR_LAB


def comp_loss_time(self, axes_dict, is_mirror):
    """Calculate eddy-current losses in rotor permanent magnets in time domain assuming power density
    is given by (cf. https://www.femm.info/wiki/SPMLoss):

        Pmag = Jm^2/sigma_m with Jm = -sigma_m*dAz/dt + Jc where Jc=<Jm> on the magnet surface

    Parameters
    ----------
    self: LossModelMagnet
        a LossModelMagnet object
    axes_dict: {Data}
        Dict containing Time (including (anti-)periodicties) and Indices axes used in any Loss module
    is_mirror : bool
        True to mirror magnetic mesh quantities calculate in stator and rotor frames to get the same Time axis

    Returns
    -------
    Pmagnet_density : ndarray
        Magnet loss density function of time and elements [W/m3]
    Pmagnet_dict: {ndarray}
        Dict containing the array of magnet losses over time

    """

    if self.parent.parent.parent is None:
        raise ValueError("Cannot calculate magnet losses if simu is not in an Output")
    else:
        output = self.parent.parent.parent

    machine = output.simu.machine

    if isinstance(machine.rotor, LamSlotMag):
        magnet = machine.rotor.magnet
    elif isinstance(machine.rotor, LamHole):
        hole0 = machine.rotor.hole[0]
        magnet = hole0.get_magnet_dict()["magnet_0"]

    # Get rotor length
    Lst = machine.rotor.L1

    # Get magnet electrical conductivity
    sigma_m = magnet.mat_type.elec.get_conductivity(T_op=self.parent.Trot)

    # Get magnet segmentation coefficient
    if magnet.Lmag is None or magnet.Nseg is None or magnet.Nseg == 1:
        kseg = 1
    else:
        kseg = self.comp_kseg(machine)

    if output.mag is None:
        raise ValueError("Cannot calculate magnet losses if OutMag is None")

    if output.mag.meshsolution is not None:
        # Case with same time periodicities in both stator and rotor frames
        meshsol = output.mag.meshsolution

    elif output.mag.meshsolution_dict is None:
        raise ValueError(
            "Cannot calculate magnet losses if OutMag.meshsolution and OutMag.meshsolution_dict are both None"
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
        raise ValueError("Cannot calculate magnet losses for group=" + self.group)

    # Get magnetic vector potential over time and for each element center in current group
    if "A_z^{element}" in meshsol:
        Az = meshsol["A_z^{element}"].field
    else:
        raise ValueError(
            "Cannot calculate magnet losses if  A_z calculated on element center is not in meshsolution"
        )

    # Get mesh spatial symmetries (including (anti)-periodicities)
    per_a = meshsol.mesh.sym

    # Get surface and number of all elements
    Se_all = meshsol.mesh.get_element_area()

    # Get list of element indices for each magnet
    list_Imag = []
    ind_list = []
    for key in meshsol.group:
        if self.group in key and key != self.group:
            ind = int(key.split("_")[-1])
            ind_list.append(ind)
            list_Imag.append(meshsol.group[key])
    Igrp = meshsol.group[self.group]

    # Calculate induced current density and loss density in each magnet
    time_val = axes_dict["time"].get_values(is_smallestperiod=True)
    Pmagnet_density = np.zeros((time_val.size, len(Igrp)))
    jj = 0
    for kmag in list_Imag:
        Se_mag = Se_all[kmag]

        # Compute magnetic vector potential derivative over time
        dAz_dt = Az.get_data_along("time=derivate", "indice=" + str(kmag), "z")

        if is_mirror:
            # Rebuild mesh quantities on time steps given by axes_dict
            dAz_dt_val = dAz_dt.get_along(
                "time=axis_data", "indice", "z=mean", axis_data={"time": time_val}
            )[dAz_dt.symbol]
        else:
            dAz_dt_val = dAz_dt.get_along("time[smallestperiod]", "indice", "z=mean")[
                dAz_dt.symbol
            ]

        # Calculate eddy-current current density in this magnet
        Jm = -sigma_m * dAz_dt_val

        # Ensure average current flowing through the surface is 0
        Jc = np.matmul(Jm, Se_mag)[:, None] / Se_mag.sum()
        Jm -= Jc

        # Calculate loss density due to eddy-current
        Pmagnet_density[:, jj : (jj + len(kmag))] = kseg * Jm**2 / sigma_m

        # Increment by the number elements of in this magnet
        jj += len(kmag)

    # Integrate volumic density over elements volume
    Pmagnet = Lst * per_a * np.matmul(Pmagnet_density, Se_all[Igrp])

    Pmagnet_dict = {self.group + " losses": Pmagnet}

    # Get fundamental frequency
    felec = output.elec.OP.get_felec()

    # Save coefficients to rebuild losses for same (Id,Iq) but at a different speed
    A = Pmagnet.mean() / felec**2
    self.coeff_dict = {"2": A}

    return Pmagnet_density, Pmagnet_dict

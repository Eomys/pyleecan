import numpy as np

from ....Classes.LamHole import LamHole
from ....Classes.LamSlotMag import LamSlotMag
from ....Functions.labels import ROTOR_LAB, STATOR_LAB


def comp_loss_freq(self):
    """Calculate eddy-current losses in rotor permanent magnets assuming power density depending on frequency
    is given by (cf. https://www.femm.info/wiki/SPMLoss):

        Pmag = Jm^2/sigma_m with Jm = -sigma_m*1j*2pi*f*Az + Jc where Jc=<Jm> on the magnet surface

    Parameters
    ----------
    self: LossModelMagnet
        a LossModelMagnet object

    Returns
    -------
    Pmagnet_density : ndarray
       Average magnet loss density (frequency=0Hz) for all elements [W/m3]
    Pmag_dict: {ndarray}
        Dict containing the array of magnet losses by contribution and for all frequencies in magnetic flux density [W]
    freqs: ndarray
        frequency vector of magnetic flux density harmonics [Hz]
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

    # Get fundamental frequency
    felec = output.elec.OP.get_felec()

    if output.mag is None:
        raise ValueError("Cannot calculate magnet losses if OutMag is None")

    if output.mag.meshsolution is not None:
        # Case with same time periodicities in both stator and rotor frames
        meshsol = output.mag.meshsolution

    elif output.mag.meshsolution_dict is None:
        raise ValueError(
            "Cannot calculate proximity losses if OutMag.meshsolution and OutMag.meshsolution_dict are both None"
        )
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
        Az_dt = meshsol["A_z^{element}"].field
    else:
        raise ValueError(
            "Cannot calculate magnet losses if  A_z calculated on element center is not in meshsolution"
        )

    # Get mesh spatial symmetries (including (anti)-periodicities)
    per_a = meshsol.mesh.sym

    # Get all element surfaces
    Se = meshsol.mesh.get_element_area()

    # Get list of element indices for each magnet
    list_Imag = []
    ind_list = []
    for key in meshsol.group:
        if self.group in key and key != self.group:
            ind = int(key.split("_")[-1])
            ind_list.append(ind)
            list_Imag.append(meshsol.group[key])
    ind_all = meshsol.group[self.group]

    # Calculate induced current density and loss density
    jj = 0
    for ii, kmag in enumerate(list_Imag):
        Se_mag = Se[kmag]

        # derivation in frequency domain
        Az_df = Az_dt.get_along("freqs", "indice=" + str(kmag), "z=mean")
        if ii == 0:
            freqs = Az_df["freqs"]
            w = 2 * np.pi * freqs[:, None]
            # if self.type_skin_effect:
            #     # Get magnet conductivity including skin effect
            #     magnet_cond = CondType21(Hbar=Hmag, Wbar=1, cond_mat=magnet.mat_type)
            #     kr_skin = magnet_cond.comp_skin_effect_resistance(
            #         freqs, T_op=self.parent.Trot, b=1, zt=1
            #     )
            #     kr_skin[np.isnan(kr_skin)] = 1
            #     sigma_m = sigma_m / kr_skin[:, None]
            Pmagnet_density = np.zeros((freqs.size, len(ind_all)))
        Az_fft = Az_df["A_z^{element}"]
        Az_mean = np.matmul(Az_fft, Se_mag)[:, None] / np.sum(Se_mag)
        Jm_fft = -1j * sigma_m * w * (Az_fft - Az_mean)
        Pmagnet_density[:, jj : (jj + len(kmag))] = (
            0.5 * kseg * np.abs(Jm_fft) ** 2 / sigma_m
        )
        jj += len(kmag)

    # Integrate loss density over group volume
    Pmagnet = Lst * per_a * np.matmul(Pmagnet_density, Se[ind_all])

    # Sum over frequencies to get average loss density value per element
    Pmagnet_density = np.sum(Pmagnet_density, axis=0, keepdims=True)

    # Store losses contribution for each frequency in dict
    Pmagnet_dict = {self.group + " losses": Pmagnet}

    # Get eddy-current magnet loss polynomial coefficient
    A = np.sum(Pmagnet) / felec**2
    self.coeff_dict = {"2.0": A}

    return Pmagnet_density, Pmagnet_dict, freqs

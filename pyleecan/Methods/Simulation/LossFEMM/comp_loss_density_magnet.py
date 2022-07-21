from numpy import sum as np_sum, abs as np_abs, pi, matmul, zeros

import numpy as np

from ....Classes.CondType21 import CondType21
from ....Classes.HoleM50 import HoleM50
from ....Classes.HoleM51 import HoleM51
from ....Classes.HoleM52 import HoleM52
from ....Classes.HoleM53 import HoleM53
from ....Classes.HoleM57 import HoleM57
from ....Classes.HoleM58 import HoleM58
from ....Classes.LamHole import LamHole
from ....Classes.LamSlotMag import LamSlotMag


def comp_loss_density_magnet(self, group, coeff_dict):
    """Calculate eddy-current losses in rotor permanent magnets assuming power density
    is given by (cf. https://www.femm.info/wiki/SPMLoss):

        Pmag = Jm^2/sigma_m with Jm = -sigma_m*1j*2pi*f*Az + Jc where Jc=<Jm> on the magnet surface

    Parameters
    ----------
    self: LossFEMM
        a LossFEMM object
    group: str
        Name of part in which to calculate magnet losses

    Returns
    -------
    Pmagnet_density : ndarray
        Magnet loss density function of frequency and elements [W/m3]
    freqs: ndarray
        frequency vector [Hz]
    coeff_dict: dict
        Dict containing coefficient A and B to calculate overall losses such as P = sum(A*f + B*f^2)
    """

    if self.parent.parent is None:
        raise Exception("Cannot calculate core losses if simu is not in an Output")
    else:
        output = self.parent.parent

    machine = output.simu.machine

    per_a = output.geo.per_a
    if output.geo.is_antiper_a:
        per_a *= 2

    if isinstance(machine.rotor, LamSlotMag):
        magnet = machine.rotor.magnet
        slot = machine.rotor.slot
        if hasattr(slot, "Hmag"):
            Hmag = slot.Hmag
        else:
            Hmag = np.sqrt(slot.comp_surface_active())
        if hasattr(slot, "Wmag"):
            Wmag = slot.Wmag
        else:
            Wmag = np.sqrt(slot.comp_surface_active())

    elif isinstance(machine.rotor, LamHole):
        hole0 = machine.rotor.hole[0]
        magnet = hole0.get_magnet_dict()["magnet_0"]
        if isinstance(hole0, HoleM50):
            Hmag = hole0.H3
            Wmag = hole0.W4
        elif isinstance(hole0, (HoleM51, HoleM53, HoleM57, HoleM58)):
            Hmag = hole0.H2
            if isinstance(hole0, HoleM51):
                Wmag = (hole0.W3 + hole0.W5 + hole0.W7) / 3
            elif isinstance(hole0, HoleM52):
                Wmag = hole0.W0
            elif isinstance(hole0, HoleM53):
                Wmag = hole0.W3
            elif isinstance(hole0, HoleM57):
                Wmag = hole0.W4
            elif isinstance(hole0, HoleM58):
                Wmag = hole0.W1
        elif isinstance(hole0, HoleM52):
            Hmag = hole0.H1
        else:
            Hmag = np.sqrt(hole0.comp_surface_magnet_id(0))
            Wmag = Hmag
    else:
        raise Exception(
            "Cannot calculate magnet losses for rotor lamination other than LamSlotMag or LamHole"
        )

    # Get rotor length
    L1 = machine.rotor.L1

    # Calculate segmentation coefficient from:
    # "Effect of Eddy-Current Loss Reduction by Magnet Segmentation in Synchronous Motors With Concentrated Windings"
    # Katsumi Yamazaki, Member, IEEE, and Yu Fukushima, Equation (9)
    if magnet.Lmag is None or magnet.Nseg is None or Wmag is None:
        kseg = 1
    else:
        Lmag = magnet.Lmag
        Nseg = magnet.Nseg
        kseg = ((Lmag + Wmag) / (Lmag * Nseg + Wmag)) ** 2

    # Get fundamental frequency
    felec = output.elec.OP.get_felec()

    if output.mag is None:
        raise Exception("Cannot calculate magnet losses if OutMag is None")

    if output.mag.meshsolution is None:
        raise Exception("Cannot calculate magnet losses if OutMag.meshsolution is None")
    else:
        meshsol = output.mag.meshsolution

    group_list = list(meshsol.group.keys())

    if group not in group_list:
        raise Exception("Cannot calculate magnet losses for group=" + group)

    lab_ind = None
    for ii, sol in enumerate(meshsol.solution):
        if sol.label == "A_z^{element}" and sol.type_cell == "triangle":
            lab_ind = ii
            break
    if lab_ind is None:
        raise Exception(
            "Cannot calculate magnet losses if A_z calculated on element center is not in meshsolution"
        )

    # Get magnetic vector potential over time and for each element center in current group
    Az_dt = meshsol.solution[lab_ind].field
    axes_list = Az_dt.get_axes()
    Time_orig = axes_list[0]
    Time = Time_orig.copy()

    # Check Time axis periodicity in function of group
    is_change_Time = False
    if "rotor" in group:
        if "antiperiod" in Time_orig.symmetries:
            Time.symmetries = {"period": Time_orig.symmetries["antiperiod"]}
            is_change_Time = True
    if is_change_Time:
        Az_dt.axes[0] = Time

    # Get all element surfaces
    Se = meshsol.mesh[0].get_cell_area()

    # Get list of element indices for each magnet
    list_Imag = list()
    ind_list = list()
    for key in meshsol.group:
        if group in key and key != group:
            ind = int(key.split("_")[-1])
            ind_list.append(ind)
            list_Imag.append(meshsol.group[key])
    ind_all = meshsol.group[group]

    # Calculate induced current density and loss density
    jj = 0
    for ii, kmag in enumerate(list_Imag):
        Se_mag = Se[kmag]

        # derivation in frequency domain
        Az_df = Az_dt.get_along("freqs", "indice" + str(kmag), "z[0]")
        if ii == 0:
            freqs = Az_df["freqs"]
            w = 2 * pi * freqs[:, None]
            sigma_m = magnet.mat_type.elec.get_conductivity(T_op=self.Trot)
            if self.type_skin_effect:
                # Get magnet conductivity including skin effect
                magnet_cond = CondType21(Hbar=Hmag, Wbar=1, cond_mat=magnet.mat_type)
                kr_skin = magnet_cond.comp_skin_effect_resistance(
                    freqs, T_op=self.Trot, b=1, zt=1
                )
                kr_skin[np.isnan(kr_skin)] = 1
                sigma_m = sigma_m / kr_skin[:, None]
            Pmagnet_density = np.zeros((freqs.size, len(ind_all)))
        Az_fft = Az_df["A_z^{element}"]
        Az_mean = matmul(Az_fft, Se_mag)[:, None] / np_sum(Se_mag)
        Jm_fft = -1j * sigma_m * w * (Az_fft - Az_mean)
        Pmagnet_density[:, jj : (jj + len(kmag))] = (
            0.5 * kseg * np_abs(Jm_fft) ** 2 / sigma_m
        )
        jj += len(kmag)

        # # # derivation in time domain
        # dAz_dt = Az_dt.get_data_along("time=derivate", "indice" + str(kmag), "z[0]")
        # dAz_df = dAz_dt.get_along("freqs", "indice", "z[0]")
        # dAz_fft = dAz_df["A_z"]
        # if ii == 0:
        #     freqs = dAz_df["freqs"]
        #     w = 2 * pi * freqs[:, None]
        #     sigma_m = magnet.mat_type.elec.get_conductivity(T_op=self.Trot)
        #     if is_skin_effect:
        #         # Get magnet conductivity including skin effect
        #         magnet_cond = CondType21(Hbar=Hmag, Wbar=1, cond_mat=magnet.mat_type)
        #         kr_skin = magnet_cond.comp_skin_effect_resistance(
        #             freqs, T_op=self.Trot, b=1, zt=1
        #         )
        #         kr_skin[np.isnan(kr_skin)] = 1
        #         sigma_m = sigma_m / kr_skin[:, None]
        #     Pmagnet_density = np.zeros((freqs.size, len(ind_all)))
        # Jm_fft0 = sigma_m * (
        #     -dAz_fft + matmul(dAz_fft, Se_mag)[:, None] / np_sum(Se_mag)
        # )

        # # # Plot
        # Az_df0 = Az_dt.get_data_along("freqs", "indice" + str(kmag), "z[0]")
        # dAz_df0 = Az_df0.copy()
        # dAz_df0.values *= 1j * w[:, :, None]
        # dAz_df0.unit = "Wb/ms"
        # dAz_df0.plot_2D_Data(
        #     "freqs", "indice[0]", data_list=[dAz_dt], legend_list=["df", "dt"]
        # )
        # dAz_df0.plot_2D_Data(
        #     "time", "indice[0]", data_list=[dAz_dt], legend_list=["df", "dt"]
        # )
        # from SciDataTool import DataFreq

        # Jm_df = DataFreq(
        #     name="Current density",
        #     symbol="J_m",
        #     unit="A/m^2",
        #     values=Jm_fft,
        #     axes=Az_df0.axes,
        # )
        # Jm_df0 = DataFreq(
        #     name="Current density",
        #     symbol="J_m",
        #     unit="A/m^2",
        #     values=Jm_fft0,
        #     axes=Az_df0.axes,
        # )
        # Jm_df.plot_2D_Data(
        #     "time", "indice[0]", data_list=[Jm_df0], legend_list=["df", "dt"]
        # )
        # Jm_df.plot_2D_Data(
        #     "freqs", "indice[0]", data_list=[Jm_df0], legend_list=["df", "dt"]
        # )

    if is_change_Time:
        # Change periodicity back to original periodicity
        Az_dt.axes[0] = Time_orig

    # Calculate coefficients to evaluate magnet losses
    if coeff_dict is not None:
        # Get frequency orders
        n = freqs / felec
        # Integrate loss density over group volume
        I0 = n != 0
        Af = zeros(w.size)
        Af[I0] = (
            L1
            * per_a
            * matmul(Pmagnet_density[I0, :] / freqs[I0, None] ** 2, Se[ind_all])
        )
        # Sum over orders
        A = np_sum(Af * n ** 2)
        coeff_dict[group] = {"A": A, "B": 0, "C": 0, "a": 2, "b": 0, "c": 0}

    return Pmagnet_density, freqs

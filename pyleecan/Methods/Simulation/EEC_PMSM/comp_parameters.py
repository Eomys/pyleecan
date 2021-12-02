from numpy import isscalar

from ....Functions.Electrical.dqh_transformation import n2dqh_DataTime


def comp_parameters(self, machine, OP, Tsta=None, Trot=None):
    """Compute the parameters dict for the equivalent electrical circuit:
    resistance, inductance and back electromotive force
    Parameters
    ----------
    self : EEC_PMSM
        an EEC_PMSM object
    machine : Machine
        a Machine object
    OP : OP
        an OP object
    Tsta : float
        Average stator temperature
    Trot : float
        Average rotor temperature
    """

    if self.parameters is None:
        self.parameters = dict()
    par = self.parameters

    is_LUT = self.LUT_enforced is not None
    LUT = self.LUT_enforced

    # Store electrical frequency in parameters
    par["felec"] = OP.get_felec()

    # Store dqh voltages
    par.update(OP.get_Ud_Uq())

    # Store dqh currents
    par.update(OP.get_Id_Iq())

    # compute skin_effect
    cond = machine.stator.winding.conductor
    Xkr_skinS, Xke_skinS = cond.comp_skin_effect(T=Tsta, freq=par["felec"])

    # Stator resistance
    if "R20" not in par:
        if is_LUT and LUT.R1 is not None:
            R20 = LUT.R1
        else:
            R20 = machine.stator.comp_resistance_wind()
        par["R20"] = R20 * Xkr_skinS

    # Stator flux linkage only due to permanent magnets
    if "Phid_mag" not in par or "Phiq_mag" not in par:
        if is_LUT:
            Phi_dqh_mag_mean = LUT.get_Phidqh_mag_mean()
        else:
            Phi_dqh_mag_mean = self.fluxlink.comp_fluxlinkage(machine)
        par["Phid_mag"] = float(Phi_dqh_mag_mean[0])
        par["Phiq_mag"] = float(Phi_dqh_mag_mean[1])

    # Stator winding flux
    if (
        par["Id"] is not None
        and par["Iq"] is not None
        and ("Phid" not in par or "Phiq" not in par)
    ):
        if is_LUT:
            Slice_MLUT = LUT.axes_dict["z"]
            is_rebuild_skew = (
                Slice_MLUT.values.size == 1 and machine.rotor.skew is not None
            )

            if LUT.is_interp_along_curve or is_rebuild_skew:

                # Interpolate stator winding flux using LUT
                Phi_wind = LUT.interp_Phi_wind(OP=OP)

                # dqh transform
                Phi_dqh = n2dqh_DataTime(
                    Phi_wind, is_dqh_rms=True, phase_dir=LUT.get_phase_dir()
                )

                # Get Phi_dqh_mean
                Phi_dqh_mean = Phi_dqh.get_along("time=mean", "phase")[Phi_dqh.symbol]

            else:
                # Get dqh flux function of current
                Phi_dqh_mean = self.interp_Phi_dqh(Id=par["Id"], Iq=par["Iq"])
        else:
            Phi_dqh_mean = self.indmag.comp_inductance(machine=machine, OP_ref=OP)

        par["Phid"] = Phi_dqh_mean[0]  # * Xke_skinS
        par["Phiq"] = Phi_dqh_mean[1]  # * Xke_skinS
        if par["Phid"].size == 1:
            par["Phid"] = float(par["Phid"])
            par["Phiq"] = float(par["Phiq"])

    # compute inductance if necessary
    if "Ld" not in par or "Lq" not in par:

        if par["Id"] not in [0, None] and par["Iq"] not in [0, None]:

            par["Ld"] = (par["Phid"] - par["Phid_mag"]) / par["Id"]
            par["Lq"] = (par["Phiq"] - par["Phiq_mag"]) / par["Iq"]

        else:
            par["Ld"] = None
            par["Lq"] = None

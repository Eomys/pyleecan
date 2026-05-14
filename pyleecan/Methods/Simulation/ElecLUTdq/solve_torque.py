import numpy as np


def _get_refined_axis_count(axis_count, other_axis_count, n_interp):
    """Return a safe interpolation count for one dq axis."""

    axis_count = int(axis_count)
    if axis_count == 1:
        return 1

    other_axis_count = int(other_axis_count)
    n_interp = int(n_interp)
    refined_count = int(axis_count * n_interp / (axis_count + other_axis_count))

    return max(2, refined_count)


def _select_closest_torque(Tem_interp, Imax_interp, target_torque, mask):
    """Return the local index minimizing torque error, then current."""

    torque_error = np.abs(Tem_interp[mask] - target_torque)
    current = Imax_interp[mask]
    return np.lexsort((current, torque_error))[0]


def solve_torque(self, LUT, Rs):
    """Solve EEC to achieve a requested torque with respect to voltage and current constraints.

    Parameters
    ----------
    self : ElecLUTdq
        a ElecLUTdq object
    LUT : LUTdq
        Calculated look-up table
    Rs: float
        Stator phase resistance [Ohm]

    Returns
    ----------
    out_dict: dict
        Dict containing all output quantities
    """

    output = self.parent.parent
    machine = output.simu.machine
    OP = output.elec.OP

    target_torque = OP.Tem_av_ref
    if target_torque is None:
        raise ValueError("OP.Tem_av_ref must be defined for torque resolution")

    Urms_max = self.Urms_max
    Irms_max = self.Irms_max
    has_voltage_limit = Urms_max is not None and np.isfinite(Urms_max)
    has_current_limit = Irms_max is not None and np.isfinite(Irms_max)
    Urms_limit = float(Urms_max) if has_voltage_limit else np.inf
    Irms_limit = float(Irms_max) if has_current_limit else np.inf
    felec = OP.get_felec()
    ws = 2 * np.pi * felec
    qs = machine.stator.winding.qs
    p = machine.get_pole_pair_number()

    delta_torque = 1e10
    delta_torque_max = 0.1
    niter = 1
    niter_max = 20
    is_target_reached = True

    Id_min = self.Id_min
    Id_max = self.Id_max
    Iq_min = self.Iq_min
    Iq_max = self.Iq_max
    Nd = _get_refined_axis_count(self.n_Id, self.n_Iq, self.n_interp)
    Nq = _get_refined_axis_count(self.n_Iq, self.n_Id, self.n_interp)

    is_loss_model = LUT.simu.loss is not None

    while abs(delta_torque) > delta_torque_max and niter < niter_max:
        Id_vect = np.linspace(Id_min, Id_max, Nd)
        Iq_vect = np.linspace(Iq_min, Iq_max, Nq)
        Id, Iq = np.meshgrid(Id_vect, Iq_vect)
        Id, Iq = Id.ravel(), Iq.ravel()

        Imax_interp = np.sqrt(Id**2 + Iq**2)

        Phid, Phiq, _ = LUT.interp_Phi_dqh(Id, Iq)

        Ud = Rs * Id - Phiq * ws
        Uq = Rs * Iq + Phid * ws
        Umax_interp = np.sqrt(Ud**2 + Uq**2)

        Tem_interp = qs * p * (Phid * Iq - Phiq * Id)

        U_cond = Umax_interp <= Urms_limit
        I_cond = Imax_interp <= Irms_limit

        if target_torque >= 0:
            torque_cond = Tem_interp >= target_torque
            torque_dir_cond = Tem_interp >= 0
        else:
            torque_cond = Tem_interp <= target_torque
            torque_dir_cond = Tem_interp <= 0

        if is_loss_model:
            Ploss_dqh = LUT.interp_Ploss_dqh(Id, Iq, N0=OP.N0)
            Ploss_ovl = np.sum(Ploss_dqh, axis=1)
            Ploss_dqh_wo_joule = LUT.interp_Ploss_dqh(
                Id, Iq, N0=OP.N0, exclude_models=["LossModelWinding"]
            )
            P_in = qs * (Ud * Id + Uq * Iq) + np.sum(Ploss_dqh_wo_joule, axis=1)
        else:
            Ploss_ovl = qs * Rs * (Id**2 + Iq**2)
            P_in = qs * (Ud * Id + Uq * Iq)

        P_out = P_in - Ploss_ovl

        feasible_cond = np.logical_and(U_cond, I_cond)
        i0 = np.logical_and(feasible_cond, torque_cond)

        if np.any(i0):
            imin = np.argmin(Imax_interp[i0])
            delta_torque = Tem_interp[i0][imin] - target_torque
            is_target_reached = True
        else:
            is_target_reached = False
            feasible_same_direction = np.logical_and(feasible_cond, torque_dir_cond)
            if np.any(feasible_same_direction):
                i0 = feasible_same_direction
                imin = _select_closest_torque(
                    Tem_interp, Imax_interp, target_torque, i0
                )
                delta_torque = Tem_interp[i0][imin] - target_torque
            elif np.any(feasible_cond):
                i0 = feasible_cond
                imin = _select_closest_torque(
                    Tem_interp, Imax_interp, target_torque, i0
                )
                delta_torque = Tem_interp[i0][imin] - target_torque
            else:
                i1 = np.logical_and(U_cond, torque_cond)
                i2 = np.logical_and(I_cond, torque_cond)

                if np.any(i1):
                    i0 = i1
                    imin = np.argmin(Imax_interp[i0])
                    delta_torque = Tem_interp[i0][imin] - target_torque
                elif np.any(i2):
                    i0 = i2
                    imin = np.argmin(Imax_interp[i0])
                    delta_torque = Tem_interp[i0][imin] - target_torque
                elif np.any(torque_dir_cond):
                    i0 = torque_dir_cond
                    imin = _select_closest_torque(
                        Tem_interp, Imax_interp, target_torque, i0
                    )
                    delta_torque = 0
                else:
                    i0 = np.ones_like(Tem_interp, dtype=bool)
                    imin = _select_closest_torque(
                        Tem_interp, Imax_interp, target_torque, i0
                    )
                    delta_torque = 0

            if not np.any(feasible_cond):
                # The selected point is necessarily outside at least one hard limit.
                # Avoid repeatedly zooming into an infeasible area when no feasible
                # candidate exists in the current grid.
                delta_torque = 0

        if abs(delta_torque) > delta_torque_max:
            jd = np.where(Id_vect == Id[i0][imin])[0][0]
            jq = np.where(Iq_vect == Iq[i0][imin])[0][0]

            jd_min = max([jd - 1, 0])
            jd_max = min([jd + 1, Nd - 1])
            jq_min = max([jq - 1, 0])
            jq_max = min([jq + 1, Nq - 1])

            Id_min = Id_vect[jd_min]
            Id_max = Id_vect[jd_max]
            Iq_min = Iq_vect[jq_min]
            Iq_max = Iq_vect[jq_max]

        niter += 1

    if not is_target_reached:
        self.get_logger().warning(
            "Torque target cannot be reached within current and voltage constraints, "
            "taking closest feasible torque"
        )

    if has_voltage_limit and Umax_interp[i0][imin] > Urms_limit:
        self.get_logger().warning("Voltage constraint cannot be reached")

    if has_current_limit and Imax_interp[i0][imin] > Irms_limit:
        self.get_logger().warning("Current constraint cannot be reached")

    out_dict = dict()
    out_dict["P_in"] = P_in[i0][imin]
    out_dict["P_out"] = P_out[i0][imin]
    if out_dict["P_in"] == 0:
        out_dict["efficiency"] = 0
    else:
        out_dict["efficiency"] = out_dict["P_out"] / out_dict["P_in"]
    out_dict["Tem_av"] = Tem_interp[i0][imin]

    out_dict["Id"] = Id[i0][imin]
    out_dict["Iq"] = Iq[i0][imin]
    out_dict["Ud"] = Ud[i0][imin]
    out_dict["Uq"] = Uq[i0][imin]
    i_rms = np.sqrt(out_dict["Id"] ** 2 + out_dict["Iq"] ** 2)
    u_rms = np.sqrt(out_dict["Ud"] ** 2 + out_dict["Uq"] ** 2)
    out_dict["is_current_limited"] = bool(
        Irms_max is not None and np.isfinite(Irms_max) and i_rms >= 0.98 * Irms_max
    )
    out_dict["is_voltage_limited"] = bool(
        Urms_max is not None and np.isfinite(Urms_max) and u_rms >= 0.98 * Urms_max
    )
    if out_dict["is_voltage_limited"] and out_dict["is_current_limited"]:
        out_dict["control_region"] = "FW"
    elif out_dict["is_voltage_limited"]:
        out_dict["control_region"] = "MTPV"
    else:
        out_dict["control_region"] = "MTPA"

    out_dict["Phid"] = Phid[i0][imin]
    out_dict["Phiq"] = Phiq[i0][imin]

    Phidqh_mag = LUT.get_Phi_dqh_mag_mean()
    out_dict["Phid_mag"] = Phidqh_mag[0]
    out_dict["Phiq_mag"] = Phidqh_mag[1]
    out_dict["Erms"] = ws * Phidqh_mag[0]

    if is_loss_model:
        out_dict["Pjoule"] = Ploss_dqh[i0, 0][imin]
        out_dict["Pstator"] = Ploss_dqh[i0, 1][imin]
        out_dict["Pmagnet"] = Ploss_dqh[i0, 2][imin]
        out_dict["Protor"] = Ploss_dqh[i0, 3][imin]
        out_dict["Pprox"] = Ploss_dqh[i0, 4][imin]
    else:
        out_dict["Pjoule"] = Ploss_ovl[i0][imin]

    if Id[i0][imin] != 0:
        out_dict["Ld"] = (Phid[i0][imin] - out_dict["Phid_mag"]) / Id[i0][imin]
    if Iq[i0][imin] != 0:
        out_dict["Lq"] = Phiq[i0][imin] / Iq[i0][imin]

    Tem_rip_pp = LUT.interp_Tem_rip_dqh(Id[i0][imin], Iq[i0][imin])
    if Tem_rip_pp is not None:
        out_dict["Tem_rip_pp"] = float(Tem_rip_pp)
        if out_dict["Tem_av"] == 0:
            out_dict["Tem_rip_norm"] = 0
        else:
            out_dict["Tem_rip_norm"] = np.abs(Tem_rip_pp / out_dict["Tem_av"])

    return out_dict

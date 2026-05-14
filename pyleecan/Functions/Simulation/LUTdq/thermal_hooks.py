import numpy as np


DEFAULT_REFERENCE_TEMPERATURE = 20.0


def _as_temperature(value, fallback=DEFAULT_REFERENCE_TEMPERATURE):
    if value is None:
        return fallback
    try:
        temperature = float(value)
    except (TypeError, ValueError):
        return fallback
    if not np.isfinite(temperature):
        return fallback
    return temperature


def get_conductor_resistivity(
    conductor, T_op=None, T_ref=DEFAULT_REFERENCE_TEMPERATURE
):
    """Evaluate a conductor resistivity callback at temperature ``T_op``."""

    material = getattr(conductor, "cond_mat", None)
    electrical = getattr(material, "elec", None) if material is not None else None
    if electrical is None or not hasattr(electrical, "get_resistivity"):
        return np.nan
    try:
        return float(electrical.get_resistivity(T_op=T_op, T_ref=T_ref))
    except Exception:
        return np.nan


def get_magnet_brm(magnet, T_op=None, T_ref=DEFAULT_REFERENCE_TEMPERATURE):
    """Evaluate a magnet remanence callback at temperature ``T_op``."""

    material = getattr(magnet, "mat_type", None)
    magnetic = getattr(material, "mag", None) if material is not None else None
    if magnetic is None or not hasattr(magnetic, "get_Brm"):
        return np.nan
    try:
        return float(magnetic.get_Brm(T_op=T_op, T_ref=T_ref))
    except Exception:
        return np.nan


def iter_machine_conductors(machine):
    """Yield ``(label, conductor, is_stator)`` for machine windings."""

    if machine is None or not hasattr(machine, "get_lam_list"):
        return

    label_counts = {}
    for lamination in machine.get_lam_list(is_int_to_ext=None):
        winding = getattr(lamination, "winding", None)
        conductor = getattr(winding, "conductor", None) if winding is not None else None
        if conductor is None:
            continue

        base = "stator" if getattr(lamination, "is_stator", False) else "rotor"
        index = label_counts.get(base, 0)
        label_counts[base] = index + 1
        label = base if index == 0 else f"{base}_{index}"
        yield label, conductor, getattr(lamination, "is_stator", False)


def _iter_lamination_magnets(lamination):
    if hasattr(lamination, "get_all_mag_obj"):
        try:
            for magnet in lamination.get_all_mag_obj():
                if magnet is not None:
                    yield magnet
            return
        except Exception:
            pass

    if hasattr(lamination, "get_hole_list"):
        try:
            hole_list = lamination.get_hole_list()
        except Exception:
            hole_list = []
        for hole in hole_list:
            if not hasattr(hole, "get_magnet_dict"):
                continue
            try:
                magnet_dict = hole.get_magnet_dict()
            except Exception:
                continue
            for magnet in magnet_dict.values():
                if magnet is not None:
                    yield magnet


def iter_machine_magnets(machine):
    """Yield ``(label, magnet, is_stator)`` for machine magnets."""

    if machine is None or not hasattr(machine, "get_lam_list"):
        return

    seen_ids = set()
    count = 0
    for lamination in machine.get_lam_list(is_int_to_ext=None):
        for magnet in _iter_lamination_magnets(lamination):
            obj_id = id(magnet)
            if obj_id in seen_ids:
                continue
            seen_ids.add(obj_id)
            label = f"magnet_{count}"
            count += 1
            yield label, magnet, getattr(lamination, "is_stator", False)


def resolve_lut_temperatures(elec=None, Tsta=None, Trot=None, Tmag=None):
    """Resolve LUT temperatures from explicit values or an Electrical object."""

    if elec is not None:
        if Tsta is None:
            Tsta = getattr(elec, "Tsta", None)
        if Trot is None:
            Trot = getattr(elec, "Trot", None)

    Tsta = _as_temperature(Tsta)
    Trot = _as_temperature(Trot)
    Tmag = _as_temperature(Tmag, fallback=Trot)
    return {"Tsta": Tsta, "Trot": Trot, "Tmag": Tmag}


def build_lut_temperature_context(machine, elec=None, Tsta=None, Trot=None, Tmag=None):
    """Evaluate the M4 temperature hooks for a machine without mutating it.

    The returned dict is intentionally simple so future thermal solvers can
    replace the scalar temperatures with per-region values while preserving the
    current isothermal default behavior.
    """

    temperatures = resolve_lut_temperatures(elec=elec, Tsta=Tsta, Trot=Trot, Tmag=Tmag)
    conductor_resistivity = {}
    magnet_Brm = {}

    for label, conductor, is_stator in iter_machine_conductors(machine):
        temperature = temperatures["Tsta"] if is_stator else temperatures["Trot"]
        value = get_conductor_resistivity(conductor, T_op=temperature)
        if np.isfinite(value):
            conductor_resistivity[label] = value

    for label, magnet, _is_stator in iter_machine_magnets(machine):
        value = get_magnet_brm(magnet, T_op=temperatures["Tmag"])
        if np.isfinite(value):
            magnet_Brm[label] = value

    return {
        **temperatures,
        "conductor_resistivity": conductor_resistivity,
        "magnet_Brm": magnet_Brm,
    }


def apply_lut_temperature_context(
    simu, source_elec=None, Tsta=None, Trot=None, Tmag=None
):
    """Apply scalar LUT temperatures to a simulation copy and return hook values."""

    elec = source_elec if source_elec is not None else getattr(simu, "elec", None)
    temperatures = resolve_lut_temperatures(elec=elec, Tsta=Tsta, Trot=Trot, Tmag=Tmag)

    target_elec = getattr(simu, "elec", None)
    if target_elec is not None:
        if hasattr(target_elec, "Tsta"):
            target_elec.Tsta = temperatures["Tsta"]
        if hasattr(target_elec, "Trot"):
            target_elec.Trot = temperatures["Trot"]

    target_mag = getattr(simu, "mag", None)
    if target_mag is not None and hasattr(target_mag, "T_mag"):
        target_mag.T_mag = temperatures["Tmag"]

    return build_lut_temperature_context(
        getattr(simu, "machine", None),
        Tsta=temperatures["Tsta"],
        Trot=temperatures["Trot"],
        Tmag=temperatures["Tmag"],
    )

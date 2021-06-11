from numpy import angle, pi, floor_divide

from ...Methods import NotImplementedYetError
from ...Functions.FEMM.get_mesh_param import get_mesh_param
from ...Functions.Winding.find_wind_phase_color import get_phase_id
from ...Functions.labels import (
    decode_label,
    get_obj_from_label,
    WIND_LAB,
    ROTOR_LAB,
    HOLEM_LAB,
)


def assign_FEMM_surface(femm, surf, prop, FEMM_dict, machine):
    """Assign the property given in parameter to surface having the label given
    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
    surf : Surface
        the surface to assign
    prop : str
        The property to assign in FEMM
    FEMM_dict : dict
        dictionary containing the main parameters of FEMM
    machine : Machine
        Machine to draw
    Returns
    -------
    None

    """

    label = surf.label
    label_dict = decode_label(label)
    mesh_dict = get_mesh_param(label_dict, FEMM_dict)

    Clabel = 0  # By default no circuit
    Ntcoil = 0  # By default no circuit
    mag = 0  # By default no magnetization

    # point_ref is None => don't assign the surface
    if surf.point_ref is not None:
        # Select the surface
        point_ref = surf.point_ref
        femm.mi_addblocklabel(point_ref.real, point_ref.imag)
        femm.mi_selectlabel(point_ref.real, point_ref.imag)

        # Get circuit or magnetization properties if needed
        if WIND_LAB in label_dict["surf_type"]:  # If the surface is a winding
            if ROTOR_LAB in label_dict["lam_type"]:  # Winding on the rotor
                Clabel = "Circr" + prop[:-1][2:]
            else:  # winding on the stator
                Clabel = "Circs" + prop[:-1][2:]
            lam_obj = get_obj_from_label(machine, label_dict=label_dict)
            wind_mat = lam_obj.winding.get_connection_mat(lam_obj.slot.get_Zs())
            Nrad_id = label_dict["R_id"]  # zone radial coordinate
            Ntan_id = label_dict["T_id"]  # zone tangential coordinate
            Zs_id = label_dict["S_id"]  # Zone slot number coordinate
            # Get the phase value in the correct slot zone
            q_id = get_phase_id(wind_mat, Nrad_id, Ntan_id, Zs_id)
            Ntcoil = wind_mat[Nrad_id, Ntan_id, Zs_id, q_id]
        elif HOLEM_LAB in label_dict["surf_type"]:  # LamHole
            mag_obj = get_obj_from_label(machine, label_dict=label_dict)
            if mag_obj.type_magnetization == 1:  # Parallel
                # calculate pole angle and angle of pole middle
                T_id = label_dict["T_id"]
                hole = mag_obj.parent
                Zh = hole.Zh
                alpha_p = 360 / Zh
                mag_0 = (
                    floor_divide(angle(point_ref, deg=True), alpha_p) + 0.5
                ) * alpha_p

                mag_dict = hole.comp_magnetization_dict()
                mag = mag_0 + mag_dict["magnet_" + str(T_id)] * 180 / pi

                # modifiy magnetisation of south poles
                if "_S_" in label:
                    mag = mag + 180
            else:
                raise NotImplementedYetError(
                    "Only parallele magnetization are available for HoleMagnet"
                )
        elif "Magnet" in label:  # LamSlotMag
            if "Radial" in label and "_N_" in label:  # Radial magnetization
                mag = "theta"  # North pole magnet
            elif "Radial" in label:
                mag = "theta + 180"  # South pole magnet
            elif "Parallel" in label and "_N_" in label:
                mag = angle(point_ref) * 180 / pi  # North pole magnet
            elif "Parallel" in label:
                mag = angle(point_ref) * 180 / pi + 180  # South pole magnet
            elif "Hallbach" in label:
                Zs = lam.slot.Zs
                mag = str(-(Zs / 2 - 1)) + " * theta + 90 "
        elif "Ventilation" in label:
            prop = "Air"
        elif "Hole" in label:
            prop = "Air"
        # Set the surface property
        femm.mi_setblockprop(
            prop,
            mesh_dict["automesh"],
            mesh_dict["meshsize"],
            Clabel,
            mag,
            mesh_dict["group"],
            Ntcoil,
        )
        femm.mi_clearselected()

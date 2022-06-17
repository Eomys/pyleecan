from numpy import angle, pi, floor_divide
from ...Classes.LamHole import LamHole
from ...Classes.LamHoleNS import LamHoleNS
from ...Functions.FEMM.get_mesh_param import get_mesh_param
from ...Methods import NotImplementedYetError
from ...Functions.Winding.find_wind_phase_color import get_phase_id
from ...Functions.labels import (
    decode_label,
    get_obj_from_label,
    WIND_LAB,
    ROTOR_LAB,
    HOLEM_LAB,
    HOLEV_LAB,
    MAG_LAB,
    VENT_LAB,
    BAR_LAB,
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

    group = mesh_dict["group"]

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
        if WIND_LAB in label_dict["surf_type"] or BAR_LAB in label_dict["surf_type"]:
            # If the surface is a winding or a bar => Set circuit
            lam_obj = get_obj_from_label(machine, label_dict=label_dict)
            wind_mat = lam_obj.winding.get_connection_mat(lam_obj.get_Zs())
            Nrad_id = label_dict["R_id"]  # zone radial coordinate
            Ntan_id = label_dict["T_id"]  # zone tangential coordinate
            Zs_id = label_dict["S_id"]  # Zone slot number coordinate
            # Get the phase value in the correct slot zone
            q_id = get_phase_id(wind_mat, Nrad_id, Ntan_id, Zs_id)
            if ROTOR_LAB in label_dict["lam_type"]:  # Winding on the rotor
                Clabel = "Circr" + str(q_id)
            else:  # winding on the stator
                Clabel = "Circs" + str(q_id)
            Ntcoil = wind_mat[Nrad_id, Ntan_id, Zs_id, q_id]
        elif HOLEM_LAB in label_dict["surf_type"]:  # LamHole
            mag_obj = get_obj_from_label(machine, label_dict=label_dict)
            # Parallel (default) or Tangential
            if mag_obj.type_magnetization in [1, 3, None]:
                # calculate pole angle and angle of pole middle
                T_id = label_dict["T_id"]
                hole = mag_obj.parent
                Zh = hole.Zh
                lam = hole.parent
                alpha_p = 360 / Zh
                mag_0 = (
                    floor_divide(angle(point_ref, deg=True), alpha_p) + 0.5
                ) * alpha_p

                mag_dict = hole.comp_magnetization_dict()
                mag = mag_0 + mag_dict["magnet_" + str(T_id)] * 180 / pi

                # modifiy magnetisation of south poles
                if isinstance(lam, LamHole):
                    if (label_dict["S_id"] % 2) == 1:
                        mag = mag + 180
                elif isinstance(lam, LamHoleNS):
                    if hole in lam.hole_south:
                        mag = mag + 180
                # Modify magnetisation for Tangential
                if mag_obj.type_magnetization == 3:
                    mag = mag - 90

                # Assign magnet group
                nb_hole = int(len(machine.rotor.get_hole_list()))
                nb_mag_per_hole = machine.rotor.get_magnet_number(
                    sym=machine.rotor.get_Zs()
                )
                grp_id = (
                    label_dict["S_id"] * nb_hole * nb_mag_per_hole + label_dict["T_id"]
                )
                group = group[grp_id]

            else:
                raise NotImplementedYetError(
                    "Only parallele magnetization are available for HoleMagnet found: "
                    + label
                )
        elif MAG_LAB in label_dict["surf_type"]:  # LamSlotMag
            mag_obj = get_obj_from_label(machine, label_dict=label_dict)

            # type_magnetization: 0 for radial, 1 for parallel, 2 for Hallbach
            if mag_obj.type_magnetization == 0 and (label_dict["S_id"] % 2) == 0:
                mag = "theta"  # Radial North pole magnet
            elif mag_obj.type_magnetization == 0:
                mag = "theta + 180"  # Radial South pole magnet
            elif mag_obj.type_magnetization == 1 and (label_dict["S_id"] % 2) == 0:
                mag = angle(point_ref) * 180 / pi  # Parallel North pole magnet
            elif mag_obj.type_magnetization == 1:
                mag = angle(point_ref) * 180 / pi + 180  # Parallel South pole magnet
            elif mag_obj.type_magnetization == 2:
                lam_obj = mag_obj.parent
                Zs = lam_obj.get_Zs()
                mag = str(-(Zs / 2 - 1)) + " * theta + 90 "
            elif mag_obj.type_magnetization == 3 and (label_dict["S_id"] % 2) == 0:
                mag = angle(point_ref) * 180 / pi - 90  # Tangential North pole magnet
            elif mag_obj.type_magnetization == 3:
                mag = (
                    angle(point_ref) * 180 / pi + 180 - 90
                )  # Tangential South pole magnet

            # Assign magnet group (assuming one magnet per pole)
            group = group[label_dict["S_id"]]

        elif VENT_LAB in label_dict["surf_type"]:
            vent_obj = get_obj_from_label(machine, label_dict=label_dict)
            prop = "Air"
        elif HOLEV_LAB in label_dict["surf_type"]:
            hole_obj = get_obj_from_label(machine, label_dict=label_dict)
            prop = "Air"

        # Set the surface property
        femm.mi_setblockprop(
            prop,
            mesh_dict["automesh"],
            mesh_dict["meshsize"],
            Clabel,
            mag,
            group,
            Ntcoil,
        )
        femm.mi_clearselected()

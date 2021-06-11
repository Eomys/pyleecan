# -*- coding: utf-8 -*-
from numpy import angle, pi, floor_divide
from ...Classes.HoleM50 import HoleM50
from ...Classes.HoleM51 import HoleM51
from ...Classes.HoleM52 import HoleM52
from ...Classes.HoleM53 import HoleM53
from ...Methods import NotImplementedYetError
from ...Functions.FEMM.get_mesh_param import get_mesh_param
from ...Functions.Winding.find_wind_phase_color import get_phase_id
from ...Functions.labels import decode_label


def assign_FEMM_surface(femm, surf, prop, FEMM_dict, rotor, stator):
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
    rotor : Lamination
        The rotor of the machine
    stator : Lamination
        The stator of the machine
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

    # Select the lamination according to the label
    if "Rotor" in label:
        lam = rotor
    else:
        lam = stator

    # point_ref is None => don't assign the surface
    if surf.point_ref is not None:
        # Select the surface
        point_ref = surf.point_ref
        femm.mi_addblocklabel(point_ref.real, point_ref.imag)
        femm.mi_selectlabel(point_ref.real, point_ref.imag)

        # Get circuit or magnetization properties if needed
        if "Wind" in label or "Bar" in label:  # If the surface is a winding
            if "Rotor" in label:  # Winding on the rotor
                Clabel = "Circr" + prop[:-1][2:]
            else:  # winding on the stator
                Clabel = "Circs" + prop[:-1][2:]
            # Decode the label
            # TODO from create_FEMM_circuit_material -> move to decode/encode func.
            wind_mat = lam.winding.get_connection_mat(lam.slot.Zs)
            st = label.split("_")
            Nrad_id = int(st[2][1:])  # zone radial coordinate
            Ntan_id = int(st[3][1:])  # zone tangential coordinate
            Zs_id = int(st[4][1:])  # Zone slot number coordinate
            # Get the phase value in the correct slot zone
            q_id = get_phase_id(wind_mat, Nrad_id, Ntan_id, Zs_id)
            Ntcoil = wind_mat[Nrad_id, Ntan_id, Zs_id, q_id]
        elif "HoleMagnet" in label:  # LamHole
            if "Parallel" in label:
                # calculate pole angle and angle of pole middle
                # label like 'HoleMagnet_Rotor_Parallel_N_R0_T0_S0'
                label_split = label.split("_")
                R_id = int(label_split[-3][1:])
                T_id = int(label_split[-2][1:])
                alpha_p = 360 / lam.hole[R_id].Zh
                mag_0 = (
                    floor_divide(angle(point_ref, deg=True), alpha_p) + 0.5
                ) * alpha_p

                mag_dict = lam.hole[R_id].comp_magnetization_dict()
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

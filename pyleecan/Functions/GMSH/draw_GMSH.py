from ...Classes.Arc import Arc
from ...Classes.Arc2 import Arc2
from ...Classes.MachineSIPMSM import MachineSIPMSM

from ...Functions.labels import (
    HOLEM_LAB_S,
    MAG_LAB,
    short_label,
    LAM_LAB,
    LAM_LAB_S,
    SHAFT_LAB,
    decode_label,
    SLID_LAB,
    AIRGAP_LAB,
    BOT_LAB,
    AIRBOX_LAB,
)
from ...Functions.GMSH import InputError
from ...Functions.GMSH.get_sliding_band import get_sliding_band
from ...Functions.GMSH.get_air_box import get_air_box
from ...Functions.GMSH.get_boundary_condition import get_boundary_condition
from ...Functions.GMSH.draw_surf_line import draw_surf_line
import sys
import gmsh
import cmath

from os import replace
from os.path import splitext

from numpy import pi


def draw_GMSH(
    output,
    sym,
    boundary_prop,
    is_lam_only_S=False,
    is_lam_only_R=False,
    user_mesh_dict={},
    path_save="GMSH_model.msh",
    is_sliding_band=True,
    is_airbox=False,
    is_set_labels=False,
    is_run=False,
):
    """Draws a machine mesh in GMSH format

    Parameters
    ----------
    output : Output
        Output object
    sym : int
        the symmetry applied on the stator and the rotor (take into account antiperiodicity)
    boundary_prop : dict
        dictionary to match FEA boundary conditions (dict values) with line boundary property (dict keys)
    is_lam_only_S: bool
        Draw only stator lamination
    is_lam_only_R: bool
        Draw only rotor lamination
    user_mesh_dict :dict
        Dictionary to enforce the mesh size on some surface/lines (key: surface label, value dict:key=line id, value:nb element)
    path_save : str
        Path to save the result msh file
    is_sliding_band : bool
        True uses sliding band, else airgap (Not implemented yet)
    is_airbox : bool
        True to add the airbox
    is_set_label : bool
        True to set all line labels as physical groups
    is_run : bool
        True to launch Gmsh GUI at the end

    Returns
    -------
    GMSH_dict : dict
        dictionary containing the main parameters of GMSH File
    """
    # check some input parameter
    if is_lam_only_S and is_lam_only_R:
        raise InputError(
            "is_lam_only_S and is_lam_only_R can't be True at the same time"
        )

    # get machine
    machine = output.simu.machine
    mesh_dict = {}
    tol = 1e-6

    # Default stator mesh element size
    mesh_size_S = machine.stator.Rext / 100.0  # Stator
    mesh_size_R = machine.rotor.Rext / 25.0  # Rotor
    mesh_size_SB = 2.0 * pi * machine.rotor.Rext / 360.0  # Sliding Band
    mesh_size_AB = machine.stator.Rext / 50.0  # AirBox

    # For readibility
    model = gmsh.model
    factory = model.geo

    # Start a new model
    gmsh.initialize()
    gmsh.option.setNumber("General.Terminal", int(False))
    gmsh.option.setNumber("Geometry.CopyMeshingMethod", 1)
    gmsh.option.setNumber("Geometry.PointNumbers", 0)
    gmsh.option.setNumber("Geometry.LineNumbers", 0)
    gmsh.option.setNumber("Mesh.CharacteristicLengthMin", min(mesh_size_S, mesh_size_R))
    gmsh.option.setNumber("Mesh.CharacteristicLengthMax", max(mesh_size_S, mesh_size_R))
    model.add("Pyleecan")

    # build geometry
    alpha = 0
    rotor_list = list()
    if machine.shaft is not None:
        rotor_list.extend(machine.shaft.build_geometry(sym=sym, alpha=alpha))
    rotor_surf = machine.rotor.build_geometry(sym=sym, alpha=alpha)
    if sym == 1 and machine.shaft is not None:
        # Remove Rotor internal radius (use shaft one)
        # first surface is a SurfRing (cf Lamination.build_geometry)
        rotor_surf[0] = rotor_surf[0].out_surf
    rotor_list.extend(rotor_surf)
    stator_list = list()
    stator_list.extend(machine.stator.build_geometry(sym=sym, alpha=alpha))

    #####################
    # Adding Rotor
    #####################
    # set origin
    oo = factory.addPoint(0, 0, 0, 0, tag=-1)
    gmsh_dict = {
        0: {
            "tag": 0,
            "label": "origin",
            "with_holes": False,
            1: {
                "tag": 0,
                "n_elements": 1,
                "bc_name": None,
                "begin": {"tag": oo, "coord": complex(0.0, 0.0)},
                "end": {"tag": None, "coord": None},
                "cent": {"tag": None, "coord": None},
                "arc_angle": None,
                "line_angle": None,
            },
        }
    }

    nsurf = 0  # number of surfaces
    # Drawing Rotor and Shaft surfaces
    if not is_lam_only_S:
        for surf in rotor_list:
            nsurf += 1
            # print(surf.label)
            gmsh_dict.update(
                {
                    nsurf: {
                        "tag": None,
                        "label": short_label(surf.label),
                    }
                }
            )
            if LAM_LAB in decode_label(surf.label)["surf_type"]:
                gmsh_dict[nsurf]["with_holes"] = True
                lam_rotor_surf_id = nsurf
            else:
                gmsh_dict[nsurf]["with_holes"] = False

            # comp. number of elements on the lines & override by user values in case
            mesh_dict = surf.comp_mesh_dict(element_size=mesh_size_R)
            if user_mesh_dict and surf.label in user_mesh_dict:
                mesh_dict.update(user_mesh_dict[surf.label])
            # Draw the surface
            draw_surf_line(
                surf,
                mesh_dict,
                boundary_prop,
                factory,
                gmsh_dict,
                nsurf,
                mesh_size_R,
            )

        lam_and_holes = list()
        ext_lam_loop = None
        rotor_cloops = list()
        # loop though all (surface) entries of the rotor lamination
        for s_data in gmsh_dict.values():
            lloop = []
            # skip this surface dataset if it is the origin
            if s_data["label"] == "origin":
                continue

            # build a lineloop of the surfaces lines
            for lvalues in s_data.values():
                if type(lvalues) is not dict:
                    continue
                lloop.extend([lvalues["tag"]])
            cloop = factory.addCurveLoop(lloop)

            label_dict = decode_label(s_data["label"])
            if (
                MAG_LAB in label_dict["surf_type"]
                or HOLEM_LAB_S in label_dict["surf_type"]
            ):
                # Surface of Hole Magnet
                rotor_cloops.extend([cloop])

            # search for the holes to substract from rotor lam
            if LAM_LAB_S in label_dict["surf_type"]:
                ext_lam_loop = cloop
            else:
                # MachineSIPSM does not have holes in rotor lam
                # only shaft is taken out if symmetry is one
                if isinstance(machine, MachineSIPMSM):
                    if sym == 1 and SHAFT_LAB in label_dict["surf_type"]:
                        lam_and_holes.extend([cloop])
                else:
                    if sym == 1:
                        lam_and_holes.extend([cloop])
                    elif SHAFT_LAB not in label_dict["surf_type"]:
                        lam_and_holes.extend([cloop])
                    else:
                        pass

                # Shaft, magnets and magnet pocket surfaces are created
                if not is_lam_only_R:
                    s_data["tag"] = factory.addPlaneSurface([cloop], tag=-1)
                    pg = model.addPhysicalGroup(2, [s_data["tag"]])
                    model.setPhysicalName(2, pg, s_data["label"])

        # Finally rotor lamination is built
        if ext_lam_loop is not None:
            lam_and_holes.insert(0, ext_lam_loop)
        if len(lam_and_holes) > 0:
            gmsh_dict[lam_rotor_surf_id]["tag"] = factory.addPlaneSurface(
                lam_and_holes, tag=-1
            )
        pg = model.addPhysicalGroup(2, [gmsh_dict[lam_rotor_surf_id]["tag"]])
        model.setPhysicalName(2, pg, gmsh_dict[lam_rotor_surf_id]["label"])
        # rotor_cloops = lam_and_holes

    # store rotor dict
    rotor_dict = gmsh_dict.copy()

    #####################
    # Adding Stator
    #####################
    # init new dict for stator
    gmsh_dict = {
        0: {
            "tag": 0,
            "label": "origin",
            "with_holes": False,
            1: {
                "tag": 0,
                "n_elements": 1,
                "bc_name": None,
                "begin": {"tag": oo, "coord": complex(0.0, 0.0)},
                "end": {"tag": None, "coord": None},
                "cent": {"tag": None, "coord": None},
            },
        }
    }

    # nsurf = 0
    if not is_lam_only_R:
        stator_cloops = []
        for surf in stator_list:
            nsurf += 1
            gmsh_dict.update(
                {
                    nsurf: {
                        "tag": None,
                        "label": short_label(surf.label),
                    }
                }
            )
            if LAM_LAB in decode_label(surf.label)["surf_type"]:
                gmsh_dict[nsurf]["with_holes"] = True
            else:
                gmsh_dict[nsurf]["with_holes"] = False

            # comp. number of elements on the lines & override by user values in case
            mesh_dict = surf.comp_mesh_dict(element_size=mesh_size_S)
            if user_mesh_dict and surf.label in user_mesh_dict:
                mesh_dict.update(user_mesh_dict[surf.label])

            # Draw the surface
            draw_surf_line(
                surf,
                mesh_dict,
                boundary_prop,
                factory,
                gmsh_dict,
                nsurf,
                mesh_size_S,
            )

        for s_data in gmsh_dict.values():
            lloop = []
            # skip this surface dataset if it is the origin
            if s_data["label"] == "origin":
                continue

            # build a lineloop of the surfaces lines
            for lvalues in s_data.values():
                if type(lvalues) is not dict:
                    continue
                lloop.extend([lvalues["tag"]])
            cloop = factory.addCurveLoop(lloop)
            stator_cloops.append(cloop)

            # Winding surfaces are created
            if LAM_LAB_S in decode_label(s_data["label"])["surf_type"] or (
                not is_lam_only_S
            ):
                s_data["tag"] = factory.addPlaneSurface([cloop], tag=-1)
                pg = model.addPhysicalGroup(2, [s_data["tag"]])
                model.setPhysicalName(2, pg, s_data["label"])

        # stator_dict = gmsh_dict.copy()

    gmsh_dict.update(rotor_dict)

    #####################
    # Adding Sliding Band
    #####################
    if is_sliding_band and (not is_lam_only_R) and (not is_lam_only_S):
        sb_list = get_sliding_band(sym=sym, machine=machine)
    else:
        sb_list = []

    # nsurf = 0
    for surf in sb_list:
        nsurf += 1
        gmsh_dict.update(
            {
                nsurf: {
                    "tag": None,
                    "label": short_label(surf.label),
                }
            }
        )
        # comp. number of elements on the lines & override by user values in case
        mesh_dict = surf.comp_mesh_dict(element_size=mesh_size_SB)
        if user_mesh_dict and surf.label in user_mesh_dict:
            mesh_dict.update(user_mesh_dict[surf.label])

        # Draw the surface
        draw_surf_line(
            surf,
            mesh_dict,
            boundary_prop,
            factory,
            gmsh_dict,
            nsurf,
            mesh_size_SB,
        )

    for s_data in gmsh_dict.values():
        lloop = []
        label_dict = decode_label(s_data["label"])

        # skip this surface dataset if it is the origin
        if s_data["label"] == "origin" or not (
            AIRGAP_LAB in label_dict["surf_type"] or SLID_LAB in label_dict["surf_type"]
        ):
            continue

        # build a lineloop of the surfaces lines
        for lvalues in s_data.values():
            if type(lvalues) is not dict:
                continue
            lloop.extend([lvalues["tag"]])

        if lloop:
            cloop = factory.addCurveLoop(lloop)
            if (
                AIRGAP_LAB in label_dict["surf_type"]
                and BOT_LAB in label_dict["surf_type"]
                and isinstance(machine, MachineSIPMSM)
            ):
                s_data["tag"] = factory.addPlaneSurface([cloop] + rotor_cloops, tag=-1)
            else:
                s_data["tag"] = factory.addPlaneSurface([cloop], tag=-1)
            pg = model.addPhysicalGroup(2, [s_data["tag"]])
            model.setPhysicalName(2, pg, s_data["label"])

    ###################
    # Adding Airbox
    ###################
    if is_airbox and (not is_lam_only_R) and (not is_lam_only_S):
        ab_list = get_air_box(sym=sym, machine=machine)
    else:
        ab_list = []

    # Default airbox mesh element size
    for surf in ab_list:
        nsurf += 1
        gmsh_dict.update(
            {
                nsurf: {
                    "tag": None,
                    "label": short_label(surf.label),
                }
            }
        )

        # comp. number of elements on the lines & override by user values in case
        mesh_dict = surf.comp_mesh_dict(element_size=mesh_size_AB)
        if user_mesh_dict and surf.label in user_mesh_dict:
            mesh_dict.update(user_mesh_dict[surf.label])

        # Draw the surface
        draw_surf_line(
            surf,
            mesh_dict,
            boundary_prop,
            factory,
            gmsh_dict,
            nsurf,
            mesh_size_AB,
        )

    for s_id, s_data in gmsh_dict.items():
        lloop = []
        if s_id == 0:
            continue
        for lvalues in s_data.values():
            if AIRBOX_LAB in decode_label(s_data["label"])["surf_type"]:
                if type(lvalues) is not dict:
                    continue
                lloop.extend([lvalues["tag"]])
            else:
                continue
        if lloop:
            cloop = factory.addCurveLoop(lloop)
            s_data["tag"] = factory.addPlaneSurface([cloop], tag=-1)
            pg = model.addPhysicalGroup(2, [s_data["tag"]])
            model.setPhysicalName(2, pg, s_data["label"])

    # Set boundary conditions in gmsh lines
    boundary_list = list(set(boundary_prop.values()))
    for propname in boundary_list:
        bc_id = []
        for s_data in gmsh_dict.values():
            for lvalues in s_data.values():
                if type(lvalues) is not dict:
                    continue
                if lvalues["bc_name"] == propname:
                    bc_id.extend([abs(lvalues["tag"])])
        if bc_id:
            pg = model.addPhysicalGroup(1, bc_id)
            model.setPhysicalName(1, pg, propname)

    # Set all line labels as physical groups
    if is_set_labels:
        groups = {}
        for s_data in gmsh_dict.values():
            for lvalues in s_data.values():
                if (
                    type(lvalues) is not dict
                    or "label" not in lvalues
                    or not lvalues["label"]
                ):
                    continue

                if lvalues["label"] not in groups.keys():
                    groups[lvalues["label"]] = []
                groups[lvalues["label"]].append(abs(lvalues["tag"]))

        for label, tags in groups.items():
            pg = model.addPhysicalGroup(1, tags)
            model.setPhysicalName(1, pg, label)

    factory.synchronize()

    # save mesh or geo file depending on file extension
    filename, file_extension = splitext(path_save)

    if file_extension == ".geo":
        gmsh.write(filename + ".geo_unrolled")
        replace(filename + ".geo_unrolled", filename + file_extension)
    else:
        gmsh.model.mesh.generate(2)
        gmsh.write(path_save)

    if is_run:
        gmsh.fltk.run()  # Uncomment to launch Gmsh GUI
    gmsh.finalize()
    return gmsh_dict

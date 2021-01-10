from ...Classes.Arc import Arc
from ...Classes.Arc2 import Arc2
from ...Classes.MachineSIPMSM import MachineSIPMSM

from ...Functions.GMSH import InputError
from ...Functions.GMSH.get_sliding_band import get_sliding_band
from ...Functions.GMSH.get_air_box import get_air_box
from ...Functions.GMSH.get_boundary_condition import get_boundary_condition

import sys
import gmsh
import cmath

from os import replace
from os.path import splitext

from numpy import pi


def _find_point_tag(d={}, p=complex(0.0, 0.0)):
    """Find a point in the GMSH dictionary

    Parameters
    ----------
    d : Dictionary
        GMSH dictionary
    p : Complex
        Point coordinates

    Returns
    -------
    tag : int
        Existing tag number or new one if it does not exist
    real : float
        Real coordinates of point
    imag : float
        Imaginary coordinates of point
    """
    tol = 1e-6
    for s_data in d.values():
        for lvalues in s_data.values():
            if type(lvalues) is not dict:
                continue
            for pvalues in lvalues.values():
                if type(pvalues) is not dict:
                    continue
                if pvalues["tag"] is not None:
                    b = pvalues["coord"]
                    if abs(p.real - b.real) < tol and abs(p.imag - b.imag) < tol:
                        return pvalues["tag"], b.real, b.imag
    return None, p.real, p.imag


def _find_points_from_line(d={}, ltag=-1):
    """Find points tag from existing lines

    Parameters
    ----------
    d : Dictionary
        GMSH dictionary
    ltag : int
        line tag

    Returns
    -------
    coord : float
        Coordinates of point if found
    """
    btag = None
    etag = None
    ctag = None
    for s_data in d.values():
        for lvalues in s_data.values():
            if type(lvalues) is not dict:
                continue
            if lvalues["tag"] != ltag:
                continue
            else:
                for pid, pvalues in lvalues.items():
                    if type(pvalues) is not dict:
                        continue
                    if pid == "begin":
                        btag = pvalues["tag"]
                    elif pid == "end":
                        etag = pvalues["tag"]
                    elif pid == "cent":
                        ctag = pvalues["tag"]
                break
    return [btag, etag, ctag]


def _find_lines_from_point(d={}, ptag=-1):
    """Find lines that have the given point tag

    Parameters
    ----------
    d : Dictionary
        GMSH dictionary
    ptag : int
        point tag

    Returns
    -------
    ltag : int
        List of line tags
    """
    lines = list()
    for s_data in d.values():
        for lvalues in s_data.values():
            if type(lvalues) is not dict:
                continue
            for pvalues in lvalues.values():
                if type(pvalues) is not dict:
                    continue
                if pvalues["tag"] == ptag:
                    lines.append(lvalues["tag"])
    return lines


def _add_line_to_dict(geo, line, d={}, idx=0, mesh_size=1e-2, n_elements=0, bc=None):
    """Draw a new line and add it to GMSH dictionary if it does not exist

    Parameters
    ----------
    geo : Model
        GMSH Model objet
    line : Object
        Line Object
    d : Dictionary
        GMSH dictionary
    idx : int
        Surface index it belongs to
    mesh_size : float
        Points mesh size
    n_elements : int
        Number of elements on the line for meshing control

    Returns
    -------
    None
    """

    dlines = list()
    ltag = None
    btag, bx, by = _find_point_tag(d, line.get_begin())
    etag, ex, ey = _find_point_tag(d, line.get_end())
    if btag is None:
        btag = geo.addPoint(bx, by, 0, meshSize=mesh_size, tag=-1)
    else:
        dlines.extend(_find_lines_from_point(d, btag))
    if etag is None:
        etag = geo.addPoint(ex, ey, 0, meshSize=mesh_size, tag=-1)
    else:
        dlines.extend(_find_lines_from_point(d, etag))
    if isinstance(line, Arc):
        ctag, cx, cy = _find_point_tag(d, line.get_center())
        if ctag is None:
            ctag = geo.addPoint(cx, cy, 0, meshSize=mesh_size, tag=-1)
        else:
            dlines.extend(_find_lines_from_point(d, ctag))
        if len(dlines) > 0:
            for iline in dlines:
                p = _find_points_from_line(d, iline)
                if p[0] == btag and p[1] == etag and p[2] == ctag:
                    ltag = iline
                    break
                elif p[0] == etag and p[1] == btag and p[2] == ctag:
                    ltag = -iline
                    break
                else:
                    pass
            if ltag is None:
                ltag = geo.addCircleArc(btag, ctag, etag, tag=-1)
                if n_elements > 0:
                    geo.mesh.setTransfiniteCurve(ltag, n_elements + 1, "Progression")
        else:
            ltag = geo.addCircleArc(btag, ctag, etag, tag=-1)
            if n_elements > 0:
                geo.mesh.setTransfiniteCurve(ltag, n_elements + 1, "Progression")

        # To avoid fill the dictionary with repeated lines
        repeated = False
        for lvalues in d[idx].values():
            if type(lvalues) is not dict:
                continue
            else:
                if lvalues["tag"] == ltag:
                    repeated = True

        if not repeated:
            nline = len(d[idx]) - 2
            arc_angle = cmath.phase(complex(ex, ey)) - cmath.phase(complex(bx, by))
            d[idx].update(
                {
                    nline: {
                        "tag": ltag,
                        "n_elements": n_elements,
                        "bc_name": bc,
                        "begin": {"tag": btag, "coord": complex(bx, by)},
                        "end": {"tag": etag, "coord": complex(ex, ey)},
                        "cent": {"tag": ctag, "coord": complex(cx, cy)},
                        "arc_angle": arc_angle,
                        "line_angle": None,
                        "label": line.label,
                    }
                }
            )

    else:
        if len(dlines) > 0:
            for iline in dlines:
                p = _find_points_from_line(d, iline)
                if p[0] == btag and p[1] == etag:
                    ltag = iline
                    break
                elif p[0] == etag and p[1] == btag:
                    ltag = -iline
                    break
                else:
                    pass
            if ltag is None:
                ltag = geo.addLine(btag, etag, tag=-1)
                if n_elements > 0:
                    geo.mesh.setTransfiniteCurve(ltag, n_elements + 1, "Progression")
        else:
            ltag = geo.addLine(btag, etag, tag=-1)
            if n_elements > 0:
                geo.mesh.setTransfiniteCurve(ltag, n_elements + 1, "Progression")

        # To avoid fill the dictionary with repeated lines
        repeated = False
        for lvalues in d[idx].values():
            if type(lvalues) is not dict:
                continue
            else:
                if lvalues["tag"] == ltag:
                    repeated = True

        if not repeated:
            nline = len(d[idx]) - 2
            line_angle = 0.5 * (
                cmath.phase(complex(ex, ey)) + cmath.phase(complex(bx, by))
            )
            d[idx].update(
                {
                    nline: {
                        "tag": ltag,
                        "n_elements": n_elements,
                        "bc_name": bc,
                        "begin": {"tag": btag, "coord": complex(bx, by)},
                        "end": {"tag": etag, "coord": complex(ex, ey)},
                        "arc_angle": None,
                        "line_angle": line_angle,
                        "label": line.label,
                    }
                }
            )

    return None


def _add_agline_to_dict(geo, line, d={}, idx=0, mesh_size=1e-2, n_elements=0, bc=None):
    """Draw a new Air Gap line and add it to GMSH dictionary if it does not exist

    Parameters
    ----------
    geo : Model
        GMSH Model objet
    line : Object
        Line Object
    d : Dictionary
        GMSH dictionary
    idx : int
        Surface index it belongs to
    mesh_size : float
        Points mesh size
    n_elements : int
        Number of elements on the line for meshing control

    Returns
    -------
    None
    """

    # TO-DO: Allow repeated points for the rotor and stator sliding bands
    dlines = list()
    ltag = None
    btag, bx, by = _find_point_tag(d, line.get_begin())
    etag, ex, ey = _find_point_tag(d, line.get_end())
    if btag is None:
        btag = geo.addPoint(bx, by, 0, meshSize=mesh_size, tag=-1)
    else:
        dlines.extend(_find_lines_from_point(d, btag))
    if etag is None:
        etag = geo.addPoint(ex, ey, 0, meshSize=mesh_size, tag=-1)
    else:
        dlines.extend(_find_lines_from_point(d, etag))
    if isinstance(line, Arc):
        ctag, cx, cy = _find_point_tag(d, line.get_center())
        if ctag is None:
            ctag = geo.addPoint(cx, cy, 0, meshSize=mesh_size, tag=-1)
        else:
            dlines.extend(_find_lines_from_point(d, ctag))
        if len(dlines) > 0:
            for iline in dlines:
                p = _find_points_from_line(d, iline)
                if p[0] == btag and p[1] == etag and p[2] == ctag:
                    ltag = iline
                    break
                elif p[0] == etag and p[1] == btag and p[2] == ctag:
                    ltag = -iline
                    break
                else:
                    pass
            if ltag is None:
                ltag = geo.addCircleArc(btag, ctag, etag, tag=-1)
                if n_elements > 0:
                    geo.mesh.setTransfiniteCurve(ltag, n_elements + 1, "Progression")
        else:
            ltag = geo.addCircleArc(btag, ctag, etag, tag=-1)
            if n_elements > 0:
                geo.mesh.setTransfiniteCurve(ltag, n_elements + 1, "Progression")

        # To avoid fill the dictionary with repeated lines
        repeated = False
        for lvalues in d[idx].values():
            if type(lvalues) is not dict:
                continue
            else:
                if lvalues["tag"] == ltag:
                    repeated = True

        if not repeated:
            nline = len(d[idx]) - 2
            arc_angle = cmath.phase(complex(ex, ey)) - cmath.phase(complex(bx, by))
            d[idx].update(
                {
                    nline: {
                        "tag": ltag,
                        "n_elements": n_elements,
                        "bc_name": bc,
                        "begin": {"tag": btag, "coord": complex(bx, by)},
                        "end": {"tag": etag, "coord": complex(ex, ey)},
                        "cent": {"tag": ctag, "coord": complex(cx, cy)},
                        "arc_angle": arc_angle,
                        "line_angle": None,
                    }
                }
            )

    else:
        if len(dlines) > 0:
            for iline in dlines:
                p = _find_points_from_line(d, iline)
                if p[0] == btag and p[1] == etag:
                    ltag = iline
                    break
                elif p[0] == etag and p[1] == btag:
                    ltag = -iline
                    break
                else:
                    pass
            if ltag is None:
                ltag = geo.addLine(btag, etag, tag=-1)
                if n_elements > 0:
                    geo.mesh.setTransfiniteCurve(ltag, n_elements + 1, "Progression")
        else:
            ltag = geo.addLine(btag, etag, tag=-1)
            if n_elements > 0:
                geo.mesh.setTransfiniteCurve(ltag, n_elements + 1, "Progression")

        # To avoid fill the dictionary with repeated lines
        repeated = False
        for lvalues in d[idx].values():
            if type(lvalues) is not dict:
                continue
            else:
                if lvalues["tag"] == ltag:
                    repeated = True

        if not repeated:
            nline = len(d[idx]) - 2
            line_angle = 0.5 * (
                cmath.phase(complex(ex, ey)) + cmath.phase(complex(bx, by))
            )
            d[idx].update(
                {
                    nline: {
                        "tag": ltag,
                        "n_elements": n_elements,
                        "bc_name": bc,
                        "begin": {"tag": btag, "coord": complex(bx, by)},
                        "end": {"tag": etag, "coord": complex(ex, ey)},
                        "arc_angle": None,
                        "line_angle": line_angle,
                    }
                }
            )

    return None


def draw_GMSH(
    output,
    sym,
    boundary_prop,
    boundary_list,
    surface_label,
    is_antiper=False,
    is_remove_vent=False,
    is_remove_slotS=False,
    is_remove_slotR=False,
    is_lam_only_S=False,
    is_lam_only_R=False,
    kgeo_fineness=1,
    kmesh_fineness=1,
    user_mesh_dict={},
    path_save="GMSH_model.msh",
    is_sliding_band=False,
    is_airbox=False,
    transform_list=[],
    is_set_labels=False,
):
    """Draws a machine mesh in GMSH format

    Parameters
    ----------
    output : Output
        Output object
    sym : int
        the symmetry applied on the stator and the rotor (take into account antiperiodicity)
    boundary_prop : dict
        dictionary to match FEA boundary conditions (dict values) with line labels (dict keys) that are set in the build_geometry methods
    boundary_list : list
        list of boundary condition names
    surface_label : dict
        dict for the translation of the actual surface labels into FEA software compatible labels
    is_remove_vent : bool
        True to remove the ventilation ducts (Default value = False)
    is_remove_slotS : bool
        True to solve without slot effect on the Stator (Default value = False)
    is_remove_slotR : bool
        True to solve without slot effect on the Rotor (Default value = False)
    kgeo_fineness : float
        global coefficient to adjust geometry fineness
    kmesh_fineness : float
        global coefficient to adjust mesh fineness
    is_antiper: bool
        To apply antiperiodicity boundary conditions
    is_lam_only_S: bool
        Draw only stator lamination
    is_lam_only_R: bool
        Draw only rotor lamination

    Returns
    -------
    GMSH_dict : dict
        Dictionnary containing the main parameters of GMSH File
    """
    # check some input parameter
    if is_lam_only_S and is_lam_only_R:
        raise InputError(
            "Only 'is_lam_only_S' or 'is_lam_only_R' can be True at the same time"
        )

    # get machine
    machine = output.simu.machine
    mesh_dict = {}
    tol = 1e-6

    # Default stator mesh element size
    mesh_size_S = machine.stator.Rext / 100.0
    mesh_size_R = machine.rotor.Rext / 25.0

    # For readibility
    model = gmsh.model
    factory = model.geo

    # Start a new model
    gmsh.initialize(sys.argv)
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
    rotor_list.extend(machine.shaft.build_geometry(sym=sym, alpha=alpha))
    rotor_list.extend(machine.rotor.build_geometry(sym=sym, alpha=alpha))
    stator_list = list()
    stator_list.extend(machine.stator.build_geometry(sym=sym, alpha=alpha))

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
    if not is_lam_only_S:
        for surf in rotor_list:
            nsurf += 1
            gmsh_dict.update(
                {
                    nsurf: {
                        "tag": None,
                        "label": surface_label.get(surf.label, "UNKNOWN"),
                    }
                }
            )
            if "Lamination_Rotor" in surf.label:
                gmsh_dict[nsurf]["with_holes"] = True
                lam_rotor_surf_id = nsurf
            else:
                gmsh_dict[nsurf]["with_holes"] = False

            # comp. number of elements on the lines & override by user values in case
            mesh_dict = surf.comp_mesh_dict(element_size=mesh_size_R)
            if user_mesh_dict:  # check if dict is not None nor empty
                mesh_dict.update(user_mesh_dict)

            # add all lines of the current surface to the gmsh_dict
            for line in surf.get_lines():
                # When symmetry is 1 the shaft surface is substrtacted from Rotor Lam instead
                if sym == 1 and line.label == "Lamination_Rotor_Yoke_Radius_Int":
                    continue
                n_elem = mesh_dict.get(line.label)
                n_elem = n_elem if n_elem is not None else 0
                bc_name = get_boundary_condition(line, boundary_prop)

                # Gmsh built-in engine does not allow arcs larger than 180deg
                # so arcs are split into two
                if (
                    isinstance(line, Arc)
                    and abs(line.get_angle() * 180.0 / cmath.pi) >= 180.0
                ):
                    rot_dir = 1 if line.is_trigo_direction == True else -1
                    arc1 = Arc2(
                        begin=line.get_begin(),
                        center=line.get_center(),
                        angle=rot_dir * cmath.pi / 2.0,
                        label=line.label,
                    )
                    arc2 = Arc2(
                        begin=arc1.get_end(),
                        center=line.get_center(),
                        angle=rot_dir * cmath.pi / 2.0,
                        label=line.label,
                    )
                    for arc in [arc1, arc2]:
                        _add_line_to_dict(
                            geo=factory,
                            line=arc,
                            d=gmsh_dict,
                            idx=nsurf,
                            mesh_size=mesh_size_R,
                            n_elements=n_elem,
                            bc=bc_name,
                        )
                elif isinstance(line, Arc) and (
                    abs(line.get_angle() * 180.0 / cmath.pi) <= tol
                ):
                    # Don't draw anything, this is a circle and usually is repeated ?
                    pass
                else:
                    _add_line_to_dict(
                        geo=factory,
                        line=line,
                        d=gmsh_dict,
                        idx=nsurf,
                        mesh_size=mesh_size_R,
                        n_elements=n_elem,
                        bc=bc_name,
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
            if "MAGNET" in s_data["label"]:
                rotor_cloops.extend([cloop])

            # search for the holes to substract from rotor lam
            if "ROTOR_LAM" in s_data["label"]:
                ext_lam_loop = cloop
            else:
                # MachineSIPSM does not have holes in rotor lam
                # only shaft is taken out if symmetry is one
                if isinstance(machine, MachineSIPMSM):
                    if sym == 1 and s_data["label"] == "SHAFT":
                        lam_and_holes.extend([cloop])
                else:
                    if sym == 1:
                        lam_and_holes.extend([cloop])
                    elif s_data["label"] != "SHAFT":
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
        gmsh_dict[lam_rotor_surf_id]["tag"] = factory.addPlaneSurface(
            lam_and_holes, tag=-1
        )
        pg = model.addPhysicalGroup(2, [gmsh_dict[lam_rotor_surf_id]["tag"]])
        model.setPhysicalName(2, pg, gmsh_dict[lam_rotor_surf_id]["label"])
        # rotor_cloops = lam_and_holes

    # store rotor dict
    rotor_dict = gmsh_dict.copy()

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
                        "label": surface_label.get(surf.label, "UNKNOWN"),
                    }
                }
            )
            if surf.label.find("Lamination_Stator") != -1:
                gmsh_dict[nsurf]["with_holes"] = True
            else:
                gmsh_dict[nsurf]["with_holes"] = False

            # comp. number of elements on the lines & override by user values in case
            mesh_dict = surf.comp_mesh_dict(element_size=mesh_size_S)
            if user_mesh_dict:  # check if dict is not None nor empty
                mesh_dict.update(user_mesh_dict)

            # add all lines of the current surface to the gmsh_dict
            for line in surf.get_lines():
                n_elem = mesh_dict.get(line.label)
                n_elem = n_elem if n_elem is not None else 0
                bc_name = get_boundary_condition(line, boundary_prop)

                # Gmsh built-in engine does not allow arcs larger than 180deg
                # so arcs are split into two
                if (
                    isinstance(line, Arc)
                    and abs(line.get_angle() * 180.0 / cmath.pi) >= 180.0
                ):
                    rot_dir = 1 if line.is_trigo_direction == True else -1
                    arc1 = Arc2(
                        begin=line.get_begin(),
                        center=line.get_center(),
                        angle=rot_dir * cmath.pi / 2.0,
                        label=line.label,
                    )
                    arc2 = Arc2(
                        begin=arc1.get_end(),
                        center=line.get_center(),
                        angle=rot_dir * cmath.pi / 2.0,
                        label=line.label,
                    )
                    for arc in [arc1, arc2]:
                        _add_line_to_dict(
                            geo=factory,
                            line=arc,
                            d=gmsh_dict,
                            idx=nsurf,
                            mesh_size=mesh_size_S,
                            n_elements=n_elem,
                            bc=bc_name,
                        )
                else:
                    _add_line_to_dict(
                        geo=factory,
                        line=line,
                        d=gmsh_dict,
                        idx=nsurf,
                        mesh_size=mesh_size_S,
                        n_elements=n_elem,
                        bc=bc_name,
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
            if (s_data["label"].find("STATOR_LAM") != -1) or (not is_lam_only_S):
                s_data["tag"] = factory.addPlaneSurface([cloop], tag=-1)
                pg = model.addPhysicalGroup(2, [s_data["tag"]])
                model.setPhysicalName(2, pg, s_data["label"])

        # stator_dict = gmsh_dict.copy()

    gmsh_dict.update(rotor_dict)

    if is_sliding_band and (not is_lam_only_R) and (not is_lam_only_S):
        sb_list = get_sliding_band(sym=sym, machine=machine)
    else:
        sb_list = []

    # Default sliding mesh element size
    mesh_size = 2.0 * cmath.pi * machine.rotor.Rext / 360.0
    # nsurf = 0
    for surf in sb_list:
        nsurf += 1
        gmsh_dict.update(
            {
                nsurf: {
                    "tag": None,
                    "label": surface_label.get(surf.label, "UNKNOWN"),
                }
            }
        )
        for line in surf.get_lines():
            n_elem = mesh_dict.get(line.label)
            n_elem = n_elem if n_elem is not None else 0
            bc_name = get_boundary_condition(line, boundary_prop)
            # Gmsh built-in engine does not allow arcs larger than 180deg
            # so arcs are split into two
            if (
                isinstance(line, Arc)
                and abs(line.get_angle() * 180.0 / cmath.pi) >= 180.0
            ):
                rot_dir = 1 if line.is_trigo_direction == True else -1
                arc1 = Arc2(
                    begin=line.get_begin(),
                    center=line.get_center(),
                    angle=rot_dir * cmath.pi / 2.0,
                    label=line.label,
                )
                arc2 = Arc2(
                    begin=arc1.get_end(),
                    center=line.get_center(),
                    angle=rot_dir * cmath.pi / 2.0,
                    label=line.label,
                )
                for arc in [arc1, arc2]:
                    _add_agline_to_dict(
                        geo=factory,
                        line=arc,
                        d=gmsh_dict,
                        idx=nsurf,
                        mesh_size=mesh_size,
                        n_elements=n_elem,
                        bc=bc_name,
                    )
            else:
                _add_agline_to_dict(
                    geo=factory,
                    line=line,
                    d=gmsh_dict,
                    idx=nsurf,
                    mesh_size=mesh_size,
                    n_elements=n_elem,
                    bc=bc_name,
                )

    for s_data in gmsh_dict.values():
        lloop = []
        # skip this surface dataset if it is the origin
        if s_data["label"] == "origin" or not (
            "AG_" in s_data["label"] or "SB_" in s_data["label"]
        ):
            continue

        # build a lineloop of the surfaces lines
        for lvalues in s_data.values():
            if type(lvalues) is not dict:
                continue
            lloop.extend([lvalues["tag"]])

        if lloop:
            cloop = factory.addCurveLoop(lloop)
            if "AG_INT" in s_data["label"] and isinstance(machine, MachineSIPMSM):
                s_data["tag"] = factory.addPlaneSurface([cloop] + rotor_cloops, tag=-1)
            else:
                s_data["tag"] = factory.addPlaneSurface([cloop], tag=-1)
            pg = model.addPhysicalGroup(2, [s_data["tag"]])
            model.setPhysicalName(2, pg, s_data["label"])

    if is_airbox and (not is_lam_only_R) and (not is_lam_only_S):
        ab_list = get_air_box(sym=sym, machine=machine)
    else:
        ab_list = []

    # Default airbox mesh element size
    mesh_size = machine.stator.Rext / 50.0
    for surf in ab_list:
        nsurf += 1
        gmsh_dict.update(
            {
                nsurf: {
                    "tag": None,
                    "label": surface_label.get(surf.label, "UNKNOWN"),
                }
            }
        )
        for line in surf.get_lines():
            n_elem = mesh_dict.get(line.label)
            n_elem = n_elem if n_elem is not None else 0
            bc_name = get_boundary_condition(line, boundary_prop)

            # Gmsh built-in engine does not allow arcs larger than 180deg
            # so arcs are split into two
            if (
                isinstance(line, Arc)
                and abs(line.get_angle() * 180.0 / cmath.pi) >= 180.0
            ):

                rot_dir = 1 if line.get_angle() > 0 else -1
                arc1 = Arc2(
                    begin=line.get_begin(),
                    center=line.get_center(),
                    angle=rot_dir * cmath.pi / 2.0,
                    label=line.label,
                )
                arc2 = Arc2(
                    begin=arc1.get_end(),
                    center=line.get_center(),
                    angle=rot_dir * cmath.pi / 2.0,
                    label=line.label,
                )
                for arc in [arc1, arc2]:
                    _add_line_to_dict(
                        geo=factory,
                        line=arc,
                        d=gmsh_dict,
                        idx=nsurf,
                        mesh_size=mesh_size,
                        n_elements=n_elem,
                        bc=bc_name,
                    )
            else:
                _add_line_to_dict(
                    geo=factory,
                    line=line,
                    d=gmsh_dict,
                    idx=nsurf,
                    mesh_size=mesh_size,
                    n_elements=n_elem,
                    bc=bc_name,
                )

    for s_id, s_data in gmsh_dict.items():
        lloop = []
        if s_id == 0:
            continue
        for lvalues in s_data.values():
            if s_data["label"].find("AIRBOX") != -1:
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

    #gmsh.fltk.run()      # Uncomment to launch Gmsh GUI
    gmsh.finalize()
    return gmsh_dict

from ...Classes.Arc import Arc
from ...Classes.Arc2 import Arc2
from ...Classes.MachineSIPMSM import MachineSIPMSM

import sys
import gmsh
import cmath


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
    for s_id, s_data in d.items():
        for lid, lvalues in s_data.items():
            if type(lvalues) is not dict:
                continue
            for pid, pvalues in lvalues.items():
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
    for s_id, s_data in d.items():
        for lid, lvalues in s_data.items():
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
    for s_id, s_data in d.items():
        for lid, lvalues in s_data.items():
            if type(lvalues) is not dict:
                continue
            for pid, pvalues in lvalues.items():
                if type(pvalues) is not dict:
                    continue
                if pvalues["tag"] == ptag:
                    lines.append(lvalues["tag"])
    return lines


def _add_line_to_dict(geo, line, d={}, idx=0, mesh_size=1e-2, n_elements=0):
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
        for lid, lvalues in d[idx].items():
            if type(lvalues) is not dict:
                continue
            else:
                if lvalues["tag"] == ltag:
                    repeated = True

        if not repeated:
            nline = len(d[idx]) - 2
            d[idx].update(
                {
                    nline: {
                        "tag": ltag,
                        "n_elements": n_elements,
                        "begin": {"tag": btag, "coord": complex(bx, by)},
                        "end": {"tag": etag, "coord": complex(ex, ey)},
                        "cent": {"tag": ctag, "coord": complex(cx, cy)},
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
        for lid, lvalues in d[idx].items():
            if type(lvalues) is not dict:
                continue
            else:
                if lvalues["tag"] == ltag:
                    repeated = True

        if not repeated:
            nline = len(d[idx]) - 2
            d[idx].update(
                {
                    nline: {
                        "tag": ltag,
                        "n_elements": n_elements,
                        "begin": {"tag": btag, "coord": complex(bx, by)},
                        "end": {"tag": etag, "coord": complex(ex, ey)},
                    }
                }
            )

    return None


def draw_GMSH(
    output,
    sym,
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
    is_sliding_band=True,
    transform_list=[],
):
    """Draws a machine mesh in GMSH format

    Parameters
    ----------
    output : Output
        Output object
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
    sym : int
        the symmetry applied on the stator and the rotor (take into account antiperiodicity)
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

    machine = output.simu.machine
    mesh_dict = {}
    tol = 1e-6
    # For readibility
    model = gmsh.model
    factory = model.geo

    # Start a new model
    gmsh.initialize(sys.argv)
    gmsh.option.setNumber("General.Terminal", int(True))
    gmsh.option.setNumber("Geometry.CopyMeshingMethod", 1)
    gmsh.option.setNumber("Geometry.PointNumbers", 0)
    gmsh.option.setNumber("Geometry.LineNumbers", 0)
    model.add("Pyleecan")

    rotor_list = list()
    rotor_list.extend(machine.shaft.build_geometry(sym=sym))
    rotor_list.extend(machine.rotor.build_geometry(sym=sym))
    stator_list = list()
    stator_list.extend(machine.stator.build_geometry(sym=sym))
    oo = factory.addPoint(0, 0, 0, 0, tag=-1)

    gmsh_dict = {
        0: {
            "tag": 0,
            "label": "origin",
            "with_holes": False,
            1: {
                "tag": 0,
                "n_elements": 1,
                "begin": {"tag": oo, "coord": complex(0.0, 0.0)},
                "end": {"tag": None, "coord": None},
                "cent": {"tag": None, "coord": None},
            },
        }
    }

    # Default rotor mesh element size
    mesh_size = machine.rotor.Rext / 25.0
    nsurf = 0
    for surf in rotor_list:
        nsurf += 1
        gmsh_dict.update({nsurf: {"tag": None, "label": surf.label}})
        if surf.label.find("Lamination_Rotor") != -1:
            gmsh_dict[nsurf]["with_holes"] = True
            lam_rotor_surf_id = nsurf
        else:
            gmsh_dict[nsurf]["with_holes"] = False
        if user_mesh_dict is not None:
            mesh_dict = surf.comp_mesh_dict(element_size=mesh_size)
            mesh_dict.update(user_mesh_dict)
        for line in surf.get_lines():
            # When symmetry is 1 the shaft surface is substrtacted from Rotor Lam instead
            if sym == 1 and line.label == "Lamination_Rotor_Yoke_Radius_Int":
                continue
            n_elem = mesh_dict.get(line.label)
            if (
                isinstance(line, Arc)
                and abs(line.get_angle() * 180.0 / cmath.pi) >= 180.0
            ):
                if line.is_trigo_direction == True:
                    arc1 = Arc2(
                        begin=line.get_begin(),
                        center=line.get_center(),
                        angle=cmath.pi / 2.0,
                        label=line.label,
                    )
                    arc2 = Arc2(
                        begin=arc1.get_end(),
                        center=line.get_center(),
                        angle=cmath.pi / 2.0,
                        label=line.label,
                    )
                else:
                    arc1 = Arc2(
                        begin=line.get_begin(),
                        center=line.get_center(),
                        angle=-cmath.pi / 2.0,
                        label=line.label,
                    )
                    arc2 = Arc2(
                        begin=arc1.get_end(),
                        center=line.get_center(),
                        angle=-cmath.pi / 2.0,
                        label=line.label,
                    )
                if n_elem is not None:
                    _add_line_to_dict(
                        geo=factory,
                        line=arc1,
                        d=gmsh_dict,
                        idx=nsurf,
                        n_elements=n_elem,
                    )
                    _add_line_to_dict(
                        geo=factory,
                        line=arc2,
                        d=gmsh_dict,
                        idx=nsurf,
                        n_elements=n_elem,
                    )
                else:
                    _add_line_to_dict(
                        geo=factory,
                        line=arc1,
                        d=gmsh_dict,
                        idx=nsurf,
                        mesh_size=mesh_size,
                    )
                    _add_line_to_dict(
                        geo=factory,
                        line=arc2,
                        d=gmsh_dict,
                        idx=nsurf,
                        mesh_size=mesh_size,
                    )
            elif isinstance(line, Arc) and (
                abs(line.get_angle() * 180.0 / cmath.pi) <= tol
            ):
                # Don't draw anything, this is a circle and usually is repeated ?
                pass
            else:
                if n_elem is not None:
                    _add_line_to_dict(
                        geo=factory,
                        line=line,
                        d=gmsh_dict,
                        idx=nsurf,
                        n_elements=n_elem,
                    )
                else:
                    _add_line_to_dict(
                        geo=factory,
                        line=line,
                        d=gmsh_dict,
                        idx=nsurf,
                        mesh_size=mesh_size,
                    )

    lam_and_holes = list()
    ext_lam_loop = None
    for s_id, s_data in gmsh_dict.items():
        lloop = []
        if s_id == 0:
            continue
        for lid, lvalues in s_data.items():
            if type(lvalues) is not dict:
                continue
            lloop.extend([lvalues["tag"]])
        cloop = factory.addCurveLoop(lloop)
        # search for the holes to substract from rotor lam
        if s_data["label"].find("Lamination_Rotor") != -1:
            ext_lam_loop = cloop
        else:
            # MachineSIPSM does not have holes in rotor lam
            # only shaft is taken out if symmetry is one
            if isinstance(machine, MachineSIPMSM):
                if sym == 1 and s_data["label"] == "Shaft":
                    lam_and_holes.extend([cloop])
            else:
                if sym == 1:
                    lam_and_holes.extend([cloop])
                elif s_data["label"] != "Shaft":
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
    gmsh_dict[lam_rotor_surf_id]["tag"] = factory.addPlaneSurface(lam_and_holes, tag=-1)
    pg = model.addPhysicalGroup(2, [gmsh_dict[lam_rotor_surf_id]["tag"]])
    model.setPhysicalName(2, pg, gmsh_dict[lam_rotor_surf_id]["label"])

    # Default rotor mesh element size
    mesh_size = machine.stator.Rext / 100.0
    nsurf = 0
    for surf in stator_list:
        nsurf += 1
        gmsh_dict.update({nsurf: {"tag": None, "label": surf.label}})
        if surf.label.find("Lamination_Stator") != -1:
            gmsh_dict[nsurf]["with_holes"] = True
        else:
            gmsh_dict[nsurf]["with_holes"] = False
        if user_mesh_dict is not None:
            mesh_dict = surf.comp_mesh_dict(element_size=mesh_size)
            mesh_dict.update(user_mesh_dict)
        for line in surf.get_lines():
            n_elem = mesh_dict.get(line.label)
            # Gmsh built-in engine does not allow arcs larger than 180deg
            # so arcs are split into two
            if (
                isinstance(line, Arc)
                and abs(line.get_angle() * 180.0 / cmath.pi) == 180.0
            ):
                if line.is_trigo_direction == True:
                    arc1 = Arc2(
                        begin=line.get_begin(),
                        center=line.get_center(),
                        angle=cmath.pi / 2.0,
                        label=line.label,
                    )
                    arc2 = Arc2(
                        begin=arc1.get_end(),
                        center=line.get_center(),
                        angle=cmath.pi / 2.0,
                        label=line.label,
                    )
                else:
                    arc1 = Arc2(
                        begin=line.get_begin(),
                        center=line.get_center(),
                        angle=-cmath.pi / 2.0,
                        label=line.label,
                    )
                    arc2 = Arc2(
                        begin=arc1.get_end(),
                        center=line.get_center(),
                        angle=-cmath.pi / 2.0,
                        label=line.label,
                    )
                if n_elem is not None:
                    _add_line_to_dict(
                        geo=factory,
                        line=arc1,
                        d=gmsh_dict,
                        idx=nsurf,
                        n_elements=n_elem,
                    )
                    _add_line_to_dict(
                        geo=factory,
                        line=arc2,
                        d=gmsh_dict,
                        idx=nsurf,
                        n_elements=n_elem,
                    )
                else:
                    _add_line_to_dict(
                        geo=factory,
                        line=arc1,
                        d=gmsh_dict,
                        idx=nsurf,
                        mesh_size=mesh_size,
                    )
                    _add_line_to_dict(
                        geo=factory,
                        line=arc2,
                        d=gmsh_dict,
                        idx=nsurf,
                        mesh_size=mesh_size,
                    )
            else:
                if n_elem is not None:
                    _add_line_to_dict(
                        geo=factory,
                        line=line,
                        d=gmsh_dict,
                        idx=nsurf,
                        n_elements=n_elem,
                    )
                else:
                    _add_line_to_dict(
                        geo=factory,
                        line=line,
                        d=gmsh_dict,
                        idx=nsurf,
                        mesh_size=mesh_size,
                    )

    for s_id, s_data in gmsh_dict.items():
        lloop = []
        if s_id == 0:
            continue
        for lid, lvalues in s_data.items():
            if type(lvalues) is not dict:
                continue
            lloop.extend([lvalues["tag"]])
        cloop = factory.addCurveLoop(lloop)
        # Winding surfaces are created
        if s_data["label"].find("Lamination_Stator") != -1:
            s_data["tag"] = factory.addPlaneSurface([cloop], tag=-1)
            pg = model.addPhysicalGroup(2, [s_data["tag"]])
            model.setPhysicalName(2, pg, s_data["label"])
        else:
            # Stator lamination is built
            if not is_lam_only_S:
                s_data["tag"] = factory.addPlaneSurface([cloop], tag=-1)
                pg = model.addPhysicalGroup(2, [s_data["tag"]])
                model.setPhysicalName(2, pg, s_data["label"])

    factory.synchronize()
    gmsh.model.mesh.generate(2)

    # Save and close
    gmsh.write(path_save)
    # gmsh.fltk.run()      # Uncomment to launch Gmsh GUI
    gmsh.finalize()

    return gmsh_dict

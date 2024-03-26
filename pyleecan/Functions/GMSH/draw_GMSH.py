from ...Classes.Arc import Arc
from ...Classes.Arc2 import Arc2
from ...Classes.MachineSIPMSM import MachineSIPMSM
from ...Classes.MachineSCIM import MachineSCIM
from ...Classes.MachineWRSM import MachineWRSM

from ...Functions.labels import (
    HOLEM_LAB_S,
    MAG_LAB,
    BAR_LAB,
    short_label,
    LAM_LAB,
    YOKE_LAB,
    WIND_LAB_S,
    LAM_LAB_S,
    SHAFT_LAB,
    decode_label,
    SLID_LAB,
    AIRGAP_LAB,
    BOT_LAB,
    TOP_LAB,
    AIRBOX_LAB,
    AIRBOX_R_LAB,
    AR_B_LAB,
    AR_T_LAB,
    SBR_B_LAB,
    SBR_T_LAB,
    AS_BL_LAB,
    AS_BR_LAB,
    AS_TL_LAB,
    AS_TR_LAB
)
from ...Functions.GMSH import InputError
from ...Functions.GMSH.get_sliding_band import get_sliding_band
from ...Functions.GMSH.get_air_box import get_air_box
from ...Functions.GMSH.get_boundary_condition import get_boundary_condition
from ...Functions.GMSH.draw_surf_line import draw_surf_line
from ...Functions.GMSH.comp_gmsh_mesh_dict import comp_gmsh_mesh_dict
import sys
import gmsh
import cmath

from os import replace
from os.path import splitext

from numpy import pi

from ...Functions.get_logger import get_logger
def draw_GMSH(
    output,
    sym,
    boundary_prop,
    is_lam_only_S=False,
    is_lam_only_R=False,
    user_mesh_dict={},
    path_save="GMSH_model.msh",
    is_sliding_band=False,
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
        True uses sliding band, else airgap 
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
    lam_list = machine.get_lam_list()
    lam_int = lam_list[0]
    lam_ext = lam_list[1]
    lab_int = lam_int.get_label()
    lab_ext = lam_ext.get_label()

    # For readibility
    model = gmsh.model
    factory = model.occ

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
                "label": None,
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
            mesh_dict = comp_gmsh_mesh_dict(surface=surf, element_size=mesh_size_R, user_mesh_dict=user_mesh_dict)

            # Draw the surface
            draw_surf_line(
                surf,
                mesh_dict,
                boundary_prop,
                model,
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
                or BAR_LAB in label_dict["surf_type"]
            ):
                # Surface of Hole Magnet
                rotor_cloops.extend([cloop])

            # search for the holes to substract from rotor lam
            if LAM_LAB_S in label_dict["surf_type"]:
                ext_lam_loop = cloop
            else:
                # MachineSIPSM does not have holes in rotor lam
                # only shaft is taken out if symmetry is one
                if ( 
                    isinstance(machine, MachineSIPMSM) 
                    or isinstance(machine, MachineSCIM)
                    or isinstance(machine, MachineWRSM)
                ):
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
                    factory.synchronize()
                    pg = model.addPhysicalGroup(2, [s_data["tag"]])
                    model.setPhysicalName(2, pg, s_data["label"])

        # Finally rotor lamination is built
        if ext_lam_loop is not None:
            lam_and_holes.insert(0, ext_lam_loop)
        if len(lam_and_holes) > 0:
            gmsh_dict[lam_rotor_surf_id]["tag"] = factory.addPlaneSurface(
                lam_and_holes, tag=-1
            )
        factory.synchronize()
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
                "label": None,
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
            mesh_dict = comp_gmsh_mesh_dict(surface=surf, element_size=mesh_size_S, user_mesh_dict=user_mesh_dict)

            # Draw the surface
            draw_surf_line(
                surf,
                mesh_dict,
                boundary_prop,
                model,
                gmsh_dict,
                nsurf,
                mesh_size_S,
            )

        for s_data in gmsh_dict.values():
            lloop = []
            # skip this surface dataset if it is the origin
            if s_data["label"] == "origin":
                continue

            if sym == 1:
                inner_loop = []
                # build a lineloop of the surfaces lines independently for yoke
                # and bore is considered a hole
                for lvalues in s_data.values():
                    if type(lvalues) is not dict:
                        continue
                    
                    if WIND_LAB_S in s_data["label"]:
                        lloop.extend([lvalues["tag"]])
                        inner_loop.extend([lvalues["tag"]])
                    elif(
                        lvalues["label"] is not None
                        and LAM_LAB in lvalues["label"]
                        and YOKE_LAB in lvalues["label"]
                    ):
                        lloop.extend([lvalues["tag"]])
                    else:
                        inner_loop.extend([lvalues["tag"]])    
                #print(s_data["label"],lloop,inner_loop)
                cloop = factory.addCurveLoop(lloop)
                #stator_cloops.append(cloop)

                
                if LAM_LAB_S in decode_label(s_data["label"])["surf_type"] or (
                    not is_lam_only_S
                ):
                    # Winding surfaces are created
                    if WIND_LAB_S in s_data["label"]:
                        s_data["tag"] = factory.addPlaneSurface([cloop], tag=-1)
                        factory.synchronize()
                        pg = model.addPhysicalGroup(2, [s_data["tag"]])
                        model.setPhysicalName(2, pg, s_data["label"])
                    # Lamination surfaces are created
                    else:
                        inner_cloop = factory.addCurveLoop(inner_loop)
                        s_data["tag"] = factory.addPlaneSurface([cloop, inner_cloop], tag=-1)
                        factory.synchronize()
                        pg = model.addPhysicalGroup(2, [s_data["tag"]])
                        model.setPhysicalName(2, pg, s_data["label"])
            else:
                for lvalues in s_data.values():
                    if type(lvalues) is not dict:
                        continue
                    lloop.extend([lvalues["tag"]])
                cloop = factory.addCurveLoop(lloop)
                #stator_cloops.append(cloop)

                # All surfaces are created
                if LAM_LAB_S in decode_label(s_data["label"])["surf_type"] or (
                    not is_lam_only_S
                ):
                    s_data["tag"] = factory.addPlaneSurface([cloop], tag=-1)
                    factory.synchronize()
                    pg = model.addPhysicalGroup(2, [s_data["tag"]])
                    model.setPhysicalName(2, pg, s_data["label"])
            

    stator_dict = gmsh_dict.copy()
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
        mesh_dict = comp_gmsh_mesh_dict(surface=surf, element_size=mesh_size_SB, user_mesh_dict=user_mesh_dict)

        # Draw the surface
        draw_surf_line(
            surf,
            mesh_dict,
            boundary_prop,
            model,
            gmsh_dict,
            nsurf,
            mesh_size_SB,
        )

    if is_sliding_band and (not is_lam_only_R) and (not is_lam_only_S):
        if sym == 1:
            lloop1 = []
            lloop2 = []
            lloop3 = []
            lloop4 = []
            lloop5 = []
            for s_data in gmsh_dict.values():            
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
                    
                    if (
                        AIRGAP_LAB in label_dict["surf_type"]
                        and BOT_LAB in label_dict["surf_type"]
                        and AR_B_LAB in lvalues["label"]
                    ):
                        lloop1.extend([lvalues["tag"]])                 
                    elif (
                        SLID_LAB in label_dict["surf_type"]
                        and BOT_LAB in label_dict["surf_type"]
                        and SBR_B_LAB in lvalues["label"]
                    ):
                        lloop2.extend([lvalues["tag"]])  
                    elif (
                        SLID_LAB in label_dict["surf_type"]
                        and TOP_LAB in label_dict["surf_type"]
                        and SBR_T_LAB in lvalues["label"]
                    ):
                        lloop3.extend([lvalues["tag"]])  
                    elif (
                        AIRGAP_LAB in label_dict["surf_type"]
                        and TOP_LAB in label_dict["surf_type"]
                        and AR_T_LAB in lvalues["label"]
                    ):
                        lloop4.extend([lvalues["tag"]])  
                    elif (
                        AIRGAP_LAB in label_dict["surf_type"]
                        and TOP_LAB in label_dict["surf_type"]
                        and AIRBOX_R_LAB in lvalues["label"]
                    ):
                        lloop5.extend([lvalues["tag"]])
                    else:    
                        pass
                
            cloop1 = factory.addCurveLoop(lloop1)
            cloop2 = factory.addCurveLoop(lloop2)
            cloop3 = factory.addCurveLoop(lloop3)
            cloop4 = factory.addCurveLoop(lloop4)
            cloop5 = factory.addCurveLoop(lloop5)
            
            for s_data in gmsh_dict.values():
                label_dict = decode_label(s_data["label"])

                # skip this surface dataset if it is the origin
                if s_data["label"] == "origin" or not (
                    AIRGAP_LAB in label_dict["surf_type"] or SLID_LAB in label_dict["surf_type"]
                ):
                    continue

                if (
                    AIRGAP_LAB in label_dict["surf_type"]
                    and BOT_LAB in label_dict["surf_type"]
                ):
                    s_data["tag"] = factory.addPlaneSurface([cloop1], tag=-1)
                    factory.synchronize()
                    rotor_ag_before = (2,s_data["tag"])
                elif (
                    SLID_LAB in label_dict["surf_type"]
                    and BOT_LAB in label_dict["surf_type"]
                ):
                    s_data["tag"] = factory.addPlaneSurface([cloop2, cloop1], tag=-1)
                    factory.synchronize()
                    pg = model.addPhysicalGroup(2, [s_data["tag"]])
                    model.setPhysicalName(2, pg, s_data["label"])                
                elif (
                    SLID_LAB in label_dict["surf_type"]
                    and TOP_LAB in label_dict["surf_type"]
                ):
                    s_data["tag"] = factory.addPlaneSurface([cloop4, cloop3], tag=-1)
                    factory.synchronize()
                    pg = model.addPhysicalGroup(2, [s_data["tag"]])
                    model.setPhysicalName(2, pg, s_data["label"])
                elif (
                    AIRGAP_LAB in label_dict["surf_type"]
                    and TOP_LAB in label_dict["surf_type"]
                ):
                    s_data["tag"] = factory.addPlaneSurface([cloop5, cloop4], tag=-1)
                    #s_data["tag"] = factory.addPlaneSurface([cloop5], tag=-1)
                    factory.synchronize()
                    stator_ag_before = (2,s_data["tag"])
                else:
                    continue
                

            if is_sliding_band and (not is_lam_only_R) and (not is_lam_only_S):    
                rotor_surf_gmsh_list = []
                for tid in rotor_dict:
                    # Discard Origin
                    if tid == 0:    
                        continue
                    rotor_surf_gmsh_list.append((2, tid))

                stator_surf_gmsh_list = []
                for tid in stator_dict:
                    # Discard Origin
                    if tid == 0:    
                        continue
                    stator_surf_gmsh_list.append((2, tid))
                
                cut1 = model.occ.cut([rotor_ag_before], rotor_surf_gmsh_list, removeObject=True, removeTool=False)
                
                # All These because CUT alone is not working for the stator
                stat_copy = model.occ.copy(stator_surf_gmsh_list)
                ints1 = model.occ.intersect([stator_ag_before],[stat_copy[0]],removeObject=True,removeTool=True,tag=-1)
                stat_copy.pop(0)
                cut2 = model.occ.cut(ints1[0],stat_copy,removeObject=True,removeTool=True,tag=-1)

                if len(cut1[0]) > 1:
                    # Remove extra surfaces
                    model.occ.remove([cut1[0][1]])
                    factory.synchronize() 
                    pg = model.addPhysicalGroup(2, [cut1[0][0][1]])
                    model.setPhysicalName(2, pg, lab_int + "_" + AIRGAP_LAB + BOT_LAB)   
                else:
                    factory.synchronize()
                    pg = model.addPhysicalGroup(2, [cut1[0][0][1]])
                    model.setPhysicalName(2, pg, lab_int + "_" + AIRGAP_LAB + BOT_LAB)  

                if len(cut2[0]) > 1:
                    # Remove extra surfaces
                    model.occ.remove([cut2[0][0]])
                    factory.synchronize()
                    pg = model.addPhysicalGroup(2, [cut2[0][1][1]])
                    model.setPhysicalName(2, pg, lab_ext + "_" + AIRGAP_LAB + TOP_LAB)   
                else:
                    factory.synchronize()
                    pg = model.addPhysicalGroup(2, [cut2[0][0][1]])
                    model.setPhysicalName(2, pg, lab_ext + "_" + AIRGAP_LAB + TOP_LAB)  
                
        else:
            for s_key, s_data in gmsh_dict.items():
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
                    factory.synchronize()
                    pg = model.addPhysicalGroup(2, [s_data["tag"]])
                    model.setPhysicalName(2, pg, s_data["label"])          
                    if (AIRGAP_LAB in s_data["label"] and BOT_LAB in s_data["label"]):
                        rotor_ag_before = (2,s_data["tag"])
                        rotor_ag_key_before = s_key
                    if (AIRGAP_LAB in s_data["label"] and TOP_LAB in s_data["label"]):
                        stator_ag_before = (2,s_data["tag"])
                        stator_ag_key_before = s_key
                

            if is_sliding_band and (not is_lam_only_R) and (not is_lam_only_S):    
                rotor_surf_gmsh_list = []
                for tid in rotor_dict:
                    # Discard Origin
                    if tid == 0:    
                        continue
                    rotor_surf_gmsh_list.append((2, tid))

                stator_surf_gmsh_list = []
                for tid in stator_dict:
                    # Discard Origin
                    if tid == 0:    
                        continue
                    stator_surf_gmsh_list.append((2, tid))

                cut1 = model.occ.cut([rotor_ag_before], rotor_surf_gmsh_list, removeObject=True, removeTool=False)
                cut2 = model.occ.cut([stator_ag_before], stator_surf_gmsh_list, removeObject=True, removeTool=False)

                if len(cut1[0]) > 1:
                    # Remove extra surfaces
                    model.occ.remove([cut1[0][0]])
                    factory.synchronize()                 
                    pg = model.addPhysicalGroup(2, [cut1[0][1][1]])
                    model.setPhysicalName(2, pg, lab_int + "_" + AIRGAP_LAB + BOT_LAB)   
                else:
                    factory.synchronize()
                    pg = model.addPhysicalGroup(2, [cut1[0][0][1]])
                    model.setPhysicalName(2, pg, lab_int + "_" + AIRGAP_LAB + BOT_LAB)  

                # Look at the lines in the resulting surface, then update the dictionary
                # with MASTER/SLAVE BC when line angles match symmetry angles
                # MASTER is x-axis and SLAVE is 2Pi/sym
                rotor_ag_after = model.getEntitiesForPhysicalGroup(2, pg)
                rotor_ag_new_lines = model.getBoundary([(2,rotor_ag_after)])
                nline = 0
                for type_entity_l, rotor_ag_line in rotor_ag_new_lines:
                    rotor_ag_new_points = model.getBoundary([(type_entity_l, abs(rotor_ag_line))])
                    btag = rotor_ag_new_points[0][1]
                    etag = rotor_ag_new_points[1][1]
                    bxy = model.getValue(0, btag, [])
                    exy = model.getValue(0, etag, [])
                    exy_angle = cmath.phase(complex(exy[0], exy[1])) 
                    bxy_angle = cmath.phase(complex(bxy[0], bxy[1]))
                    if exy_angle == bxy_angle and abs(exy_angle) < 1e-6:
                        b_name = boundary_prop[AS_BR_LAB]
                        l_name = AS_BR_LAB
                    elif (exy_angle == bxy_angle) and (abs(abs(exy_angle) - 2.0*pi/sym) < 1e-6):
                        b_name = boundary_prop[AS_BL_LAB]
                        l_name = AS_BL_LAB
                    else:
                        b_name = None
                        l_name = None
                    gmsh_dict[rotor_ag_before[1]].update(
                        {
                            "tag" : rotor_ag_after[0],
                            "label" : lab_int + "_" + AIRGAP_LAB + BOT_LAB,
                            nline : {
                                "tag": abs(rotor_ag_line),
                                "label": l_name,
                                "n_elements": None,
                                "bc_name": b_name,
                                "begin": {"tag": btag, "coord": complex(bxy[0], bxy[1])},
                                "end": {"tag": etag, "coord": complex(exy[0], exy[1])},
                                "arc_angle": None,
                                "line_angle": None,
                            }
                        }                            
                    )
                    nline = nline + 1
                        

                if len(cut2[0]) > 1:
                    # Remove extra surfaces
                    model.occ.remove([cut2[0][0]])
                    factory.synchronize()
                    pg = model.addPhysicalGroup(2, [cut2[0][1][1]])
                    model.setPhysicalName(2, pg, lab_ext + "_" + AIRGAP_LAB + TOP_LAB)   
                else:
                    factory.synchronize()
                    pg = model.addPhysicalGroup(2, [cut2[0][0][1]])
                    model.setPhysicalName(2, pg, lab_ext + "_" + AIRGAP_LAB + TOP_LAB)  
                
                # Look at the lines in the resulting surface, then update the dictionary
                # with MASTER/SLAVE BC when line angles match symmetry angles
                # MASTER is x-axis and SLAVE is 2Pi/sym
                stator_ag_after = model.getEntitiesForPhysicalGroup(2, pg)
                stator_ag_new_lines = model.getBoundary([(2,stator_ag_after)])
                nline = 0
                for type_entity_l, stator_ag_line in stator_ag_new_lines:
                    stator_ag_new_points = model.getBoundary([(type_entity_l, abs(stator_ag_line))])
                    btag = stator_ag_new_points[0][1]
                    etag = stator_ag_new_points[1][1]
                    bxy = model.getValue(0, btag, [])
                    exy = model.getValue(0, etag, [])
                    exy_angle = cmath.phase(complex(exy[0], exy[1])) 
                    bxy_angle = cmath.phase(complex(bxy[0], bxy[1]))
                    if exy_angle == bxy_angle and abs(exy_angle) < 1e-6:
                        b_name = boundary_prop[AS_TR_LAB]
                        l_name = AS_TR_LAB
                    elif (exy_angle == bxy_angle) and (abs(abs(exy_angle) - 2.0*pi/sym) < 1e-6):
                        b_name = boundary_prop[AS_TL_LAB]
                        l_name = AS_TL_LAB
                    else:
                        b_name = None
                        l_name = None
                    gmsh_dict[stator_ag_before[1]].update(
                        {
                            "tag" : stator_ag_after[0],
                            "label" : lab_ext + "_" + AIRGAP_LAB + TOP_LAB,
                            nline : {
                                "tag": abs(stator_ag_line),
                                "label": l_name,
                                "n_elements": None,
                                "bc_name": b_name,
                                "begin": {"tag": btag, "coord": complex(bxy[0], bxy[1])},
                                "end": {"tag": etag, "coord": complex(exy[0], exy[1])},
                                "arc_angle": None,
                                "line_angle": None,
                            }
                        }                            
                    )
                    nline = nline + 1             

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
        mesh_dict = comp_gmsh_mesh_dict(surface=surf, element_size=mesh_size_AB, user_mesh_dict=user_mesh_dict)

        # Draw the surface
        draw_surf_line(
            surf,
            mesh_dict,
            boundary_prop,
            model,
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
            factory.synchronize()
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
            factory.synchronize()
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
            factory.synchronize()
            pg = model.addPhysicalGroup(1, tags)
            model.setPhysicalName(1, pg, label)


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

# -*- coding: utf-8 -*-
import gmsh
import sys

from os import replace
from os.path import splitext


def _remove_entities(gmsh, labels):
    """
    Remove model entities that have one of the given labels in their physical
    groups names.

    Parameters
    ----------

    gmsh :
        gmsh object

    labels : list
        list of labels

    """
    # TODO add test that entities are not in surf or part of other 'keeper'entities
    # get all group names
    grps = gmsh.model.getPhysicalGroups(-1)
    grp_names = [gmsh.model.getPhysicalName(*grp) for grp in grps]

    # get entities that will be removed
    pt_list = []
    line_list = []
    surf_list = []
    for grp, name in zip(grps, grp_names):
        if any([label in name.lower() for label in labels]):
            dim = grp[0]
            entities = gmsh.model.getEntitiesForPhysicalGroup(dim, grp[1])
            if dim == 0:
                pt_list.extend(entities.tolist())
            elif dim == 1:
                line_list.extend(entities.tolist())
            elif dim == 2:
                surf_list.extend(entities.tolist())

    # get lines of surfaces
    for surf in surf_list:
        lines = gmsh.model.getBoundary([(2, surf)])  # TODO check if holes are included
        for line in lines:
            line_list.append(line[1])

    # get points of lines
    for line in line_list:
        pts = gmsh.model.getBoundary([(1, line)])
        for pt in pts:
            pt_list.append(pt[1])

    # get unique list of entities to remove
    line_list = list(set(line_list))
    pt_list = list(set(pt_list))

    # delete unused entities
    for surf in surf_list:
        # gmsh.model.removeEntities((2, surf), recursive=False)
        gmsh.model.geo.remove([(2, surf)], recursive=False)

    for line in line_list:
        # gmsh.model.removeEntities((1, line), recursive=False)
        gmsh.model.geo.remove([(1, line)], recursive=False)

    for pt in pt_list:
        # gmsh.model.removeEntities((0, pt), recursive=False)
        gmsh.model.geo.remove([(0, pt)], recursive=False)

    # synchronize to apply changes to model
    gmsh.model.geo.synchronize()


def _get_names_physical(gmsh, dimtag):
    grp_tags = gmsh.model.getPhysicalGroupsForEntity(*dimtag)
    names = [gmsh.model.getPhysicalName(1, tag) for tag in grp_tags]

    return names


def process_mesh(
    self, file_in, file_out, is_get_lam=True, is_get_magnet=False, is_hole_air=True
):
    """Preprocess the GMSH model, i.e. remove unused parts, rename boundaries, ..."""
    # TODO utilize 'translation' dict

    gmsh.initialize()
    gmsh.open(file_in)
    gmsh.model.geo.removeAllDuplicates()

    # remove unused model parts
    _remove_entities(gmsh, labels=["stator", "w_sta"])

    # get group names
    grps = gmsh.model.getPhysicalGroups(-1)
    grp_names = [gmsh.model.getPhysicalName(*grp) for grp in grps]

    # get lists of some surfaces by name
    magnet_list = []
    for grp, name in zip(grps, grp_names):
        if "magnet" in name.lower():
            entities = gmsh.model.getEntitiesForPhysicalGroup(*grp)
            if grp[0] == 2:
                magnet_list.extend(entities.tolist())

    if True:  # is_get_lam:
        lam_list = []
        for grp, name in zip(grps, grp_names):
            if "rotor_lam" in name.lower():
                entities = gmsh.model.getEntitiesForPhysicalGroup(*grp)
                if grp[0] == 2:
                    lam_list.extend(entities.tolist())

        lam_lines = []
        for lam in lam_list:
            lam_lines.extend(gmsh.model.getBoundary([(2, lam)], oriented=False))
        lam_lines = list(set([lam[1] for lam in lam_lines]))  # unique

        hole_lines = []
        for line in lam_lines:
            names = _get_names_physical(
                gmsh,
                dimtag=[
                    1,
                    line,
                ],
            )
            if any(["h_rotor" in name.lower() for name in names]):
                hole_lines.append(line)

    if is_get_lam and not is_get_magnet:
        ext = "Master"
    else:
        ext = "Slave"

    # setup dict to store physical groups, key: group name, value: list of tags
    groups_dict = {}

    # get lines of magnets for processing their physical groups
    for id, magnet in enumerate(magnet_list):
        lines = gmsh.model.getBoundary([(2, magnet)])
        # store new group names in 'groups_dict' to set it later
        for line in lines:
            names = _get_names_physical(
                gmsh,
                dimtag=[
                    1,
                    abs(line[1]),
                ],
            )
            if not names:
                print(f"Warning: Found magnet line without label - line {line[1]}")

            if is_get_magnet or (is_get_lam and line[1] in lam_lines):
                for name in names:
                    if "Magnet" in name:
                        if (
                            line[1] in lam_lines
                        ):  # only lines with direct contact for now
                            # replace number and add 'Slave'
                            s = name.split("_")
                            s.append(ext)  # add extension
                            s[2] = str(id)  # renumber
                            key = "_".join(s)  # new name
                            if key not in groups_dict.keys():
                                groups_dict[key] = []
                            groups_dict[key].append(line)

            # Test if other lines (with 'Hole' phy. group) and same phy. group ext.
            # ('Left', ...) share the same points to add them as well
            # TODO if not used with direct contact (see above),
            #      but I will keep it for Contact Simulation
            # if is_get_lam:
            #     # get the name of the magnets line
            #     s = None
            #     for name in names:
            #         if "Magnet" in name:
            #             s = name.split('_')
            #     # basic check of magnet line name
            #     if s is not None and len(s) >= 3:
            #         for hline in hole_lines:
            #             if hline != abs(line[1]): # skip if hole line == magnet line
            #                 # test for same extension ('Left', 'Right', ...)
            #                 names = _get_names_physical(gmsh, dimtag=[1, hline])
            #                 if any([s[2] in name for name in names]):
            #                     p1 = [x[1] for x in gmsh.model.getBoundary([line])]
            #                     p2 = [x[1] for x in gmsh.model.getBoundary([(1, hline)])]
            #                     pt = [p for p in p1 if p in p2]
            #                     if pt:
            #                         if len(s) == 3:
            #                             s.append('Master') # add extension
            #                         s[1] = str(id) # renumber
            #                         key = "_".join(s) # new name
            #                         if key not in groups_dict.keys():
            #                             groups_dict[key] = []
            #                         groups_dict[key].append((1, hline))
            #         if not is_hole_air:
            #             pass # TODO implement

        if is_get_magnet:
            # store new magnet body name
            s = "Magnet_" + str(id) + "_Body"
            groups_dict[s] = [
                (2, magnet),
            ]

    if is_get_lam:
        # store new lamination body name
        for id, lam in enumerate(lam_list):
            s = "Lamination_" + str(id) + "_Body"
            if s not in groups_dict:
                groups_dict[s] = []
            groups_dict[s].append((2, lam))

        # store hole if not air
        if not is_hole_air:
            pass  # TODO

    # add symmetry boundaries to keeper dict 'groups_dict'
    if is_get_lam:
        keeper_list = [
            "MASTER_ROTOR_BOUNDARY",
            "SLAVE_ROTOR_BOUNDARY",
            "Rotor_Tangential_Bridge",
            "Rotor_Radial_Bridge",
            "ROTOR_BORE_CURVE",
        ]

        for line in lam_lines:
            names = _get_names_physical(gmsh, dimtag=[1, line])
            for key in keeper_list:
                if any([key in name for name in names]):
                    if key not in groups_dict:
                        groups_dict[key] = []
                    groups_dict[key].append((1, line))

    # update group names
    grps = gmsh.model.getPhysicalGroups(-1)
    grp_names = [gmsh.model.getPhysicalName(*grp) for grp in grps]

    # delete unused surfaces
    del_list = ["shaft", "h_rotor"]
    if not is_get_magnet:
        del_list.append("magnet")

    if not is_get_lam:
        del_list.append("rotor_lam")

    for grp, name in zip(grps, grp_names):
        if any([n in name.lower() for n in del_list]):
            entities = gmsh.model.getEntitiesForPhysicalGroup(*grp).tolist()
            for entity in entities:
                if grp[0] == 2:
                    gmsh.model.geo.remove([(2, entity)], recursive=False)

    # set new physical group names after removing all 'old' physical groups
    gmsh.model.removePhysicalGroups(dimTags=[])
    for name in grp_names:
        gmsh.model.removePhysicalName(name)

    for key, values in groups_dict.items():
        # lines
        tags = [abs(dimtag[1]) for dimtag in values if dimtag[0] == 1]
        tags = list(set(tags))
        if tags:
            print(f"Add physical group {key} with lines {tags}")
            pg = gmsh.model.addPhysicalGroup(1, tags, tag=-1)
            gmsh.model.setPhysicalName(1, pg, key)
        # surfaces
        tags = [abs(dimtag[1]) for dimtag in values if dimtag[0] == 2]
        tags = list(set(tags))
        if tags:
            print(f"Add physical group {key} with surface {tags}")
            pg = gmsh.model.addPhysicalGroup(2, tags, tag=-1)
            gmsh.model.setPhysicalName(2, pg, key)

    # cleanup
    # get all entities
    gmsh.model.geo.synchronize()
    entities_all = gmsh.model.getEntities(dim=-1)
    surf_list = gmsh.model.getEntities(dim=2)
    print(surf_list)

    # get lines of surfaces
    line_list = []
    for surf in surf_list:
        line_list.extend(gmsh.model.getBoundary([surf]))
    line_list = [(line[0], abs(line[1])) for line in line_list]

    # remove all lines that are not part of the surfaces
    for entity in entities_all:
        if (entity[0], abs(entity[1])) not in line_list and entity[0] == 1:
            gmsh.model.geo.remove([entity], recursive=False)

    # entities_all = gmsh.model.getEntities(dim=-1)

    # remove unknown/unused physical groups
    # TODO

    # save
    gmsh.model.geo.synchronize()

    # gmsh.model.geo.mesh.setTransfiniteSurface(tag)
    for surf in surf_list:
        gmsh.model.mesh.setRecombine(2, surf[1])

    # gmsh.option.setNumber("Mesh.RecombinationAlgorithm", 1)

    gmsh.model.mesh.generate(2)
    # gmsh.model.mesh.recombine()
    gmsh.model.mesh.refine()
    # gmsh.model.mesh.refine()
    # gmsh.model.mesh.recombine()
    # gmsh.model.mesh.refine()

    # save mesh or geo file depending on file extension
    filename, file_extension = splitext(file_out)

    if file_extension == ".geo":
        gmsh.write(filename + ".geo_unrolled")
        replace(filename + ".geo_unrolled", filename + file_extension)
    else:
        gmsh.model.mesh.generate(2)
        gmsh.write(file_out)

    # gmsh.fltk.run()      # Uncomment to launch Gmsh GUI

    # update group names once again
    grps = gmsh.model.getPhysicalGroups(-1)
    grp_names = [gmsh.model.getPhysicalName(*grp) for grp in grps]

    gmsh.finalize()

    return gmsh, grps, grp_names

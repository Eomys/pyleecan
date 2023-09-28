# -*- coding: utf-8 -*-

from ....Classes.Arc1 import Arc1
from ....Classes.Arc2 import Arc2
from ....Classes.Arc3 import Arc3
from ....Functions.FEMM.get_mesh_param import get_mesh_param
from ....Functions.FEMM.get_FEMM_BC_propname import get_FEMM_BC_propname
from ....Functions.labels import (
    DRAW_PROP_LAB,
    decode_label,
    BOUNDARY_PROP_LAB,
    RADIUS_PROP_LAB,
    YOKE_LAB,
    BORE_LAB,
    LAM_LAB,
)


def draw_FEMM(
    self,
    femm,
    nodeprop=None,
    maxseg=None,
    FEMM_dict=None,
    hide=False,
    BC_dict=None,
    is_draw=True,
    type_set_BC=0,
):
    """draw the Surface in FEMM

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
    nodeprop :
        Nodal property
        (Default value = None)
    maxseg :
        Meshed with elements that span at most maxsegdeg degrees per element
        (Default value = None)
    FEMM_dict : dict
        dictionary containing the main parameters of FEMM
    hide :
        0 = not hidden in post-processor, 1 == hidden in post processor
        (Default value = False)
    BC_dict : dict
        Boundary condition dict ([line label] = BC name)
    is_draw : bool
        1 to draw the list of surfaces given
    type_set_BC : bool
        1 to set BC of the yoke only, 0 to set all

    Returns
    -------
    None

    """
    # Check if the Surface is correct
    self.check()

    # Draw all the lines
    lines = self.get_lines()

    for line in lines:
        label_dict = decode_label(self.label)  # Use surface mesh param
        # Bore / Yoke radius should have different mesh property
        if line.prop_dict not in [None, dict()]:
            if RADIUS_PROP_LAB in line.prop_dict:
                if YOKE_LAB in line.prop_dict[RADIUS_PROP_LAB]:
                    label_dict["surf_type"] = LAM_LAB + YOKE_LAB
                elif BORE_LAB in line.prop_dict[RADIUS_PROP_LAB]:
                    label_dict["surf_type"] = LAM_LAB + BORE_LAB
                else:
                    raise Exception(
                        "Unknown prop_dict for line of surface " + self.label
                    )
            if DRAW_PROP_LAB in line.prop_dict and not line.prop_dict[DRAW_PROP_LAB]:
                continue  #  This line should not be drawn
        mesh_dict = get_mesh_param(label_dict, FEMM_dict)

        group = mesh_dict["group"]
        if isinstance(group, list):
            group = group[label_dict["S_id"]]

        # Get or create the Boundary Condition (if any)
        if line.prop_dict is not None and BOUNDARY_PROP_LAB in line.prop_dict:
            is_yoke_BC = LAM_LAB + YOKE_LAB in line.prop_dict[BOUNDARY_PROP_LAB]

            if type_set_BC == 0 or (type_set_BC == 1 and is_yoke_BC):
                propname = get_FEMM_BC_propname(
                    femm=femm,
                    line_label=line.prop_dict[BOUNDARY_PROP_LAB],
                    BC_dict=BC_dict,
                )

            else:
                propname = "None"  # No BC to set
        else:
            propname = "None"  # No BC to set
        # Draw the Line
        if type(line) in [Arc1, Arc2, Arc3]:
            line.draw_FEMM(
                femm=femm,
                nodeprop=nodeprop,
                maxseg=maxseg,
                element_size=mesh_dict["element_size"],
                propname=propname,
                hide=hide,
                group=group,
                is_draw=is_draw,
            )
        else:
            line.draw_FEMM(
                femm=femm,
                nodeprop=nodeprop,
                propname=propname,
                element_size=mesh_dict["element_size"],
                automesh=mesh_dict["automesh"],
                hide=hide,
                group=group,
                is_draw=is_draw,
            )

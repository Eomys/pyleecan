# -*- coding: utf-8 -*-

from pyleecan.Classes.Arc1 import Arc1
from pyleecan.Classes.Arc2 import Arc2
from pyleecan.Classes.Arc3 import Arc3


def draw_FEMM(
    self,
    nodeprop=None,
    maxseg=None,
    propname=None,
    elementsize=None,
    automesh=None,
    hide=False,
    group=None,
):
    """draw the Surface in FEMM

    Parameters
    ----------
    nodeprop :
        Nodal property
         (Default value = None)
    maxseg :
        Meshed with elements that span at most maxsegdeg degrees per element
         (Default value = None)
    propname :
        Boundary property ’propname’
         (Default value = None)
    elementsize :
        Local element size along segment no greater than elementsize
        (Default value = None)
    automesh :
        0 = mesher defers to the element constraint defined by
        elementsize, 1 = mesher automatically chooses mesh size along
        the selected segments
        (Default value = None)
    hide :
        0 = not hidden in post-processor, 1 == hidden in post processor
        (Default value = False)
    group :
        the group the SurLine object belongs
         (Default value = None)

    Returns
    -------
    None
    
    """
    # Check if the Surface is correct
    self.check()
    # Draw all the lines
    lines = self.get_lines()
    for line in lines:
        if type(line) in [Arc1, Arc2, Arc3]:
            line.draw_FEMM(
                nodeprop=nodeprop,
                maxseg=maxseg,
                propname=propname,
                hide=hide,
                group=group,
            )
        else:
            line.draw_FEMM(
                nodeprop=nodeprop,
                propname=propname,
                elementsize=elementsize,
                automesh=automesh,
                hide=hide,
                group=group,
            )

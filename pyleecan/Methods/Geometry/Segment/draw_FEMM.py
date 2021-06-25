# -*- coding: utf-8 -*-

from ....Functions.FEMM import boundary_prop
from ....Functions.labels import BOUNDARY_PROP_LAB


def draw_FEMM(
    self,
    femm,
    nodeprop=None,
    propname=None,
    element_size=None,
    automesh=None,
    hide=False,
    group=None,
):
    """<   Draw the segment in FEMM and assign the property

    Parameters
    ----------
    femm : FEMMHandler
        client to send command to a FEMM instance
    nodeprop :
        Nodal property
         (Default value = None)
    propname :
        Boundary property ’propname’
         (Default value = None)
    element_size :
        Local element size along segment no greater than element_size
         (Default value = None)
    automesh :
        0 = mesher defers to the element constraint defined by
        element_size, 1 = mesher automatically chooses mesh size along
        the selected segments
        (Default value = None)
    hide :
        0 = not hidden in post-processor, 1 == hidden in post processorc
         (Default value = False)
    group :
        group the segment belongs
         (Default value = None)

    Returns
    -------


    """

    # Get BC (if any)
    if self.prop_dict is not None and BOUNDARY_PROP_LAB in self.prop_dict:
        propname = boundary_prop[self.prop_dict[BOUNDARY_PROP_LAB]]

    # Add the nodes
    X1, Y1 = self.begin.real, self.begin.imag
    X2, Y2 = self.end.real, self.end.imag
    femm.mi_addnode(X1, Y1)
    femm.mi_selectnode(X1, Y1)
    femm.mi_setnodeprop(nodeprop, group)
    femm.mi_clearselected()
    femm.mi_addnode(X2, Y2)
    femm.mi_selectnode(X2, Y2)
    femm.mi_setnodeprop(nodeprop, group)
    femm.mi_clearselected()
    # add the segment
    femm.mi_addsegment(X1, Y1, X2, Y2)
    # Set property
    femm.mi_selectsegment((X1 + X2) / 2, (Y1 + Y2) / 2)
    femm.mi_setsegmentprop(propname, element_size, automesh, hide, group)
    femm.mi_clearselected()

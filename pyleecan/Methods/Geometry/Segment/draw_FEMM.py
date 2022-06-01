def draw_FEMM(
    self,
    femm,
    nodeprop=None,
    propname=None,
    element_size=None,
    automesh=None,
    hide=False,
    group=None,
    is_draw=True,
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
    is_draw : bool
        1 to draw the list of surfaces given

    Returns
    -------
    None
    """

    # Determine locations of the nodes
    X1, Y1 = self.begin.real, self.begin.imag
    X2, Y2 = self.end.real, self.end.imag

    if is_draw:
        # Adding nodes
        femm.mi_addnode(X1, Y1)
        femm.mi_addnode(X2, Y2)

    # Adding property on the node
    femm.mi_selectnode(X1, Y1)
    femm.mi_setnodeprop(nodeprop, group)
    femm.mi_clearselected()
    femm.mi_selectnode(X2, Y2)
    femm.mi_setnodeprop(nodeprop, group)
    femm.mi_clearselected()

    if is_draw:
        # Adding the segment
        femm.mi_addsegment(X1, Y1, X2, Y2)

    # Set property of the segment
    femm.mi_selectsegment((X1 + X2) / 2, (Y1 + Y2) / 2)
    femm.mi_setsegmentprop(propname, element_size, automesh, hide, group)
    femm.mi_clearselected()

def get_xoutput_ref(self):
    """Return the reference XOutput (or Output) either from xoutput_ref or output_list

    Parameters
    ----------
    self : XOutput
        A XOutput object
    Returns
    -------
    xoutput_ref: XOutput
        reference XOutput (or Output) (if defined)
    """

    if self.xoutput_ref_index is not None:
        return self.output_list[self.xoutput_ref_index]
    else:
        return self.xoutput_ref

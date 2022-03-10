from os.path import join


def run(self, out):
    """PostProcessing to clean a LUT from un-necessary output
    after the corresponding simulation

    Parameters
    ----------
    self : PostLUT
        A PostLUT object
    out: LUT
        LUT object coming from LUT calculation workflow to cleanup
    """

    assert out.simu.var_simu.is_keep_all_output is True

    # Clean all reference Output (only use output_list)
    out.elec = None
    out.mag = None
    out.struct = None
    out.force = None
    out.loss = None

    # Clean all un-necessary data from output_list
    for out_single in out.output_list:
        # out_single.elec is not cleaned
        out_single.mag.clean(clean_level=5)
        out_single.struct = None
        out_single.force = None
        out_single.loss = None

    # Save/Store LUT object
    if self.is_save_LUT:
        out.save(
            save_path=join(out.get_path_result(), "LUT.h5"),
        )
    if self.is_store_LUT:
        self.LUT = out

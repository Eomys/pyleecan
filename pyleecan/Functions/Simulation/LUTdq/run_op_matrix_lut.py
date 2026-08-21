from ._utils import prepare_lut_varload_simu


def run_op_matrix_lut(simu, op_matrix):
    """Run a LUT-based electrical sweep on an arbitrary OP matrix."""

    simu_step = prepare_lut_varload_simu(simu, op_matrix)
    xoutput = simu_step.run()

    return {
        "simu": simu_step,
        "xoutput": xoutput,
        "OP_matrix": simu_step.var_simu.OP_matrix,
    }

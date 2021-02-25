from numpy import ndarray, min as np_min, max as np_max

from SciDataTool import VectorField, Data


def log_datakeeper_step_result(simulation, datakeeper_list, index, simu_type):
    """Log the content of the datakeeper for the step index (if index=None, use reference)"""
    if simulation.layer == 2:
        msg = "    "
    else:
        msg = ""
    if simu_type is not None:
        msg += simu_type + " "
    if simulation.index is None:
        msg += "Reference "
    msg += "Results: "
    for datakeeper in datakeeper_list:
        if index is None:
            value = datakeeper.result_ref
        else:
            value = datakeeper.result[index]
        # Format log
        if isinstance(value, ndarray):
            msg += (
                datakeeper.symbol
                + "=array(min="
                + format(np_min(value), ".4g")
                + ",max="
                + format(np_max(value), ".4g")
                + ")"
            )
        elif isinstance(value, list):
            msg += (
                datakeeper.symbol
                + "=list(min="
                + format(np_min(value), ".4g")
                + ",max="
                + format(np_max(value), ".4g")
                + ")"
            )
        elif isinstance(value, Data) or isinstance(value, VectorField):
            msg += datakeeper.symbol + "=" + type(value).__name__
        elif value is None:
            msg += datakeeper.symbol + "=None"
        else:
            msg += datakeeper.symbol + "=" + format(value, ".4g")
        if datakeeper.unit is not None:
            msg += " [" + datakeeper.unit + "], "
        else:
            msg += ", "
    msg = msg[:-2]
    simulation.get_logger().info(msg)
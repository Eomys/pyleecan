from numpy import array


class XOutputError(Exception):
    pass


def _get_symbol_data_(self, symbol, index):
    """Helper function to get data and label by symbol to avoid duplicate code."""
    # Get the data
    if symbol in self.keys():  # DataKeeper or OptiObjective
        data = self[symbol]
        values = array(data.result)[index]
    elif symbol in [pe.symbol for pe in self.paramexplorer_list]:  # ParamSetter
        data = self.get_paramexplorer(symbol)
        values = array(data.value)[index]
    else:  # ParamSetter
        symbol_ = next(iter(self.keys()))
        self.get_logger().warning(
            f"XOutput.plot_pareto(): Symbol '{symbol}' not found. "
            + f"Using symbol '{symbol_}' instead."
        )
        symbol = symbol_
        data = self[symbol]
        values = array(data.result)[index]

    # label definition
    label = symbol
    if data.unit not in ["", None]:
        label += " [{}]".format(data.unit)

    return values, label

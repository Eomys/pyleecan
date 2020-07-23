class XOutputError(Exception):
    pass


def get_param_array(self, symbol):
    """Get the parameter value array"""
    symbols = [paramexplorer.symbol for paramexplorer in self.paramexplorer_list]

    if symbol not in symbols:
        raise XOutputError("Unknown symbol {}".format(symbol))
    else:
        pe_index = symbols.index(symbol)

    return self.paramexplorer_list[pe_index].value

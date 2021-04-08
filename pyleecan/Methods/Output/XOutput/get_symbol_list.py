def get_symbol_list(self):
    """
    Return the list of the symobl of the DataKeeper and ParamExplorer
    """
    symbol_list = self.keys()  # DataKeeper or OptiObjective
    symbol_list.extend([pe.symbol for pe in self.paramexplorer_list])

    return symbol_list

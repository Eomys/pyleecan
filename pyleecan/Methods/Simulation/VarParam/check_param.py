class ParamExplorerError(Exception):
    pass


class VarParamError(Exception):
    pass


class DataKeeperError(Exception):
    pass


def check_param(self):
    """Check VarParam parameters validity 
    
    Raises
    ------
    ParamExplorerError: Error in ParamExplorer setting
    VarParamError: Error in VarParam general setting
    DataKeeperError: Error in DataKeeper setting
    """

    # Check the reference simulation
    if self.parent == None:
        raise VarParamError("VarParam object must be inside a Simulation object")

    # Check ParamExplorers
    for paramexplorer in self.paramexplorer_list:
        if paramexplorer.setter is None:
            raise ParamExplorerError("ParamExplorer.setter must be defined")
        elif len(paramexplorer.symbol) == 0:
            raise ParamExplorerError("ParamExplorer.symbol cannot be empty")
        elif len(paramexplorer.value_list) == 0:
            raise ParamExplorerError("ParamExplorer.value_list cannot be empty")

    # Default simulation index
    if self.ref_simu_index is not None:
        assert len(self.ref_simu_index) == len(self.paramexplorer_list), VarParamError(
            "Index must have {} dimensions".format(len(self.paramexplorer_list))
        )

    # Keep every output if there is no DataKeeper defined
    if len(self.datakeeper_list) == 0 and self.is_keep_all_output is False:
        logger = self.get_logger()
        logger.warning(
            "No datakeeper has been define in VarParam, setting is_keep_all_output as True."
        )
        self.is_keep_all_output = True

    if self.ref_simu_index is not None:
        # Check ref_simu_index length
        assert len(self.ref_simu_index) == len(self.paramexplorer_list), VarParamError(
            "Wrong ref_simu_index lentgh expected {} got {}".format(
                len(self.ref_simu_index), len(self.paramexplorer_list)
            )
        )

        # # Check index value for each parameter
        # for i, val in self.ref_simu_index:
        # TODO implement ParamExplorer.get_size method to compare index with size

    # Check DataKeepers
    for datakeeper in self.datakeeper_list:
        if datakeeper.symbol in ["", None]:
            raise DataKeeperError("DataKeeper.symbol cannot be empty")
        elif datakeeper.keeper is None:
            raise DataKeeperError("DataKeeper.keeper must be defined")

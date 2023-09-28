from ....Classes.ParamExplorerSet import ParamExplorerSet


class ParamExplorerError(Exception):
    pass


class VarParamSweepError(Exception):
    pass


class DataKeeperError(Exception):
    pass


def check_param(self):
    """Check VarParamSweep parameters validity

    Raises
    ------
    ParamExplorerError: Error in ParamExplorer setting
    VarParamSweepError: Error in VarParamSweep general setting
    DataKeeperError: Error in DataKeeper setting
    """
    # run the base class check first
    super(type(self), self).check_param()

    # Check ParamExplorers
    for paramexplorer in self.paramexplorer_list:
        if paramexplorer.setter is None:
            raise ParamExplorerError("ParamExplorer.setter must be defined")
        elif len(paramexplorer.symbol) == 0:
            raise ParamExplorerError("ParamExplorer.symbol cannot be empty")
        elif (
            isinstance(paramexplorer, ParamExplorerSet)
            and len(paramexplorer.value) == 0
        ):
            raise ParamExplorerError("ParamExplorer.value_list cannot be empty")

    # Default simulation index
    N_simu = self.get_simu_number()

    # Keep every output if there is no DataKeeper defined
    if len(self.datakeeper_list) == 0 and self.is_keep_all_output is False:
        logger = self.get_logger()
        logger.warning(
            "No datakeeper has been define in VarParamSweep, setting is_keep_all_output as True."
        )
        self.is_keep_all_output = True

    # Check DataKeepers
    for datakeeper in self.datakeeper_list:
        if datakeeper.symbol in ["", None]:
            raise DataKeeperError("DataKeeper.symbol cannot be empty")
        elif datakeeper.keeper is None:
            raise DataKeeperError("DataKeeper.keeper must be defined")

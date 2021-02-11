from ....Classes.ParamExplorerSet import ParamExplorerSet
from ....Methods.Simulation.VarSimu.check_param import check_param as check_param_


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
    # run the base class check first
    check_param_(self)

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
    if self.ref_simu_index is not None:
        assert self.ref_simu_index < N_simu, VarParamError(
            "ref_simu_index must be less than {}, got {}".format(
                N_simu, self.ref_simu_index
            )
        )

    # Keep every output if there is no DataKeeper defined
    if len(self.datakeeper_list) == 0 and self.is_keep_all_output is False:
        logger = self.get_logger()
        logger.warning(
            "No datakeeper has been define in VarParam, setting is_keep_all_output as True."
        )
        self.is_keep_all_output = True

    # Check DataKeepers
    for datakeeper in self.datakeeper_list:
        if datakeeper.symbol in ["", None]:
            raise DataKeeperError("DataKeeper.symbol cannot be empty")
        elif datakeeper.keeper is None:
            raise DataKeeperError("DataKeeper.keeper must be defined")

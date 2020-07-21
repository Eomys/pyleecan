class ParamSetterError(Exception):
    pass


class VarParamError(Exception):
    pass


class DataKeeperError(Exception):
    pass


def check_param(self):
    """Check VarParam parameters validity 
    
    Raises
    ------
    ParamSetterError: Error in ParamSetter setting
    VarParamError: Error in VarParam general setting
    DataKeeperError: Error in DataKeeper setting
    """

    # Check the reference simulation
    if self.parent == None:
        raise VarParamError("VarParam object must be inside a Simulation object")

    # Check ParamSetters
    for paramsetter in self.paramsetter_list:
        if paramsetter.setter is None:
            raise ParamSetterError("ParamSetter.setter must be defined")
        elif len(paramsetter.symbol) == 0:
            raise ParamSetterError("ParamSetter.symbol cannot be empty")
        elif len(paramsetter.value_list) == 0:
            raise ParamSetterError("ParamSetter.value_list cannot be empty")

    # Default simulation index
    if self.ref_simu_index is not None:
        assert len(self.ref_simu_index) == len(self.paramsetter_list), VarParamError(
            "Index must have {} dimensions".format(len(self.paramsetter_list))
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

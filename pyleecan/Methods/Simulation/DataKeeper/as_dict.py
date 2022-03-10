from numpy import ndarray


def as_dict(self, **kwargs):
    """
    Convert this object in a json serializable dict (can be use in __init__).
    Optional keyword input parameter is for internal use only
    and may prevent json serializability.
    """

    DataKeeper_dict = dict()
    DataKeeper_dict["name"] = self.name
    DataKeeper_dict["physic"] = self.physic
    DataKeeper_dict["symbol"] = self.symbol
    DataKeeper_dict["unit"] = self.unit
    if self._keeper_str is not None:
        DataKeeper_dict["keeper"] = self._keeper_str
    elif "keep_function" in kwargs and kwargs["keep_function"]:
        DataKeeper_dict["keeper"] = self.keeper
    else:
        DataKeeper_dict["keeper"] = None
        if self.keeper is not None:
            self.get_logger().warning(
                "DataKeeper.as_dict(): "
                + f"Function {self.keeper.__name__} is not serializable "
                + "and will be converted to None."
            )
    if self._error_keeper_str is not None:
        DataKeeper_dict["error_keeper"] = self._error_keeper_str
    elif "keep_function" in kwargs and kwargs["keep_function"]:
        DataKeeper_dict["error_keeper"] = self.error_keeper
    else:
        DataKeeper_dict["error_keeper"] = None
        if self.error_keeper is not None:
            self.get_logger().warning(
                "DataKeeper.as_dict(): "
                + f"Function {self.error_keeper.__name__} is not serializable "
                + "and will be converted to None."
            )
    DataKeeper_dict["result"] = self.result.copy() if self.result is not None else None
    if DataKeeper_dict["result"] is not None:
        for ii in range(len(DataKeeper_dict["result"])):
            if hasattr(DataKeeper_dict["result"][ii], "as_dict"):
                DataKeeper_dict["result"][ii] = DataKeeper_dict["result"][ii].as_dict()
            elif isinstance(DataKeeper_dict["result"][ii], ndarray):
                DataKeeper_dict["result"][ii] = DataKeeper_dict["result"][ii].tolist()
    DataKeeper_dict["result_ref"] = self.result_ref
    if hasattr(DataKeeper_dict["result_ref"], "as_dict"):
        DataKeeper_dict["result_ref"] = DataKeeper_dict["result_ref"].as_dict()
    elif isinstance(DataKeeper_dict["result_ref"], ndarray):
        DataKeeper_dict["result_ref"] = DataKeeper_dict["result_ref"].tolist()
    # The class name is added to the dict for deserialisation purpose
    DataKeeper_dict["__class__"] = "DataKeeper"
    return DataKeeper_dict

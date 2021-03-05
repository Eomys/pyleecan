def as_dict(self):
    """Convert this object in a json seriable dict (can be use in __init__)"""

    DataKeeper_dict = dict()
    DataKeeper_dict["name"] = self.name
    DataKeeper_dict["symbol"] = self.symbol
    DataKeeper_dict["unit"] = self.unit
    if self._keeper_str is not None:
        DataKeeper_dict["keeper"] = self._keeper_str
    else:
        DataKeeper_dict["keeper"] = None
    if self._error_keeper_str is not None:
        DataKeeper_dict["error_keeper"] = self._error_keeper_str
    else:
        DataKeeper_dict["error_keeper"] = None
    DataKeeper_dict["result"] = self.result.copy() if self.result is not None else None
    if DataKeeper_dict["result"] is not None:
        for ii in range(len(DataKeeper_dict["result"])):
            if hasattr(DataKeeper_dict["result"][ii], "as_dict"):
                DataKeeper_dict["result"][ii] = DataKeeper_dict["result"][ii].as_dict()
    # The class name is added to the dict for deserialisation purpose
    DataKeeper_dict["__class__"] = "DataKeeper"
    return DataKeeper_dict

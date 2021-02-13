from ....Classes._frozen import FrozenClass
from numpy import ndarray


def as_dict(self, **kwargs):
    """
    Convert this object in a json serializable dict (can be use in __init__).
    Optional keyword input parameter is for internal use only
    and may prevent json serializability.
    """
    # Get the properties inherited from ParamExplorer
    ParamExplorerSet_dict = super(type(self), self).as_dict(keep_function=keep_function)
    if self.value is None:
        ParamExplorerSet_dict["value"] = None
    else:
        ParamExplorerSet_dict["value"] = list()
        for obj in self.value:
            if isinstance(obj, FrozenClass):
                if "SciDataTool" in obj.__class__.__module__:
                    ParamExplorerSet_dict["value"].append(obj.as_dict())
                else:
                    ParamExplorerSet_dict["value"].append(obj.as_dict(**kwargs))
            elif isinstance(obj, ndarray):
                ParamExplorerSet_dict["value"].append(obj.tolist())
            else:
                ParamExplorerSet_dict["value"].append(obj)
    # The class name is added to the dict for deserialisation purpose
    # Overwrite the mother class name
    ParamExplorerSet_dict["__class__"] = "ParamExplorerSet"
    return ParamExplorerSet_dict

from ....Classes._frozen import FrozenClass
from numpy import ndarray


def as_dict(self):
    """Convert this object in a json seriable dict (can be use in __init__)"""

    # Get the properties inherited from ParamExplorer
    ParamExplorerSet_dict = super(type(self), self).as_dict()
    ParamExplorerSet_dict["value"] = (
        self.value.copy() if self.value is not None else None
    )
    if self.value is None:
        ParamExplorerSet_dict["value"] = None
    else:
        ParamExplorerSet_dict["value"] = list()
        for obj in self.value:
            if isinstance(obj, FrozenClass):
                ParamExplorerSet_dict["value"].append(obj.as_dict())
            elif isinstance(obj, ndarray):
                ParamExplorerSet_dict["value"].append(obj.tolist())
            else:
                ParamExplorerSet_dict["value"].append(obj)
    # The class name is added to the dict for deserialisation purpose
    # Overwrite the mother class name
    ParamExplorerSet_dict["__class__"] = "ParamExplorerSet"
    return ParamExplorerSet_dict

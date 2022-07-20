from ....Functions.load import load_init_dict
from ....Functions.Load.import_class import import_class
from ....Classes._check import check_var
from numpy import ndarray, array


def _set_OP_matrix(self, value):
    """setter of OP_matrix"""
    if isinstance(value, list):
        value = array(value)
    if isinstance(value, str):  # Load from file
        try:
            value = load_init_dict(value)[1]
        except Exception as e:
            self.get_logger().error(
                "Error while loading " + value + ", setting None instead"
            )
            value = None
    if isinstance(value, dict) and "__class__" in value:
        class_obj = import_class(
            "pyleecan.Classes", value.get("__class__"), "OP_matrix"
        )
        value = class_obj(init_dict=value)
    elif isinstance(value, ndarray):
        # Conver matrix to OP_matrix object
        class_obj = import_class("pyleecan.Classes", "OPMatrix", "OP_matrix")
        value_obj = class_obj()
        value_obj._set_None()
        # N0, Id, Iq, Tem, Pem is the most commun OP_matrix format
        if value.shape[1] == 5:
            value_obj.set_OP_array(value, "N0", "Id", "Iq", "Tem", "Pem")
        elif value.shape[1] == 4:
            value_obj.set_OP_array(value, "N0", "Id", "Iq", "Tem")
        else:
            value_obj.set_OP_array(value, "N0", "Id", "Iq")
        value = value_obj
    elif type(value) is int and value == -1:  # Default constructor
        OP_matrix = import_class("pyleecan.Classes", "OPMatrix", "OP_matrix")
        value = OP_matrix()
    check_var("OP_matrix", value, "OPMatrix")
    self._OP_matrix = value

    if self._OP_matrix is not None:
        self._OP_matrix.parent = self

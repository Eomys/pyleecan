from ....Functions.path_tools import abs_file_path
from ntpath import basename

PYTHON_DEFAULT_ENCODING = "utf-8-sig"
PATH_FUNCTION_RULE_COMPLEX_MOT = "pyleecan\Functions\Converter\MotorCAD\\"


def _set_fct_name(self, value):
    """find the path of functions

    Parameters
    ----------
    self : Rule
        A Rule object
    value : str
        name of file for complex rule

    """
    self._fct_name = value
    if isinstance(self.fct_name, str):
        module = __import__(
            f"pyleecan.Functions.Converter.MotorCAD.{self.fct_name}",
            fromlist=(self.fct_name),
        )

        self.other_to_P = getattr(module, "other_to_P")
        self.P_to_other = getattr(module, "P_to_other")

from ....Functions.path_tools import abs_file_path
from ntpath import basename

PYTHON_DEFAULT_ENCODING = "utf-8-sig"
PATH_FUNCTION_RULE_COMPLEX_MOT = "pyleecan\Functions\Converter\MotorCAD\\"


def _set_fct_name(self, value):
    self._fct_name = value
    if isinstance(self.fct_name, str):
        self._fct_name = PATH_FUNCTION_RULE_COMPLEX_MOT + self.fct_name + ".py"

        f = open(self._fct_name, "r", encoding=PYTHON_DEFAULT_ENCODING)
        exec(f.read(), globals())
        f.close()

        self.other_to_P = eval("other_to_P")
        self.P_to_other = eval("P_to_other")

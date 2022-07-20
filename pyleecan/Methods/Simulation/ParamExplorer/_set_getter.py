from ....Classes._check import CheckTypeError
from ntpath import basename
from ....Functions.path_tools import abs_file_path
from ....Generator import PYTHON_DEFAULT_ENCODING


def _set_getter(self, value):
    """setter of getter"""
    # Create the function if getter is defined as a string (e.g. simu.machine.rotor.slot.W0)
    if isinstance(value, str) and value[:4] == "simu":
        value_split = value.split(".")
        value = (
            "lambda simu: getattr(eval('"
            + ".".join(value_split[:-1])
            + "'), '"
            + value_split[-1]
            + "')"
        )
    if value is None:
        self._getter_str = None
        self._getter_func = None
    elif isinstance(value, str) and "lambda" in value:
        self._getter_str = value
        self._getter_func = eval(value)
    elif isinstance(value, str) and value[-3:] == ".py":
        if "<" in value and ">" in value:
            # path like "<PARAM_DIR>/setter_rotor.py"
            self._getter_str = value
            value = abs_file_path(value)
        else:  # Direct path
            self._getter_str = value
        f = open(value, "r", encoding=PYTHON_DEFAULT_ENCODING)
        exec(f.read(), globals())
        f.close()
        self._getter_func = eval(basename(value[:-3]))
    elif callable(value):
        self._getter_str = None
        self._getter_func = value
    else:
        raise CheckTypeError(
            "For property getter Expected function or str (path to python file or lambda), got: "
            + str(type(value))
        )

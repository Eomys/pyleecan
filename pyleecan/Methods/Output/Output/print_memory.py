from sys import getsizeof
from ....Functions.Load.import_class import import_class


def print_memory(self, tab_level=0, detail_level=1, is_print=True):
    """Print an estimation of the memory usage for each property of the object

    Parameters
    ----------
    self : Output
        An Output object
    tab_level : int
        Number of tab ("    ") to add before each line
    detail_level : int
        Select how many data to display (0: only object size, 1: object + properties, 2:object + detailed properties)
    is_print: bool
        True print, else return str

    Returns
    -------
    mem_str: str
        if is_print == False, return the string that descibe the memory usage of the object
    """

    tab = ""
    for _ in range(tab_level):
        tab += "    "

    Output = import_class("pyleecan.Classes", "Output")
    if type(self) is Output:
        mem_str = tab + "Total Output size: " + str(getsizeof(self)) + " o\n"
    else:  # XOutput (print only the Output part of the size)
        mem_str = tab + "Total Output size: " + str(Output.__sizeof__(self)) + " o\n"
    if detail_level == 0:
        print(mem_str)
        return
    mem_str += tab + "path_result: " + str(getsizeof(self.path_result)) + " o\n"
    mem_str += tab + "logger_name: " + str(getsizeof(self.logger_name)) + " o\n"

    mem_str += tab + "simu: " + str(getsizeof(self.simu)) + " o\n"
    if detail_level > 1:
        mem_str += detail_prop(self, "simu", tab_level=tab_level + 1)

    mem_str += tab + "geo: " + str(getsizeof(self.geo)) + " o\n"
    if detail_level > 1:
        mem_str += detail_prop(self, "geo", tab_level=tab_level + 1)

    mem_str += tab + "elec: " + str(getsizeof(self.elec)) + " o\n"
    if detail_level > 1:
        mem_str += detail_prop(self, "elec", tab_level=tab_level + 1)

    mem_str += tab + "mag: " + str(getsizeof(self.mag)) + " o\n"
    if detail_level > 1:
        mem_str += detail_prop(self, "mag", tab_level=tab_level + 1)

    mem_str += tab + "force: " + str(getsizeof(self.force)) + " o\n"
    if detail_level > 1:
        mem_str += detail_prop(self, "force", tab_level=tab_level + 1)

    mem_str += tab + "struct: " + str(getsizeof(self.struct)) + " o\n"
    if detail_level > 1:
        mem_str += detail_prop(self, "struct", tab_level=tab_level + 1)

    mem_str += tab + "post: " + str(getsizeof(self.post)) + " o\n"

    if is_print:
        print(mem_str)
    else:
        return mem_str


def detail_prop(self, prop_name, tab_level=1):
    """Detail the content of the property"""

    tab = ""
    for _ in range(tab_level):
        tab += "    "

    mem_str = ""
    prop = getattr(self, prop_name)
    for attr in dir(prop):
        if (
            # Not method
            not callable(getattr(prop, attr))
            # Not private properties
            and not attr.startswith("_")
            # Not following properties
            and attr not in ["VERSION", "logger_name", "parent"]
        ):
            mem_str += (
                tab
                + prop_name
                + "."
                + attr
                + ": "
                + str(getsizeof(getattr(prop, attr)))
                + " o\n"
            )
    return mem_str

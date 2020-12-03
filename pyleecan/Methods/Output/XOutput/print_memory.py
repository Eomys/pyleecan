from sys import getsizeof


def print_memory(self, tab_level=0, detail_level=1, is_print=True):
    """Print an estimation of the memory usage for each property of the object

    Parameters
    ----------
    self : XOutput
        An XOutput object
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

    mem_str = tab + "Total XOutput size: " + str(getsizeof(self)) + " o\n"
    if detail_level == 0:
        print(mem_str)
        return

    mem_str += tab + "Reference simulation:\n"
    mem_str += super(type(self), self).print_memory(
        tab_level=tab_level + 1, detail_level=detail_level, is_print=False
    )

    mem_str += "\nXOutput Data:\n"
    # Paramexplorer_list
    S1 = 0
    if self.paramexplorer_list is not None:
        for obj in self.paramexplorer_list:
            S1 += getsizeof(obj)
    mem_str += tab + "    paramexplorer_list: " + str(S1) + " o\n"
    # output_list
    S2 = 0
    out_list_str = ""
    if self.output_list is not None:
        for ii, obj in enumerate(self.output_list):
            S = getsizeof(obj)
            S2 += S
            out_list_str += (
                tab + "        output_list[" + str(ii) + "]: " + str(S) + " o\n"
            )
            if detail_level > 2:
                out_list_str += self.output_list[ii].print_memory(
                    tab_level=3, detail_level=detail_level - 2, is_print=False
                )
    mem_str += tab + "    output_list: " + str(S2) + " o\n"
    mem_str += out_list_str
    # xoutput_dict
    S3 = 0
    if self.xoutput_dict is not None:
        for key, value in self.xoutput_dict.items():
            S3 += getsizeof(key) + getsizeof(value)
    mem_str += tab + "    xoutput_dict: " + str(S3) + " o\n"
    mem_str += tab + "    nb_simu: " + str(getsizeof(self.nb_simu)) + " o\n"

    if is_print:
        print(mem_str)
    else:
        return mem_str

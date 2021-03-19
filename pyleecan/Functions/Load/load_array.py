from numpy import loadtxt


def load_array(file, sep=":", delimiter=","):
    """Function to load numpy nD arrays. The data delimiter must be choosen correctly.
    Further the file must contain a header on the first line with the arrays shape.
    Example header: '# data: (2, 3, 4, 5)'

    Parameters
    ----------

    file: str
        the file that should be loaded

    sep: str
        seperator that delimits the shape information in the header

    delimiter: str
        data delimiter

    Returns
    -------

    data: ndarray
        the loaded numpy array
    """
    # Load the array from disk
    with open(file) as f:
        first_line = f.readline().strip()

    data = None
    if sep in first_line:
        try:
            tup_str = first_line.split(sep)[1][1:-1]
            shape = tuple(int(x) for x in tup_str.split(",") if x != "")
            data = loadtxt(file, delimiter=delimiter).reshape(shape)
        except Exception as error:
            print("Exception occured while runing load_array():" + str(error))

    return data

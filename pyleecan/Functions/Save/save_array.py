from numpy import ndindex, savetxt


def save_array(
    file, data, fmt="%7.2f", delimiter=",", header="data", slice="slice", sep=":"
):
    """Function to save numpy nD arrays. Therefore the array is sliced except for
    the last 2 dimenions.

    Parameters
    ----------

    file: str
        the save filename

    header: str
        some file header string

    sep: str
        seperator that delimits the shape information in the header

    delimiter: str
        data delimiter

    fmt: str
        string to define the output number format that is passed to numpy.savetext

    Returns
    -------

    None
    """
    # Write the array to disk
    with open(file, "w") as outfile:
        # writing a header to get the shape while loading
        outfile.write(f"#{header}{sep}{data.shape}\n")

        # iterating through ndarray except and write slices of the last 2 dims
        if len(data.shape) > 2:
            d = len(data.shape) - 2
            for i in ndindex(data.shape[:d]):
                # writing a break to indicate different slices...
                outfile.write(f"#{slice}{sep}{i}\n")
                savetxt(outfile, data[i], delimiter=delimiter, fmt=fmt)
        else:
            savetxt(outfile, data, delimiter=delimiter, fmt=fmt)

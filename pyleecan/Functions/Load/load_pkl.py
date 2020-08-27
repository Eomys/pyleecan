from cloudpickle import load


def load_pkl(file_path):
    """
    Load pyleecan object from pkl file

    Parameters
    ----------

    file_path: str
        file path

    Returns
    -------

    obj: Pyleecan object
    """
    with open(file_path, "rb") as file_:
        # file is a group
        obj = load(file_)

    return obj

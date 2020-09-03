from cloudpickle import dump


def save_pkl(obj, save_path):
    """Save a Pyleecan object in a pkl file using cloudpickle
    
    Parameters
    ----------
    obj: Pyleecan object
        object to save
    save_path: str
        file path
    """

    with open(save_path, "wb") as save_file:
        dump(obj, save_file)

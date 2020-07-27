def __missing__(self, key):
    """
    Called by XOutput.__getitem__() to implement self[key] 
    for dict subclasses when key is not in the dictionary.
    """
    return self.xoutput_dict.__missing__(key)

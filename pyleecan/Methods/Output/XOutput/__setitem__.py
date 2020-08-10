def __setitem__(self, key, value):
    """Called to implement assignment to self[key]."""
    if isinstance(key, int) or isinstance(key, slice):
        return self.output_list.__setitem__(key, value)
    else:
        return self.xoutput_dict.__setitem__(key, value)

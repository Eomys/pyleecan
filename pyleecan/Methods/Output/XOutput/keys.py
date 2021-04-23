def keys(self):
    """Return xoutput_dict keys to behave like a dict"""
    if self.xoutput_dict is None:
        return list()
    else:
        return self.xoutput_dict.keys()

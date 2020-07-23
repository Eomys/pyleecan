def __getitem__(self, idx):
    """Method to behave like a list or a dict and iterate in the object"""
    if isinstance(idx, int) or isinstance(idx, slice):
        return self.output_list.__getitem__(idx)
    else:
        return self.xoutput_dict.__getitem__(idx)

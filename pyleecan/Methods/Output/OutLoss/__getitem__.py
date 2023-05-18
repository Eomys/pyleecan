def __getitem__(self, idx):
    """Method to behave like a dict and iterate in the object"""
    return self.loss_dict.__getitem__(idx)

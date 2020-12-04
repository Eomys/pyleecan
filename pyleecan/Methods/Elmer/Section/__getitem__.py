def __getitem__(self, idx):
    """Method to behave like a dict and get the value (and comment as a tuple)"""
    value = self._statements.__getitem__(idx)
    comment = self._comments.__getitem__(idx)
    return (value, comment)

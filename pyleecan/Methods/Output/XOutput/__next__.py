def __next__(self):
    """Method to behave like a list and iterate in the object"""
    return next(self.output_list)

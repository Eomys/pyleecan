def copy(self):
    """Return a copy of the class"""
    return type(self)(init_dict=self.as_dict())

def copy(self, **kwargs):
    """Return a copy of the class"""
    return type(self)(init_dict=self.as_dict(**kwargs))

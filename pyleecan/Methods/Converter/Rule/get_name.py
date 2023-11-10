def get_name(self):
    """Return the name of file or function

    Parameters
    ----------
    self : Rule
        A Rule object
    """
    return self.file_name or self.fct_name

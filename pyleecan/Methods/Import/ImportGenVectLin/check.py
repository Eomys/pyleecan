from ....Methods.Import import ImportError


def check(self):
    """Check that the object is correctly set
    """
    if self.start is None:
        raise ImportError("Start must not be None")
    if self.stop is None:
        raise ImportError("Stop must not be None")
    if self.num is None:
        raise ImportError("Num must not be None")
    if self.stop <= self.start:
        raise ImportError("You must have start < stop")
    if self.endpoint is None:
        self.endpoint = True

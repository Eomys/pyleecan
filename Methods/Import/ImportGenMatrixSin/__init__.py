# -*- coding: utf-8 -*-
from pyleecan.Methods.Import import ImportError


class GenSinEmptyError(ImportError):
    """Raised when the sin_list is empty
    """

    pass


class GenSinDimError(ImportError):
    """Raised when the ImportGenVectSin of the sin_list has different size (N)
    """

    pass


class GenSinTransposeError(ImportError):
    """Raised when the ImportGenVectSin of the sin_list has different is_transpose
    """

    pass


class InitSinMatDimError(ImportError):
    """Raised when the init_vector is called with wrong arguments
    """

    pass

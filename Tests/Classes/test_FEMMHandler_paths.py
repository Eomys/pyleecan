import sys

import pytest

from pyleecan.Classes._FEMMHandler import _FEMMHandler


@pytest.mark.skipif(sys.platform == "win32", reason="Wine/FEMM paths are only used on Linux and macOS")
def test_openfemm_forwards_paths():
    """openfemm(winepath=..., femmpath=...) must pass the user paths on to openfemm_Linux
    (they were replaced by empty strings, so the given paths were silently ignored)."""
    handler = _FEMMHandler()
    with pytest.raises(Exception, match="Given path for wine does not exist"):
        handler.openfemm(1, winepath="/nonexistent/wine/dir", femmpath="/nonexistent/femm")

import os
import tempfile
import re
import uuid
from pathlib import Path

import pytest


TEMP_ROOT = Path(__file__).resolve().parents[1] / ".local" / "pytest-temp"


def pytest_configure(config):
    """Keep pytest temporary files inside the ignored local workspace."""

    temp_root = TEMP_ROOT
    temp_root.mkdir(parents=True, exist_ok=True)
    for name in ("TMPDIR", "TEMP", "TMP"):
        os.environ[name] = str(temp_root)
    tempfile.tempdir = str(temp_root)


@pytest.fixture
def tmp_path(request):
    """Provide a pathlib tmp_path without using the system temp root."""

    safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", request.node.name)
    path = TEMP_ROOT / "cases" / f"{safe_name}-{uuid.uuid4().hex}"
    path.mkdir(parents=True, exist_ok=False)
    return path

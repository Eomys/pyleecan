from os.path import dirname, normpath, join, isfile

from generate_pyleecan_exe import generate_executable
from local_build_paths import get_local_build_paths


if __name__ == "__main__":
    repo_root = normpath(join(dirname(__file__), ".."))
    env_python = join(
        get_local_build_paths(repo_root).env_path, "Scripts", "python.exe"
    )
    generate_executable(
        start=5 if isfile(env_python) else 4,
        stop=5,
        new_version=0,
        branch="master",
        is_clean_end=False,
        is_debug=False,
        project_path=repo_root,
    )

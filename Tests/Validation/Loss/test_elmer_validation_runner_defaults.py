import ast
from pathlib import Path


def _load_module_constants(file_path):
    module = ast.parse(Path(file_path).read_text(encoding="utf-8"))
    constant_dict = {}

    for node in module.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name) and target.id.startswith("DEFAULT_"):
                constant_dict[target.id] = ast.literal_eval(node.value)

    return constant_dict


def test_elmer_validation_runners_default_to_release_baseline():
    repo_root = Path(__file__).resolve().parents[3]
    leaf_constants = _load_module_constants(
        repo_root / "Tests" / "Validation" / "Loss" / "run_elmer_validation_leaf.py"
    )
    prius_constants = _load_module_constants(
        repo_root / "Tests" / "Validation" / "Loss" / "run_elmer_validation_prius.py"
    )

    assert leaf_constants["DEFAULT_NT_TOT"] == 48
    assert leaf_constants["DEFAULT_NA_TOT"] == 720
    assert leaf_constants["DEFAULT_KMESH_FINENESS"] == 1.0

    assert prius_constants["DEFAULT_NT_TOT"] == 48
    assert prius_constants["DEFAULT_NA_TOT"] == 720
    assert prius_constants["DEFAULT_KMESH_FINENESS"] == 1.0

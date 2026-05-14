import pyleecan.Functions.get_path_binary as binary_module


def test_get_path_binary_prefers_env_override(monkeypatch, tmp_path):
    exe_path = tmp_path / "pvpython.exe"
    exe_path.write_text("", encoding="utf-8")

    monkeypatch.setattr(binary_module, "os_name", "nt")
    monkeypatch.setattr(binary_module, "which", lambda _: None)
    monkeypatch.setattr(
        binary_module, "_iter_windows_install_paths", lambda *args, **kwargs: iter(())
    )
    monkeypatch.setenv("PYLEECAN_PVPYTHON", str(exe_path))

    assert binary_module.get_path_binary("pvpython") == str(exe_path.resolve())


def test_get_path_binary_uses_windows_install_fallback(monkeypatch, tmp_path):
    install_dir = tmp_path / "ParaView 6.1.0" / "bin"
    install_dir.mkdir(parents=True)
    exe_path = install_dir / "paraview.exe"
    exe_path.write_text("", encoding="utf-8")

    monkeypatch.setattr(binary_module, "os_name", "nt")
    monkeypatch.setattr(binary_module, "which", lambda _: None)
    monkeypatch.setenv("ProgramW6432", str(tmp_path))
    monkeypatch.setenv("ProgramFiles", str(tmp_path))
    monkeypatch.setenv("ProgramFiles(x86)", "")
    monkeypatch.setattr(
        binary_module,
        "glob",
        lambda pattern: [str(install_dir)] if "ParaView" in pattern else [],
    )

    assert binary_module.get_path_binary("paraview") == str(exe_path.resolve())
    assert binary_module.get_path_binary("paraview", is_include_file=False) == str(
        install_dir.resolve()
    )


def test_get_path_binary_scans_d_software_windows_fallback(monkeypatch, tmp_path):
    install_dir = tmp_path / "ParaView 6.1.0" / "bin"
    install_dir.mkdir(parents=True)
    exe_path = install_dir / "paraview.exe"
    exe_path.write_text("", encoding="utf-8")

    monkeypatch.setattr(binary_module, "os_name", "nt")
    monkeypatch.setattr(binary_module, "which", lambda _: None)
    monkeypatch.setenv("ProgramW6432", "")
    monkeypatch.setenv("ProgramFiles", "")
    monkeypatch.setenv("ProgramFiles(x86)", "")
    monkeypatch.setattr(
        binary_module,
        "glob",
        lambda pattern: [str(install_dir)] if pattern.startswith("D:/Software") else [],
    )

    assert binary_module.get_path_binary("paraview") == str(exe_path.resolve())

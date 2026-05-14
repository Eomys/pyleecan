from importlib import import_module

from pyleecan.Functions.ParaView.resolve_result_file import resolve_result_file

build_script_module = import_module(
    "pyleecan.Functions.ParaView.build_paraview_render_script"
)
launch_module = import_module("pyleecan.Functions.ParaView.launch_paraview")
render_module = import_module("pyleecan.Functions.ParaView.render_vtu_screenshot")


def test_resolve_result_file_selects_latest_step(tmp_path):
    result_dir = tmp_path / "elmer"
    result_dir.mkdir()
    (result_dir / "step_t0001.vtu").write_text("", encoding="utf-8")
    (result_dir / "step_t0003.vtu").write_text("", encoding="utf-8")
    (result_dir / "step_t0002.vtu").write_text("", encoding="utf-8")

    assert resolve_result_file(result_dir).endswith("step_t0003.vtu")


def test_build_paraview_render_script_includes_requested_metadata(tmp_path):
    script = build_script_module.build_paraview_render_script(
        input_path=tmp_path / "step_t0003.vtu",
        array_name="Magnetic Flux Density",
        output_path=tmp_path / "shot.png",
        component="Magnitude",
        time_index=-1,
        image_size=(1200, 900),
    )

    assert "Magnetic Flux Density" in script
    assert "shot.png" in script
    assert "Magnitude" in script
    assert "ImageResolution=[image_width, image_height]" in script


def test_launch_paraview_uses_resolved_binary_and_file(monkeypatch, tmp_path):
    result_file = tmp_path / "step_t0001.vtu"
    result_file.write_text("", encoding="utf-8")
    calls = {}

    monkeypatch.setattr(launch_module, "get_path_binary", lambda _: "C:\\ParaView\\paraview.exe")

    def fake_popen(cmd):
        calls["cmd"] = cmd
        return cmd

    monkeypatch.setattr(launch_module.subprocess, "Popen", fake_popen)

    launch_module.launch_paraview(result_file)

    assert calls["cmd"] == ["C:\\ParaView\\paraview.exe", str(result_file.resolve())]


def test_render_vtu_screenshot_falls_back_to_pvbatch(monkeypatch, tmp_path):
    result_file = tmp_path / "step_t0005.vtu"
    result_file.write_text("", encoding="utf-8")
    output_file = tmp_path / "render.png"
    calls = {}

    monkeypatch.setattr(
        render_module, "resolve_result_file", lambda *_args, **_kwargs: str(result_file)
    )
    monkeypatch.setattr(
        render_module,
        "build_paraview_render_script",
        lambda **_kwargs: "print('render')\n",
    )

    def fake_get_path_binary(name):
        if name == "pvpython":
            return None
        if name == "pvbatch":
            return "C:\\ParaView\\pvbatch.exe"
        return None

    def fake_run(cmd, check):
        calls["cmd"] = cmd
        calls["check"] = check
        return None

    monkeypatch.setattr(render_module, "get_path_binary", fake_get_path_binary)
    monkeypatch.setattr(render_module.subprocess, "run", fake_run)

    resolved_output = render_module.render_vtu_screenshot(
        result_path=result_file,
        array_name="B",
        output_path=output_file,
    )

    assert calls["cmd"][0] == "C:\\ParaView\\pvbatch.exe"
    assert calls["cmd"][1].endswith(".py")
    assert calls["check"] is True
    assert resolved_output == str(output_file.resolve())

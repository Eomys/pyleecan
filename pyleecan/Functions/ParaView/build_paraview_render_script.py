def build_paraview_render_script(
    input_path,
    array_name,
    output_path,
    component="Magnitude",
    time_index=-1,
    image_size=(1600, 1200),
):
    """Build a pvpython/pvbatch script that renders a VTU/VTK screenshot."""

    width, height = image_size
    component_value = "" if component is None else str(component)

    return f"""from pathlib import Path
from paraview import servermanager
from paraview.simple import *

input_path = {str(input_path)!r}
array_name = {str(array_name)!r}
output_path = {str(output_path)!r}
component_name = {component_value!r}
time_index = {int(time_index)}
image_width = {int(width)}
image_height = {int(height)}

Path(output_path).parent.mkdir(parents=True, exist_ok=True)

reader = OpenDataFile(input_path)
if reader is None:
    raise RuntimeError(f"Unable to open ParaView data file: {{input_path}}")

UpdatePipeline()
animation_scene = GetAnimationScene()
animation_scene.UpdateAnimationUsingDataTimeSteps()
timesteps = list(getattr(reader, "TimestepValues", []))
if timesteps:
    if time_index < 0:
        resolved_time_index = len(timesteps) - 1
    else:
        resolved_time_index = min(time_index, len(timesteps) - 1)
    animation_scene.AnimationTime = timesteps[resolved_time_index]
    UpdatePipeline(time=timesteps[resolved_time_index], proxy=reader)

dataset = servermanager.Fetch(reader)
association = None
data_array = None
resolved_array_name = array_name

point_data = dataset.GetPointData()
cell_data = dataset.GetCellData()


def _find_candidate_arrays(data_collection, collection_name):
    candidate_list = []
    if data_collection is None:
        return candidate_list

    for index in range(data_collection.GetNumberOfArrays()):
        name = data_collection.GetArrayName(index)
        if not name:
            continue
        array = data_collection.GetArray(index)
        if array is None:
            continue
        candidate_list.append((collection_name, name, array))

    return candidate_list


if resolved_array_name not in ("", "None", "auto", "Auto", "AUTO"):
    if point_data is not None:
        data_array = point_data.GetArray(resolved_array_name)
        if data_array is not None:
            association = "POINTS"
    if association is None and cell_data is not None:
        data_array = cell_data.GetArray(resolved_array_name)
        if data_array is not None:
            association = "CELLS"
else:
    candidate_list = _find_candidate_arrays(point_data, "POINTS")
    candidate_list.extend(_find_candidate_arrays(cell_data, "CELLS"))

    preferred_tokens = [
        "magnetic flux density e",
        "magnetic flux density",
        "current density",
        "displacement",
        "potential",
    ]

    selected = None
    for token in preferred_tokens:
        for candidate in candidate_list:
            if token in candidate[1].lower():
                selected = candidate
                break
        if selected is not None:
            break

    if selected is None and candidate_list:
        selected = candidate_list[0]

    if selected is not None:
        association, resolved_array_name, data_array = selected

if association is None:
    raise RuntimeError(
        f"Array '{{array_name}}' was not found in point or cell data for {{input_path}}"
    )

render_view = CreateView("RenderView")
render_view.ViewSize = [image_width, image_height]
render_view.InteractionMode = "2D"

display = Show(reader, render_view)
display.Representation = "Surface"

number_of_components = data_array.GetNumberOfComponents()
if number_of_components <= 1 or component_name in ("", "None"):
    ColorBy(display, (association, resolved_array_name))
else:
    ColorBy(display, (association, resolved_array_name, component_name))

display.SetScalarBarVisibility(render_view, True)
display.RescaleTransferFunctionToDataRange(True, False)
render_view.ResetCamera()
Render()
SaveScreenshot(output_path, render_view, ImageResolution=[image_width, image_height])
"""

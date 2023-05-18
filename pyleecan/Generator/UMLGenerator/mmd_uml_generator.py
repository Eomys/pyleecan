from os.path import dirname, abspath, normpath, join
from os import listdir, getcwd
from Diagram import Diagram

"""
This script generate UMLs thanks to the class diagram feature of the mermaid library 
(see https://mermaid-js.github.io/mermaid/#/classDiagram to learn more about it).
This python script generates mermaid code stored in .mmd files in path_to_pyleecan/UMLs/code.
Then, it uses the mermaid-cli package (https://github.com/mermaid-js/mermaid-cli) to convert these .mmd
files into graphical views of the diagrams as .svg files, stored in path_to_pyleecan/UMLs/svg.
The mermaid-cli package should be installed before running this scipt.

Installation process:

    - pip install mermaid

    - Install Node.js and npm from https://nodejs.org (npm comes with Node.js
    in the Windows installer). Add Node.js to the system path.
    
    - From the root folder of pyleecan (where the files package.json and package-lock.json are located),
    run the command "npm ci". This should install all the required node modules in a node_module folder
    
    - In VSCode, a debug configuration can be added to launch.json to generate UMLs as follows :
        {
            "name": "Python: Code gen (UML)",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/pyleecan/Generator/UMLGenerator/mmd_uml_generator.py",
            "console": "integratedTerminal"
        },
        
    - It may be necessary to allow the execution of powershell scripts. To do this on windows 11, go to
    Settings > Update and safety > Developpers space and check the box :
    "Modify execution policy to allow the execution of local unsigned Powershell scipts
    and require a signature for remote scripts"
    (after generating the UML you can uncheck this)

If the generation of .svg file fails, it is still possible to use the .mmd files to see the diagrams.
Here are two solutions:
    - Copy/paste the content of the .mmd file into the mermaid live website (https://mermaid.live)
    - Put the content of the .mmd file into a mermaid tag in a markdown (.md) file and use a 
    markdown preview that support mermaid (for exemple in VSCode with the extension
    Markdown Preview Mermaid Support https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)
"""

DOC_DIR = normpath(abspath(join(dirname(__file__), "..", "ClassesRef")))


def main():
    # Generate the UML of each main folder (Machine, Geometry, Slot...)
    list_dir = [join(DOC_DIR, folder_name) for folder_name in listdir(DOC_DIR)]
    for path in list_dir:
        Diagram([path]).draw_diagram()

    # Full UML
    Diagram([DOC_DIR], name="Pyleecan").draw_diagram()

    # Only machine classes (without component like Laminations)
    Diagram(
        [DOC_DIR], name="only_machines", parent_class_name="Machine", composition=False
    ).draw_diagram()

    # Only lamination classes (without component like Slots)
    Diagram(
        [DOC_DIR],
        name="only_laminations",
        parent_class_name="Lamination",
        composition=False,
    ).draw_diagram()


if __name__ == "__main__":
    main()

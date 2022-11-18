import os
from os.path import abspath, dirname, join, isdir, isfile
from shutil import rmtree, copy
import re
from datetime import datetime
import click

TAB = "    "
TAB7 = TAB + TAB + TAB + TAB + TAB + TAB + TAB


def generate_executable(
    start=1,
    stop=6,
    new_version=0,
    branch="master",
    is_clean_end=False,
    is_debug=False,
    project_path=None,
):
    """Function to create a new exe for pyleecan
    Step 1: Clone latest version of pyleecan
    Step 2: Clean up folder
    Step 3: Update software version (if needed)
    Step 4: Create virtual env with requirements
    Step 5: Generate GUI exe
    Step 6: Generate installer

    Parameters
    ----------
    start : int
        To select the first step to run
    stop : int
        To select the last step to run
    new_version : int
        0: Use current version, 1: ask before update, 2: Update
    branch : str
        Branch to clone
    is_clean_end : bool
        To delete the folder at the end
    is_debug : bool
        To add a debug console in pyinstaller
    project_path : str
        Path to the folder to use to create the exe
    """

    start_time = datetime.now()

    ## Path definition
    # Path to main folder (clone + generation)
    PRJ_PATH = (
        project_path
        if project_path
        else join(os.getenv("APPDATA"), "PYLEECAN_EXE_GENERATION").replace("\\", "/")
    )
    # Path to script containing the software version
    version_path = join(PRJ_PATH, "pyleecan", "__init__.py").replace("\\", "/")
    # Path to the class folder (for hidden import in exe)
    class_path = join(PRJ_PATH, "pyleecan", "Classes")
    # Path to define the environment
    ENV_PATH = join(PRJ_PATH, "Exenv").replace("\\", "/")
    # Path to result forder of pyinstaller
    dist_path = join(PRJ_PATH, "dist", "Pyleecan").replace("\\", "/")
    # Path of the license file
    license_path = join(PRJ_PATH, "LICENSE").replace("\\", "/")
    # Repository link
    REPO_LINK = "https://github.com/Eomys/pyleecan.git"
    # REPO_LINK = "https://github.com/EOMYS-Public/pyleecan.git"
    # Path to installer program
    iscc_path = "C:/Program Files (x86)/Inno Setup 6/iscc.exe"
    # Path to installer generation script
    install_path = join(PRJ_PATH, "Exe_gen", "pyleecan.iss").replace("\\", "/")
    install_path_2 = join(PRJ_PATH, "pyleecan.iss").replace("\\", "/")
    spec_path = join(PRJ_PATH, "Exe_gen", "pyleecan.spec")  # Original path
    spec_path_2 = join(PRJ_PATH, "pyleecan.spec")  # To move the spec file
    out_path = join(PRJ_PATH, "Output", "Pyleecan Setup.exe").replace("\\", "/")

    print("Starting Pyleecan exe generation...")

    ###################
    # 1 Folder setup
    ###################
    print("###################################")
    if start <= 1 and stop >= 1:
        print("Step 1: Setting up working directory")
        if isdir(PRJ_PATH):
            print("Deleting previous folder " + PRJ_PATH)
            # os.system('Rmdir /S /Q "' + PRJ_PATH + '"')
            rmtree(PRJ_PATH)
        # Clone pyleecan
        os.system("git clone -b " + branch + " " + REPO_LINK + " " + PRJ_PATH)
    else:
        print("Skipping step 1: Folder Setup")

    ####################
    # 2 : Folder cleanup
    ####################
    if start <= 2 and stop >= 2:
        print("Step 2: Cleaning up working directory")
        print("Removing " + join(PRJ_PATH, "Tests"))
        rmtree(join(PRJ_PATH, "Tests"))
        print("Removing " + join(PRJ_PATH, "Tutorials"))
        rmtree(join(PRJ_PATH, "Tutorials"))
        # Delete all .ui files
        for root, dirs, files in os.walk(join(PRJ_PATH, "pyleecan", "GUI")):
            for name in files:
                if name[-3:] == ".ui" or name == "gen_list.json":
                    print("Deleting " + join(root, name))
                    os.remove(join(root, name))
    else:
        print("Skipping step 2: Folder Cleanup")

    ##############
    # Get version
    ##############
    os.chdir(PRJ_PATH)
    version_file = open(version_path, "r")
    version = None
    for line in version_file:
        if re.match("^__version__", line):
            if line.count("'") > 0:
                version = line[line.index("'") + 1 : -2]
            else:
                version = line[line.index('"') + 1 : -2]
    version_file.close()
    print("\n###################################")
    print("Current version of the software is " + version)

    ###################
    # 3 Update software version
    ###################
    if start <= 3 and new_version > 0 and stop >= 3:
        print("Step 3: Updating software version...")
        S_version = version.split(".")
        version = ".".join(S_version[:-1]) + "." + str(int(S_version[-1]) + 1)
        if new_version > 1:
            answer = "y"
        else:
            answer = input("Update it to " + version + " ? (y/n)")
        if answer.lower() == "y":
            edit_line_in_file(
                version_path,
                "^__version__",
                '__version__ = "' + version + '"',
            )
            # Commit / push new version
            os.system("git add " + version_path)
            os.system('git commit -m "Updating version for release"')
            os.system("git push origin " + branch)
        else:
            input("Please update (and commit) version")
    else:
        print("Skipping step 3: Version Update")

    print("\n###################################")

    ###################
    # 4 Set environment
    ###################
    if start <= 4 and stop >= 4:
        print("Step 4: Setting Virtual env for release...")

        # Creating Python env in which to install needed package
        os.system("python -m venv " + ENV_PATH)
        # Updating packages
        os.system(join(ENV_PATH, "Scripts", "pip") + " install -U pip")
        os.system(join(ENV_PATH, "Scripts", "pip") + " install -U pyinstaller==5.1")
        os.system(join(ENV_PATH, "Scripts", "pip") + " install gmsh-sdk")
        # Installing required packages
        os.system(
            join(ENV_PATH, "Scripts", "pip")
            + " install -r "
            + join(PRJ_PATH, "requirements-full.txt")
        )
    else:
        print("Skipping step 4: environment setup")

    print("\n###################################")
    ###################
    # 5 Generate GUI .exe with Pyinstaller
    ###################
    if start <= 5 and stop >= 5:
        print("Step 5: Start .exe generation with pyinstaller...")
        copy(spec_path, spec_path_2)
        edit_line_in_file(
            spec_path_2,
            "^          debug=",
            "          debug=" + str(is_debug) + ",",
        )
        edit_line_in_file(
            spec_path_2,
            "^          console=",
            "          console=" + str(is_debug) + ",",
        )
        # Add direct import of the classes
        import_txt = "             hiddenimports=[\n"
        for root, dirs, files in os.walk(class_path):
            for name in files:
                if name[-3:] == ".py" and "__init__" not in name:
                    path = join(root, name).replace("\\", "/")
                    path = path[: path.index(".")]
                    path = path.replace("/", ".")
                    path = path[len(PRJ_PATH) + 1 :]
                    import_txt += TAB7 + "'" + path + "',\n"
        edit_line_in_file(
            spec_path_2,
            "^ *hiddenimports=",
            import_txt[:-1],
        )
        # Generating the executable
        os.system(
            join(ENV_PATH, "Scripts", "pyinstaller")
            + " "
            + spec_path_2
            + " --noconfirm"
        )
    else:
        print("Skipping step 5: Pyinstaller")

    print("\n###################################")
    ###################
    # 6 Generate installer
    ###################
    if start <= 6 and stop >= 6:  # installer
        # Editing installer generation script
        print("Step 6: Start installer generation...")
        copy(install_path, install_path_2)
        edit_line_in_file(
            install_path_2,
            "^#define MainPath",
            '#define MainPath "' + dist_path + '"',
        )
        edit_line_in_file(
            install_path_2,
            "^#define MyAppVersion",
            '#define MyAppVersion "' + version + '"',
        )
        edit_line_in_file(
            install_path_2,
            "^LicenseFile=",
            "LicenseFile=" + license_path,
        )
        files_str = 'Source: "{#MainPath}\*"; DestDir: "{app}"; Flags: ignoreversion\n'
        for name in os.listdir(dist_path):
            if isdir(join(dist_path, name)):
                files_str += (
                    'Source: "{#MainPath}/'
                    + name
                    + '/*"; DestDir: "{app}/'
                    + name
                    + '"; Flags: ignoreversion recursesubdirs\n'
                )
        edit_line_in_file(
            install_path_2,
            "^\[Files\]",
            "[Files]\n" + files_str,
        )

        # Generate Installer exe
        try:
            cmd = '"' + iscc_path + '" ' + install_path_2
            if os.system(cmd) != 0:
                raise ("Error while running " + cmd + "\nPlease install Inno Setup")
        except Exception as e:
            print("Please install Inno Setup\n" + str(e))
        # Rename exe
        exe_name = "Pyleecan v" + version + " installer.exe"
        out_path2 = join(dirname(out_path), exe_name)
        print("Renaming " + out_path + " to " + out_path2)
        if isfile(out_path2):
            os.remove(out_path2)
        os.rename(out_path, out_path2)

        # Clean folder
        if isdir(PRJ_PATH) and is_clean_end:
            print("Deleting folder " + PRJ_PATH)
            os.system('Rmdir /S /Q "' + PRJ_PATH + '"')
    else:
        print("Skipping step 6: Installer")

    print("Exceution time: " + str(datetime.now() - start_time))


def edit_line_in_file(file_path, pattern, substring):
    """Edit every line that matches the pattern to substring
    @param[in] file_path Path to the file to edit
    @param[in] pattern A regex to find the lines to edit
    @param[in] substring String to replace the old one
    """

    Modif = 0  # To be sure that we edit something

    # Check that the file to edit exist
    if not isfile(file_path):
        raise FileNotFoundError("The given path doesn't lead to a file")

    # Create a new file (file_name.tmp) for the new version (avoid to change
    # the original file)
    out_file_path = file_path + ".tmp"
    out_file = open(out_file_path, "w")

    # Generation of the edited version of the file
    with open(file_path) as edit_file:
        for line in edit_file:
            # Try to modify every line then add it to the tmp file
            # We count the number of changes we make
            if re.match(pattern, line):
                Modif += 1
                out_file.write(substring + "\n")
            else:
                out_file.write(line)
        out_file.close()

    # Check that there were some changes made
    if Modif > 0:
        # We replace the original file by the new one
        os.remove(file_path)
        os.rename(out_file_path, file_path)
        print(str(Modif) + " change(s) (" + substring + ") made in " + file_path)
        if Modif > 1:  # More than one modification: check
            print(
                "More than one modification in the file, please check that \
            it's normal"
            )
            input("Press <ENTER> to continue")
    else:
        # There was no change so we remove the new version
        os.remove(out_file_path)
        print("############\nWarning: No change in " + file_path + "\n######")


if __name__ == "__main__":
    generate_executable()

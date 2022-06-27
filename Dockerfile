FROM mcr.microsoft.com/windows:20H2
ENV chocolateyUseWindowsCompression=false
RUN @powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
RUN choco config set cachelocation C:\chococache
RUN choco feature enable -n allowGlobalConfirmation
RUN choco install python3 --version=3.8.6 --params "/InstallDir:C:\\Python"
RUN set PATH="/c/Python:/c/Python/Scripts:/c/Python/Lib/site-packages:$PATH"
RUN choco install femm
RUN choco install git
RUN choco install gmsh
WORKDIR C:\\app

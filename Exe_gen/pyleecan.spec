# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(3000)
block_cipher = None


a = Analysis([SPECPATH + '/pyleecan/run_GUI.py'],
             pathex=[SPECPATH],
             binaries=[],
             datas=[(SPECPATH + '\\Exenv\\Lib\\site-packages\\pyvista','.\\pyvista'),
                    (SPECPATH + '\\Exenv\\Lib\\site-packages\\scipy','.\\scipy'),
                    (SPECPATH + '\\Exenv\\Lib\\site-packages\\scipy.libs','.\\scipy.libs'),
                    (SPECPATH + '\\Exenv\\Lib\\site-packages\\matplotlib','.\\matplotlib'),
					(SPECPATH + '\\Exenv\\Lib\\site-packages\\vtkmodules','.\\vtkmodules'),
                    (SPECPATH + '\\Exenv\\Lib\\site-packages\\pyzmq.libs','.\\pyzmq.libs'),
					(SPECPATH + '\\Pyleecan\\Data','.\\pyleecan\\Data'),
					(SPECPATH + '\\Pyleecan\\Classes\\Class_Dict.json','.\\Pyleecan\\Classes')],
             hiddenimports=[# Leave first line empty for Import of pyd
                            'pyleecan.GUI.Dialog.DMachineSetup.DMachineSetup',
							'pyleecan.GUI.Dialog.DMatLib.DMatLib',
                            'pyleecan.GUI.Tools.SidebarWindow',
                            'pyleecan.GUI.Tools.MachinePlotWidget',
                            'pyleecan.Functions.GMSH.draw_GMSH',
                            'pyleecan.GUI.Tools.WTreeEdit.WTreeEdit',
                            'pyleecan.GUI.Tools.GuiOption.WGuiOption'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Pyleecan',
          debug=True,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          icon= SPECPATH + '\\Exe_gen\\pyleecan_64.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Pyleecan')

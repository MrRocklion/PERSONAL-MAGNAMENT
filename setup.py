import sys
import os
from cx_Freeze  import setup, Executable
files=["config.json","ui_main.py","ico.ico"]
base = ""
if sys.platform == 'win32':
    base = "Win32GUI"

if sys.platform == 'win64':
    base = "Win64GUI"
exe = Executable(script="main.py",base=base,icon="ico.ico")
setup(
    name= "Personal Magnament",
    version= "1.0",
    description="Aplicacion para gestionar ingreso y salidas del personal",
    author="David Diaz",
    options={'build_exe':{'include_files':files}},
    executables=[exe]
)
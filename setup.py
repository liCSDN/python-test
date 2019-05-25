#encoding: utf-8

#from cx_Freeze import setup,Executable
import sys
from cx_Freeze import *
import os
os.environ['TCL_LIBRARY'] = r'D:\Program Files\python\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'D:\Program Files\python\tcl\tk8.6'

include_files=[
    r'D:\Program Files\python\DLLs\tcl86t.dll',
    r'D:\Program Files\python\DLLs\tk86t.dll'
]

build_exe_options = {"packages":["os","tkinter"],"include_files":include_files}

base = None
if sys.platform == "win32":
    base = "Win32GUI"
setup(

    name = " Aron",
    version = "1.0",
    description = "weather - meishan",
    options = {"build_exe":build_exe_options},
    executables = [Executable("tweather.py",base=base)]
)
#打包命令
#python setup.py bdist_msi

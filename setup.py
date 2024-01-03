import cx_Freeze
import sys
import os 

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\gkumar\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\gkumar\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("main.py", base=base, icon="Desktop_Icon.ico")]

cx_Freeze.setup(
    name="Attendance marking using multiple face recognition Software",
    options={
        "build_exe": {
            "packages": ["tkinter", "os"],
            "include_files": [
                "Desktop_Icon.ico",
                "tcl86t.dll",
                "tk86t.dll",
                "config.ini",
                "public",
                "data",
                "database",
                "attendance_report"
            ]
        }
    },
    version="1.0",
    description="Attendance marking system using multiple face recognition system | Developed By Ganesh Kumar",
    executables=executables
)

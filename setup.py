
from cx_Freeze import Executable, setup

# base = "Console"
# executables = [Executable("data_prediction.py", base=base)]
executables = Executable(script="data_prediction.py", icon="pyc.ico")

setup(
    name="Data_prediction&plotting",
    executables=[executables],
    options={
        "build_exe": {
            "packages": [
                "plotly.offline",
                "plotly.graph_objs",
                "re",
                "random",
                "pickle",
                "collections",
                "xlrd",
                "os",
            ],
            "excludes": [
                "pandas",
                "matplotlib",
                "numpy",
            ],
            "optimize": 2,
            "includes": ["idna.idnadata"],
            "include_files": ["pyc.ico"],
        }
    },
    version="0.1",
    description="Data prediction & plotting using Python and Plotly",
)

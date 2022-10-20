import sys

from cx_Freeze import setup, Executable

setup( name = "Translator", version = "1.1",

       description = "pathAI",

       executables = [Executable("main.py",

                                 base = "Win32GUI")])
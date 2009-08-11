from distutils.core import setup
import py2exe

py2exe_options = {
    "compressed": 1,
    "optimize": 2,
    "bundle_files": 1,
    "packages": ['email'],
    }

setup(
    options = {"py2exe": py2exe_options},
    console = [
        {"script" : "skype2prowl.py"}],
    zipfile = None,
    )

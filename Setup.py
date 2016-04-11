    #python setup.py py2exe

from distutils.core import setup
import py2exe

options = {
   #     "bundle_files": 1,                 # create singlefile exe
   #     "compressed"  : 1,                 # compress the library archive
   #     "optimize"    : 2,                 # do optimize
    }

setup(
        console = ["restime.py"],             # py file to create exe
        options = {"py2exe" : options},
        zipfile = None                     # append zip-archive to the executable
    )

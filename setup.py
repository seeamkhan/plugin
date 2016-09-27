"""This is setup file for py2exe.
Using this file you can create a single exe file for a python script.
All you need to change the python file name in this file and save.
Then open any terminal and run: 'python setup.py py2exe'"""

import sys
try:
    import py2exe
except:
    raw_input('Please install py2exe first...')
    sys.exit(-1)

from distutils.core import setup
import shutil

sys.argv.append('py2exe')

setup(
    options={
        'py2exe': {'bundle_files': 1, 'compressed': True}
    },
    console=[
        {'script': "plugin-check.py"}
    ],
    zipfile=None,
)

shutil.move('dist\\plugin-check.exe', '.\\plugin-check.exe')
shutil.rmtree('build')
shutil.rmtree('dist')
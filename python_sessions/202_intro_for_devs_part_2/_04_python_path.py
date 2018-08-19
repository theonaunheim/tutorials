'''
             _   _                               _   _     
 _ __  _   _| |_| |__   ___  _ __    _ __   __ _| |_| |__  
| '_ \| | | | __| '_ \ / _ \| '_ \  | '_ \ / _` | __| '_ \ 
| |_) | |_| | |_| | | | (_) | | | | | |_) | (_| | |_| | | |
| .__/ \__, |\__|_| |_|\___/|_| |_| | .__/ \__,_|\__|_| |_|
|_|    |___/                        |_|                    

'''
##=============================================================================
## Generally
##=============================================================================
##
## See also: https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH
##
## If we want to import a Python package or module, where should we look?
## Obviously, it would be wasteful and inefficient to search the entire
## filesystem for a single .py file.
##
## Python only looks for Python files on the PYTHONPATH and in the current
## working directory. The PYTHONPATH is a list of of folders on your system.
## Note: 'os' is for interacting with your operating system. 'sys' is for
## interacting with your interpreter.

import os
import sys

for directory in sys.path:
    print(directory)

# You probably noticed that there is a blank line in the above signifying
# the presence of an empty string.
print(sys.path[0])

## When you enter the REPL with the 'python' command, this first element
## is blank, signifying no addition to the PYTHONPATH. If you were to
## execute the interpreter by executing a particular script, the folder
## containing the the script is added to the PYTHONPATH.
##
## For example, if we were to execute:
##
##     python static/_03_/module_1.py
##
## That module would be able to import other items in its folder.

# If you ever want to add an arbitrary folder to the path ...
print('\n'.join(sys.path))

# Crossplatform way to get home folder is:
home_folder = os.path.expanduser('~')
documents_folder = os.path.join(home_folder, 'Documents')

# You can append an item to the path ...
sys.path.append(documents_folder)

# And then go from there.
print('\n'.join(sys.path))

##=============================================================================
## Questions
##=============================================================================

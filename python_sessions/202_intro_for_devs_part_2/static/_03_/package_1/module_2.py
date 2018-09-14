from . import module_3
from .. import module_1
from ..._02_ import package_1

print('''
We just did a relative import that added static._02_.module_1
and static._01_.package_1 to the module_2 namspace. We used the
following commands

# Go up a directory and import module 1.
from .. import module_1

# Go up 2 directories, go down one directory into _01_ and import.
from ..._01_ import package_1

# Imports a module from the same folder.
from . import module_3

''')

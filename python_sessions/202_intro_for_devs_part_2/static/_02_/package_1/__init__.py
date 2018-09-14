'''Package docstring goes in __init__.py.

Generally it's a good idea to only use the __init__.py
file to import submodules into the namespace to build
a clean API. That said you can put variables, classes, 
function definitions, or whatever you want in here.

'''

from . import module_2
from .module_3 import api_func


# Functions are executed
print('Importing the package executes __init__.py')

# Here's a class.
class MyClass(object):

    def method(self):
        print('I am a method of a class defined in package_1')

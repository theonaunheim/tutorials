'''
                  _                                           _ 
 _ __   __ _  ___| | ____ _  __ _  ___  ___    __ _ _ __   __| |
| '_ \ / _` |/ __| |/ / _` |/ _` |/ _ \/ __|  / _` | '_ \ / _` |
| |_) | (_| | (__|   < (_| | (_| |  __/\__ \ | (_| | | | | (_| |
| .__/ \__,_|\___|_|\_\__,_|\__, |\___||___/  \__,_|_| |_|\__,_|
|_|                         |___/                               
                     _       _           
 _ __ ___   ___   __| |_   _| | ___  ___ 
| '_ ` _ \ / _ \ / _` | | | | |/ _ \/ __|
| | | | | | (_) | (_| | |_| | |  __/\__ \
|_| |_| |_|\___/ \__,_|\__,_|_|\___||___/
                                         

'''
##=============================================================================
## Generally
##=============================================================================
##
## Often times it is easier to split up a program into discrete
## organizational units of code. In Python, these units take the
## form of modules:
##
## https://docs.python.org/3/tutorial/modules.html
##
## and packages:
##
## https://docs.python.org/3/tutorial/modules.html#packages
##
##=============================================================================
## Modules
##=============================================================================
##
## Modules are simply plaintext files with ending with the a '.py'
## extension. The code variables, classes, code, etc. in these
## modules can be triggered by either executing the module in your
## shell:
##
##     python my_module.py
##     python my_module.py argument_1
##
## Or by accessing the module through from inside another piece
## of Python code. The module's name will simply be the name of
## the file but without the '.py' extension:
##
## You can then use the code in these modules
##
## /static                        (Folder)
##     /_02_                      (Folder)
##         module_1.py            (Python file)

import static._02_.module_1 as module_1

## Note: notice that modules are subject to the same rules as Python variables
## for the most part (e.g. cannot start with a number, cannot contain anything
## other than alphanumerics and underscores).
##
## This has a variety of effects:
##
## First, it establishes a namespace for the module.
## 
## Because everything is an object, we use '.' to access internal elements of
## the module as attributes. We use these attributes to help organize our code
## instead of using a namespace operator, like one my use '::' in C++.
##
## Second, it executes the code inside the module.
##
## In this case, it executes a print function, defines
## a variable a variable, defines a function. Note:
## Python has no such thing as forward declarations.
##
## Take a look at module.py and see what just happened.

# Trigger module function with local argument.
module_1.mod_func('Local text')

# Print module level variable
print(module_1.mod_var)

# Because modules are objects, you can use them like other objects.
# You can place them in containers
import os
import webbrowser

module_list = [os, webbrowser]

for module in module_list:
    print(module.__file__)


# You can pass them to functions
def function(module):
    print(module.__doc__)


# Executing function.
function(module_1)

# And you can assign names within the namespace
module_1.arb_var = 'Arbitrary variable is arbitrary.'

# Printing variable.
print(module_1.arb_var)

##=============================================================================
## Packages
##=============================================================================
##
## Packages are folders with a file called '__init__.py' inside them. 
## They are generally used to organize modules and are used in much
## the same fashion.
##
## Though modules are not generally executed directly, if a file called
## '__main__.py' is added to them, they can be executed by using the
## '-m' argument:
##
##     python -m my_package
##
## Similarly, they may also be accessed from inside of other bits of
## Python code. The module's name will simply be the name of the folder.
##
## You can then use the code in these modules
##
## /static                        (Folder)
##     /_01_                      (Folder)
##         /package_1             (Package)
##             __init__.py        (Package Required File)
##             module_2.py        (Module)
##             module_3.py

import static._02_.package_1 as package_1

## Again, this has a variety of effects.
##
## First, it imports the package into this paticular namespace.
##
## Second, it executes the __init__.py.
##
## Third, this __init__.py in turn can import additional modules.
##
## Take a look at the source code of the module we imported!

# We can directly access items in the package code.
instance = package_1.MyClass()
instance.method()

# We can access modules that were added in their entirity to the package
package_1.module_2.other_func()

# We can access functions that were imported into the package.
package_1.api_func()

# Like modules, we can directly interact with the package namespace
package_1.arb_var = 'Arbitrary variable is arbitrary'
print(package_1.arb_var)

##=============================================================================
## Questions?
##=============================================================================

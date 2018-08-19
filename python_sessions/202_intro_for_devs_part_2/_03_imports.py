r'''_02_imports.py
 _                            _       
(_)_ __ ___  _ __   ___  _ __| |_ ___ 
| | '_ ` _ \| '_ \ / _ \| '__| __/ __|
| | | | | | | |_) | (_) | |  | |_\__ \
|_|_| |_| |_| .__/ \___/|_|   \__|___/
            |_|                       

'''
##=============================================================================
## Generally
##=============================================================================
##
## So these modules are handy and all, but how do we make them
## visible to other modules? The answer is to use imports. The
## use of import statements allows you to a) add entire modules
## so that you can access their namespaces, or b) pull items
## from modules into your current namespace.
##
## https://docs.python.org/3/reference/import.html
##
## Programs all start out with a top-level namespace, which is
## designated as '__main__'.
##
## If the interpreter is run from the REPL by:
##
##    python
##
## the __main__ namespace will be empty except for builtin
## commands.
##
## If the interpreter is used to run a script, like:
##
##     python program.py
##
## the __main__ namespace will include the items in the function namespace.
##
## 

print('The __name__ of the top-level namespace: ' + __name__ + '.')

## Side note: __name__ will resolve to __main__ in the top-level
## namespace. It will resolve to the module name in all other
## namespaces. Don't take my word for it. Execute this module. Then try
## the above code in the interpreter. Does the result differ?

import __main__

## You can then add additional namespaces through use of the import
## statement. These are closely linked with the concept of modules. Here
## we import a module and access its namespace.

import static._03_.module_1

# Which allows us to read that namespace (essentially executing it).
rv = static._03_.module_1.mod_1_func()
print('Return value is ' + rv)
print(
    'We can also access names like ' +
     static._03_.module_1.arb_value
)

# And assign to that namespace.
static._03_.module_1.arb_value = 5

## In addition to importing entire namespaces, the import statement
## also has the ability to import a single class/function/name from
## another namespace. That way we can move certain items around
## for the sake of convenience. This uses the from X import Y syntax.

# Import a name from another namespace
from static._03_.module_1 import arb_value


# And use it within this namespace.
print(arb_value + 5)

## The final thing import statement allows for is setting aliases.
## To set a name at the time of import, use 'as' keyword syntax. For
## example we can create a shortned name for a namespace

import static._03_.module_1 as m1


# Which cuts down the typing we need to do.
m1.mod_1_func()

# Similarly we can set an alias when we import a single name.
from static._03_.module_1 import arb_value as av

print(av)

##=============================================================================
## Absolute imports
##=============================================================================
##
## See also: https://www.python.org/dev/peps/pep-0328/
##
## When importing packages, typically one imports in a manner that lists
## all the folders of the inport path. This is known as an absolute
## import. Note that if we are importing from the "part_2_writing_programs" 
## section we can import a module using the entire path given the following
## structure:
##
## /static                        (Folder)
##     /_03_                      (Folder)
##         /package_1             (Python package)
##             module_2.py        (Python module)

import static._03_.package_1.module_3

##=============================================================================
## Relavtive imports
##=============================================================================
##
## But what if we don't want to list the entire path? What if we just want
## to import a Python module from one folder up? Python also provides for
## relative imports which solves this problem with ease. If we were to run:
## 

import static._03_.package_1.module_2

##
## Which in turn contains the following Python source:
##
## from .. import module_1
## from ..._01_ import package_1
## from . import module_3
## 
## ... it would:
##
## Go up a directory and import module 1 like this:
##
## from .. import module_1
##
## Go up 2 directories, go down one directory into _01_ and import like this:
##
## from ..._02_ import package_1
##
## Imports a module from the same folder like this:
##
## from . import _00_intro
##
##=============================================================================
## Circular imports
##=============================================================================
##
## Unless you do something really stupid, Python is generally smart enough to
## recognize things that have already been imported and will refrain from
## importing them again.
##
##=============================================================================
## Questions?
##=============================================================================

'''
   _ __   __ _ _ __ ___   ___  ___
  | '_ \ / _` | '_ ` _ \ / _ \/ __|
  | | | | (_| | | | | | |  __/\__ \
  |_| |_|\__,_|_| |_| |_|\___||___/
'''
##============================================================================
## Generally
##============================================================================
##
## Note: In Python we use 'names' to store information. In Python, names are
## do not set aside memory--rather names are simply handles for a lookup table
## that is used at runtime. It is not strictly correct but for the purposes
## of this this presentation we will use the words 'variable' and 'name'
## interchangably.
##
## We use the equals ('=') operator to 'assign' or bind a Python object to a
## name. It looks like this:
my_variable = 5

# Which allows us to use that data (like with the print statement):
print(my_variable)

# However, the below is not the same as assigning a value.
# This is actually testing for equality ('==')!
5 == 3 + 2

# We can assign pretty much whatever we want to a variable, including other
# names.
new_variable = my_variable
print(new_variable)

# Python does not have a "const" keyword enforcing immutability at runtime.
# However, convention is to use all capital letters and respect the contract
CONSTANT_STR = "Please don't modify me at runtime. You will not make friends."
VALID_COMMANDS = ('Install', 'Remove', 'Repair')

## A name has to follow these rules:
##     1. It cannot have spaces (or other whitespace).
##     2. It can only contain letters, numbers, and underscores ('_').
##     3. It cannot start with a number.
##     4. It cannot be a keyword reserved by the Python language.

i_am_a_good_name = True

## 7_am_a_bad_name = 5
## i am also a b@d name = 5
## False = 'this will fail.'

##============================================================================
## A Puzzle!
##============================================================================
a = 17
b = a
a = 4
# b = ???

x = [4, 3, 2]
y = x
x.append(1)
# y = ???

##============================================================================
## Keywords (we will get to these in a bit)
##============================================================================
##
## False      class      finally    is         return
## None       continue   for        lambda     try
## True       def        from       nonlocal   while
## and        del        global     not        with
## as         elif       if         or         yield
## assert     else       import     pass       async
## break      except     in         raise      await
##
##============================================================================
## A few conventions
##============================================================================

# A foolish consistency is the hobgoblin of little minds ...
# PEP8 is the authoritative source: https://www.python.org/dev/peps/pep-0008/

# Modules are lower-case with underscores.
import csv

# Functions are lower-case with underscores.
def my_function():
    pass


# Variables are lower case with underscores.
variable_5 = True

# Classes are Pascal Case.
class PascalCase(object):
    pass


# Side note: Python does not enforce encapsulation, but convention dictates:
_private  = "Private variables/functions/methods start with an underscore."
public    = "Public variables/functions/methods need no underscore."
__mangled = "Double underscore prefix mangles the name (generally for OOP)."
__init__  = "Double underscore prefix + suffix should be reserved for Python."
continue_ = "Single underscore suffix is used to prevent name clashes."

##============================================================================
## Questions
##============================================================================

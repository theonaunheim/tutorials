'''
                         _   _             
  _____  _____ ___ _ __ | |_(_) ___  _ __  
 / _ \ \/ / __/ _ \ '_ \| __| |/ _ \| '_ \ 
|  __/>  < (_|  __/ |_) | |_| | (_) | | | |
 \___/_/\_\___\___| .__/ \__|_|\___/|_| |_|
                  |_|                      
 _                     _ _ _             
| |__   __ _ _ __   __| | (_)_ __   __ _ 
| '_ \ / _` | '_ \ / _` | | | '_ \ / _` |
| | | | (_| | | | | (_| | | | | | | (_| |
|_| |_|\__,_|_| |_|\__,_|_|_|_| |_|\__, |
                                   |___/ 

'''
##=============================================================================
## Generally
##=============================================================================
##
## Exception handling in Python is relatively simple and is done in
## a manner much like other programming languages with try/catch blocks.
## The difference for Python is that our blocks are delimited with
## indentation and the nomenclature is try/exception.
##
## For exception handling documentation:
## https://docs.python.org/3.6/tutorial/errors.html
##
## For a list of common exceptions:
## https://docs.python.org/3/library/exceptions.html

# This will raise an exception, stopping the entire script.
print(nonexistant_object)

# To field this NameError we use the following syntax:
try:
    print(nonexistant_object)
except NameError:
    print('NameError just happened.')

# This error will propagate up the call stack and will halt
# execution if not handled.
def function():
    print(nonexistant_object)

try:
    function()
except NameError:
    print('NameError just happened.')

# Exceptions are subclassed, and we can catch subclasses
# To catch all exceptions, you can:
try:
    print(nonexistant_object)
except Exception:
    print('An exception of any kind was caught.')

# As everything is an object, we have the ability to inspect
# our exceptions:
try:
    print(nonexistant_object)
except Exception as e:
    print(e.args)

# We can catch multiple errors in the same block:
try:
    print(nonexistant_object)
except NameError as e1:
    print('NameError occurred.')
except Exception as e2:
    print('A general exception occurred which was not a NameError.')

# We can add a finally statement.
try:
    print(nonexistant_object)
except NameError as e1:
    print('NameError occurred.')
finally:
    print('Finally it has happened to me right in front of my face.')

# We can reraise errors
try:
    print(nonexistant_object)
except NameError as e1:
    # can also just 'raise' without argument to do last error.
    raise e1 

# Lastly, we can capture multiple exceptions at the same time:
try:
    print(nonexistant_object)
except (NameError, FileNotFoundError) as e:
    print('NameError or FileNotFoundError occurred.')

# Caveat: unlike other compound statements, except clauses do not preserve
# variables after the except clause.
e

##=============================================================================
## Custom Exceptions
##=============================================================================

# You can create your own exceptions by subclassing
class VanityException(Exception):
    pass


# You can create your own exceptions by instantiating.
raise Exception('I am an exception of general type!')

##=============================================================================
## Questions
##=============================================================================

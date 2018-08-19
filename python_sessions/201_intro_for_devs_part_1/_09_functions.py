'''
   __                  _   _
  / _|_   _ _ __   ___| |_(_) ___  _ __  ___
 | |_| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 |  _| |_| | | | | (__| |_| | (_) | | | \__ \
 |_|  \__,_|_| |_|\___|\__|_|\___/|_| |_|___/

'''
##=============================================================================
## Functions
##=============================================================================
##
## See also: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
##
## Functions are the basis for all re-useable code. Luckily for us, Python
## makes functions stupid simple to design, use, and pass about. Like
## everything else, functions are first class objects that can be inspected and
## tinkered with.
##
## We define functions and methods with the 'def' keyword. Asynchronous
## functions and methods will have the 'async def' syntax.
##
## See also: https://docs.python.org/3/library/asyncio-task.html#coroutines
##
##=============================================================================
## Function definition
##=============================================================================
##
## A function will typically be defined like this:


def func_name(func_arg_1, func_arg_2, keyword_arg_3='default_value'):
    '''Docstring describing what function does.

       More information if needed. You name your arguments in the
       parentheses after the function name. You can then use those
       arguments in your function body.

    '''

    # Function body is indented where we do our work.
    print('Starting function body.')
    count = str(func_arg_1).zfill(2)
    total = str(func_arg_2).zfill(2)

    # A return value will immediately stop the function and return.
    if keyword_arg_3.lower() == 'rutabaga':
        print("This function does not accept root vegetables.")
        return "You get nothing! You lose! Good day, sir."

    print("This function is not a rutabaga. We can proceed.")
    print("It was not short-circuited by the conditional return.")

    return_val = 'We have eaten ' + count + ' of ' + total + ' ' + keyword_arg_3

    # We then supply our return value. You can only supply one return
    # value, but it can be an object like a list containing multple
    # items within that one value. If you don't explicitly return a value,
    # your function will return 'None'.
    return return_val


## By convention, we give top-level functions two lines of space. Remember,
## Python thrives on a little breathing space.
##
##=============================================================================
## Function usage definition
##=============================================================================

# To use our function, we use the functions name with parentheses:
print("Running " + str(func_name))
output = func_name(1, 2, keyword_arg_3='coconuts')
print(output)

# To use our function, we use the functions name with parentheses:
print('Running ' + str(func_name))
output = func_name(1, 2, keyword_arg_3='rutabaga')
print(output)

##=============================================================================
## Function scope definition
##=============================================================================

var_1 = 'I am outside the function scope.'


def scope_example():
    print("I have access to var_1.")
    var_2 = 'Only the function has access to this variable.'
    var_3 = 'Others can access to this indirectly because it is returned.'
    return var_3


# This works because it is declared outside of the function's scope.
print(var_1)

# This fails because var_2 is defined solely inside the function.
print(var_2)

# This does not work because var_3 is defined inside the funciton.
print(var_3)

# This works because the value of var_3 was returned from scope.
quasi_var_3 = scope_example()
print(quasi_var_3)

##=============================================================================
## Warning
##=============================================================================

# Be wary of return values.
# Some functions return things.
a = 'abc'.upper()
print(a)

# Some functions do not.
my_list = [1, 2, 3]

# This is a mistake
my_new_list = my_list.append(1)
print(type(my_new_list))

# This actually changed the original list.
print(my_list)

##=============================================================================
## Functions Type Hints
##=============================================================================
##
## Python does not enforce type checking unless you explicitly do so or use a
## third party module. That said, Python annotations can be useful for
## documenting what we want to accept in a standardized format.
##
## As you can see from our definition above of func_name() we want arguments 1
## and 2 to be integers. We want argument 3 to be a string. It is also apparent
## that we want the function to return a string. We could have written the
## definition as:

def func_name(func_arg_1: int,
              func_arg_2: int,
              keyword_arg_3: str='default_value') -> str:
    '''Type annotated function.

       Reminder: pass is just a placeholder for 'do nothing' for the sake of
       indentation.

    '''
    pass

# Note: there are also variable annotations, such as:
a = 5 # type: int

##=============================================================================
## Questions?
##=============================================================================
